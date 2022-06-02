
in-progress....
# Technical challenge assignment.

1. Setup a Kubernetes cluster on an infrastructure of your choice ( EKS/AKS, ) or your own environment
2.Install Istio service mesh on the Kubernetes Cluster created in step 1.
3. Debug and deploy a sample application (https://github.com/aztec-se-adp/crp2-tech-challenge) into the created cluster with service mesh enabled for the application.
4. Implement a Python or Golang app / script to perform a periodically health-check for the cluster/apps  e.g.: usage of the pods (cpu,memory), status of pod/node ..etc without using kubectl if possible.
5.cAll the tasks above must be managed in the automation manner / infrastructure as code / configuration as code using terraform.
6.cDescribes all the steps above (includes difficulty and challenging) in the README.md file and push it along with the source code above to your public GitHub repository and share the link with us in advance so that we can schedule the next interview session.
7. In the next interview session, we will discuss and review this technical challenge. Ideally, the environment would be created again before the interview if there are any questions we want to discuss on the live system.




## Setup Cluster

```bash

#### check terraform version
terrsform verion

## configure aws
---aws configure 

cd cluster-setup

terraform init -upgrade
terraform plan -out terraform.plan
terraform apply terraform.plan


#### Check status of the cluster
aws eks --region us-east-2 describe-cluster --name demoCluster --query cluster.status  
 ---> "ACTIVE"

## Verify istio
 kubectl get pods -n istio-system


```

---aws configure 


 
