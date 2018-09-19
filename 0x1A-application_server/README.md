## 0x1A - Application server

### Description

Installing gunicorn and running the app server.

---

### Project Takeaways

- How to serve a Flask app with Gunicorn and Nginx on Ubuntu 14.04
- Running Gunicorn
- Upstarting Gunicorn

---

### Tasks

- Install Gunicorn
  - Git clone your AirBnB_clone_v2
  - Install Gunicorn and other libraries required by your application
  - Create an Upstart script that starts a Gunicorn instance to serve web_flask/0-hello_route.py from your AirBnB_clone_v2
  - Setup Nginx so that the route /airbnb-onepage/ points to your Gunicorn instance
  - Nginx must serve this page both locally and on its public IP on port 80
  - Upload your Upstart config file as 0-welcome_gunicorn-upstart_config
  - Upload your Nginx config file as 0-welcome_gunicorn-nginx_config

- Pass a query parameter
  - Create an Upstart script that starts a Gunicorn instance to serve web_flask/6-number_odd_or_even.py from your AirBnB_clone_v2
  - Setup Nginx so that the route/airbnb-dynamic/ points to your Gunicorn instance
  - Nginx must serve this page both locally and on its public IP on port 80
  - Upload your Upstart config file as 1-pass_parameter-upstart_config
  - Upload your Nginx config file as 1-pass_parameter-nginx_config

- Let's do this for your API
  - Git clone your AirBnB_clone_v3
  - data dump
  - Create an Upstart script that starts a Gunicorn instance to serve api/v1/app.py from your AirBnB_clone_v3
  - Make sure to use the necessary environment variables for your AirBnB_clone_v3 app
  - Setup Nginx so that the route /api/ points to your Gunicorn instance
  - Nginx must serve this page both locally and on its public IP on port 80
  - Upload your Upstart config as 2-api-upstart_config
  - Upload your Nginx config as 2-api-nginx_config



---

### Technologies Used
* Language: Python
* Operating System: Ubuntu 14.04 LTS (Trusty64)
---

### Author
Mitali Sengupta

<img src="http://pluspng.com/img-png/twitter-png-file-png-image-200.png" width=2% height=2%/> [@aadhibangalan](https://twitter.com/aadhibangalan) 

<img src="https://assets-cdn.github.com/images/icons/emoji/octocat.png" width=2% height=2%/>[MitaliSengupta](https://github.com/MitaliSengupta)
