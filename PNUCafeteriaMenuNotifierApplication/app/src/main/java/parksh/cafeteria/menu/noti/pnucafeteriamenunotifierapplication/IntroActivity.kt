package parksh.cafeteria.menu.noti.pnucafeteriamenunotifierapplication

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import com.google.android.gms.tasks.OnCompleteListener
import com.google.firebase.iid.FirebaseInstanceId
import kotlinx.android.synthetic.main.activity_intro.*

class IntroActivity : AppCompatActivity() {
    private val TAG = "IntroActivity"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_intro)

        getFirebaseInstance()
    }

    fun getFirebaseInstance() {
        FirebaseInstanceId.getInstance().instanceId
            .addOnCompleteListener (OnCompleteListener { task ->
                if(!task.isSuccessful) {
                    Log.w(TAG, task.exception)
                    btn_restart.visibility = View.VISIBLE
                    return@OnCompleteListener
                }

                val token = task.result?.token
                Log.d(TAG, token)

                val intent = Intent(this, MainActivity::class.java)
                intent.putExtra("FirebaseToken", token)
                startActivity(intent)
                finish()
            })
    }

    fun clickRestartButton(v : View) {
        getFirebaseInstance()
    }
}
