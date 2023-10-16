pipeline {
   agent any

  tools {nodejs "nodejs"}

  environment {
    DOCKERHUB_CREDENTIALS = credentials('ilkai-dockerhub')
  }

  stages {
    stage('Clone Repo') {
      steps {
        git branch: 'main', url: 'https://github.com/IlkayKaysanak/DevOps-UserM.git'
      }
    }
    stage('Install Dependencies') {
            steps {
                sh 'npm install'
                sh 'pip install selenium'
                //sh 'apt-get update'
                //sh 'apt-get install -y chromium-driver'
            }
            
        }

    stage('Snyk Scan') {
        steps{
        snykSecurity organisation: 'ilkaykaysanak', projectName: 'DevOps-UserM', severity: 'medium', snykInstallation: 'Snyk', snykTokenId: 'snyk-token', targetFile: 'package.json'
        }
    }
    stage('Build Image') {
      steps {
         script {
                    withDockerRegistry(credentialsId: 'ilkai-dockerhub') {
                        sh "docker build -t ilkai/devopsuserm:latest -f Dockerfile ."
                        sh "docker build -t ilkai/mysql-database:latest -f Dockerfile2 ."
                        sh "docker push ilkai/devopsuserm:latest"
                        sh "docker push ilkai/mysql-database:latest"
                        sh "docker pull selenium/standalone-chrome"
                        sh "docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome"
                    }
      }
    }
    }
 stage('Trivy Scan'){
      steps{
            sh "docker run aquasec/trivy image ilkai/devopsuserm:latest"
            }
    }
    stage('Deploy to test cluster') {
            steps {
                
                script {
                     sh "gcloud auth activate-service-account --key-file=/var/lib/jenkins/jenkins-sa.json"
                     sh "gcloud container clusters get-credentials ilkaicluster --zone us-central1-c --project cogent-bison-401008"
                    
                     sh 'kubectl apply -f dev-deployment.yaml'
                     sh 'kubectl apply -f mysql-deployment.yaml'
                     
                   
                }
            }
        }
         
        stage('Run Selenium Test') {
            steps {
                
                sh 'python3 test.py '
            }
        }
      /* stage('Prod Repo'){
        // yukardaki işlemlerin aynısı olucak 
       }
       stage('Prod k8s'){
        // yukardaki işlemlerin aynısı olucak
       }
       stage('Kasten Install'){
        
        steps {
                
                script {
                     sh "helm repo add kasten https://charts.kasten.io/ "
                     sh "kubectl create namespace kasten-io"
                    
                     sh 'helm install k10 kasten/k10 --namespace=kasten-io'
                     sh 'helm upgrade k10 kasten/k10 --namespace=kasten-io \
    --reuse-values \
    --set externalGateway.create=true \
    --set auth.tokenAuth.enabled=true'
                     
                   
                }
            }
       }
       */
       stage('Kasten Backup') {
            steps {
                
                sh "gcloud auth activate-service-account --key-file=/var/lib/jenkins/jenkins-sa.json"
                sh "gcloud container clusters get-credentials ilkaicluster --zone us-central1-c --project cogent-bison-401008"
                sh 'kubectl apply -f kasten-backup.yaml'
            }
        }
  }
  
}






