# Singleton Design Pattern Examples

This directory contains examples of the Singleton Design Pattern implemented in Python, PHP, and Node.js. The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This is useful for managing shared resources, such as database connections or configuration settings, in an application.

## What is the Singleton Pattern?

The Singleton Pattern is a design pattern that restricts the instantiation of a class to a single instance. It ensures that there is only one object of the class in the system, which can be accessed globally. This is achieved by:

1. Making the constructor private or inaccessible.
2. Providing a static method to retrieve or create the single instance.

## Structure of the Directory
- `singleton-in-python.py`: Singleton implementation in Python.
- `singleton-in-php.php`: Singleton implementation in PHP.
- `singleton-in-node.js`: Singleton implementation in Node.js.
- `readme.md`: Documentation for the Singleton examples.

## How to Use the Examples

### 1. Trying the Python Code

Prerequisite: Python 3 must be installed on your system.

Run the following commands:
```bash
clear && python3 -m venv test && cp ./singleton-in-python.py ./test && python3 ./singleton-in-python.py && rm -R ./test
```

Explanation:
- `python3 -m venv test`: Creates a virtual environment.
- `cp ./singleton-in-python.py ./test`: Copies the Python Singleton script into the environment.
- `python3 ./singleton-in-python.py`: Runs the script.
- `rm -R ./test`: Cleans up by removing the virtual environment.

### 2. Trying the PHP Code

Prerequisite: A PHP runtime environment.

Use the online PHP interpreter at [Online PHP Editor](https://onlinephp.io/):
1. Copy the contents of `singleton-in-php.php`.
2. Paste it into the editor.
3. Click "Run" to execute the script and see the output.

### 3. Trying the Node.js Code

Prerequisite: Node.js must be installed on your system.

Run the following command:
```bash
node singleton-in-node.js
```

This will execute the Node.js implementation of the Singleton pattern.

## Learning Outcomes

By exploring these examples, you will:
- Understand how the Singleton pattern is implemented in different programming languages.
- Learn how to restrict instantiation and provide global access to a single instance.
- Gain insight into practical use cases for the Singleton pattern.

## Notes

- Ensure the prerequisites for each language are met before running the examples.
- The implementations are for educational purposes and may require adaptation for production use.

If you have any questions or need further assistance, feel free to reach out!
