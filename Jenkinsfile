pipeline {
    agent any

    environment {
        VERCEL_TOKEN = credentials('VERCEL_TOKEN') // Vercel Token stored in Jenkins Credentials
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
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }


        stage('Deploy to Vercel') {
            steps {
                echo 'Deploying to Vercel...'
                withCredentials([string(credentialsId: 'VERCEL_TOKEN', variable: 'VERCEL_TOKEN')]) {
                    sh """
                    vercel --token $VERCEL_TOKEN --prod --confirm --cwd .
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'deactivate || true'
        }
        success {
            echo 'Deployment to Vercel successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
