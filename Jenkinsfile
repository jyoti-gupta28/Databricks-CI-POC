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
                sh 'python3 -m pip install --upgrade pip'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 CICD_Pipeline.py'
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
