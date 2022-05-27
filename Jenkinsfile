
  
pipeline {
  agent any 
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
    stage('Test') {
            steps {
                /* `make check` returns non-zero on test failures,
                * using `true` to allow the Pipeline to continue nonetheless
                */
                sh 'make check || true' 
                junit '**/target/*.xml'
            }
    }
    
  }
}
