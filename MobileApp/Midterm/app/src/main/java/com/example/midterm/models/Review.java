package com.example.midterm.models;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.Serializable;

public class Review  {
    String review, rating, created_at;

    public Review() {
    }

    public Review(JSONObject json) throws JSONException {

        review = json.getString("review");
        rating = json.getString("rating");
        created_at = json.getString("created_at");

    }

    public String getReview() {
        return review;
    }

    public void setReview(String review) {
        this.review = review;
    }

    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }

    public String getCreated_at() {
        return created_at;
    }

    public void setCreated_at(String created_at) {
        this.created_at = created_at;
    }
}
