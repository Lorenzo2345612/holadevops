pipeline {
    agent any

    environment {
        VENV_PATH = "${HOME}/venv/bin/activate"
        TIMESTAMP = sh(script: "date +%Y%m%d%H%M%S", returnStdout: true).trim()
        BRANCH_NAME = "feature-${TIMESTAMP}"
    }

    stages {
        stage('Estandar de código') {
            steps {
                dir('calculadora') {
                    sh '''
                    echo "Estandar de código"
                    source $VENV_PATH
                    flake8 .
                    '''
                }
            }
        }

        stage('Pruebas unitarias') {
            steps {
                dir('calculadora') {
                    sh '''
                    echo "Pruebas unitarias"
                    source $VENV_PATH
                    python3 test_calculadora.py
                    '''
                }
            }
        }

        stage('Realizar pull request') {
            steps {
                dir('calculadora') {
                    script {
                        def timestamp = sh(script: "date +%Y%m%d%H%M%S", returnStdout: true).trim()
                        def branch = "feature/${timestamp}"

                        sh """
                        echo "Realizar pull request"
                        source $VENV_PATH
                        git checkout -b ${branch}
                        git add .
                        git commit -m "Cambios realizados en la calculadora"
                        git push origin ${branch}
                        gh pr create --base main --head ${branch} --title "Cambios realizados en la calculadora" --body "Se han realizado cambios en la calculadora"
                        """
                    }
                }
            }
        }
    }
}
