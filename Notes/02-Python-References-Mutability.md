# Day 2 – Python Object References & Mutability

## 1. Variables Store References

Variables do NOT store objects.
They store references (addresses) to objects.

Example:

```python
x = [1, 2]
y = x
```

Both x and y refer to the same list.

---

## 2. Mutable vs Immutable

### Mutable Objects

Can be modified after creation.

Examples:

- list
- dictionary
- set

Example:

```python
x = [1, 2]
y = x

x.append(3)

print(y)
```

Output:

```python
[1, 2, 3]
```

Reason:
Both variables point to the same list.

---

### Immutable Objects

Cannot be modified after creation.

Examples:

- int
- float
- bool
- string
- tuple

Example:

```python
a = "Hello"
b = a

a += " World"

print(b)
```

Output:

```python
Hello
```

Reason:
A new string object is created and assigned to `a`.

---

## 3. Difference Between == and is

### ==

Checks whether values are equal.

```python
x = [1,2]
y = [1,2]

print(x == y)
```

Output:

```python
True
```

---

### is

Checks whether both variables refer to the same object.

```python
x = [1,2]
y = x

print(x is y)
```

Output:

```python
True
```

---

## 4. += vs +

### += on Lists

Modifies the existing list.

```python
x = [1,2]
y = x

x += [3]
```

Result:

```python
x -> [1,2,3]
y -> [1,2,3]
```

Object ID remains the same.

---

### +

Creates a new list.

```python
x = [1,2]
y = x

x = x + [3]
```

Result:

```python
x -> [1,2,3]
y -> [1,2]
```

Object ID changes.

---

## 5. append()

```python
numbers.append(10)
```

Adds one element to the existing list.

No new list is created.

---

## 6. Reassigning Variables

```python
x = [1,2]
y = x

x = []
```

Output:

```python
print(y)
```

```
[1,2]
```

Reason:
`x` now refers to a new empty list.
`y` still refers to the original list.

---

## 7. Finding Largest Number

```python
def largest_number(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest
```

Time Complexity:

```
O(n)
```

---

## 8. Handling Empty Lists

Possible approaches:

- Return None ✅
- Raise ValueError ✅

Choose based on how the function is expected to behave.

---

## 9. id()

```python
print(id(x))
```

Returns the identity (unique identifier) of the object.

Useful for checking whether two variables refer to the same object.

---

## Key Takeaways

✔ Variables store references, not objects.

✔ Mutable objects can be modified in place.

✔ Immutable objects create a new object when "modified."

✔ == compares values.

✔ is compares object identity.

✔ += modifies a list.

✔ + creates a new list.

✔ Think about edge cases (empty input) while writing functions.

---

## Interview Tips

❌ Avoid:

```python
if x is 10:
```

✅ Use:

```python
if x == 10:
```

Use `is` mainly with `None`.

```python
if result is None:
```

---

## New Concepts Learned

- Object References
- Mutable Objects
- Immutable Objects
- Object Identity
- id()
- Variable Reassignment
- Edge Case Handling
