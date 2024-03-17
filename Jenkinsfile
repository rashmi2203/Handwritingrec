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
                // Build Docker image with a unique tag
                script {
                    def dockerTag = "handwri:${BUILD_NUMBER}" // Use build number as tag
                    docker.build(dockerTag)
                }
            }
        }

        // Other stages omitted for brevity
    }

    post {
        success {
            // Archive Docker image as an artifact
            archiveArtifacts(artifacts: '*.tar.gz', allowEmptyArchive: true)
        }
    }
}
