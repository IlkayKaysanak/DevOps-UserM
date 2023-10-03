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
                bat 'npm install'
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
                        bat "docker build -t ilkai/devopsuserm:${BUILD_ID} -f Dockerfile ."
                        bat "docker push ilkai/devopsuserm:${BUILD_ID}"
                    }
      }
    }
    }
     stage('Trivy Scan'){
      steps{
            bat "docker run aquasec/trivy image ilkai/devopsuserm:latest"
            }
    }
  }
  
}
