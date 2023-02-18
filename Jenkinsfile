pipeline {
     agent any
     stages{
         stage('Clone Git '){
             steps{
             echo 'This is Downloading stage'
             git 'https://github.com/umaaravindan/Jenkins_Sample.git'
         }
         }
     stage('Build'){
         steps{
             echo ' THis is Building stage'
             sh "chmod u+x num1.py"
             
         }
     }
     stage('Testing'){
         steps{
             echo ' THis is testing stage'
             sh "./num1.py 10 20 1"
         }
     }
     stage('Deploy'){
         steps{
             echo ' THis is testing stage'
         }
     }
     stage('Monitor'){
         steps{
             echo ' THis is testing stage'
         }
     }
     }
}
