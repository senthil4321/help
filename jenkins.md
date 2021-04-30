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
### Using the Credential in the Job
1. In the job goto section Build Environment
1. Check Use secret text(s) or file(s)
1. Add Username and Password variables
1. Use the variables in other part of the Job

*Note*
> The secret(s) will be masked (****) in case they are printed to the build log

### Ref.
1. https://support.cloudbees.com/hc/en-us/articles/203802500-Injecting-Secrets-into-Jenkins-Build-Jobs
1. https://www.jenkins.io/doc/pipeline/steps/credentials-binding/

### Dynamic list

#### Ref.
* https://stackoverflow.com/questions/44570163/jenkins-dynamic-declarative-pipeline-parameters
* https://stackoverflow.com/questions/54676040/storing-list-of-values-in-the-environment-variable-in-declarative-jenkins-pipeli
### Set build name
* https://stackoverflow.com/questions/43639099/set-the-build-name-and-description-from-a-jenkins-declarative-pipeline
### How to wait for condition with retry
```groovy

```
#### Ref.
* https://stackoverflow.com/questions/53987649/jenkins-pipeline-waituntil-bash-command-returns-certain-string
### Jenkins scp
* https://stackoverflow.com/questions/44377238/use-ssh-credentials-in-jenkins-pipeline-with-ssh-scp-or-sftp
### Nexus integration - choice parameters
* https://support.cloudbees.com/hc/en-us/articles/217958928-How-to-populate-Choice-Parameter-with-artifact-information-using-Nexus-REST-API-?mobile_site=true

### parameter separator plugin
* https://plugins.jenkins.io/parameter-separator/
* https://stackoverflow.com/questions/44820799/grouping-and-decorating-groups-of-parameters-in-jenkins
### Import nexus certificate
* https://magicmonster.com/kb/prg/java/ssl/pkix_path_building_failed/ 
```
keytool -import -alias nexus -keystore  cacerts -file C:\tmp\nexus.cer
Path jre\lib\security
```
---
### Useful plugin
* URLTrigger Plug-in 
* Active Choices Plug-in
  * Enables dynamic choice
* Maven Artifact ChoiceListProvider (Nexus)
  * Artifact as options
### build status
* https://stackoverflow.com/questions/44022775/jenkins-ignore-failure-in-pipeline-build-step
### jenkins Commit file to git pipeline
```groovy
def readContent = readFile "${env.WORKSPACE}/test.txt"
writeFile file: "${env.WORKSPACE}/test.txt", text: "${readContent} Test Content\n"
bat label: 'git checkout', script: "git checkout master"
bat label: 'git config user', script: "git config user.name \"DemoUSR\""
bat label: 'git config email', script: "git config user.email \"DemoUSR@example.com\""
bat label: 'git status', script: "git status"
bat label: 'git add file', script: "git add ${env.WORKSPACE}/test.txt"
bat label: 'git commit', script: "git commit -am \"Update date to git\""
bat label: 'git push commit to remote', script: "git push https://${GIT_CREDS_USR}:${GIT_CREDS_PSW}@demogiturl.com master"    
```
>> Makesure there is no @ in password
---
### Load groovy and execute (both Jenkinsfile and groovy in same SCM)
``` groovy

```
#### Ref.
* https://stackoverflow.com/questions/37800195/how-do-you-load-a-groovy-file-and-execute-it
---
### Shared Groovy Todo
* https://stackoverflow.com/questions/37800195/how-do-you-load-a-groovy-file-and-execute-it?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* https://www.jenkins.io/blog/2017/02/15/declarative-notifications/
* https://mtijhof.wordpress.com/2019/04/22/jenkins-running-a-declarative-pipeline-from-your-shared-library/
  
## Specify node name
* https://serverfault.com/questions/359793/tell-jenkins-to-run-a-specific-project-on-a-particular-slave-node
* https://stackoverflow.com/questions/44007034/conditional-environment-variables-in-jenkins-declarative-pipeline
> It is possible to use a specific node where the program can run.Even this works in master slave configuraiton
```
node ('My Node') {
    
}
```
## String concatenation
```
def str = "SRK"
println "Full String ${str} " + str ;
```
## new workspace creation issue
> ws automatically amend the prefix "@NUMBER" when the workspace to be used was already occupied by other build job.
```
dir just move current working directory to exactly where you designate
```
## 2 times scm checkout issue

### custom workspace
#### Ref.
* https://stackoverflow.com/questions/44259039/how-to-re-use-previously-created-workspace-across-stages
* https://stackoverflow.com/questions/36934028/get-absolute-path-to-workspace-directory-in-jenkins-pipeline-plugin
* https://stackoverflow.com/questions/54698645/how-to-prevent-jenkins-parallel-stages-in-pipeline-to-create-a-new-workspace
### variable access
```groovy
env.data2= 3
param.data1=2
Hsm

```
### scm checkout
```jenkins
Todo
```
### plugin
```
addShortText(text, color, background, border, borderColor) - puts a badge with a short text, using the specified format.  For Colors supported, Google "html color names".

```
* https://www.w3schools.com/colors/color_tryit.asp?color=CornflowerBlue
* https://plugins.jenkins.io/groovy-postbuild/

### exception handling
```groovy
catch (NoSuchMethodError | java.nio.file.NoSuchFileException e) {
    println("Exception occurred: " + e.toString())  
  }
```
* https://stackoverflow.com/questions/58445522/jenkinsfile-why-java-lang-nosuchmethoderror-no-such-dsl-method-is-not-caught
