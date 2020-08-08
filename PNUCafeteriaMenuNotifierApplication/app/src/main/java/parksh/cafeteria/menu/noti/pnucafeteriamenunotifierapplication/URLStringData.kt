package parksh.cafeteria.menu.noti.pnucafeteriamenunotifierapplication

import android.util.Log
import java.text.SimpleDateFormat
import java.util.*

class URLStringData {
    private val TOKEN_REQUEST_URL = "http://unsplash.ddns.net:28300/client/setClientToken"

    fun getTokenRequestURL() : String {
        return TOKEN_REQUEST_URL
    }

    fun getMenuRequestURL() : String {
        var nowDate = getNowDate()
        var menuURL =  "http://unsplash.ddns.net:28300/menu/"
        return menuURL + nowDate
    }

    private fun getNowDate() : String {
        //yyyy.MM.dd 형태로 반환
        val now = Calendar.getInstance().time
        val formatter = SimpleDateFormat("yyyy.MM.dd")

        return formatter.format(now)
    }
}