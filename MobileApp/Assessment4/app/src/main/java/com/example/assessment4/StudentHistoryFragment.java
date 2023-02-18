package com.example.assessment4;

import android.content.Context;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import com.example.assessment4.Models.CourseHistory;
import com.example.assessment4.Models.DataServices;
import com.example.assessment4.Models.Student;
import com.example.assessment4.databinding.FragmentStudentHistoryBinding;

import java.util.ArrayList;
import java.util.List;
import java.util.zip.CheckedOutputStream;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link StudentHistoryFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class StudentHistoryFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM_HISTORY = "history";

    // TODO: Rename and change types of parameters
    private Student student;

    public StudentHistoryFragment() {
        // Required empty public constructor
    }


    // TODO: Rename and change types and number of parameters
//    public static StudentHistoryFragment newInstance(Student student) {
//        StudentHistoryFragment fragment = StudentHistoryFragment.newInstance(student);
//        Bundle args = new Bundle();
//        args.putSerializable(ARG_PARAM_HISTORY, student);
//        return fragment;
//    }
    public static StudentHistoryFragment newInstance(Student stu) {

        Bundle args = new Bundle();
        StudentHistoryFragment fragment = new StudentHistoryFragment();
        args.putSerializable(ARG_PARAM_HISTORY, stu);
        fragment.setArguments(args);
        return fragment;
    }

    FragmentStudentHistoryBinding binding;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            this.student = (Student) getArguments().getSerializable(ARG_PARAM_HISTORY);
        }
        getActivity().setTitle("Student History");
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        binding = FragmentStudentHistoryBinding.inflate(inflater, container, false);
        // Inflate the layout for this fragment
        return binding.getRoot();
    }

    ArrayList<CourseHistory> history;

    AdapterHistory adapter;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        history = this.student.getCourses();
        adapter = new AdapterHistory(getActivity(), history);
        binding.textViewStudentName.setText(student.getName().toString());

        binding.listView.setAdapter(adapter);
    }

    class AdapterHistory extends ArrayAdapter<CourseHistory> {


        public AdapterHistory(@NonNull Context context, @NonNull List<CourseHistory> objects) {
            super(context, R.layout.history_row_item, objects);
        }

        @NonNull
        @Override
        public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
            if (convertView == null){
                convertView = getLayoutInflater().inflate(R.layout.history_row_item, parent, false);
            }

            TextView textViewCourseNumber = convertView.findViewById(R.id.textViewCourseNumber);
            TextView textViewCourseName = convertView.findViewById(R.id.textViewCourseName);
            TextView textViewCourseHours = convertView.findViewById(R.id.textViewCourseHours);
            TextView textViewCourseLetterGrade = convertView.findViewById(R.id.textViewCourseLetterGrade);

            CourseHistory history = getItem(position);

            textViewCourseHours.setText(history.getHours().toString());
            textViewCourseLetterGrade.setText(history.getLetterGrade());
            textViewCourseName.setText(history.getName().toString());
            textViewCourseNumber.setText(history.getNumber().toString());

            return convertView;

        }
    }
}