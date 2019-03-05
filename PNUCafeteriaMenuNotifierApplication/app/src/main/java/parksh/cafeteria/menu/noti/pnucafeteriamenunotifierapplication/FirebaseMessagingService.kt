package parksh.cafeteria.menu.noti.pnucafeteriamenunotifierapplication

import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.media.RingtoneManager
import android.support.v4.app.NotificationCompat
import android.util.Log
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class FirebaseMessagingService : FirebaseMessagingService() {
    private val MESSAGING_TAG = "MessagingService"
    private val TOKEN_REQUEST_URL = "http://unsplash.ddns.net:28300/client/setClientToken"

    override fun onNewToken(token: String?) {
        /*
            토큰 발행 시 호출되는 함수
            토큰 발행 후 서버 연결
             -> 서버로 토큰 데이터 전송하도록 기능 개발

            ** 토큰 발행 기준 **
            * Application 설치 및 재설치
            * 앱 데이터 전체 삭제 등의 문제 발생 시
        */
        Log.d(MESSAGING_TAG, "New Token : $token")
        HTTPRequestService().execute(TOKEN_REQUEST_URL, token)
    }

    override fun onMessageReceived(message: RemoteMessage) {
        //메세지 수신에 대한 처리
        Log.d(MESSAGING_TAG, "From: ${message.from}")

        if(message.notification != null) {
            Log.d(MESSAGING_TAG, "Notification Message Body : ${message.notification?.body}")
            sendNotification(message.notification?.body)
        }
    }

    private fun sendNotification(messageBody: String?) {
        val intent = Intent(this, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
            putExtra("Notification", messageBody)
        }

        var pendingIntent = PendingIntent.getActivity(this, 0,
                                                        intent, PendingIntent.FLAG_ONE_SHOT)
        val notificationSound = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION)

        var notificationBuilder = NotificationCompat.Builder(this, "Notification")
                                                            .setSmallIcon(R.mipmap.ic_launcher)
                                                            .setContentTitle("PNU Cafeteria Menu")
                                                            .setContentText(messageBody)
                                                            .setAutoCancel(true)
                                                            .setSound(notificationSound)
                                                            .setContentIntent(pendingIntent)

        var notiManager: NotificationManager = this.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notiManager.notify(0, notificationBuilder.build())
    }
}