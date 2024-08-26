# Island Perimeter

## Description
This project involves creating a Python function def island_perimeter(grid): that calculates the perimeter of an island represented in a 2D grid. The grid is a list of lists where 0 represents water and 1 represents land. The goal is to compute the perimeter of the single island within the grid, considering only horizontal and vertical connections between land cells.

## Project Structure
- **Repository:** `alx-interview`
- **Directory:** `0x09-island_perimeter`
- **File:** `0-island_perimeter.py`

## Example Usage
```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
```

## Resources
- **Python Documentation:** Working with nested lists.
- **GeeksforGeeks:** Python multi-dimensional arrays.
- **TutorialsPoint:** Python lists.
- **YouTube:** Tutorials on Python 2D arrays and lists.

## License
This project is © 2024 ALX, All rights reserved.~
