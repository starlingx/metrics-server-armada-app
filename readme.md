# Metrics Server Armada App 

This Armada App is responsible to deliver the metrics server inside the ISO.
>Metrics Server is a scalable, efficient source of container resource metrics for Kubernetes built-in autoscaling pipelines.

## Structure
```
metrics-server-armada-app
├── centos_build_layer.cfg
├── centos_iso_image.inc
├── centos_pkg_dirs
├── centos_pkg_dirs_containers
├── centos_stable_docker_images.inc
├── readme.md
├── requirements.txt
├── sample-app
│   ├── centos
│   │   ├── docker
│   │   │   ├── Dockerfile
│   │   │   └── src
│   │   │       ├── package.json
│   │   │       └── sample-application.js
│   │   └── sample-app.stable_docker_image
│   └── readme.md
├── stx-metrics-server-helm
│   ├── centos
│   │   ├── build_srpm.data
│   │   └── stx-metrics-server-helm.spec
│   └── stx-metrics-server-helm
│       ├── files
│       │   ├── index.yaml
│       │   ├── metadata.yaml
│       │   └── repositories.yaml
│       ├── helm-charts
│       │   ├── Makefile
│       │   └── metrics-server
│       │       ├── Chart.yaml
│       │       ├── templates
│       │       │   ├── apiservice.yaml
│       │       │   ├── clusterrole-aggregated-reader.yaml
│       │       │   ├── clusterrolebinding-auth-delegator.yaml
│       │       │   ├── clusterrolebinding.yaml
│       │       │   ├── clusterrole.yaml
│       │       │   ├── deployment.yaml
│       │       │   ├── pdb.yaml
│       │       │   ├── psp.yaml
│       │       │   ├── rolebinding.yaml
│       │       │   ├── serviceaccount.yaml
│       │       │   └── service.yaml
│       │       └── values.yaml
│       └── manifests
│           └── metrics-server_manifest.yaml
├── test-requirements.txt
└── tox.ini
```
Important files
- metrics-server_manifest.yaml - Armada Manifest
- helm-charts - Metrics Server helm charts
- stx-metrics-server-helm.spec - Steps to generate
- centos_iso_image.inc - It inserts the rpm inside the ISO
- centos_pkg_dirs - Folders to build the pkgs
- sample-app - Sample app application

## Install
- Navigate to the path `/usr/local/share/applications/helm/`
- The `metrics-server-1.0-1.tgz` will be present
- Run `system application-upload metrics-server-1.0-1.tgz`
- Run `system application-list` to see if it was uploaded
- Run `system helm-override-update
    --reuse-values --set sampleApp.create=true
    metrics-server metrics-server metrics-server` If you want to deploy the sample app
- Run `system application-apply metrics-server`
- Run` system application-list` to see if it was applied
- Run `kubectl get pods -l app=metrics-server -n metrics-server` to see the pod running




