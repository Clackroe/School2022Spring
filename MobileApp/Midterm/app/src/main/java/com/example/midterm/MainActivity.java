package com.example.midterm;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import com.example.midterm.models.Product;

public class MainActivity extends AppCompatActivity implements ProductsFragment.ProductListener, ReviewsFragment.ReviewsListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, new ProductsFragment())
                .addToBackStack(null)
                .commit();
    }

    @Override
    public void toReviews(Product prod) {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, ReviewsFragment.newInstance(prod))
                .addToBackStack(null)
                .commit();
    }

    @Override
    public void toCreate(Product prod) {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.rootView, CreateReviewFragment.newInstance(prod))
                .addToBackStack(null)
                .commit();
    }
}