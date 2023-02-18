package com.example.assessment4;

import android.content.Context;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Toast;

import com.example.assessment4.Models.DataServices;
import com.example.assessment4.Models.Student;
import com.example.assessment4.databinding.FragmentStudentsBinding;

import java.nio.channels.DatagramChannel;
import java.util.ArrayList;


public class StudentsFragment extends Fragment {
    public StudentsFragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getActivity().setTitle("Students");
    }

    FragmentStudentsBinding binding;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        binding = FragmentStudentsBinding.inflate(inflater, container, false);
        // Inflate the layout for this fragment
        return binding.getRoot();
    }

    ArrayAdapter<Student> adapter;
    ArrayList<Student> students;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        students = DataServices.getStudents();
        adapter = new ArrayAdapter<>(getActivity(), android.R.layout.simple_list_item_1, students);
        binding.listView.setAdapter(adapter);

        binding.listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Student student = students.get(i);

                mListener.toHistory(student);
            }
        });
    }

    iStudentsFragment mListener;

    @Override
    public void onAttach(@NonNull Context context) {
        super.onAttach(context);
        mListener = (iStudentsFragment) context;
    }

    interface iStudentsFragment{
        void toHistory(Student student);
    }
}