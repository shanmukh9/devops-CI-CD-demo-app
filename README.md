# DevOps Bootcamp for Scaler

This repository contains code that was demoed at the Scaler DevOps bootcamp. Please find the slides [here](https://docs.google.com/presentation/d/1uadhfAhfI_cuWs5DsSrkjdZvqxt1LE1fA8c_uhBTSxI/edit?usp=sharing). I'd recommend going through the slides and as you see a slide that says "Demo", switching to this repository and looking at the files.

Contents
========

 * [Git](#git)
 * [Flask](#flask)
 * [Github Actions](#actions)
 * [Docker](#docker)
 * [Heroku](#heroku)
 * [Ansible](#ansible)

#### Git

Installing git: https://github.com/git-guides/install-git
Create a git repo and make your first commit.

#### Flask

https://flask.palletsprojects.com/en/2.0.x/installation/
https://flask.palletsprojects.com/en/2.0.x/quickstart/ 

#### Github Actions
https://github.com/features/actions
Workflows File: https://github.com/asquare14/scaler-bootcamp-app/tree/main/.github/workflows

#### Docker
Installing docker: https://docs.docker.com/get-docker/ 
Some commands used:
```
docker build -t demo-app:latest .
docker run -d -p 5000:5000 demo-app  
```
Docker Repository for this app: https://hub.docker.com/repository/docker/asquare14/demo-app

#### Heroku

Documentation: https://devcenter.heroku.com/articles/github-integration

#### Ansible

Installation: https://docs.ansible.com/ansible/latest/installation_guide/index.html
Sample playbook: https://github.com/asquare14/scaler-bootcamp-app/blob/main/flask.yml
