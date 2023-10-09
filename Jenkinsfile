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
    stage('NPM Install') {
            steps {
                sh 'npm install'
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
                     sh "gcloud container clusters get-credentials ilkaicluster --zone us-central1 --project cogent-bison-401008"
                     sh 'kubectl apply -f mysql-deployment.yaml'
                     sh 'kubectl apply -f dev-deployment.yaml'
                    
                   
                }
            }
        }
  }
  
}



