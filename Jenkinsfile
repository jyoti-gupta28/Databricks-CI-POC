pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/jyoti-gupta28/Databricks-CI-POC.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python CICD_Pipeline1.py'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline ran successfully!'
        }
        failure {
            echo 'CI/CD Pipeline failed.'
        }
    }
}
