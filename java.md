#Java
## TODO
 - [ ] Stream map
 - [ ] Supplier Consumer
 - [ ] Collection

## Example
```
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
## Ref.

 1. https://www.javatpoint.com/java-8-method-reference
 1. https://www.baeldung.com/java-8-collectors
 1. http://tutorials.jenkov.com/java-collections/map.html#implementations
 1. https://www.google.com/amp/s/www.geeksforgeeks.org/stream-map-java-examples/amp/
 1. https://stackoverflow.com/questions/52532565/what-are-practical-uses-of-the-java-util-function-function-identity-method
 1. https://nofluffjuststuff.com/magazine/2016/09/time_to_really_learn_generics_a_java_8_perspective
