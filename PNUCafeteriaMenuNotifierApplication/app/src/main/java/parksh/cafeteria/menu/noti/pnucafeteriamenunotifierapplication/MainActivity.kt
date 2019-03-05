package parksh.cafeteria.menu.noti.pnucafeteriamenunotifierapplication

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if(intent.hasExtra("FirebaseToken")) {
            tv_tokenValue.text = intent.getStringExtra("FirebaseToken")
        } else {
            Toast.makeText(this, "전달된 데이터가 없음", Toast.LENGTH_SHORT).show()
        }
    }

    fun getCafeteriaMenu() : String? {
        val menuRequestURL = URLStringData().getMenuRequestURL()
        val result = HTTPRequestService().execute(menuRequestURL).get()?: return null

        return result
    }

    fun getMenuData(v: View) {
        var menuData = getCafeteriaMenu()
    }

    fun tokenValueRequest(v : View) {
        var tokenRequestURL = URLStringData().getTokenRequestURL()
        val value = tv_tokenValue.text.toString()
        HTTPRequestService().execute(tokenRequestURL, value)
    }
}