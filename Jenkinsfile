#!/usr/bin/env groovy
pipeline {
    agent {
        label 'master'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
    }

    environment {
        CONDA_PATH = "${tool 'Miniconda-CPython-3.6'}"
        CONDA_ENV = "mfaas"  
        PATH = "${CONDA_PATH}/bin:fake_bright:${PATH}"  
    }
            
    stages {            
        stage('Initialize') {
            steps {
                sh """
                    source activate ${CONDA_ENV}
                    pip install pipenv
                    pipenv install -e .[dev]
                    """
            }
        }

        stage('Test') {
            steps {
                sh "pipenv run pytest --junitxml report.xml"
                junit "report.xml"
            }
        }
    }
}
