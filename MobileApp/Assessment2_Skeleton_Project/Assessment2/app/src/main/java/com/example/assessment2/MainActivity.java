package com.example.assessment2;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Set;

public class MainActivity extends AppCompatActivity {
    TextView textViewWeight, textViewGender;
    Profile profile;

    public static final String KEY_PROFILE = "PROFILE";

    private ActivityResultLauncher<Intent> startWeightForResult = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            new ActivityResultCallback<ActivityResult>() {
                @Override
                public void onActivityResult(ActivityResult result) {
                    if (result.getResultCode() == RESULT_OK){
                        Intent data = result.getData();
                        String weight = data.getStringExtra(SetWeightActivity.KEY_WEIGHT);
                        textViewWeight.setText(weight);
                    }else{

                    }
                }
            });

    private ActivityResultLauncher<Intent> startGenderForResult = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            new ActivityResultCallback<ActivityResult>() {
                @Override
                public void onActivityResult(ActivityResult result) {
                    if (result.getResultCode() == RESULT_OK){
                        Intent data = result.getData();
                        String gender = data.getStringExtra(SetGenderActivity.KEY_GENDER);
                        textViewGender.setText(gender);
                    }else{

                    }
                }
            });

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle("Main");

        textViewGender = findViewById(R.id.textViewGender);
        textViewWeight = findViewById(R.id.textViewWeight);

        findViewById(R.id.buttonSetWeight).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, SetWeightActivity.class);
                startWeightForResult.launch(intent);
            }
        });

        findViewById(R.id.buttonSetGender).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, SetGenderActivity.class);
                startGenderForResult.launch((intent));
            }
        });

        findViewById(R.id.buttonReset).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                textViewGender.setText("N/A");
                textViewWeight.setText("N/A");
                profile = new Profile();
            }
        });

        findViewById(R.id.buttonSubmit).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (textViewWeight.getText().toString().equals("N/A"))
                    Toast.makeText(MainActivity.this, "Please Setup Weight", Toast.LENGTH_SHORT).show();
                else if (textViewGender.getText().toString().equals("N/A"))
                    Toast.makeText(MainActivity.this, "Please Setup Your Gender", Toast.LENGTH_SHORT).show();

                else{
                    String weight = textViewWeight.getText().toString();
                    String gender = textViewGender.getText().toString();
                    profile = new Profile(weight, gender);

                    Intent intent = new Intent(MainActivity.this, ProfileActivity.class);
                    intent.putExtra(KEY_PROFILE, profile);
                    startActivity(intent);
                }
            }
        });

    }
}