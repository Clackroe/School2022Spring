package com.example.inclass03;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class ProfileActivity extends AppCompatActivity {

    TextView textViewNameP, textViewEmailP, textViewIDP, textViewDeptP;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);
        setTitle("Profile");

        textViewNameP = findViewById(R.id.textViewNameP);
        textViewEmailP = findViewById(R.id.textViewEmailP);
        textViewIDP = findViewById(R.id.textViewIDP);
        textViewDeptP = findViewById(R.id.textViewDeptP);

        if(getIntent() != null && getIntent().hasExtra(RegistrationActivity.KEY_PROFILE)){
            Profile profile = (Profile)getIntent().getSerializableExtra(RegistrationActivity.KEY_PROFILE);

            textViewNameP.setText(profile.getName());
            textViewEmailP.setText(profile.getEmail());
            textViewIDP.setText(profile.getId());
            textViewDeptP.setText(profile.getDepartment());
        }


    }
}