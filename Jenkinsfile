pipeline {
    agent any

    options {
        timestamps()
        ansiColor('xterm')
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
                    find sources -name "*.py" -print -exec python3 -m py_compile {} \\;
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

        // Uncomment if you add pytest and tests/
        // stage('Test') {
        //     steps {
        //         sh '''
        //             set -e
        //             python3 -m pip install --user pytest
        //             pytest -q --maxfail=1
        //         '''
        //     }
        // }

        stage('Archive Artifacts') {
            steps {
                // Archive compiled bytecode and any outputs
                sh 'mkdir -p dist && cp -r __pycache__ dist/ 2>/dev/null || true'
                archiveArtifacts artifacts: 'dist/**, calc_output.txt', fingerprint: true
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
``
