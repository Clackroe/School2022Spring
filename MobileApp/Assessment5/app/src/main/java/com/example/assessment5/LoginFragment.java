package com.example.assessment5;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import com.example.assessment5.databinding.FragmentLoginBinding;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.FormBody;
import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class LoginFragment extends Fragment {
    public LoginFragment() {
        // Required empty public constructor
    }

    FragmentLoginBinding binding;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        binding = FragmentLoginBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        getActivity().setTitle("Login");

        binding.buttonCreateNewAccount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mListener.gotoRegister();
            }
        });

        binding.buttonLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String email = binding.editTextEmail.getText().toString();
                String password = binding.editTextPassword.getText().toString();
                if(email.isEmpty() || password.isEmpty()) {
                    Toast.makeText(getContext(), "Please enter email and password", Toast.LENGTH_SHORT).show();
                } else {
                    //perform the login ..


                }
            }
        });
    }

    LoginListener mListener;

    @Override
    public void onAttach(@NonNull Context context) {
        super.onAttach(context);
        if (context instanceof LoginListener) {
            mListener = (LoginListener) context;
        } else {
            throw new RuntimeException(context.toString() + " must implement LoginListener");
        }
    }

    private final OkHttpClient client = new OkHttpClient();
    private void Login(String email, String password){

        RequestBody requestBody = new FormBody.Builder()
                .add("email", email)
                .add("password", password)
                .build();

        Request request = new Request.Builder()
                .url("https://www.theappsdr.com/api/login")
                .post(requestBody)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                Toast.makeText(getContext(), "Unable to Login!!", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {

                String body = response.body().string();
                if (response.isSuccessful()){

                    try {
                        JSONObject jsonObject = new JSONObject(body);

                        int id = jsonObject.getInt("user_id");
                        String status = jsonObject.getString("status");
                        String token = jsonObject.getString("token");
                        String fname = jsonObject.getString("user_fname");
                        String lname = jsonObject.getString("user_lname");
                        String role = jsonObject.getString("user_role");


                        SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);

                        SharedPreferences.Editor editor = sharedPref.edit();

                        editor.putInt("user_id", id);
                        editor.putString("token", token);
                        editor.putString("user_fname", fname);
                        editor.putString("user_lname", lname);
                        editor.putString("user_role", role);
                        editor.apply();


                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            mListener.gotoRegister();
                        }
                    });

            }else {
                }
        }
        });

    }

    interface LoginListener {
        void authSuccessful();
        void gotoRegister();
    }
}