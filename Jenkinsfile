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
                sh 'cd mysql-connector-python-8.0.18 && python3 setup.py install && cd ..'
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
                sh 'pytest'
            }
        }
    }
}
