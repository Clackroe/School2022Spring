package com.example.evaluation1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {





    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText editTextNumberA, editTextNumberB;
        TextView textViewMethod, textViewQuotient;
        Button buttonCalculate, buttonReset;

        buttonReset = findViewById(R.id.buttonReset);
        buttonCalculate = findViewById(R.id.buttonCalculate);
        textViewMethod = findViewById(R.id.textViewMethod);
        textViewQuotient = findViewById(R.id.textViewQuotient);
        editTextNumberA = findViewById(R.id.editTextNumberA);
        editTextNumberB = findViewById(R.id.editTextNumberB);

       buttonReset.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View view) {
               editTextNumberA.setText("");
               editTextNumberB.setText("");
               textViewQuotient.setText("0.00");
           }
       });

       buttonCalculate.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View view) {
               try {
                   String A = editTextNumberA.getText().toString();
                   double numA = Integer.parseInt(A);

                   String B = editTextNumberB.getText().toString();
                   double numB = Integer.parseInt(B);

                   double quo = numA / numB;
                   if (numB == 0){
                       Toast.makeText(MainActivity.this, "Please do not divide by 0", Toast.LENGTH_SHORT).show();
                   }
                   else
                        //String.format("%.2f",23.59004)
                        textViewQuotient.setText("" + String.format("%.2f",quo));
               } catch (Exception e){
                   Toast.makeText(MainActivity.this, "Please Enter Valid Numbers!", Toast.LENGTH_SHORT).show();
               }

           }
       });

    }

}