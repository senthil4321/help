# Help file for log4j2 configuration
## Available Options

> Log4j, Logback, and Log4j2
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
```
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
## Ref.
1. https://logging.apache.org/log4j/2.x/faq.html
1. https://logging.apache.org/log4j/2.x/manual/configuration.html
## Eclipse run config
Add class path folder in run config to select log4j xml.
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

### PatternLayout
* https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/PatternLayout.html

## Appender
* https://logging.apache.org/log4j/2.x/manual/appenders.html#ConsoleAppender
