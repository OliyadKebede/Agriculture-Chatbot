package com.example.agribot;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

import androidx.appcompat.app.AppCompatActivity;

@SuppressLint("CustomSplashScreen")
public class SplashActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        new Handler().postDelayed(() -> {
            Intent intent = new Intent(SplashActivity.this, OnboardActivity.class);
            startActivity(intent);
             overridePendingTransition(R.anim.fade_in, R.anim.fade_out);
            finish();
        },0);


    }
}
