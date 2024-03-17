pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from version control
                git branch: 'main', url: 'https://github.com/rashmi2203/Handwritingrec.git'
            }
        }

        stage('Build') {
            steps {
                // Build Docker image
                script {
                    docker.build("hello-world")
                }
            }
        }

        stage('Test') {
            steps {
                // Run tests if applicable
                script {
                    docker.image("hello-world").run("-p 5000:5000 --name flaskapp-test -e ENVIRONMENT=test").stop()
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy Docker container
                script {
                    docker.image("hello-world").run("-p 5000:5000 --name flaskapp -d")
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}
