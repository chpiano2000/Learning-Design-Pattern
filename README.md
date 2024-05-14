## Design Patterns vs Solid Principles

- Solid is the priciples of writing good code.
- Design Patterns are designed based on Solide Principles.

## Singleton Pattern

### Problem

- Ensure that a class has _just a single instance_
- A global access point to that instance

### Use cases

- Resource Manager:
  - Window task magager, macos activity monitor
- configuration manager
  - Logging class, config, class

### Implementation

- Implementing round-robin class, which return which server to round to in the list of servers
- [code](./singleton/singleton.py)

## Strategy Pattern

- Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

### Implementation

- Suppose that we have to develop a function to calculate all the discount campaigns
- [before code](./strategy/before.py)
  - This is a bad implementation because the function `get_price` has a lot of responsibilities.
  - Each campagin is a different responsibility, but the function `get_price` takes all of them.
  - This is a bad implementation because the function `get_price` is not scalable.
- [after code](./strategy/after.py)
  - This is a good implementation because the function `get_price` has only one responsibility.
  - There will be a dedicated function to calculate the price of each campaign.
  - the `get_price` is even more cleaner since the is a mapper between the campaign name and the function that calculates the price.
  - This is a good implementation because the function `get_price` is scalable, there will be no change in the function `get_price` when a new campaign is added.

## Facade Pattern

- Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

### Implementation

- [facade](Facade/facade.py) class is a class that provides access to the subsystems, which in this case is a set of price calculators:

  - `Discount` calculator
  - `Shipping` calculator
  - `Fees` calculator

- These calculator classes aren’t aware of the facade’s existence. They operate within the system and work with each other directly.
