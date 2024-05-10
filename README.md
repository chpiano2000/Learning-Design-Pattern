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
