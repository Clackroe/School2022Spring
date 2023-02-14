package com.example.assessment3;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity implements WelcomeFragment.WelcomeFragmentListener,
        RegistrationFragment.RegFragListener, SetGenderFragment.SetGenderFragmentListener, ProfileFragment.FragmentProfileListener {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle("Main Activity");

        getSupportFragmentManager().beginTransaction()
                .add(R.id.rootView, new WelcomeFragment())
                .commit();
    }

    @Override
    public void toRegFragment() {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, new RegistrationFragment(), "registration-fragment")
                .addToBackStack(null)
                .commit();
    }

    @Override
    public void toSetGender() {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, new SetGenderFragment())
                .addToBackStack(null)
                .commit();
    }

    @Override
    public void submitProfile(Profile profile) {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, ProfileFragment.newInstance(profile))
                .addToBackStack(null)
                .commit();
    }

    @Override
    public void setGender(String gender) {

       RegistrationFragment regFragment = (RegistrationFragment) getSupportFragmentManager().findFragmentByTag("registration-fragment");
       if (regFragment != null){
           regFragment.setGender(gender);
       }
       getSupportFragmentManager().popBackStack();
    }

    @Override
    public void cancelGender() {
        getSupportFragmentManager().popBackStack();
    }

    @Override
    public void closeProfile() {
        getSupportFragmentManager().popBackStack();
    }
}