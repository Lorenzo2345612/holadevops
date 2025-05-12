pipeline {
    agent any

    stages {
        stage('Estandar de código') {
            steps {
                dir('calculadora') {
                    sh '''
                    echo "Estandar de código"
                    . ~/venv/bin/activate
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
                    . ~/venv/bin/activate
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
                        . ~/venv/bin/activate
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
