variable "region" {
  default     = "us-east-2"
}

provider "aws" {
  region = var.region
}

data "aws_availability_zones" "available" {}

provider "kubernetes" {
    host                   = data.aws_eks_cluster.cluster.endpoint
    token                  = data.aws_eks_cluster_auth.cluster.token
    cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
}

locals {
  cluster_name = "demoCluster"
}
