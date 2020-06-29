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
## How to manage credentials in Jenkins?
### Adding Credential to store
1. goto Manage Jenkins > Manage Credentials > System > Global credentials
1. Click Add Credentials to add the credential
###Using the Credential in the Job
1. In the job goto section Build Environment
1. Check Use secret text(s) or file(s)
1. Add Username and Password variables
1. Use the variables in other part of the Job

*Note*
> The secret(s) will be masked (****) in case they are printed to the build log

### Ref.
1. https://support.cloudbees.com/hc/en-us/articles/203802500-Injecting-Secrets-into-Jenkins-Build-Jobs
1. https://www.jenkins.io/doc/pipeline/steps/credentials-binding/

