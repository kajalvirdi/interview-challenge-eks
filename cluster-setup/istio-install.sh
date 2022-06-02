#!/bin/sh
curl -L https://git.io/getLatestIstio | ISTIO_VERSION=1.10.3 sh -
cd istio-1.10.3
export PATH="$PATH:$(pwd)/bin"
echo "installing istio..."
echo $PATH
istioctl install --set profile=demo -y
istioctl verify-install
