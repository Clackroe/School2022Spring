package com.example.assessment4;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import com.example.assessment4.Models.Student;

public class MainActivity extends AppCompatActivity implements StudentsFragment.iStudentsFragment {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, new StudentsFragment())
                .addToBackStack(null)
                .commit();
    }


    @Override
    public void toHistory(Student student) {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, StudentHistoryFragment.newInstance(student))
                .addToBackStack(null)
                .commit();
    }
}