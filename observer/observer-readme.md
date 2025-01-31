# Observer Design Pattern Examples

This directory contains examples of the Observer Design Pattern implemented in Python, PHP, and Node.js. The Observer pattern is used to define a one-to-many dependency between objects so that when one object (the subject) changes state, all its dependents (observers) are notified and updated automatically.

## What is the Observer Pattern?

The Observer Pattern is a behavioral design pattern that allows objects (observers) to subscribe to updates from another object (the subject). It is commonly used in event-driven systems, messaging services, and GUI frameworks.

## Structure of the Directory
- `observer-in-python.py`: Observer pattern implementation in Python.
- `observer-in-php.php`: Observer pattern implementation in PHP.
- `observer-in-node.js`: Observer pattern implementation in Node.js.
- `readme.md`: Documentation for the Observer examples.

## How to Use the Examples

### 1. Trying the Python Code

**Prerequisite:** Python 3 must be installed on your system.

Run the following command:
```bash
clear && python3 -m venv test && cp ./observer-in-python.py ./test && python3 ./observer-in-python.py && rm -R ./test
```
This will execute the Python implementation of the Observer Pattern.

### 2. Trying the PHP Code

**Prerequisite:** A PHP runtime environment.

Use the online PHP interpreter at [Online PHP Editor](https://onlinephp.io/):
1. Copy the contents of `observer-in-php.php`.
2. Paste it into the editor.
3. Click "Run" to execute the script and see the output.

Alternatively, run it locally using:
```bash
php observer-in-php.php
```

### 3. Trying the Node.js Code

**Prerequisite:** Node.js must be installed on your system.

Run the following command:
```bash
node observer-in-node.js
```
This will execute the Node.js implementation of the Observer Pattern.

## Learning Outcomes

By exploring these examples, you will:
- Understand how the Observer pattern is implemented in different programming languages.
- Learn how to establish a subscription mechanism for objects.
- Gain insight into practical use cases such as event-driven programming and messaging systems.

## Notes

- Ensure the prerequisites for each language are met before running the examples.
- The implementations are for educational purposes and may require adaptation for production use.

If you have any questions or need further assistance, feel free to reach out!
