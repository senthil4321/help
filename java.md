# Java
## TODO
 - [ ] Stream map
 - [ ] Supplier Consumer
 - [ ] Collection
 - [ ] Autoclosable
 - [ ] Method Reference
 - [ ] Anonymous Inner class
 - [ ] Anonymous Function
 - [ ] Functional Interfaces

## Example
```java
Optional<T> max(Comparator<? super T> comparator)

Employee maxId = employees.stream()
    .max(new Comparator<Employee>() {
        @Override
        public int compare(Employee e1, Employee e2) {
            return e1.getId() - e2.getId();
        }
    }).orElse(Employee.DEFAULT_EMPLOYEE);

// Anonymous inner class implementation of Comparator<Object>
Employee maxName = employees.stream()
    .max(new Comparator<Object>() {
        @Override
        public int compare(Object o1, Object o2) {
            return o1.toString().compareTo(o2.toString());
        }
    }).orElse(Employee.DEFAULT_EMPLOYEE);
```
## Anonymous Inner class

Anonymous inner classes are very handy when you need to implement an interface which may not be highly reusable (and therefore not worth refactoring to its own named class). An instructive example is using a custom java.util.Comparator<T> for sorting.
```
TODO Add example
```
### Ref.
https://stackoverflow.com/questions/2755445/how-can-i-write-an-anonymous-function-in-java
## Stream
### Stages
1. Source
1. Intermediate
   1. filter
1. Terminal
   1. collect
## Method Reference
It is possible to replace lambda with method reference if argument type and return type matches
```
TODO code
```
### Kinds of Method References
1. Reference to a Constructor
### Ref.
1. https://www.baeldung.com/java-8-functional-interfaces
1. https://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html
## Functional Interfaces
 > Functional interfaces provide target types for lambda expressions and method references.[java.util.function](https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html)
1. Function
 > Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.
