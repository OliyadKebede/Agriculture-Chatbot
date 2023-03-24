package com.example.agribot;


import android.content.Intent;
import android.os.Bundle;

import android.view.View;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.AppCompatButton;

public class OnboardActivity extends AppCompatActivity {
    AppCompatButton first_button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.menu_screen);
        first_button= findViewById(R.id.first_button);
        first_button.setOnClickListener(view -> {
            startActivity(new Intent(OnboardActivity.this, MainActivity.class));
            finish();
        });

    }



}