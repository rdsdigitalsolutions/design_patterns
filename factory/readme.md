
# Factory Design Pattern Examples

This directory contains examples of the Factory Design Pattern implemented in Python, PHP, and Node.js. 
The Factory pattern provides a way to instantiate objects without exposing the creation logic, ensuring that the code remains flexible and easier to maintain.

## What is the Factory Pattern?

The Factory Pattern is a creational design pattern that defines an interface or abstract class for creating objects, 
but allows subclasses or separate classes to decide which class to instantiate. This pattern is useful when:
- The exact type of the object being created is determined at runtime.
- You want to centralise the creation logic for better flexibility and decoupling.

## Structure of the Directory
- `factory-in-python.py`: Factory implementation in Python.
- `factory-in-php.php`: Factory implementation in PHP.
- `factory-in-node.js`: Factory implementation in Node.js.
- `readme.md`: Documentation for the Factory examples.

## How to Use the Examples

### 1. Trying the Python Code

Prerequisite: Python 3 must be installed on your system.

Run the following commands:
```bash
clear && python3 -m venv test && cp ./factory-in-python.py ./test && python3 ./factory-in-python.py && rm -R ./test
```

Explanation:
- `python3 -m venv test`: Creates a virtual environment.
- `cp ./factory-in-python.py ./test`: Copies the Python Factory script into the environment.
- `python3 ./factory-in-python.py`: Runs the script.
- `rm -R ./test`: Cleans up by removing the virtual environment.

### 2. Trying the PHP Code

Prerequisite: A PHP runtime environment.

Use the online PHP interpreter at [Online PHP Editor](https://onlinephp.io/):
1. Copy the contents of `factory-in-php.php`.
2. Paste it into the editor.
3. Click "Run" to execute the script and see the output.

### 3. Trying the Node.js Code

Prerequisite: Node.js must be installed on your system.

Run the following command:
```bash
node factory-in-node.js
```

This will execute the Node.js implementation of the Factory pattern.

## Learning Outcomes

By exploring these examples, you will:
- Understand how the Factory pattern is implemented in different programming languages.
- Learn how to centralise object creation logic while keeping your code flexible and modular.
- Gain insight into practical use cases for the Factory pattern.

## Notes

- Ensure the prerequisites for each language are met before running the examples.
- The implementations are for educational purposes and may require adaptation for production use.

If you have any questions or need further assistance, feel free to reach out!
