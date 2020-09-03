# Hello World Web Application API

I have build REST API server in Python using the Flask framework.   

**Flask** is a popular micro framework for building web applications. Since it is a micro-framework, it is very easy to use and lacks most of the advanced functionality which is found in a full-fledged framework.  

## Setup
- Install Python 3.  
[Download and install python 3.](https://www.python.org/downloads/)
- Install Docker.  
[Download and install Docker](https://docs.docker.com/engine/install/)

- Build docker Image:  
Open terminal and run: 
```
docker build -t helloFlaskDocker .
```
- To run the docker container.
```
docker run -p 8080:8080 helloFlaskDocker
```

# Questions and Answers

**1. What other information would you add to health endpoint json object in step 2? Explain what would be the use case for that extra information?**

I would also prefer to use the last downtime of the application which can be implemented using a parallel thread to check  this would help to check the resilience of server and provide effective scaling.

**2. What branching strategy would you use for development?**

I prefer to use feature and env based branching strategy , here every developer whenever adding to a new feature to the software creates a branch by the id of that particular feature . When the feature is functional completely it is merged to the dev branch for integration testing ,  and further to stage for full stage testing , the master contains the latest stable version of software , moreover we use git tags to track the latest release by versions.

**3. What CICD tool/service would you use?**

I prefer to use Jenkins because it provides best  flexibility in terms of pipelines , it supports many plugins to provide integrations with different platforms like Github, Gitlab , Bitbucket etc and quite feasible for any pipeline structure. Also a good user interface is a plus point. The built in automation module is handy to have but I prefer to integrate with Ansible .Other than Jenkins I have worked with CircleCI and TeamCity.

**4. What stages would you have in the CICD pipeline?**

Prod , Stage , Dev and Sandbox. 

**5. What would be the purpose of each stage in CICD pipeline?**

- **Prod** - the stable product runs here and ready to be consumed by end users
- **Stage** - the  integration testing and pre-end users check the product here
- **Dev** - Highly unstable and active for development  for development  users 
- **Sandbox(optional)** - generally a playground for dev to test things out when researching on new ways.