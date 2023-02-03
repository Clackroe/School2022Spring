package com.example.assessment2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;


public class SetWeightActivity extends AppCompatActivity {

    public static final String KEY_WEIGHT = "WEIGHT";

    EditText editTextWeight;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_weight);
        setTitle("Set Weight");

        editTextWeight = findViewById(R.id.editTextNumberDecimal);

        findViewById(R.id.buttonSet).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (editTextWeight.getText().toString().isEmpty())
                    Toast.makeText(SetWeightActivity.this, "Enter a Valid Weight!", Toast.LENGTH_SHORT).show();
                else {
                    try {

                        String weight = editTextWeight.getText().toString();
                        Intent intent = new Intent();
                        intent.putExtra(KEY_WEIGHT, weight);
                        setResult(RESULT_OK, intent);
                        finish();


                    } catch (Exception e) {
                        Toast.makeText(SetWeightActivity.this, "Enter a Valid Weight!", Toast.LENGTH_SHORT).show();
                    }
                }
            }
        });

        findViewById(R.id.buttonCancel).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
    }
}