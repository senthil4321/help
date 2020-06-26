# Jenkins
## Pipeline
> Declarative Pipeline is easy to use compared to scripted pipeline
> Declarative Pipeline can be put in SCM
***
### `when` directive

***
### Jenkins load pipeline from SCM. How to change the Jenkinsfile location.
Use Script Path `./script/Jenkinsfile`
***
###
https://gist.github.com/HarshadRanganathan/97feed7f91b7ae542c994393447f3db4
https://stackoverflow.com/questions/59040218/how-to-ssh-into-a-server-in-jenkinsfile
***
### Jenkins Declarative pipeline defining credential
```groovy
 environment {
                DATA = credentials('NAME_OF_THE_DEFINITION')
            }
```
How to access the environment variable?
```
%DATA%
```
***

### when condition
> There can be only one steps block inside stage. Condition can enable /
disable all the steps in the block.
```
pipeline {
    agent any
    parameters {
        choice(
            choices: ['greeting' , 'silence'],
            description: '',
            name: 'REQUESTED_ACTION')
    }
    stages {
        stage ('Speak') {
            when {
                // Only say hello if a "greeting" is requested
                expression { params.REQUESTED_ACTION == 'greeting' }
            }
            steps {
                echo "Hello, greeting!"
            }
        }
    }
}
```
Ref.
1. https://www.jenkins.io/blog/2017/01/19/converting-conditional-to-pipeline/
***
