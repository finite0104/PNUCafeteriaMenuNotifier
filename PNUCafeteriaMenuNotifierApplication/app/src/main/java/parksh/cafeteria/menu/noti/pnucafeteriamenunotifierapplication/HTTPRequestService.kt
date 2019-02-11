package parksh.cafeteria.menu.noti.pnucafeteriamenunotifierapplication

import android.os.AsyncTask
import java.io.BufferedInputStream
import java.io.BufferedReader
import java.io.DataOutputStream
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL
import java.nio.charset.StandardCharsets

class HTTPRequestService : AsyncTask<String, String, String>() {
    override fun onPreExecute() {
        //Before doInBackground
    }

    override fun doInBackground(vararg params: String?): String? {
        val serverURL = URL(params[0])
        var result:String?
        if(params[1] != null) {
            result = getRequest(serverURL)
        } else {
            val token = params[1].toString()
            result = postRequest(serverURL, token)
        }

        return result
    }

    fun postRequest(serverURL: URL, token: String) : String? {
        val conn = serverURL.openConnection() as HttpURLConnection
        conn.requestMethod = "POST"
        conn.connectTimeout = 300000
        conn.doOutput = true

        val sendTokenValue: ByteArray = token.toByteArray(StandardCharsets.UTF_8)
        conn.setRequestProperty("Charset", "utf-8")
        conn.setRequestProperty("Content-Length", sendTokenValue.size.toString())
        conn.setRequestProperty("Content-Type", "application/json")

        try {
            val outputStream = DataOutputStream(conn.outputStream)
            outputStream.write(sendTokenValue)
            outputStream.flush()
        } catch (e: Exception) {
            //TODO : Exception Message 표시 및 Connection 연결 종료
            e.printStackTrace()
            conn.disconnect()
        }

        if(conn.responseCode == HttpURLConnection.HTTP_OK) {
            try {
                val inputStream = BufferedInputStream(conn.inputStream)
                val data: String?
                data = readDataStream(inputStream)

                return data
            } catch (e : Exception) {
                e.printStackTrace()
            } finally {
                conn.disconnect()
            }
        }
        return null
    }

    fun getRequest(serverURL : URL) : String? {
        val conn = serverURL.openConnection() as HttpURLConnection
        conn.requestMethod = "GET"
        conn.connectTimeout = 300000
        conn.doOutput = true
        conn.setRequestProperty("Content-Type", "application/json")

        if(conn.responseCode == HttpURLConnection.HTTP_OK) {
            try {
                val inputStream = BufferedInputStream(conn.inputStream)
                val data: String?
                data = readDataStream(inputStream)

                return data
            } catch (e : Exception) {
                e.printStackTrace()
            } finally {
                conn.disconnect()
            }
        }
        return null
    }

    fun readDataStream(inputStream: BufferedInputStream) : String? {
        val bufferedReader = BufferedReader(InputStreamReader(inputStream))
        val stringBuilder = StringBuilder()
        bufferedReader.forEachLine { stringBuilder.append(it) }

        return stringBuilder.toString()
    }

    override fun onPostExecute(result: String?) {
        //After doInBackground
    }
}