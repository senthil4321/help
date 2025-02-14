# Jenkins
## Pipeline
> Declarative Pipeline is easy to use compared to scripted pipeline
> Declarative Pipeline can be put in SCM
***
### `when` directive

### Dynamically enable stage during pipeline execution
```groovy
stage('stage1') {
when {
environment name: 'STATUS', value: 'true'
}
steps {
            echo 'stage1'
            script{
            println "Status " + env.STATUS
            }
}
}
stage('stage2') {
when {
environment name: 'STATUS', value: 'false'
}
steps {
            echo 'stage2'
            script{
            println "Status "+ env.STATUS
            env.STATUS = true
            println "Status "+ env.STATUS
            }
}
}
stage('stage3') {
when {
environment name: 'STATUS', value: 'false'
}
steps {
            echo 'stage3'
            script{
                println env.STATUS
            }
}
}
```
***
### Jenkins load pipeline from SCM. How to change the Jenkinsfile location.
Use Script Path `./script/Jenkinsfile`
***
###
* https://gist.github.com/HarshadRanganathan/97feed7f91b7ae542c994393447f3db4
* https://stackoverflow.com/questions/59040218/how-to-ssh-into-a-server-in-jenkinsfile
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
```groovy
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
### loading script file

* https://stackoverflow.com/questions/37800195/how-do-you-load-a-groovy-file-and-execute-it
### bat 
Using '@' before bat command prevents command echo. 
```* https://stackoverflow.com/questions/35043665/change-windows-shell-in-jenkins-from-cygwin-to-git-bash-msys
@dir
```
## passing parameter to downstram job

```groovy
booleanParam(name: 'SCM_CHECKOUT', value: true)
//For choice parameter use String
string(name: 'SRK_CHOICE', value: "Master")
```
#### Ref.
* https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/#-build-%20build%20a%20job
* https://stackoverflow.com/questions/37025175/how-to-pass-boolean-parameter-value-in-pipeline-to-downstream-jobs
### Sample pipeline script
* https://gist.github.com/merikan/228cdb1893fca91f0663bab7b095757c
### Lessons learned
1. It requires two checkouts for loading data from file using groovy script. Example loading data for parameter list. This is because load parameter script gets executed before scm checkout.First checkout downloads the new files and second check out loads data from file for next run.
1. when block - All condition should be true for the stage to get executed
1. Take care of new workspace when using node block in calling functions. One node declaration per call seems to work good. 
1. `when` string hadling read documentation. 'false' and '0' are considered as true
1. While passing string parameter to downstream job, string parameter value should be one of the item in choice list of downstram job. Passing non choice item results in error.
1. It does not worth learning poorly designed interface. The best thing to do is to circumvent the limitation. Eg. Pasing quoted string to sed from `adb shell` executed from jenkins.
1. It is possible to use groovy ide for debugging and testing Jenkins groovy script
### git bash Jenkins
* https://stackoverflow.com/questions/35043665/change-windows-shell-in-jenkins-from-cygwin-to-git-bash-msys
### Jenkins build every 2 hours
```
H H/2 * * *
```
`H` option produces even load. 
```
H/15 * * * * - every fifteen minutes (perhaps at :07, :22, :37, :52):
H(0-29)/10 * * * * - every ten minutes in the first half of every hour (three times, perhaps at :04, :14, :24)
H 9-16/2 * * 1-5 - once every two hours every weekday (perhaps at 10:38 AM, 12:38 PM, 2:38 PM, 4:38 PM)
H H 1,15 1-11 * - once a day on the 1st and 15th of every month except December
```
#### Ref. 
* https://stackoverflow.com/questions/19443732/configure-cron-job-to-run-every-15-minutes-on-jenkins/21939671#21939671
### post always
Post always section can be added to stage or after all stages
```groovy
Todo
```
### sonar analyser
Sonar analyser mvn plugin will push the analysis to sonar server. 
```bash
mvn sonar:sonar -Dsonar.login=<myAuthenticationToken> -Dsonar.site=<URL>
```
1. Create sonar property file in java project
1. Run the `mvn sonar:sonar` command to push the analysis
## Jenkins configure dynamically Node name
```groovy
pipeline {
    agent {
        node {
            label "${NODE_LABEL}"
        }
    }

    parameters {
        choice(name: 'NODE_LABEL', choices: ['DEMO||DEMO_LOCAL'], description: 'Set the node to run')
```

### Ref.
* https://stackoverflow.com/questions/53822658/execute-a-job-when-node-connect-itself-to-jenkins
## reply
> Replay runs the pipeline script with modification. The replay script allows for quick modification and execution of existing script without changing the pipeline configuration or creating a new commit. 
### Ref .
* https://www.jenkins.io/doc/book/pipeline/development/
## agent node config
Multiple ways of specifying the agent, label
```groovy
Agent available tags
any, docker, dockerfile, kubernetes, label, none
```

label
Execute the Pipeline, or stage, on an agent available in the Jenkins environment with the provided label. For example: agent { label 'my-defined-label' }
Label conditions can also be used. For example: agent { label 'my-label1 && my-label2' } or agent { label 'my-label1 || my-label2' }

node
agent { node { label 'labelName' } } behaves the same as agent { label 'labelName' }, but node allows for additional options (such as customWorkspace).

### Refer the documentation
* https://www.jenkins.io/doc/book/pipeline/syntax/

## Stage Level - Agent config
```groovy
pipeline {
agent { node { label 'Linux1' } }
options {
        timeout(time: 45, unit: 'MINUTES')
    }
    stages {
        stage ("Stage1 Linux") {
         agent {
            label 'Linux1'
        }
          steps {
              sh 'uptime'
          }
       
        }
        stage ("Stage 2 Windows") {
         agent {
            label 'Windows1'
        }
          steps {
              bat 'dir'
          }
       
        }        
    }
}
```
## Running a step in diffent Agent Node
```groovy
pipeline {
agent {
node {
label 'Linux1'
}
}
options {
        timeout(time: 45, unit: 'MINUTES')
    }
    stages {
        stage ("Running Step in Linux1 and Windows1") {
            steps {
                sh 'hostname'
                node('Linux1') {
                    sh 'uptime'
                }                
                node('Windows1') {
                    bat "dir"
                }
            }
        }
    }
}
```
### Ref.
* https://stackoverflow.com/questions/48284128/run-jenkins-stage-on-different-nodes
* https://stackoverflow.com/questions/44870978/how-to-run-multiple-stages-on-the-same-node-with-declarative-jenkins-pipeline

## Runing Parallel stages and stages within stage
* https://www.jenkins.io/blog/2018/07/02/whats-new-declarative-piepline-13x-sequential-stages/
### groovy return multiple items
```groovy
node {
    obj = parsePath(path)
    path1 = obj.path1
    path2 = obj.path2
}

def parsePath(String path)
{
    return [path1:path.toLower(), path2:path.toUpper()]
}
```
* https://stackoverflow.com/questions/6757539/how-to-accept-multiple-parameters-from-returning-function-in-groovy
## groovy generic param to function
```groovy
def demo(def data)
{
println(data)
}
```
## loading groovy script from file
```groovy
        stage('Set Env') {
            steps {
                script{
                    env.ID = params.ID
                    // Load script from file
                    def util = load "${env.WORKSPACE}/GetData.groovy"
                    util.printTest()
                    println("Groovy script loading success ")
                }
            }
        }
```
### input
* https://stackoverflow.com/questions/42501553/jenkins-declarative-pipeline-how-to-read-choice-from-input-step
---
## pipeline-parameters
* https://devopscube.com/declarative-pipeline-parameters/
## use-def-in-jenkins-pipeline
* https://stackoverflow.com/questions/47216731/how-can-i-use-def-in-jenkins-pipeline
