# Skip List Data Structure Implementation

**Assignment 359 - Topic 3**

A comprehensive implementation of the Skip List data structure in Python with full functionality, tests, and visualizations.

## Overview

A **Skip List** is a probabilistic data structure that provides expected O(log n) time complexity for search, insertion, and deletion operations. It uses a hierarchy of linked lists with progressively fewer elements at each level, creating "express lanes" that allow for faster traversal.

## Contribution

### Tanisha Ahuja 
- Core Implementation
- **Primary skip list implementation** (`skip_list.py`)
- **SkipNode class** with multiple forward pointers
- **SkipList class** with core operations:
  - `insert()`, `delete()` methods
  - `display()` for structure visualization
  - `get_all_items()` for sorted traversal
  - `__len__()`, `__contains__()` magic methods
- **Visualization utilities** (`visualization.py`)
- **Demo function** with comprehensive examples
- **Documentation** , **readme** and code comments
- **Comprehensive test suite** (`test_skip_list.py`)

### Arpita Arora
- Building the presentation and adding visuals to it.

## Reference

- [OpenDSA Skip List Tutorial](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/SkipList.html)
- Pugh, William (1990). "Skip Lists: A Probabilistic Alternative to Balanced Trees". Communications of the ACM, 33(6), 668-676.
- [OpenDSA Skip List Chapter](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/SkipList.html)
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 12: Binary Search Trees and Skip Lists.
- [Skip List Visualization](https://www.cs.usfca.edu/~galles/visualization/SkipList.html) - Interactive skip list demonstration
- Sedgewick, R., & Wayne, K. (2011). "Algorithms" (4th ed.). Addison-Wesley. Chapter 3.3: Balanced Search Trees and Skip Lists.
- [GeeksforGeeks Skip List Tutorial](https://www.geeksforgeeks.org/skip-list/) - Implementation guide and examples
- Herlihy, M., & Shavit, N. (2012). "The Art of Multiprocessor Programming" (2nd ed.). Morgan Kaufmann. Chapter 14: Concurrent Data Structures.

## Features

### Core Implementation (`skip_list.py`)
- **SkipNode class**: Represents nodes with multiple forward pointers
- **SkipList class**: Main skip list implementation with:
  - `insert(key, value)`: Insert or update a key-value pair
  - `search(key)`: Search for a key (returns value or None)
  - `delete(key)`: Delete a key (returns True/False)
  - `display()`: Show the skip list structure
  - `get_all_items()`: Get all items in sorted order
  - `__len__()`: Get the number of elements
  - `__contains__()`: Check membership (`key in skip_list`)

### Testing (`test_skip_list.py`)
Comprehensive unit tests including:
- Basic operations (insert, search, delete)
- Edge cases (empty list, duplicates, non-existent keys)
- Large datasets (100+ elements)
- Random operation sequences
- Performance benchmarks
- Different data types (integers, strings)

### Visualization (`visualization.py`)
Multiple visualization styles:
- **Standard display**: Level-by-level representation
- **Detailed visualization**: ASCII art showing connections
- **Tower visualization**: Compact view showing node heights

## How Skip Lists Work

1. **Structure**: Multiple levels of linked lists
   - Level 0 contains all elements in sorted order
   - Each higher level acts as an "express lane"
   - Elements are promoted to higher levels probabilistically

2. **Search**: Start at the highest level, move forward until the next element is too large, then drop down a level
   - Expected time: O(log n)

3. **Insert**: Similar to search, find the position, then insert at level 0 and promote to higher levels with probability p (typically 0.5)
   - Expected time: O(log n)

4. **Delete**: Find the node and update all forward pointers pointing to it
   - Expected time: O(log n)

## Usage

### Basic Example

```python
from skip_list import SkipList

# Create a skip list
sl = SkipList(max_level=4, p=0.5)

# Insert key-value pairs
sl.insert(3, "three")
sl.insert(7, "seven")
sl.insert(12, "twelve")

# Search for a key
value = sl.search(7)  # Returns "seven"

# Check membership
if 3 in sl:
    print("Found!")

# Delete a key
sl.delete(7)

# Display structure
sl.display()

# Get all items in sorted order
items = sl.get_all_items()  # [(3, "three"), (12, "twelve")]
```

### Running the Demo

```bash
# Run the basic demonstration
python skip_list.py

# Run all unit tests
python test_skip_list.py

# Run visualization demo
python visualization.py
```

## File Structure

```
assignment359/
├── skip_list.py         # Core skip list implementation
├── test_skip_list.py    # Comprehensive unit tests
├── visualization.py     # Visualization utilities
└── README.md           # This file
```

## Performance Characteristics

| Operation | Average Case | Worst Case | Space |
|-----------|-------------|------------|-------|
| Search    | O(log n)    | O(n)       | O(n)  |
| Insert    | O(log n)    | O(n)       | O(n)  |
| Delete    | O(log n)    | O(n)       | O(n)  |
| Space     | O(n log n)* | O(n²)**    | -     |

\* Expected space complexity  
\*\* Worst case with maximum level promotion

## Key Parameters

- **max_level**: Maximum number of levels (default: 16)
  - Typically set to log₂(n) where n is the expected number of elements
  
- **p**: Probability of promoting to next level (default: 0.5)
  - p = 0.5 gives expected O(log n) performance
  - p = 0.25 uses less space but slightly slower

## Example Output

```
Skip List Structure:
============================================================
Level 2: [7:seven] -> [19:nineteen] -> None
Level 1: [7:seven] -> [12:twelve] -> [19:nineteen] -> None
Level 0: [3:three] -> [6:six] -> [7:seven] -> [9:nine] -> [12:twelve] -> [17:seventeen] -> [19:nineteen] -> [21:twenty-one] -> None
============================================================
```

## Advantages of Skip Lists

1. **Simplicity**: Easier to implement than balanced trees
2. **No Rebalancing**: No complex rebalancing operations needed
3. **Probabilistic Balance**: Automatically maintains balance with high probability
4. **Concurrent Access**: Easier to implement concurrent operations than trees
5. **Good Cache Performance**: Sequential access at each level

## Testing

The test suite includes:
- 15+ unit test cases
- Edge case handling
- Large dataset testing (10,000+ elements)
- Performance benchmarks
- Random operation testing

Run tests with:
```bash
python -m pytest test_skip_list.py -v
# or
python test_skip_list.py
```

## Implementation Notes

1. **Sentinel Node**: Uses a header node with maximum level to simplify operations
2. **Level Generation**: Uses geometric distribution for random level selection
3. **Update Array**: Maintains pointers during search for efficient insertion/deletion
4. **Level Management**: Automatically adjusts the maximum level as needed

## References

- Pugh, William (1990). "Skip Lists: A Probabilistic Alternative to Balanced Trees"
- [OpenDSA Skip List Chapter](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/SkipList.html)

## Author

Assignment 359 - Topic 3 Implementation

## License

Educational use for Assignment 359.

