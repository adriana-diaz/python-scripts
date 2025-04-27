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
