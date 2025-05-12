Branch git commands
#get all branches
git branch -r  

#create a new branch
git checkout -b feature/agent 

#switch to new branch
git checkout new_branch 

#sync remote and local branch
git fetch --all -Pp


brew install python3
python3 --version

Agent related
pip install google-adk

python -m venv venv && source venv/bin/activate
pip install agent-starter-pack


Preparation to create virtual environment
sudo apt update
sudo apt install python3.12-venv

Create Virtual environment 
python3 -m venv .venv   
source .venv/bin/activate
pip install -r requirements.txt  

Reactivate Virtual environment
# Deactivate the current (broken) environment
rm -rf .venv       # Delete the .venv directory (use appropriate command for your OS)
python3 -m venv .venv  # Recreate the virtual environment
source .venv/bin/activate  # Reactivate
Install pip (If Missing): After recreating the virtual environment, install pip explicitly:
pip install -r requirements.txt  

g Cloud login


gcloud auth login
gcloud config set project demoproject-436108


Port 8080 is in use by another program. 
lsof -i:8080
kill <PID>

SQl Proxy 
curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.14.3/cloud-sql-proxy.linux.amd64
chmod +x cloud-sql-proxy./cloud-sql-proxy demoproject-436108:europe-north1:demo &

Killing open proxy
ps aux | grep cloud-sql-proxy
Kill PID 

https://cloud.google.com/sql/docs/mysql/connect-auth-proxy#macos-64-bit


Setup dev env
Install VScode
install docker
https://docs.docker.com/desktop/install/mac-install/

Installing brew
https://brew.sh/

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install git 

https://git-scm.com/download/mac
$ brew install git
 git config --global user.email "laleha@google.com"
 git config --global user.name "Laleh"

https://www.youtube.com/watch?v=i_23KUAEtUM

Set up python 
https://code.visualstudio.com/docs/python/python-tutorial
Install gcloud 
https://cloud.google.com/sdk/docs/install

******************************
 Build and test docker 

docker build -t hello-world-image .
docker run -it hello-world-image




Deploy to cloud run

gcloud auth login
export PROJECT_ID=cloudrun-375213
gcloud auth configure-docker europe-docker.pkg.dev
docker build -t europe-docker.pkg.dev/$PROJECT_ID/repos/helloimage  .
docker push europe-docker.pkg.dev/$PROJECT_ID/repos/helloimage:latest

gcloud run deploy hello-world --image europe-docker.pkg.dev/$PROJECT_ID/repos/helloimage:latest  --region europe-north1






gcloud config list


Cloud build  , deploy 
Sql connection—> can 
Secret manager  database
Call Gemini API
Connect to  memory instance , store in redis 


