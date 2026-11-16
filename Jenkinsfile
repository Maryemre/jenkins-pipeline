
pipeline {
    agent any

    stages {

        stage('Installation du projet') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Lancement des tests') {
            steps {
                bat 'python -m pytest tests/ -v'
            }
        }

    }
}
