pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8.0-buster'
                }
            }
            steps {
                sh 'python3 setup.py install'
                sh 'python3 -m py_compile ppa1.py ppa2webservice.py'
            }
        }
        stage('Test') {
            agent{
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'pip install mysql-connector'
                sh 'pytest'
            }
        }
    }
}
