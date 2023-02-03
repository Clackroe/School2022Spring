package com.example.assessment2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.RadioGroup;

public class SetGenderActivity extends AppCompatActivity {

    public static final String KEY_GENDER = "GENDER";

    RadioGroup radioGroup;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_gender);
        setTitle("Set Gender");

        radioGroup = findViewById(R.id.radioGroupGender);

        findViewById(R.id.buttonSet).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String gender = "Female";
                if (radioGroup.getCheckedRadioButtonId() == R.id.radioButtonFemale)
                    gender = "Female";
               else if (radioGroup.getCheckedRadioButtonId() == R.id.radioButtonMale)
                    gender = "Male";
                Intent intent = new Intent();
                intent.putExtra(KEY_GENDER, gender);
                setResult(RESULT_OK, intent);
                finish();

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