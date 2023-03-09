package com.example.midterm;

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
import android.widget.ImageView;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import com.example.midterm.databinding.FragmentReviewsBinding;
import com.example.midterm.models.Product;
import com.example.midterm.models.Review;
import com.squareup.picasso.Picasso;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link ReviewsFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class ReviewsFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PRODUCT = "PRODUCT_KEY";

    // TODO: Rename and change types of parameters
    private Product mProd;

    public ReviewsFragment() {
        // Required empty public constructor
    }
    private final OkHttpClient client = new OkHttpClient();


    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @return A new instance of fragment ReviewsFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static ReviewsFragment newInstance(Product param1) {
        ReviewsFragment fragment = new ReviewsFragment();
        Bundle args = new Bundle();
        args.putSerializable(ARG_PRODUCT, param1);

        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mProd = (Product) getArguments().getSerializable(ARG_PRODUCT);
        }
        getActivity().setTitle("Product Reviews");
    }

    ReviewsAdapter adapter;


    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        String img_url = mProd.getImg_url();
       Picasso.get().load(img_url).into(binding.imageViewProductIcon);

       binding.textViewProductName.setText(mProd.getName());
       binding.textViewProductPrice.setText(mProd.getPrice());


        adapter = new ReviewsAdapter(getActivity(), R.layout.row_item_review, mReviews);
        binding.listView.setAdapter(adapter);

        Request request = new Request.Builder()
                .url("https://www.theappsdr.com/api/product/reviews/" + mProd.getPid())
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                e.printStackTrace();
            }



            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
                if (response.isSuccessful()){
                    try{

                        String body = response.body().string();

                        JSONObject jsonObject = new JSONObject(body);
                        JSONArray jsonArray = jsonObject.getJSONArray("reviews");

                        for (int i = 0; i < jsonArray.length(); i++){
                            JSONObject review = jsonArray.getJSONObject(i);

                            mReviews.add(new Review(review));
                        }

                        getActivity().runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                adapter.notifyDataSetChanged();
                            }
                        });




                    }catch (JSONException e){
                        throw new RuntimeException(e);
                    }
                }else{
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            Toast.makeText(getActivity(), "Unable to get a response!", Toast.LENGTH_SHORT).show();
                        }
                    });
                }
            }
        });

        binding.buttonCreateReview.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mListener.toCreate(mProd);
            }
        });
    }






    FragmentReviewsBinding binding;
    ArrayList<Review> mReviews = new ArrayList<>();

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        binding = FragmentReviewsBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }
    ReviewsListener mListener;

    @Override
    public void onAttach(@NonNull Context context) {
        super.onAttach(context);
        mListener = (ReviewsListener) context;
    }

    interface ReviewsListener{
        void toCreate(Product pid);
    }

    class ReviewsAdapter extends ArrayAdapter<Review> {


        public ReviewsAdapter(@NonNull Context context, int resource, @NonNull List<Review> objects) {
            super(context, resource, objects);
        }

        @NonNull
        @Override
        public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
            if (convertView == null){

                convertView = LayoutInflater.from(parent.getContext()).inflate(R.layout.row_item_review, parent, false);
            }

            Review review = getItem(position);

            TextView reviewTitle = convertView.findViewById(R.id.textViewReview);
            TextView reviewCreated = convertView.findViewById(R.id.textViewReviewDate);
            ImageView reviewRating = convertView.findViewById(R.id.imageViewReviewRating);

            reviewTitle.setText(review.getReview());
            reviewCreated.setText(review.getCreated_at());

            int rating = Integer.parseInt(review.getRating());

            if (rating == 1)
                reviewRating.setImageResource(R.drawable.stars_1);
            else if (rating == 1)
                reviewRating.setImageResource(R.drawable.stars_2);
            else if (rating == 1)
                reviewRating.setImageResource(R.drawable.stars_3);
            else if (rating == 1)
                reviewRating.setImageResource(R.drawable.stars_4);
            else
                reviewRating.setImageResource(R.drawable.stars_5);




            return convertView;
        }
    }
}