# AI Coding Agent Instructions

## Project Overview
This is an **algorithm solutions repository** containing Python implementations of competitive programming and coding interview problems. Solutions are organized chronologically by date (e.g., `20260221/`, `20260222/`) with files named by problem ID from online judge platforms.

## Architecture & Organization

### Directory Structure
- **Date-based folders**: `YYYYMMDD/` format (e.g., `20260221/`, `20260222/`) represent the date problems were solved
- **Problem files**: Named by problem number (e.g., `1003.py`, `2753.py`, `10171.py`) from platforms like BOJ, Codeforces, AtCoder, or LeetCode
- **Goal**: Track algorithm practice progression over time

### Key Characteristics
- **Single-file solutions**: Each problem is a standalone Python script
- **Direct implementation**: Solutions focus on correctness and clarity without external dependencies (beyond Python stdlib)
- **Educational context**: Code prioritizes understanding the algorithm over production practices

## Development Patterns

### Input/Output Handling
**Standard pattern**: Use `sys.stdin.readline()` for all input instead of `input()`
```python
import sys
a, b, c = map(int, sys.stdin.readline().split())  # Multiple values on one line
n = int(sys.stdin.readline())                      # Single integer
```
**Reasoning**: More efficient for large inputs in competitive programming

### Solution Structure
1. Import required modules (sys, collections, etc.)
2. Read input using `sys.stdin.readline()`
3. Process algorithm logic directly in global scope
4. Print result with `print()`

See examples: [1003.py](20260221/1003.py), [2753.py](20260221/2753.py), [1712.py](20260222/1712.py)

### Common Imports
- `sys` - for stdin
- `collections.defaultdict` - for dynamic dictionaries
- Standard library math/logic only; no external packages

## When Adding New Solutions

**Filename convention**: Use the problem ID as filename (e.g., `16430.py` for problem #16430)

**Folder placement**: Create solution in the current date folder (check latest `YYYYMMDD/` folder in repo)

**Template pattern**:
```python
import sys

# Read input
n = int(sys.stdin.readline())
# ... more input reading

# Algorithm logic
result = ...

# Output
print(result)
```

## Anti-Patterns to Avoid
- ❌ Using `input()` instead of `sys.stdin.readline()`
- ❌ Complex imports or external dependencies
- ❌ Comments explaining obvious code (only document non-obvious algorithms)
- ❌ Multiple functions/classes (inline all logic)
- ❌ Error handling/validation (assume valid input per problem statement)

## Debugging Approach
- Test solutions with provided sample input/output
- Verify edge cases (1-element arrays, zero values, negative numbers)
- Trace algorithm logic step-by-step if output doesn't match
- Reference problem statement for input/output format specifics
