## sonarqube
> sonarqube has or uses pmd, codestyle findbug 
* https://stackoverflow.com/questions/5479019/is-sonarqube-replacement-for-checkstyle-pmd-findbugs
## Mechanism
1. Sonarqube mvn plugin analysis the java source code locally and pushes the analysis data to the server.
1. Analysis results are stored in server
## Configuration 
1. Create sonar property file in the java project
1. Run mvn goal with server URL to analyse and push the results to the server
