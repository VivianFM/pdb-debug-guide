# Python Debugging with `pdb`

This repository provides a concise example and overview of Python's built-in debugger, `pdb`. 

---

## Overview

The Python Debugger (`pdb`) is part of Python’s standard library and is used to:
- Insert breakpoints in code;
- Inspect and modify program state at runtime;
- Step through code line by line;
- Analyze execution flow and identify bugs efficiently.

---

## Example

```python
import pdb

def greeting(name):
    print(f"Hello, {name}!")

def main():
    name = "User"
    breakpoint()  # Program execution will pause here
    greeting(name)
    print("Program finished.")

if __name__ == "__main__":
    main()
```

In this example:
- The `breakpoint()` pause the program when it is reached.
- breakpoint() can be replaced by import pdb; pdb.set_trace() 

---

## Debugging Commands

Below are commonly used `pdb` commands:

| Command | Description                                |
|---------|--------------------------------------------|
| `n`     | Continue to the next line within the same function |
| `c`     | Continue execution until the next breakpoint |
| `q`     | Quit the debugger and exit the program     |
| `p`     | Print the value of an expression or variable |
| `l`     | List source code around the current line   |
| `s`     | Step into a function call                  |
| `r`     | Continue until the current function returns|

---

## When to Use `pdb`

- Investigating unexpected program behavior
- Verifying assumptions by inspecting variable values
- Debugging complex logic without modifying source output with print statements
- Performing interactive testing during development

---

## Additional Resources

- Official Documentation: [Python `pdb` Module](https://docs.python.org/3/library/pdb.html)
- Related Tools: `breakpoint()` (Python 3.7+), `ipdb` (IPython Debugger)
