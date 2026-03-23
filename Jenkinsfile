pipeline {
    agent any

    options {
        timestamps()
        // Removed ansiColor('xterm')
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    set -e
                    python3 --version
                    which python3 || true
                '''
            }
        }

        stage('Build (Compile)') {
            steps {
                sh '''
                    set -e
                    # Compile all Python files under sources/
                    if [ -d sources ]; then
                        find sources -name "*.py" -print -exec python3 -m py_compile {} \\;
                    else
                        echo "Directory 'sources' not found. Adjust path or create it."
                        exit 1
                    fi
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                    set -e
                    # Run with a number argument; change as needed
                    python3 sources/calc.py --num 8 | tee calc_output.txt
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                // Archive __pycache__ wherever they are + output file
                archiveArtifacts artifacts: '**/__pycache__/**, calc_output.txt', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Build failed. Check logs above.'
        }
    }
}
