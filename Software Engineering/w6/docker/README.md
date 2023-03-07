# Bonus Activity: Docker

## Introduction

In this bonus activity, you will be introduced to Docker, which is a tool that allows you to create and manage containers. Containers are packages that contain all dependencies, libraries, and files needed to run an application or service. Containers are meant to be lightweight, portable, and easy to deploy on any machine.

## Task 1: Installations

- Complete `TODO 1` by installing Docker Desktop for your operating system:
  - [Windows](https://docs.docker.com/docker-for-windows/install/)
  - [Mac](https://docs.docker.com/docker-for-mac/install/)
  - [Linux](https://docs.docker.com/engine/install/)

## Task 2: A Simple Docker File

- Complete `TODO 2` by downloading the alpine image from Docker Hub by running the following command in your terminal:
  - `docker pull alpine`
- Create a file named `Dockerfile` in this directory (`docker`) and add the following content to it:
  - `FROM alpine`
  - `RUN apk add --update nodejs npm`
  - `RUN npm install -g http-server`
  - `WORKDIR /app`
  - `COPY . /app`
  - `EXPOSE 8080`
  - `CMD ["http-server", "-p", "8080"]`
- Complete `TODO 3` by building the Docker image by running the following command in your terminal:
  - `docker build -t w6 .`
- Complete `TODO 4` by running the Docker image by running the following command in your terminal:
  - `docker run -p 8080:8080 w6`
- Complete `TODO 5` by visiting the following URL in your browser:
  - `http://localhost:8080`

## Task 3: Hosting a Docker Image on Docker Hub

- Complete `TODO 6` by creating an account on [Docker Hub](https://hub.docker.com/).
- Complete `TODO 7` by logging into Docker Hub by running the following command in your terminal:
  - `docker login`
  - **NOTE:** You may need to logout on your browser and through your terminal before logging in again.
    - to logout on your browser, click on your profile picture in the top right corner and click `Logout`
    - to logout through your terminal, run the following command: `docker logout`
- Complete `TODO 8` by tagging the Docker image by running the following command in your terminal:
  - `docker tag w6 <DockerHubName>/w6`
  - **NOTE:** Replace `<DockerHubName>` with your Docker Hub username (e.g., `dgaryuncc/w6`)
- Complete `TODO 9` by pushing the Docker image to Docker Hub by running the following command in your terminal:
  - `docker push <DockerHubName>/w6`

## Submission Details

- On Canvas, submit the following:
  - A zip file of the entire `docker` directory, renamed as your NinerNetID.zip (e.g., dgary9.zip)
    - **TIP:** If you are struggling to remember how to zip your submission, here's an example of how to do it from the terminal on Mac or Linux machines: `zip -r -X dgary9.zip .`
    - **TIP:** For Windows users who want to use their terminal to zip their submission, you can use the `7za` command. Here's an example of how to do it: `7za dgary9.zip .`
    - **NOTE:** In the above examples, `dgary9` is the NinerNetID of the student submitting the assignment and `.` is the directory that contains the files to be zipped, which is the current directory (`docker`) in this case.
  - Leave a comment on your submission that tells us your Docker Hub username (e.g., `dgaryuncc`)
