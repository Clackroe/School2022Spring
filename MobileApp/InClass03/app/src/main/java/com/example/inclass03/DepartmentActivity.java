package com.example.inclass03;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.RadioGroup;

public class DepartmentActivity extends AppCompatActivity {

public static final String KEY_DEPT = "DEPT";
    RadioGroup radioGroup;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_department);
        setTitle("Department");

         radioGroup = findViewById(R.id.radioGroup);

        findViewById(R.id.buttonSelectDepartment).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int selectedID = radioGroup.getCheckedRadioButtonId();
                String dept =getString(R.string.cs_label);

                if(selectedID == R.id.radioButtonCS)
                    dept = getString(R.string.cs_label);
                else if (selectedID == R.id.radioButtonSS)
                    dept = getString(R.string.ss_label);
                else if (selectedID == R.id.radioButtonBI)
                    dept = getString(R.string.bi_label);
                else if (selectedID == R.id.radioButtonDS)
                    dept = getString(R.string.ds_label);
                Intent intent = new Intent();
                intent.putExtra(KEY_DEPT, dept);
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