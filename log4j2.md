# Help file for log4j2 configuration
## Available Options
> Log4j, Logback, and  Log4j2 ❤️
## Selected 
Log4j2
#### Log4j2
> Log4j2 provides support for SLF4J, automatically reloads logging configuration, and supports advanced filtering options. In addition to these features, it also allows lazy evaluation of log statements based on lambda expressions, offers asynchronous loggers for low-latency systems, and provides a garbage-free mode to avoid any latency caused by garbage collector operations.

####
* https://stackify.com/compare-java-logging-frameworks/
## Appenders
> Appenders are responsible for delivering LogEvents to their destination. 
## Refer the reference link 2
## Place the log4j2.xml file in the below location.
### Location
```
src/main/resources
```
### Log level
* OFF
* FATAL
* ERROR
* WARN
* INFO
* DEBUG
* TRACE
* ALL
### Sample config
log4j2.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
    </Console>
  </Appenders>
  <Loggers>
    <Root level="error">
      <AppenderRef ref="Console"/>
    </Root>
  </Loggers>
</Configuration>
```
## log in color windows
 > Log in color windows require jansi maven dependency
 
 > Enable ansi in windows with the following flag in the log4j2 - `disableAnsi="false"`

 > Use eclipse ANSI plugin in windows
1. [ANSI Windows](https://stackoverflow.com/questions/28604171/how-to-print-logs-in-color-using-log4j2-highlight-pattern/42554705#42554705)
1. [ANSI Windows2](https://stackoverflow.com/questions/48472049/how-to-colorize-log4j2-output-on-console-in-intellij)
### Ref.
1. https://logging.apache.org/log4j/2.x/faq.html
1. https://logging.apache.org/log4j/2.x/manual/configuration.html
### ansi
```xml
<PatternLayout
pattern="%highlight{%d{dd-MM-yy HH:mm:ss} %-5p %-40.40c{6}: %-15.15M: %m%n }{FATAL=red blink, ERROR=red, WARN=yellow bold, INFO=green bold, DEBUG=green bold, TRACE=blue}"
disableAnsi="false" />
```
## Eclipse run config
The name of property file should be `log4j2.property`
Add class path folder in run config to select `log4j2.xml`.

### Ref.
* https://stackoverflow.com/questions/5081316/where-is-the-correct-location-to-put-log4j-properties-in-an-eclipse-project
---
1. Logger: It is used to log the messages
1. Appender: It is used to publish the logging information to the destination like file, database, console etc
1. Layout: It is used to format logging information in different styles

* https://examples.javacodegeeks.com/enterprise-java/log4j/log4j-conversion-pattern-example/
* https://www.tutorialspoint.com/log4j/log4j_patternlayout.htm

## Logger config
* https://logging.apache.org/log4j/2.x/manual/architecture.html
* https://logging.apache.org/log4j/2.x/manual/configuration.html
### Every configuration must have a root logger.
Refer Configuring Loggers

## Layouts
An Appender uses a Layout to format a LogEvent into a form that meets the needs of whatever will be consuming the log event.

### HTML Layout
<HtmlLayout datePattern="ISO8601" timezone="GMT+0"/>

### Layout Patterns Reference

```
Patterns
The conversions that are provided with Log4j are:
c{precision}
logger{precision}  

highlight{pattern}{style}
```
### Ref.--- Important info about ansi color and alternate naming :heart:
* https://logging.apache.org/log4j/2.x/manual/layouts.html

### PatternLayout --- Important info about spacing and formatting :heart:
* https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/PatternLayout.html

## Appender
* https://logging.apache.org/log4j/2.x/manual/appenders.html#ConsoleAppender

## Additivity - TODO Good
* https://logging.apache.org/log4j/2.x/manual/configuration.html

## Sample
### Config1
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
	<Appenders>
		<Console name="Console" target="SYSTEM_OUT">
			<PatternLayout disableAnsi="true">
				<Pattern>%highlight{	 - %msg%n}
				</Pattern>
			</PatternLayout>
		</Console>
		<Console name="ConsoleMsgOnly" target="SYSTEM_OUT">
			<PatternLayout disableAnsi="false">
				<Pattern>%highlight{%-5level %-36.36logger %msg%n}
				</Pattern>
			</PatternLayout>
		</Console>
		<File name="MyFile" fileName="logs/app.log">
			<PatternLayout>
				<Pattern>%d %p %c{1.} [%t] %m%n</Pattern>
			</PatternLayout>
		</File>
	</Appenders>
	<Loggers>
		<Root level="debug">
			<AppenderRef ref="ConsoleMsgOnly" />
			<AppenderRef ref="MyFile" />
		</Root>
	</Loggers>
</Configuration>
### sample config
* https://howtodoinjava.com/log4j2/log4j2-properties-example/
```
## Import and auto import

Organise import and Type filter update to make auto import work for logger
```java
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;
 
```
### Logger name
In most cases, applications name their loggers by passing the current class's name to LogManager.getLogger(...). Because this usage is so common, Log4j 2 provides that as the default when the logger name parameter is either omitted or is null. For example, in all examples below the Logger will have a name of "org.apache.test.MyTest".
```java
package org.apache.test;
 
public class MyTest {
    private static final Logger logger = LogManager.getLogger();
}
```
#### Ref.
* http://logging.apache.org/log4j/2.x/manual/api.html
### LAP
> Logger, Appender and Pattern Layout
---
## lessons learned and best practice
* Define logger in base class and derrived class separately. This prevent confusion  in log location.
* https://owasp.org/www-community/vulnerabilities/Poor_Logging_Practice#:~:text=Loggers%20should%20be%20declared%20to,declares%20a%20non-static%20logger.
* Doing `isDebugEnabled` repeatedly has the effect of making the code feel like it is more about logging than the actual task at hand. In addition, it results in the logging level being checked twice; once on the call to isDebugEnabled and once on the debug method. A better alternative would be:
```java
logger.debug("Logging in user {} with birthday {}", user.getName(), user.getBirthdayCalendar());

```
* formatted logger
```java
logger.printf(Level.INFO, "Logging in user %1$s with birthday %2$tm %2$te,%2$tY", user.getName(), user.getBirthdayCalendar());
```
loggging method name
Log4j2 no need to log the method name. If needed it can  be enabled with the Pattenlayout config.

Avoid using Exception string in methodname
### Tutorial
* https://www.scalyr.com/blog/log4j2-configuration-detailed-guide/
---
## log4j2 schema mapping
log4j2.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration strict="true"
	xmlns="http://logging.apache.org/log4j/2.0/config"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://logging.apache.org/log4j/2.0/config 
           https://raw.githubusercontent.com/apache/logging-log4j2/master/log4j-core/src/main/resources/Log4j-config.xsd">
	<Appenders>
		<Console name="Console" target="SYSTEM_OUT">
			<PatternLayout
				pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n" />
		</Console>
	</Appenders>
	<Loggers>
		<Root level="Debug">
			<AppenderRef ref="Console" />
		</Root>
	</Loggers>
</Configuration>```
### Ref.
* https://stackoverflow.com/questions/13904481/in-log4j2-how-do-i-associate-an-xml-schema-with-log4j2-xml

## MVN
```xml
		<log4j2.version>2.14.1</log4j2.version>
		<dependency>
			<groupId>org.apache.logging.log4j</groupId>
			<artifactId>log4j-api</artifactId>
			<version>${log4j2.version}</version>
		</dependency>
		<dependency>
			<groupId>org.apache.logging.log4j</groupId>
			<artifactId>log4j-core</artifactId>
			<version>${log4j2.version}</version>
		</dependency>
```
### Property Substitution
* 
