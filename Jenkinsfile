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
                    # Check if there is at least one .py file
                    if ! find . -type f -name "*.py" | grep -q .; then
                        echo "No Python files (*.py) found in the workspace."
                        exit 1
                    fi

                    # POSIX-safe compile of every .py file
                    find . -type f -name "*.py" -exec sh -c '
                        for f do
                            echo "Compiling $f"
                            python3 -m py_compile "$f"
                        done
                    ' _ {} +
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                    set -e
                    if [ -f "coding.py" ]; then
                        echo "Running coding.py --num 8"
                        python3 coding.py --num 8 | tee calc_output.txt
                    else
                        # Try to find a calc.py if coding.py doesn't exist
                        CALC_PATH="$(find . -type f -name "calc.py" | head -n 1 || true)"
                        if [ -n "$CALC_PATH" ]; then
                            echo "Running $CALC_PATH --num 8"
                            python3 "$CALC_PATH" --num 8 | tee calc_output.txt
                        else
                            echo "No coding.py or calc.py found. Skipping run."
                            : # no-op
                        fi
                    fi
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
