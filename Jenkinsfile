pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('9f2f1f2b-0707-48d0-ae49-3bc48a90bc89')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t shanmukh9/my-demo-app:latest .  --network=host'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push shanmukh9/my-demo-app:latest'
			}
		}
	
	
	stage('Deploy on agent') {
             
            steps 
   {
                sh "docker run -d -p 7000:5000 shanmukh9/my-demo-app"
 
            }
        }
		
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
