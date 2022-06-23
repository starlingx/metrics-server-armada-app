# Build variables
%global helm_folder /usr/lib/helm

%global sha e67ee73cfc51e27eaf46b2af0ae8debd16c86d26

Summary: Metrics-server helm chart
Name: metrics-server-helm
Version: 1.0
Release: %{tis_patch_ver}%{?_tis_dist}
License: Apache-2.0
Group: base
Packager: Wind River <info@windriver.com>
URL: https://github.com/kubernetes-sigs/metrics-server#installation

Source0: metrics-server-%{sha}.tgz
Source1: repositories.yaml
Source2: index.yaml
Source3: Makefile

BuildArch:     noarch

Patch01: 0001-Add-sample-app-to-metrics-server.patch

BuildRequires: helm
BuildRequires: chartmuseum

%description
StarlingX Metrics-Server Helm Charts

%prep
%setup -n metrics-server

%patch01 -p1

%build
# Host a server for the charts
chartmuseum --debug --port=8879 --context-path='/charts' --storage="local" --storage-local-rootdir="." &
sleep 2
helm repo add local http://localhost:8879/charts

# Create the tgz file
cd ../
cp %{SOURCE3} ./
make metrics-server

# terminate helm server (the last backgrounded task)
kill %1

%install
cd ../
install -d -m 755 ${RPM_BUILD_ROOT}%{helm_folder}
install -p -D -m 755 *.tgz ${RPM_BUILD_ROOT}%{helm_folder}

%files
%defattr(-,root,root,-)
%{helm_folder}/*

