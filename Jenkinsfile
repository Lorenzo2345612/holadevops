pipeline {
    agent any

    stages {
        stage('Estandar de codigo') {
            steps {
                sh "
                cd calculadora
                echo 'Estandar de codigo'
                # Activar el entorno virtual
                . ~/venv/bin/activate

                # Ejecutar pruebas de estilo de código
                flake8 .
                "
            }
        }
        stage('Pruebas unitarias') {
            steps {
                sh """
                cd calculadora
                echo 'Pruebas unitarias'
                # Activar el entorno virtual
                . ~/venv/bin/activate

                # Ejecutar pruebas unitarias
                python3 test_calculadora.py
                """
            }
        }
        stage('Realizar pull request') {
            steps {
                sh """
                cd calculadora
                echo 'Realizar pull request'
                # Activar el entorno virtual
                . ~/venv/bin/activate
                # Crear un nuevo branch
                git checkout -b feature/$(date +%Y%m%d%H%M%S)
                # Hacer commit de los cambios
                git add .
                git commit -m "Cambios realizados en la calculadora"
                # Hacer push del branch
                git push origin feature/$(date +%Y%m%d%H%M%S)
                # Crear un pull request
                gh pr create --base main --head feature/$(date +%Y%m%d%H%M%S) --title "Cambios realizados en la calculadora" --body "Se han realizado cambios en la calculadora"
                """

            }
        }
    }
}