[Function](https://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html)
1. Supplier
1. Consumer
1. Predicate
1. Operator
   * Code 
 ```java
    List<String> numList = Arrays.asList("one", "two", "three");
    UnaryOperator<String> unaryOperator = data -> data.toUpperCase();
    numList.replaceAll(unaryOperator);
 ```
### Todo
Lazy generalization

## Bit Operation
### bit mask generation
```
int mask |= 1 << 4;
```
### bitset api java.util.BitSet

```java

```

### Ref.
1. http://sys.cs.rice.edu/course/comp314/10/p2/javabits.html
## jshell
Jshell instraduced in java 9 provides Read Eval Process Loop
## toString
TODO
1. https://stackoverflow.com/questions/16527932/ok-to-use-json-output-as-default-for-tostring/39089678
## Ref.

 1. https://www.javatpoint.com/java-8-method-reference
 1. https://www.baeldung.com/java-8-collectors
 1. http://tutorials.jenkov.com/java-collections/map.html#implementations
 1. https://www.google.com/amp/s/www.geeksforgeeks.org/stream-map-java-examples/amp/
 1. https://stackoverflow.com/questions/52532565/what-are-practical-uses-of-the-java-util-function-function-identity-method
 1. https://nofluffjuststuff.com/magazine/2016/09/time_to_really_learn_generics_a_java_8_perspective
 1. https://www.logicbig.com/tutorials/core-java-tutorial/java-util-stream/stream-cheat-sheet.html
 1. https://www.baeldung.com/java-bouncy-castle
### socket
Linux socket does not send new line character.
Use `isavailable()` to check for message
```
Linux socke
```
### Eventbus
> Publisher / Subscriber model based on type
* Sync
* Async
#### Ref.
* https://guava.dev/releases/16.0/api/docs/com/google/common/eventbus/AsyncEventBus.html
### Matchers
#### todo
Grop
#### Ref.
* http://tutorials.jenkov.com/java-regex/matcher.html
#### DI

* https://gist.github.com/stantonk/8e37cd97da1c0c800d27

### USB 
* https://github.com/todbot/usbSearch/
---
### Serial Port
#### github project - good option
* http://fazecast.github.io/jSerialComm/
* https://github.com/Fazecast/jSerialComm
## code
### try with resource 
#### Other
* https://javalibs.com/artifact/org.scream3r/jssc
* https://mvnrepository.com/artifact/org.rxtx/rxtx/2.1.7
---
### jdk download
* https://adoptopenjdk.net/?variant=openjdk15&jvmVariant=hotspot
* https://jdk.java.net/15/
---
### compare version
* https://stackoverflow.com/questions/198431/how-do-you-compare-two-version-strings-in-java/198442#198442
---
### version
* https://github.com/vdurmont/semver4j
---
## ui
### jface data binding
* https://git.eclipse.org/c/platform/eclipse.platform.ui.git/plain/examples/org.eclipse.jface.examples.databinding/src/org/eclipse/jface/examples/databinding/snippets/Snippet004DataBindingContextErrorLabel.java
### sdk example
* https://help.eclipse.org/2020-12/index.jsp?topic=/org.eclipse.platform.doc.isv/samples/samples.html
## config
* http://wilddiary.com/reading-property-file-java-using-apache-commons-configuration/
### system property and composite config
* https://commons.apache.org/proper/commons-configuration/apidocs/src-html/org/apache/commons/configuration2/SystemConfiguration.html#line.42
* https://commons.apache.org/proper/commons-configuration/userguide/howto_compositeconfiguration.html#Composite_Configuration_Details

## Java POJO
### Property Change Support
> With property change support added to the POJO, when the property of Java Object change all the listener of the object will be notified. 

* https://docs.oracle.com/javase/7/docs/api/java/beans/PropertyChangeSupport.html
## version handling

* https://stackoverflow.com/questions/2469922/generate-a-version-java-file-in-maven
* https://stackoverflow.com/questions/18456111/what-is-the-maven-way-for-automatic-project-versions-when-doing-continuous-deliv
---
## Protocol Parser
### block parser
* https://github.com/raydac/java-binary-block-parser
### Protocol buffer java
* https://developers.google.com/protocol-buffers/docs/javatutorial
## byte printing
```
String.format("%02x ",b)
Byte.toUnsignedInt(b) Java8
```
### wait for condition
* https://github.com/jhalterman/failsafe
* https://stackoverflow.com/questions/25325442/wait-x-seconds-or-until-a-condition-becomes-true
* https://www.javadoc.io/doc/org.awaitility/awaitility/latest/org/awaitility/Durations.html
* https://github.com/awaitility/awaitility/wiki/Usage#simple
```java

```
---
### String format
```java
MessageFormat.format("Some {0}, {1}, {2}", var1, var2, var3);
```
---
### String regex escape
```
Regex escape \Q and \E Usage in string "\\Q \\E
```
### Exception Handling
> Question to ask?
1. Handle exception if the program can continue with error. 
1.1 Program failing because of missing log config is nok.
1.2 File Parser Program failing because of missing input is ok.
#### Ref.
* https://www.baeldung.com/java-exceptions
* https://dzone.com/articles/9-best-practices-to-handle-exceptions-in-java
---
## code quality
* https://rhamedy.medium.com/a-short-summary-of-java-coding-best-practices-31283d0167d3
## lessons learned and best practice

```java
Shell shell ;
public Commands(Shell shell)
this.shell  = shell ;// This is a run time bug.
```
Fix1. 
```java
public Commands(final Shell shell)
this.shell  = shell ;//IDE Throws error
```
Above error is caught early because of
Benefit of following coding best practice

Change Small 
Compile
Checkin
Test 
## Singleton
Java a singleton with parameters is not a singleton.
https://stackoverflow.com/questions/1050991/singleton-with-arguments-in-java
## design
It is possible to send function defined as functional interface to a class constructor.
## other intresting
* https://tomassetti.me/parsing-in-java/#
## http client
* https://www.vogella.com/tutorials/REST/article.html
## debug
It is possible to execute custom function calls during debug break point
## Timer and TimerTask
Timer task can also be run with Executor Service
## path param and query param
* https://stackoverflow.com/questions/11552248/when-to-use-queryparam-vs-pathparam
## type conversation - upcasting and down casting
### Downcasting
Upcasting and Downcasting
It is possible to covert from base type to extended type, if you are sure that the type is of extended.
* https://www.baeldung.com/java-type-casting
Bi predicate
