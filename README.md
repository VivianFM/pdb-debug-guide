# Python Debugging with `pdb`

This repository provides a simple example and practical overview of Python's built-in debugger (`pdb`).

---

## Overview

The Python Debugger (`pdb`) is part of the Python Standard Library and is used to:
- Insert breakpoints in code;
- Inspect and modify program state during execution;
- Step through code line by line;
- Analyze control flow and diagnose logic errors.

---

## Example

```python
def greeting(name):
    print(f"Hello, {name}!")

def main():
    name = "User"
    breakpoint()  # Execution pauses here and enters interactive debugging mode
    greeting(name)
    print("Program finished.")

if __name__ == "__main__":
    main()
```

### Notes:
- The `breakpoint()` pauses the program when it is reached.
- `breakpoint()` can be replaced by `import pdb`; `pdb.set_trace()`.

---

### Debugger Interface

When the program pauses, you’ll see something like:

```
> /path/to/main.py(7)main()
-> greeting(name)
(Pdb)
```

- `>` indicates the current call stack frame.
- `->` marks the next line to be executed.
- `(Pdb)` is the interactive prompt for entering debugging commands.

---

## Debugging Commands

| Command | Description |
|---------|-------------|
| `n` (next) | Executes the next line **in the current function**. If the next line is a function call, it executes the entire function without stepping in. |
| `s` (step) | Executes the next line and **steps into** function calls if present. Useful for inspecting function internals. |
| `c` (continue) | Continues execution until the next breakpoint. |
| `q` (quit) | Exits the debugger and terminates the program. |
| `p <expression>` | Prints the value of a variable or expression. |
| `l` (list) | Displays lines of source code around the current line. |
| `r` (return) | Continues execution until the current function returns. |

---

### `next` vs `step`: Practical Difference

At the `(Pdb)` prompt:

- Typing `n` will **execute `greeting(name)` as a single step**, without entering its body. You’ll see something like:

        Hello, User!
        > /path/to/main.py(8)main()
        -> print("Program finished.")
        (Pdb)
  
- Typing `s` will **step into `greeting(name)`**, allowing you to debug each line inside the function. You’ll see something like:

        > /path/to/main.py(1)main()
        -> def greeting(name):
        (Pdb) 

Use `s` when you want to inspect how a function works. Use `n` when you trust it and want to move past it.

---

## When to Use `pdb`

- Tracing unexpected behavior in function calls;
- Inspecting variable state at runtime;
- Verifying control flow through conditionals or loops;
- Avoiding excessive `print()` debugging;
- Quickly pausing and resuming code for interactive inspection.

---

## Additional Resources

- 📖 [Official Python `pdb` Documentation](https://docs.python.org/3/library/pdb.html)
