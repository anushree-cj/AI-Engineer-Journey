# 📘 Day 03 - Functions (Part 2)

## Topics Covered

- `return` vs `print()`
- Default Parameters
- `None` as a default parameter
- Positional Arguments
- Keyword Arguments
- Mixing Positional & Keyword Arguments
- `*args`
- `**kwargs`
- Identity values for addition and multiplication

---

# 1. return vs print()

### print()

- Displays the output.
- Does not return the value.
- Function returns `None` if no explicit `return` is used.

```python
def square(x):
    print(x * x)

a = square(4)
print(a)
```

Output:

```
16
None
```

### return

- Sends a value back to the caller.
- Immediately exits the function.

```python
def square(x):
    return x * x

result = square(4)
print(result)
```

Output:

```
16
```

---

# 2. return Ends the Function

```python
def fun():
    return
    print("Hello")
```

The `print()` statement is never executed because `return` exits the function immediately.

---

# 3. Default Parameters

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Naruto")
```

Output:

```
Hello Guest
Hello Naruto
```

### Remember

- Default value is used only when no argument is passed.
- If an argument is provided, the default value is ignored.

---

# 4. None as a Default Parameter

```python
def greet(name=None):
    if name is None:
        name = "Guest"
    print("Hello", name)
```

### Difference

```python
if name is None
```

Checks only for `None`.

```python
if not name
```

Checks all falsy values:

- None
- ""
- 0
- False
- []
- {}
- ()

---

# 5. Positional Arguments

Arguments are assigned according to their position.

```python
def introduce(name, age):
    print(name, age)

introduce("Naruto", 18)
```

Output:

```
Naruto 18
```

---

# 6. Keyword Arguments

Arguments are assigned using parameter names.

```python
introduce(age=18, name="Naruto")
```

Output:

```
Naruto 18
```

### Remember

Keyword argument order does not matter.

---

# 7. Mixing Positional & Keyword Arguments

### ✅ Valid

```python
fun(10, 20)
fun(a=10, b=20)
fun(10, b=20)
```

### ❌ Invalid

```python
fun(a=10, 20)
```

Error:

```
SyntaxError:
positional argument follows keyword argument
```

---

# 8. Multiple Values for the Same Parameter

```python
def person(name, age):
    ...

person("Naruto", name="Sasuke")
```

Error:

```
TypeError:
got multiple values for argument 'name'
```

Reason:

`name` receives two values.

---

# 9. \*args

Collects all remaining positional arguments into a tuple.

```python
def show(*args):
    print(args)
```

```python
show(10, 20, 30)
```

Output:

```
(10, 20, 30)
```

### Remember

- Type is `tuple`
- Can hold zero or more values
- Tuple is immutable

---

# 10. \*\*kwargs

Collects all remaining keyword arguments into a dictionary.

```python
def show(**kwargs):
    print(kwargs)
```

```python
show(name="Naruto", age=18)
```

Output:

```python
{'name': 'Naruto', 'age': 18}
```

### Remember

- Type is `dict`
- Stores key-value pairs

---

# 11. Combining Parameters

```python
def demo(a, b=10, *args, **kwargs):
    ...
```

Order:

```
Required Parameters
↓
Default Parameters
↓
*args
↓
**kwargs
```

---

# 12. Identity Values

For addition:

```python
total = 0
```

Because:

```
0 + x = x
```

For multiplication:

```python
result = 1
```

Because:

```
1 × x = x
```

---

# Things to Remember

- `return` immediately exits a function.
- Every function returns something. If nothing is returned explicitly, it returns `None`.
- Default parameters are ignored if an argument is provided.
- Positional arguments must always come before keyword arguments.
- `*args` collects remaining positional arguments into a tuple.
- `**kwargs` collects remaining keyword arguments into a dictionary.
- Tuples are immutable.
- Dictionaries store key-value pairs.

---

# Mistakes & Learnings

### 1. Palindrome Range

❌ Initial code:

```python
range(0, (len(text)//2)-1)
```

Skipped one comparison.

✅ Correct:

```python
range(len(text)//2)
```

---

### 2. \*args Type

Initially thought it was a list.

✅ Correct:

```
tuple
```

Reason:

Python collects positional arguments into a tuple.

---

### 3. Mixing Positional & Keyword Arguments

Initially thought:

```python
fun(10, b=20)
```

was invalid.

✅ Correct:

It is valid because positional arguments come before keyword arguments.

---

### 4. Avoid Shadowing Built-in Functions

Avoid names like:

```python
sum = 0
str = "Hello"
list = []
```

Prefer:

```python
total = 0
text = "Hello"
numbers = []
```

---

# Day 03 Summary

Today I learned how Python handles function arguments internally.

I can now confidently use:

- `return`
- Default parameters
- Positional arguments
- Keyword arguments
- `*args`
- `**kwargs`

I also understand the common errors that occur while passing arguments and how Python assigns values step by step.
