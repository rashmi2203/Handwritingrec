pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'hello-world'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git 'https://github.com/rashmi2203/Handwritingrec.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(env.DOCKER_IMAGE_NAME)
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Add any testing steps here if needed
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.example.com', 'd2c94e258dcb') {
                        docker.image(env.DOCKER_IMAGE_NAME).push()
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up any resources or perform additional post-build steps here
            }
        }
    }
}
