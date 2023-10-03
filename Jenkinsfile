pipeline {
  agent any

  tools {nodejs "nodejs"}

  environment {
    DOCKERHUB_CREDENTIALS = credentials('ilkai-dockerhub')
  }

  stages {
    stage('Checkout') {
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
    stage('Build') {
      steps {
        sh 'docker build -t ilkai/dp-alpine:latest .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push ilkai/dp-alpine:latest'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}