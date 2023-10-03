pipeline {
  agent any

  tools {nodejs "nodejs"}
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
  }
}