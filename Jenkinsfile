pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('mycreds')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t my-demo-app:latest .  --network=host'
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
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
