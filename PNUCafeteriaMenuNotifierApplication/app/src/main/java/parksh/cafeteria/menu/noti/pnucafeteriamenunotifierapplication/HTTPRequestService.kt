package parksh.cafeteria.menu.noti.pnucafeteriamenunotifierapplication

import android.os.AsyncTask
import android.util.Log
import org.json.JSONObject
import java.io.BufferedInputStream
import java.io.BufferedReader
import java.io.DataOutputStream
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL
import java.nio.charset.StandardCharsets

class HTTPRequestService : AsyncTask<String, String, String>() {
    private val TAG = "HTTPRequestService"

    override fun doInBackground(vararg params: String?): String? {
        val serverURL = URL(params[0])
        var result:String?

        if(params.size > 1) {
            val token = params[1]
            result = postRequest(serverURL, token!!)
        } else {
            result = getRequest(serverURL)
        }

        return result
    }

    private fun postRequest(serverURL: URL, token: String) : String? {
        val conn = serverURL.openConnection() as HttpURLConnection
        conn.requestMethod = "POST"
        conn.connectTimeout = 300000
        conn.doOutput = true
        conn.doInput = true
        conn.setRequestProperty("Charset", "utf-8")
        conn.setRequestProperty("Content-Type", "application/json")

        var reqBody = JSONObject()
        reqBody.put("token", token)

        try {
            val outputStream = DataOutputStream(conn.outputStream)
            outputStream.writeBytes(reqBody.toString())
            outputStream.flush()
        } catch (e: Exception) {
            //TODO : Exception Message 표시 및 Connection 연결 종료
            e.printStackTrace()
            if(conn != null) {
                conn.disconnect()
            }
            return null
        }

        if(conn.responseCode == HttpURLConnection.HTTP_OK) {
            var data: String? = null
            try {
                val inputStream = BufferedInputStream(conn.inputStream)
                data = readDataStream(inputStream)
            } catch (e : Exception) {
                e.printStackTrace()
            } finally {
                if(conn != null) {
                    conn.disconnect()
                }
            }
            return data
        } else {
            if(conn != null) {
                conn.disconnect()
            }
        }
        return null
    }

    private fun getRequest(serverURL : URL) : String? {
        val conn = serverURL.openConnection() as HttpURLConnection
        conn.requestMethod = "GET"
        conn.connectTimeout = 300000
        conn.doInput = true
        conn.setRequestProperty("Content-Type", "application/json")

        if(conn.responseCode == HttpURLConnection.HTTP_OK) {
            var data: String? = null
            try {
                val inputStream = BufferedInputStream(conn.inputStream)
                data = readDataStream(inputStream)
            } catch (e : Exception) {
                e.printStackTrace()
            } finally {
                if(conn != null) {
                    conn.disconnect()
                }
            }
            return data
        } else {
            if(conn != null) {
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
        if(result == null) {
            Log.d(TAG, "Failed")
        } else {
            Log.d(TAG, "Success")
        }
    }
}