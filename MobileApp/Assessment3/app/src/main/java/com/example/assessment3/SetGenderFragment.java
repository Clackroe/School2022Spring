package com.example.assessment3;

import android.content.Context;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RadioGroup;
import android.widget.Toast;

import com.example.assessment3.databinding.FragmentSetGenderBinding;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link SetGenderFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class SetGenderFragment extends Fragment {


    public SetGenderFragment() {
        // Required empty public constructor
    }
    public static SetGenderFragment newInstance(String param1, String param2) {
        SetGenderFragment fragment = new SetGenderFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getActivity().setTitle("Select Gender");

    }

    FragmentSetGenderBinding binding;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        binding = FragmentSetGenderBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        binding.buttonSet.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String gender;
                RadioGroup radioGroup = binding.radioGroup;
                if (radioGroup.getCheckedRadioButtonId() == binding.radioButtonMale.getId()){
                    gender = "Male";
                }
                else if (radioGroup.getCheckedRadioButtonId() == binding.radioButtonFemale.getId()) {
                    gender = "Female";
                }
                else{
                    gender = "N/A";
                }

                mListener.setGender(gender);

            }
        });

        binding.buttonCancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mListener.cancelGender();
            }
        });
    }

    SetGenderFragmentListener mListener;

    @Override
    public void onAttach(@NonNull Context context) {
        super.onAttach(context);
        mListener = (SetGenderFragmentListener) context;

    }

    interface SetGenderFragmentListener{
        void setGender(String gender);
        void cancelGender();
    }
}