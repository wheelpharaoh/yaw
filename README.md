# yaw
yet another webserver

## patterns
- [X] Documentation
- [X] Style
- [X] Unit Tests
- [X] gitOps
- [X] IaC
- [X] CI
- [X] Packaging
- [X] Containerization
- [X] Multi-Stage Buils
- [X] CD
- [X] k8s
- [X] Observability
- [X] Logs
- [ ] Metrics
- [ ] Dashboards
- [ ] Alerts

## Installation

### prereq
docker, k8s, helm, nektos/act (optional)

## Build
```sh
docker build -t yaw:0.1.0 -f ./app/Dockerfile ./app/
```

## Deploy
```sh
helm install yaw pkg/chart --values pkg/chart/values.yaml --create-namespace --namespace yaw
```

## Usage

Simple Fibonacci web server.

Query for Fibonacci numbers using the following commands:

```sh
curl http://$NODE_IP:$NODE_PORT?n=4
```
or

```sh
docker run --rm --name yaw -p 8000:8000 yaw:0.1.0
curl localhost:8000?n=4
```

## CICD

### github actions
```sh
act -s GITHUB_TOKEN=$GITHUB_TOKEN \
-P self-hosted=catthehacker/ubuntu:act-22.04 \
--container-architecture linux/amd64 \
pull_request
```
