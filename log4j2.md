# Help file for log4j2 configuration
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
> Enable ansi in windows with the following flag in the log4j2 - disableAnsi="false"

1. (ANSI Windows)[https://stackoverflow.com/questions/28604171/how-to-print-logs-in-color-using-log4j2-highlight-pattern/42554705#42554705]
## Ref.
1. https://logging.apache.org/log4j/2.x/faq.html
1. https://logging.apache.org/log4j/2.x/manual/configuration.html
