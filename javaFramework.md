#
## Web Jetty Jersey
* https://zetcode.com/articles/jerseyembeddedjetty/

## Singleton Jersey
Problem : Keep the state of the object between multiple requests
Solution : Simpy adding singletone annotation solved the problem
```java
@Path("/hello")
@Singleton

public class HelloWorldResource {
	
	private static final String TEMPLATE = "Hello, %s! Counter %d";
	private int counter = 0;
	@GET
	@Path("{name}")
    @Produces(MediaType.APPLICATION_JSON)
    public Saying sayHello(@PathParam("name") String name) {	
	    counter++;
		return new Saying(String.format(TEMPLATE, name,counter));
    }
}
```
* https://stackoverflow.com/questions/36186102/initialize-singleton-in-java-jersey-2-jax-rs/36186475
* https://www.logicbig.com/tutorials/java-ee-tutorial/jax-rs/resource-lifecycle.html
* 
## Jersey
## Jersey client and server
### Jersey + http server
```xml
<jersey.version>3.0.2</jersey.version>
	<dependencies>
		<dependency>
			<groupId>org.glassfish.jersey.core</groupId>
			<artifactId>jersey-server</artifactId>
			<version>${jersey.version}</version>
		</dependency>
		<dependency>
			<groupId>org.glassfish.jersey.containers</groupId>
			<artifactId>jersey-container-jdk-http</artifactId>
			<version>${jersey.version}</version>
		</dependency>
		<dependency>
			<groupId>org.glassfish.jersey.inject</groupId>
			<artifactId>jersey-hk2</artifactId>
			<version>${jersey.version}</version>
		</dependency>
	</dependencies>
```
* https://eclipse-ee4j.github.io/jersey.github.io/documentation/latest3x/deployment.html#deployment.javase
---
## Eclipse plugin
1. Plugin - Single feature
2. Feature - Group of plugins
3. site Place to host the feature or plugin

* https://riptutorial.com/eclipse-plugin/example/25547/hello-world
* https://stackoverflow.com/questions/1619623/eclipse-plugin-how-to-get-current-text-editor-cursor-position
* https://wiki.eclipse.org/FAQ_How_do_I_insert_text_in_the_active_text_editor%3F
* https://www.eclipse.org/articles/viewArticle/ViewArticle2.html
---
