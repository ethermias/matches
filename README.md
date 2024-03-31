# matches

# TDD
https://testdriven.io/blog/fastapi-crud/

## Create Folder Structure 
mkdir backend
mkdir backend/app backend/tests
mkdir backend/app/api backend/app/core
touch .flake8 .gitignore docker-compose.yml README.md
touch backend/.env backend/Dockerfile backend/requirements.txt

Not too bad. We’ll add more in a minute, but for now only four packages:

fastapi - the framework we’re using to build this backend
uvicorn - the ASGI server we’ll use to serve up our app
pydantic - validation library baked into fastapi that we’ll use to handle data models at different stages throughout our application
email-validator - allows pydantic to validate emails

A few interesting things going on here. We have a factory function that returns a FastAPI app with cors middleware configured. Don’t worry too much about the cors stuff - this is a rabbit hole that I don’t feel like diving into at the moment. If you want to read more, MDN has some great docs on it.

You’ll also notice we’re importing this middleware from the starlette package. FastAPI is built on top of starlette, and we’ll occasionally dip into the underlying architecture to accomplish a few things. Just a heads up. You don’t need to worry too much about this either, but feel free to checkout the docs here if you want to learn more.

A few things going on here

We’re setting up our first service - server - and telling it to build using the Dockerfile we just defined.
We’re saving the backend files to volume. More on this later.
We’ll serve up our application with uvicorn, and host the backend on localhost:8000.
All other environment variables will be taken from our .env file.
And finally - lets build our docker container and get our server up and running.

https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c

url1 = "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/teams/"


## Deploy to AWS
## EC2
// start here 
sudo yum update -y
sudo yum clean all
# sudo yum install epel-release

sudo yum install docker -y
sudo yum update  -y
sudo systemctl start docker
sudo systemctl enable docker
docker --version
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

sudo yum install git -y
git --version
git clone https://github.com/ethermias/matches.git
cd matches
git clone https://github.com/ethermias/matchesui.git
cd matchesui
change API_URL
sudo docker-compose up -d --build
sudo docker-compose logs -f -t --tail 30
sudo docker-compose down

Steps and Commands:

(This assumes you have 3 servers up and running)

1. On each server, install Docker
(Installation guide: https://docs.docker.com/engine/instal...)
curl -fsSL https://download.docker.com/linux/ubu... | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce

2. On each server, install kubernetes
(Installation guide: https://kubernetes.io/docs/setup/prod...)
curl -s https://packages.cloud.google.com/apt... | sudo apt-key add -
cat &lt&lt EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl

3. On each server, enable the use of iptables 
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

4. On the Master server only, initialize the cluster
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

(After this command finishes, copy kubeadm join provided)

5. On the Master server only, set up the kubernetes configuration file for general usage
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

6. On the Master server only, apply a common networking plugin. In this case, Flannel
kubectl apply -f https://raw.githubusercontent.com/cor...

7. On the Worker servers only, join them to the cluster using the command you copied earlier. 
kubeadm join 172.31.37.80:6443 --token ... --discovery-token-ca-cert-hash ...

And that's it! You should now have a working kubernetes cluster!

--- 
Great resources I used to learn how to work with Kubernetes:
1. Linux Academy (https://linuxacademy.com/)
2. Udemy: Docker and Kubernetes: The Complete Guide (https://www.udemy.com/course/docker-a...)
3. Kubernetes Documentation (https://kubernetes.io/docs/home/)
4. Just play with it!

## How to switch from Route53 from S3 static to kubernetes pods 

