# Sample App

Containerized application that retrieves metrics server data

## How does it work ?

 The sample app is a Nodejs app that requests the metrics every second and prints that in the console. The deployment creates a service account, roles and role binding to allows this application communicate with the api, this token is stored by default on `/var/run/secrets/kubernetes.io/serviceaccount/token`, the application is reading that token and doing the requests on the endpoint `/apis/metrics.k8s.io/v1beta1/pods` that returns all pod metrics and log it on console.

## Structure
```
sample-app
├── debian
│   └── sample-app.stable_docker_image
├── docker
│   ├── Dockerfile.debian
│   └── src
│       ├── package.json
│       └── sample-application.js
└── readme.md
```
Important files
- src - Contains Nodejs application
- Dockerfile - Application Dockerfile

## Run application
> Deploy tha sample app using `system helm-override-update --reuse-values --set atribute=value <app name> <chart name> <namespace>` follow the steps below:

- Run `system helm-override-update --reuse-values --set sampleApp.create=true metrics-server metrics-server metrics-server`
- Run `system application-apply metrics-server` to apply the override
- Run `kubectl get pods -n metrics-server` to get the name of the pod.
- Run `kubectl logs -n metrics-server <pod-name> --tail 1 -f` to see the logs and check if the sample application is requesting successfully the metrics server api

## Endpoints

All of the following endpoints are GET endpoints and they are under the base path `/apis/metrics.k8s.io/v1beta1`:
 - `/nodes` - all node metrics
- `/nodes/{node}` - metrics for a specified node
- `/namespaces/{namespace}/pods` - all pod metrics within namespace with support for all-namespaces
- `/namespaces/{namespace}/pods/{pod}` - metrics for a specified pod
- `/pods` - all pod metrics of all namespaces
