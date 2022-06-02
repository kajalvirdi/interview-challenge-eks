resource "null_resource" "init_operator" {
  provisioner "local-exec" {
    command = "/bin/bash istio-install.sh"
  }
}
