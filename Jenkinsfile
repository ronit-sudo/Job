pipeline {
    agent any

    options {
        timestamps()
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
                    # Compile every .py in the workspace (recursive)
                    found_any=false
                    while IFS= read -r -d "" f; do
                        echo "Compiling $f"
                        python3 -m py_compile "$f"
                        found_any=true
                    done < <(find . -type f -name "*.py" -print0)

                    if [ "$found_any" = false ]; then
                        echo "No Python files (*.py) found in the workspace."
                        exit 1
                    fi
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                    set -e
                    if [ ! -f "coding.py" ]; then
                        echo "coding.py not found at repo root"
                        exit 1
                    fi
                    python3 coding.py --num 8 | tee calc_output.txt
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/__pycache__/**, calc_output.txt', fingerprint: true, allowEmptyArchive: true
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

