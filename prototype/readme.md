# Prototype Design Pattern Examples

This directory contains examples of the Prototype Design Pattern implemented in Python, PHP, and Node.js. 
The Prototype pattern is used to **clone existing objects** instead of creating new ones from scratch, making object creation **faster and more efficient**.

## What is the Prototype Pattern?

The **Prototype Pattern** is a **creational design pattern** that allows cloning of existing objects instead of creating new ones via constructors. 
This pattern is useful when:
- Object creation is **expensive or resource-intensive**.
- You need to **duplicate objects while keeping the original unchanged**.
- Creating objects from scratch every time would be inefficient.

## Structure of the Directory
- `prototype-in-python.py`: Prototype pattern implementation in Python.
- `prototype-in-php.php`: Prototype pattern implementation in PHP.
- `prototype-in-node.js`: Prototype pattern implementation in Node.js.
- `readme.md`: Documentation for the Prototype examples.

## How to Use the Examples

### 1. Trying the Python Code

**Prerequisite:** Python 3 must be installed on your system.

Run the following command:
```bash
clear && python3 -m venv test && cp ./prototype-in-python.py ./test && python3 ./prototype-in-python.py && rm -R ./test
```

### 2. Trying the PHP Code
**Prerequisite:** A PHP runtime environment.

Use the online PHP interpreter at Online PHP Editor:

1. Copy the contents of prototype-in-php.php.
2. Paste it into the editor.
3. Click "Run" to execute the script and see the output.

Alternatively, run it locally using:

```
php prototype-in-php.php
```

### 3. Trying the Node.js Code
**Prerequisite:** Node.js must be installed on your system.

Run the following command:

```
node prototype-in-node.js
```
#### This will execute the Node.js implementation of the Prototype Pattern.


## Learning Outcomes
By exploring these examples, you will:

- Understand how the Prototype pattern helps clone objects efficiently.
- Learn how to create object duplicates without modifying the original.
- Gain insight into practical use cases like game development, document duplication, and cache optimization.

## Notes
- Ensure the prerequisites for each language are met before running the examples.

- The implementations are for educational purposes and may require adaptation for production use.

If you have any questions or need further assistance, feel free to reach out!