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
