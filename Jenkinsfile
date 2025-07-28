pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = credentials('Github-token2')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'feature/login',
                    credentialsId: "${GIT_CREDENTIALS}",
                    url: 'https://github.com/jyoti-gupta28/Databricks-CI-POC.git'
            }
        }
        stage('Run Python Script'){
            steps{
                bat 'python CICD_Pipeline.py'
            }
        }
        stage('Run Python script'){
            steps{
                bat 'python DBN.py'
            }
        }
    }

    post {
        failure {
            echo 'CI/CD Pipeline failed.'
        }
        success {
            echo 'CI/CD Pipeline succeeded!'
        }
    }
}
