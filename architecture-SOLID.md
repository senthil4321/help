The **SOLID** principles are five object-oriented design guidelines intended to make software more flexible, understandable, and maintainable.

Here is a practical breakdown of each principle using Python, comparing the flawed approach to the SOLID-compliant architecture.

## 1. Single Responsibility Principle (SRP)

**A class should have one, and only one, reason to change.** It should only handle one specific responsibility.

**Violation:** An `Order` class that calculates totals, saves itself to a database, and sends email receipts. If the database schema changes or the email provider changes, this class has to be modified.
**Solution:** Split the responsibilities into dedicated classes.

```python
# The Data Model
class Order:
    def __init__(self, items, total):
        self.items = items
        self.total = total

# The Database Handler
class OrderRepository:
    def save_to_database(self, order: Order):
        print(f"Saving order for ${order.total} to DB...")

# The Notification Handler
class OrderNotifier:
    def send_receipt(self, order: Order):
        print("Emailing receipt to customer...")

```

## 2. Open/Closed Principle (OCP)

**Software entities should be open for extension, but closed for modification.** You should be able to add new functionality without rewriting existing code.

**Violation:** A discount calculator with a massive `if/elif` chain. Every time you add a new customer type, you have to modify the core calculator class.
**Solution:** Use inheritance or interfaces (Strategies) so new discount rules can be added as standalone classes.

```python
from abc import ABC, abstractmethod

# The Abstraction
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass

# Extensions (Adding new ones doesn't modify existing code)
class RegularDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount

class VipDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.8  # 20% off

# The Core Class (Closed for modification)
class Checkout:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
        
    def get_final_price(self, amount: float) -> float:
        return self.discount_strategy.calculate(amount)

```

## 3. Liskov Substitution Principle (LSP)

**Subtypes must be substitutable for their base types without altering the correctness of the program.** If you replace a parent class with a child class, the code shouldn't break or require type checks.

**Violation:** Having a base `Bird` class with a `fly()` method, and a `Penguin` subclass that throws a `NotImplementedError` when `fly()` is called.
**Solution:** Restructure the hierarchy so base classes only enforce behaviors that all subclasses genuinely share.

```python
class Bird:
    def eat(self):
        print("Eating...")

# Only birds that actually fly inherit this
class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class Eagle(FlyingBird):
    pass

class Penguin(Bird):
    def swim(self):
        print("Swimming...")

```

## 4. Interface Segregation Principle (ISP)

**Clients should not be forced to depend upon interfaces they do not use.** Large, bloated interfaces should be split into smaller, more specific ones.

**Violation:** A giant `IMachine` interface with `print()`, `scan()`, and `fax()` methods. A simple, basic printer class would be forced to implement `scan()` and `fax()` as empty methods.
**Solution:** Break the interface into role-specific components.

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self): pass

# A basic printer only implements what it needs
class BasicPrinter(Printer):
    def print_document(self):
        print("Printing...")

# A multi-function printer can inherit from multiple specific interfaces
class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing...")
        
    def scan_document(self):
        print("Scanning...")

```

## 5. Dependency Inversion Principle (DIP)

**High-level modules should not depend on low-level modules; both should depend on abstractions.** You should inject dependencies rather than hardcoding them inside the class.

**Violation:** A `NotificationService` that creates a new instance of `EmailSender` directly inside its constructor. It is now permanently coupled to emails.
**Solution:** The service should depend on a generic `MessageSender` interface. You can then pass in *any* sender (Email, SMS, Push) when instantiating the service.

```python
from abc import ABC, abstractmethod

# The Abstraction
class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Low-level modules
class EmailSender(MessageSender):
    def send(self, message: str):
        print(f"Sending email: {message}")

class SmsSender(MessageSender):
    def send(self, message: str):
        print(f"Sending SMS text: {message}")

# High-level module (Depends on the abstraction, not the concrete classes)
class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender
        
    def notify_user(self, message: str):
        self.sender.send(message)

# Usage: Injecting the dependency
email_service = NotificationService(EmailSender())
sms_service = NotificationService(SmsSender())

```
