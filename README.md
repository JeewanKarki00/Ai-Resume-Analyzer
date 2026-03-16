
# AI Resume Analyzer – Kubernetes DevOps Deployment

![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)
![Autoscaling](https://img.shields.io/badge/Kubernetes-HPA-green)
![DevOps](https://img.shields.io/badge/DevOps-Practice-orange)

---

## Overview

This project demonstrates how a backend application can be containerized and deployed using modern DevOps tools.

The backend service is packaged using Docker and deployed on a Kubernetes cluster. Autoscaling is implemented using the Kubernetes Horizontal Pod Autoscaler (HPA), which automatically scales pods based on CPU usage.

The purpose of this project is to showcase practical DevOps skills including containerization, Kubernetes deployments, service networking, ingress configuration, and autoscaling.

---

## Technologies Used

* Docker
* Kubernetes
* Horizontal Pod Autoscaler (HPA)
* Kubernetes Services
* Kubernetes Ingress
* Linux
* Git & GitHub

---

## System Architecture

User
↓
Backend Application (Python)
↓
Docker Container
↓
Kubernetes Deployment
↓
Kubernetes Service
↓
Ingress
↓
Horizontal Pod Autoscaler (HPA)

---

## Features Implemented

* Containerized backend application using Docker
* Kubernetes deployment configuration for managing application pods
* Kubernetes service for internal networking
* Ingress configuration for external access
* Horizontal Pod Autoscaler (HPA) for automatic scaling
* Load generation to demonstrate autoscaling behavior

---

## Kubernetes Resources

The following Kubernetes components are used in this project:

* Deployment
* Service
* Ingress
* Horizontal Pod Autoscaler

---

## Autoscaling Demonstration

The backend service automatically scales when CPU usage exceeds the configured threshold.

Example scaling behavior:

Pods

1 → 2 → 3 → 4 → 5

When the traffic/load decreases, Kubernetes automatically scales the pods back down.

---

## Project Structure

```
ai-resume-analyzer
│
├── backend
│   ├── app.py
│   └── requirements.txt
│
├── docker
│   └── Dockerfile
│
├── kubernetes
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
│
├── screenshots
│
└── README.md
```

---


### Running Pods
<img width="1899" height="1024" alt="Screenshot 2026-03-16 145620" src="https://github.com/user-attachments/assets/76ea9b15-a4f6-4080-b040-eb36a274955f" />
<img width="1910" height="1025" alt="Screenshot 2026-03-16 145732" src="https://github.com/user-attachments/assets/10008477-751d-4a2b-beee-d6f946209a6e" />
<img width="1884" height="804" alt="Screenshot 2026-03-16 150301" src="https://github.com/user-attachments/assets/bf2c667c-3f91-4ce7-ae29-c669d14bc395" />

### Horizontal Pod Autoscaler
<img width="1919" height="1030" alt="Screenshot 2026-03-16 145519" src="https://github.com/user-attachments/assets/17741461-7230-4066-b67f-3b175df4c61c" />

---

## Author

Jeewan Karki
Cloud Analyst | Aspiring DevOps Engineer
