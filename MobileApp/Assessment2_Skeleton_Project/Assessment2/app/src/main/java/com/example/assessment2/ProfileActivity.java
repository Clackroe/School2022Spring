package com.example.assessment2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class ProfileActivity extends AppCompatActivity {

    Profile profile;
    String weight, gender;

    TextView textViewWeight, textViewGender;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);
        setTitle("Profile");

        textViewGender = findViewById(R.id.textViewGender);
        textViewWeight = findViewById(R.id.textViewWeight);

        if (getIntent() != null && getIntent().getSerializableExtra(MainActivity.KEY_PROFILE) != null) {
            profile = (Profile) getIntent().getSerializableExtra(MainActivity.KEY_PROFILE);
            weight= profile.getWeight();
            gender=profile.getGender();

            textViewWeight.setText(weight);
            textViewGender.setText(gender);

        }

        findViewById(R.id.buttonClose).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
    }
}