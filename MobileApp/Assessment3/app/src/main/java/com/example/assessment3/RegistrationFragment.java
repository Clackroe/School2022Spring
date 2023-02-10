package com.example.assessment3;

import android.content.Context;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import com.example.assessment3.databinding.FragmentRegistrationBinding;


public class RegistrationFragment extends Fragment {
    String gender = "N/A";

    public void setGender(String gender) {
        this.gender = gender;
    }

    public RegistrationFragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getActivity().setTitle("Registration");
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        binding.textViewSelectedGender.setText(this.gender);

        binding.buttonSetGender.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mListener.toSetGender();
            }
        });

        binding.buttonSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (binding.editTextName.getText().toString().isEmpty()){
                    Toast.makeText(getActivity(), "Please enter your name!!!", Toast.LENGTH_SHORT).show();
                } else if (binding.textViewSelectedGender.getText().toString() == "N/A"){
                    Toast.makeText(getActivity(), "Please Select a Gender!!", Toast.LENGTH_SHORT).show();
                }
                else{
                    Profile profile = new Profile(binding.editTextName.getText().toString(), gender);
                    mListener.submitProfile(profile);
                }
            }
        });

    }

    FragmentRegistrationBinding binding;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        binding = FragmentRegistrationBinding.inflate(inflater, container, false);
        // Inflate the layout for this fragment
        return binding.getRoot();
    }

    RegFragListener mListener;

    @Override
    public void onAttach(@NonNull Context context) {
        super.onAttach(context);
        mListener = (RegFragListener) context;
    }

    interface RegFragListener{
        void toSetGender();
        void submitProfile(Profile profile);
    }

}