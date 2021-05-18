# Junit
## TODO
1. How to handle parameterised test in junit5?
1. How to organise test class and Test method?
1. How to Name test class and test method?
1. How to write Test Driven Development code ?
## Ref. 
<TODO> Add reference to the example java project which shows the Test and Code linking.
## Junit5 RUN test once per test run

### Ref.
* https://github.com/junit-team/junit5/pull/19

###
> you can use both, Hamcrest and AssertJ, in JUnit5. Both frameworks have a simple assertThat method, that you can import and use if wanted.
Currently, we do not plan to support these frameworks within our own Assertions to avoid the dependencies. Still, one can use them very well.
####
* https://stackoverflow.com/questions/43280250/how-do-i-use-hamcrest-with-junit-5-when-junit-5-doesnt-have-an-assertthat-fun
### AssertJ - fluent assertions java library
#### 
```
assertThat(frodo.age).isEqualTo(33);
```
### command line running
```
* https://mkyong.com/junit5/junit-5-tagging-and-filtering-tag-examples/
```
### wait
* https://stackoverflow.com/questions/15938538/how-can-i-make-a-junit-test-wait

### todo
Grafana, influxdb and junit
```
```
### repeat failed test
* https://github.com/artsok/rerunner-jupiter

### Why not to use test inheritance and use extension
* https://medium.com/decisionbrain/factor-test-code-the-junit-5-way-that-is-without-inheritance-9ba2784d34

### Method Order
* https://stackoverflow.com/questions/54947645/junits-testmethodorder-annotation-not-working
### lessons learned
1. Method Order works after adding class level order annotation

### Parallel run
Parallel test run is enabled by an entry in test configuration file.
```
```
* 
### dynamic test
```
```
* 
### Parameterised test
```
```
### Extension
It is possible to use extension in another extension
