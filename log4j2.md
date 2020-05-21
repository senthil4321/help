# Help file for log4j2 configuration

## Place the log4j2.xml file in the below location.
### Location
```
src/main/resources
```
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
## Ref.
1. https://logging.apache.org/log4j/2.x/faq.html
1. https://logging.apache.org/log4j/2.x/manual/configuration.html
