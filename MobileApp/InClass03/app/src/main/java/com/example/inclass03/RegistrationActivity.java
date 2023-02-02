package com.example.inclass03;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class RegistrationActivity extends AppCompatActivity {

    EditText editTextName, editTextEmail, editTextID;
    TextView textViewDepartment;
    String department;

    public static final String KEY_PROFILE = "PROFILE";

    private ActivityResultLauncher<Intent> startDeptForResult = registerForActivityResult(new
            ActivityResultContracts.StartActivityForResult(), new ActivityResultCallback<ActivityResult>() {
        @Override
        public void onActivityResult(ActivityResult result) {
            if(result.getResultCode() == RESULT_OK){
                Intent data = result.getData();
                department = data.getStringExtra(DepartmentActivity.KEY_DEPT);

                textViewDepartment.setText(department);

            }else {
                department = null;
                textViewDepartment.setText("");
            }
        }
    });



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);
        setTitle("Registration");

        editTextName = findViewById(R.id.editTextTextName);
        editTextEmail = findViewById(R.id.editTextEmail);
        textViewDepartment = findViewById(R.id.textViewDepartment);

        textViewDepartment.setText("");

        findViewById(R.id.buttonSelectDepartment).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(RegistrationActivity.this, DepartmentActivity.class);
                startDeptForResult.launch(intent);
            }
        });

        findViewById(R.id.buttonSubmitR).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name = editTextName.getText().toString();
                String email = editTextEmail.getText().toString();
                String id = editTextID.getText().toString();

                if (name.isEmpty())
                    Toast.makeText(RegistrationActivity.this, "Enter Name!", Toast.LENGTH_SHORT).show();
                else if (email.isEmpty())
                    Toast.makeText(RegistrationActivity.this, "Enter Email!", Toast.LENGTH_SHORT).show();
                else if (id.isEmpty())
                    Toast.makeText(RegistrationActivity.this, "Enter ID!", Toast.LENGTH_SHORT).show();
                else if (department == null){
                    Toast.makeText(RegistrationActivity.this, "Select Department!", Toast.LENGTH_SHORT).show();
                }
                else {
                    Profile profile = new Profile(name, email, id, department);
                    Intent intent = new Intent(RegistrationActivity.this, ProfileActivity.class);
                    intent.putExtra(KEY_PROFILE, profile);

                    startActivity(intent);
                }

            }
        });




    }
}