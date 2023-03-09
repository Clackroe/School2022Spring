package com.example.midterm;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RadioGroup;

import com.example.midterm.databinding.FragmentCreateReviewBinding;
import com.example.midterm.models.Product;
import com.example.midterm.models.Review;
import com.squareup.picasso.Picasso;

import okhttp3.FormBody;
import okhttp3.Request;
import okhttp3.RequestBody;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link CreateReviewFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class CreateReviewFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";

    // TODO: Rename and change types of parameters
    private Product mProd;

    public CreateReviewFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @return A new instance of fragment CreateReviewFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static CreateReviewFragment newInstance(Product param1) {
        CreateReviewFragment fragment = new CreateReviewFragment();
        Bundle args = new Bundle();
        args.putSerializable(ARG_PARAM1, param1);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mProd = (Product) getArguments().getSerializable(ARG_PARAM1);
        }
    }

    FragmentCreateReviewBinding binding;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        binding = FragmentCreateReviewBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        String img_url = mProd.getImg_url();
        Picasso.get().load(img_url).into(binding.imageViewProductIcon);

        binding.textViewProductName.setText(mProd.getName());
        binding.textViewProductPrice.setText(mProd.getPrice());

        binding.buttonSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //https://www.theappsdr.com/api/product/review

                RadioGroup radGroup = binding.radioGroup;



                RequestBody formBody = new FormBody.Builder()
                        .add("pid", mProd.getPid())
                        .add("review", binding.editTextReview.getText().toString())
                       // .add("rating", "TODO")
                        .build();

                okhttp3.Request request = new Request.Builder()
                        .url("https://www.theappsdr.com/api/product/review")
                        .post(formBody)
                        .build();
            }
        });
   }
}