pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               
                git branch: 'main', url: 'https://github.com/rashmi2203/Handwritingrec.git'
            }
        }

        stage('Build') {
            steps {
               
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
