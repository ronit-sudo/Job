pipeline {
    agent any

    environment {
        // Define Python version and virtual environment path
        PYTHON = 'python3'
        VENV_DIR = '.venv'
    }

    options {
        // Keep build logs for 30 days
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        // Fail the build if any stage takes more than 30 minutes
        timeout(time: 30, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull latest code from SCM
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh """
                    ${PYTHON} -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Lint') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    pip install flake8
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                """
            }
        }

        stage('Test') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    pip install pytest
                    pytest --maxfail=1 --disable-warnings -q
                """
            }
        }

        stage('Package') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    python setup.py sdist bdist_wheel
                """
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    echo "Deploying application..."
                    # Example: pip install twine && twine upload dist/*
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            sh "rm -rf ${VENV_DIR}"
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}

