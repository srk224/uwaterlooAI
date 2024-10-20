pipeline {
    agent any

    environment {
        VERCEL_TOKEN = credentials('VERCEL_TOKEN') 
        PYTHON_VERSION = '3'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                git branch: 'main', url: 'https://github.com/srk224/uwaterlooAI'
            }
        }

        stage('Set up Python') {
            steps {
                echo 'Setting up Python environment...'
                sh """
                python${PYTHON_VERSION} -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Deploy to Vercel') {
            steps {
                echo 'Deploying to Vercel...'
                withCredentials([string(credentialsId: 'VERCEL_TOKEN', variable: 'VERCEL_TOKEN')]) {
                    sh """
                    # Authenticate with Vercel using the provided token
                    vercel login --token $VERCEL_TOKEN
                    # Deploy the project to production
                    vercel --prod --confirm --token $VERCEL_TOKEN
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up environment...'
            sh 'deactivate || true'
            sh 'rm -rf venv'
        }
        success {
            echo 'Deployment to Vercel successful!'
        }
        failure {
            echo 'Deployment failed. Please check the logs for errors.'
        }
    }
}
