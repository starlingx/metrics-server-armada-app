# Metrics Server Armada App 

This Armada App is responsible to deliver the metrics server inside the ISO.
>Metrics Server is a scalable, efficient source of container resource metrics for Kubernetes built-in autoscaling pipelines.

## Structure
```
metrics-server-armada-app
├── debian_build_layer.cfg
├── debian_iso_image.inc
├── debian_pkg_dirs
├── debian_stable_docker_images.inc
├── metrics-server-helm
│   ├── debian
│   │   ├── deb_folder
│   │   │   ├── changelog
│   │   │   ├── control
│   │   │   ├── copyright
│   │   │   ├── metrics-server-helm.install
│   │   │   └── rules
│   │   └── meta_data.yaml
│   └── files
│       ├── 0001-Add-sample-app-to-metrics-server.patch
|       ├── 0002-Add-label-platform-application-to-pods.patch
│       └── Makefile
├── readme.md
├── requirements.txt
├── sample-app
│   ├── debian
│   │   └── sample-app.stable_docker_image
│   ├── docker
│   │   ├── Dockerfile.debian
│   │   └── src
│   │       ├── package.json
│   │       └── sample-application.js
│   └── readme.md
├── stx-metrics-server-helm
│   ├── debian
│   │   ├── deb_folder
│   │   │   ├── changelog
│   │   │   ├── control
│   │   │   ├── copyright
│   │   │   ├── rules
│   │   │   ├── source
│   │   │   │   └── format
│   │   │   └── stx-metrics-server-helm.install
│   │   └── meta_data.yaml
│   └── stx-metrics-server-helm
│       ├── files
│       │   ├── Makefile
│       │   └── metadata.yaml
│       ├── fluxcd-manifests
│       │   ├── base
│       │   │   ├── helmrepository.yaml
│       │   │   ├── kustomization.yaml
│       │   │   └── namespace.yaml
│       │   ├── kustomization.yaml
│       │   └── metrics-server
│       │       ├── helmrelease.yaml
│       │       ├── kustomization.yaml
│       │       ├── metrics-server-static-overrides.yaml
│       │       └── metrics-server-system-overrides.yaml
│       └── helm-charts
│           └── Makefile
├── test-requirements.txt
└── tox.ini
```
Important files
- metrics-server_manifest.yaml - Armada Manifest
- helm-charts - Metrics Server helm charts
- stx-metrics-server-helm.spec - Steps to generate
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




