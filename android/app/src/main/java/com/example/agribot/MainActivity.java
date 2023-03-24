package com.example.agribot;

import android.content.Intent;
import android.graphics.Typeface;

import android.os.Bundle;

import android.view.Menu;
import android.view.animation.LinearInterpolator;
import android.widget.ImageButton;
import android.widget.ImageView;

import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.AppCompatEditText;
import androidx.appcompat.widget.Toolbar;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.DefaultItemAnimator;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.agrawalsuneet.dotsloader.loaders.LazyLoader;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class MainActivity extends AppCompatActivity {

    private RecyclerView recyclerView;
    private ChatAdapter mAdapter;
    private List messageArrayList;
    AppCompatEditText inputMessage;
    private boolean initialRequest;
    private Menu menu;
    ImageView option;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        inputMessage = findViewById(R.id.message);
        ImageButton btnSend = findViewById(R.id.btn_send);
        option = findViewById(R.id.option);

        String customFont = "Montserrat-Regular.ttf";
        Typeface typeface = Typeface.createFromAsset(getAssets(), customFont);
        inputMessage.setTypeface(typeface);
        recyclerView = findViewById(R.id.recycler_view);

        messageArrayList = new ArrayList<>();
        mAdapter = new ChatAdapter(messageArrayList);

        final Toolbar mToolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(mToolbar);

        LazyLoader loader = new LazyLoader(getApplicationContext(), 30, 20, ContextCompat.getColor(getApplicationContext(), R.color.black),
                ContextCompat.getColor(getApplicationContext(), R.color.black),
                ContextCompat.getColor(getApplicationContext(), R.color.black));
        loader.setAnimDuration(500);
        loader.setFirstDelayDuration(100);
        loader.setSecondDelayDuration(200);
        loader.setInterpolator(new LinearInterpolator());
        LinearLayoutManager layoutManager = new LinearLayoutManager(this);
        layoutManager.setOrientation(LinearLayoutManager.VERTICAL);
        layoutManager.setStackFromEnd(true);
        recyclerView.setLayoutManager(layoutManager);
        recyclerView.setItemAnimator(new DefaultItemAnimator());
        recyclerView.setAdapter(mAdapter);
        this.inputMessage.setText("");
        this.initialRequest = false;
        btnSend.setOnClickListener(view -> sendMessage(Objects.requireNonNull(inputMessage.getText()).toString()));


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        this.menu = menu;
        getMenuInflater().inflate(R.menu.menu, menu);
        return true;
    }

    private void sendMessage(String userMsg) {
        final String inputmessage = Objects.requireNonNull(this.inputMessage.getText()).toString().trim();
        if (!this.initialRequest) {
            Message inputMessage = new Message();
            inputMessage.setMessage(inputmessage);
            inputMessage.setId("1");
            messageArrayList.add(inputMessage);
            recyclerView.scrollToPosition(mAdapter.getItemCount() - 1);
        } else {
            Message inputMessage = new Message();
            inputMessage.setMessage(inputmessage);

            inputMessage.setId("100");
            this.initialRequest = false;
            Toast.makeText(getApplicationContext(), "Tap on the message for send", Toast.LENGTH_LONG).show();

        }

        this.inputMessage.setText("");
        mAdapter.notifyDataSetChanged();
        recyclerView.scrollToPosition(mAdapter.getItemCount() - 1);

        Message message = new Message();
        messageArrayList.add(message);
        mAdapter.notifyDataSetChanged();

        Thread thread = new Thread(() -> {
            String url = "http://localhost:8000/api/";

            JSONObject req = new JSONObject();
            try {
                req.put("msg",userMsg);
            } catch (JSONException e) {
                e.printStackTrace();
            }

            // creating a variable for our request queue.
            RequestQueue queue = Volley.newRequestQueue(getApplicationContext());

            // on below line we are making a json object request for a get request and passing our url .
            JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.POST, url, req, response -> {
                try {

                    String res = response.getString("res");

                    mAdapter.setData(res);

                    // notifying our adapter as data changed.

                } catch (JSONException e) {
                    e.printStackTrace();

                    mAdapter.setData("sorry , there is something wrong.");

                }
            }, error -> mAdapter.setData("sorry , there is something wrong."));
            queue.add(jsonObjectRequest);

            runOnUiThread(() -> {
                mAdapter.notifyDataSetChanged();
                if (mAdapter.getItemCount() > 1) {
                    Objects.requireNonNull(recyclerView.getLayoutManager()).smoothScrollToPosition(recyclerView, null, mAdapter.getItemCount() - 1);

                }

            });

        });
        thread.start();
    }



    @Override
    public void onBackPressed() {
        Intent intent = new Intent(MainActivity.this, OnboardActivity.class);
        startActivity(intent);
        super.onBackPressed();
    }
}





