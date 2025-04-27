# Python Cheatsheet 🐍💻

## 1. Using `end` to control the end of a line in `print()`
```python
print("Hello", end=" ")
print("world")
# Output:
# Hello world
```

## 2. Using `sep` to separate values in `print()`
Remember: Keyword arguments should be passed **after** any required positional arguments.
```python
print("Python", "is", "awesome", sep=" 🔥 ")
# Output:
# Python 🔥 is 🔥 awesome
```

## 3. Using `\n` to separate values in `print()`
```python
print("My\nname\nis\nBond.", end=" ")
print("James Bond.")
# Output:
# My
# name
# is
# Bond. James Bond.
```
## 4 SECTION 2 SUMMARY

A variable is a named location reserved to store values in the memory. A variable is created or initialized automatically when you assign a value to it for the first time. 

Each variable must have a unique name ‒ an identifier. A legal identifier name must be a non-empty sequence of characters, must begin with the underscore (`_`), or a letter, and it cannot be a Python keyword. The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive.

Python is a dynamically-typed language, which means you do not need to declare variables in it. (2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of the equal (`=`) sign, i.e., `var = 1`.

You can also use compound assignment operators (shortcut operators) to modify values assigned to variables, for example: `var += 1`, or `var /= 5 * 2`.

You can assign new values to already existing variables using the assignment operator or one of the compound operators, for example:

| Variable | Python Real | Quiz Expected | Why |
|:---------|:------------|:--------------|:----|
| `my_var` | ✅ Legal | ✅ Legal | Correct. |
| `m` | ✅ Legal | ✅ Legal | Correct. |
| `101` | ❌ Illegal | ❌ Illegal | Cannot start with a number. |
| `averylongVariablename` | ✅ Legal | ✅ Legal | No problem, long names are allowed. |
| `m101` | ✅ Legal | ✅ Legal | Starts with a letter, fine. |
| `m 101` | ❌ Illegal | ❌ Illegal | Contains a space. |
| `Del` | ✅ Legal | ✅ Legal | Adding a number makes it fine. |
| `del1` | ✅ Legal | ❌ Illegal | Technically allowed in Python, but the quiz marks it illegal because it resembles the reserved word `del`. |

---
