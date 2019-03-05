package parksh.cafeteria.menu.noti.pnucafeteriamenunotifierapplication

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    private val TOKEN_REQUEST_URL = "http://unsplash.ddns.net:28300/client/setClientToken"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if(intent.hasExtra("FirebaseToken")) {
            tv_tokenValue.text = intent.getStringExtra("FirebaseToken")
        } else {
            Toast.makeText(this, "전달된 데이터가 없음", Toast.LENGTH_SHORT).show()
        }

    }

    fun getCafeteriaMenu() : String {
        //var REQUEST_URL = "http://unsplash.ddns.net:28300/menu/"
        HTTPRequestService().execute()

        return ""
    }

    fun tokenValueRequest(v : View) {
        val value = tv_tokenValue.text.toString()
        HTTPRequestService().execute(TOKEN_REQUEST_URL, value)
    }
}