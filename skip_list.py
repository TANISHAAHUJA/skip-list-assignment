"""
Skip List Data Structure Implementation in Python
Topic 3 - Assignment 359

A skip list is a probabilistic data structure that allows O(log n) average time
complexity for search, insertion, and deletion operations.

Reference: https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/SkipList.html
"""

import random
from typing import Optional, Any


class SkipNode:
    """
    Node class for Skip List.
    Each node contains a key-value pair and forward pointers to next nodes at each level.
    """
    
    def __init__(self, key: Any, value: Any, level: int):
        self.key = key
        self.value = value
        # Forward pointers for each level
        self.forward = [None] * (level + 1)
    
    def __repr__(self):
        return f"SkipNode(key={self.key}, value={self.value})"


class SkipList:
    """
    Skip List implementation with insert, search, delete, and display operations.
    """
    
    def __init__(self, max_level: int = 16, p: float = 0.5):
        """
        Initialize skip list.
        
        Args:
            max_level: Maximum number of levels in the skip list
            p: Probability for level promotion (typically 0.5)
        """
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(None, None, max_level)
        self.level = 0  # Current maximum level in the skip list
    
    def random_level(self) -> int:
        """
        Generate a random level for a new node.
        Uses geometric distribution with probability p.
        
        Returns:
            Random level between 0 and max_level
        """
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a key in the skip list.
        
        Args:
            key: Key to search for
            
        Returns:
            Value associated with the key if found, None otherwise
        """
        current = self.header
        
        # Start from highest level and move down
        for i in range(self.level, -1, -1):
            # Move forward while the next node's key is less than search key
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        
        # Move to the next node at level 0
        current = current.forward[0]
        
        # Check if we found the key
        if current and current.key == key:
            return current.value
        return None
    
    def insert(self, key: Any, value: Any) -> None:
        """
        Insert a key-value pair into the skip list.
        
        Args:
            key: Key to insert
            value: Value associated with the key
        """
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find the position to insert
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        # Move to level 0
        current = current.forward[0]
        
        # If key already exists, update the value
        if current and current.key == key:
            current.value = value
        else:
            # Generate random level for new node
            new_level = self.random_level()
            
            # If new level is greater than current level, update header pointers
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            
            # Create new node
            new_node = SkipNode(key, value, new_level)
            
            # Insert node by updating forward pointers
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node
    
    def delete(self, key: Any) -> bool:
        """
        Delete a key from the skip list.
        
        Args:
            key: Key to delete
            
        Returns:
            True if key was found and deleted, False otherwise
        """
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find the node to delete
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If key found, delete it
        if current and current.key == key:
            # Update forward pointers
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            
            # Update level if necessary
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
            
            return True
        
        return False
    
    def display(self) -> None:
        """
        Display the skip list structure level by level.
        """
        print("\n" + "="*60)
        print("Skip List Structure:")
        print("="*60)
        
        for i in range(self.level, -1, -1):
            print(f"Level {i}: ", end="")
            node = self.header.forward[i]
            while node:
                print(f"[{node.key}:{node.value}]", end=" -> ")
                node = node.forward[i]
            print("None")
        print("="*60 + "\n")
    
    def get_all_items(self) -> list:
        """
        Get all key-value pairs in sorted order.
        
        Returns:
            List of (key, value) tuples in sorted order
        """
        items = []
        current = self.header.forward[0]
        while current:
            items.append((current.key, current.value))
            current = current.forward[0]
        return items
    
    def __len__(self) -> int:
        """
        Return the number of elements in the skip list.
        """
        count = 0
        current = self.header.forward[0]
        while current:
            count += 1
            current = current.forward[0]
        return count
    
    def __contains__(self, key: Any) -> bool:
        """
        Check if a key exists in the skip list.
        """
        return self.search(key) is not None
    
    def __repr__(self):
        items = self.get_all_items()
        return f"SkipList({items})"


def demo_skip_list():
    """
    Demonstration of skip list operations.
    """
    print("\n" + "="*60)
    print("SKIP LIST DEMONSTRATION")
    print("="*60 + "\n")
    
    # Create a skip list
    sl = SkipList(max_level=4, p=0.5)
    
    # Test insertions
    print("1. INSERTION TEST")
    print("-" * 60)
    test_data = [(3, "three"), (6, "six"), (7, "seven"), (9, "nine"), 
                 (12, "twelve"), (19, "nineteen"), (17, "seventeen"), 
                 (26, "twenty-six"), (21, "twenty-one"), (25, "twenty-five")]
    
    for key, value in test_data:
        print(f"Inserting: {key} -> {value}")
        sl.insert(key, value)
    
    sl.display()
    print(f"Total elements: {len(sl)}\n")
    
    # Test search
    print("2. SEARCH TEST")
    print("-" * 60)
    search_keys = [7, 19, 100, 3]
    for key in search_keys:
        result = sl.search(key)
        if result:
            print(f"Found: {key} -> {result}")
        else:
            print(f"Not found: {key}")
    print()
    
    # Test contains
    print("3. MEMBERSHIP TEST")
    print("-" * 60)
    print(f"Is 12 in skip list? {12 in sl}")
    print(f"Is 50 in skip list? {50 in sl}")
    print()
    
    # Test deletion
    print("4. DELETION TEST")
    print("-" * 60)
    delete_keys = [19, 7, 100]
    for key in delete_keys:
        result = sl.delete(key)
        print(f"Delete {key}: {'Success' if result else 'Failed (not found)'}")
    
    sl.display()
    print(f"Total elements: {len(sl)}\n")
    
    # Show sorted order
    print("5. SORTED ORDER")
    print("-" * 60)
    print("All items in sorted order:")
    for key, value in sl.get_all_items():
        print(f"  {key} -> {value}")
    print()
    
    # Test update
    print("6. UPDATE TEST")
    print("-" * 60)
    print("Updating key 12 with new value 'TWELVE'")
    sl.insert(12, "TWELVE")
    print(f"Value for key 12: {sl.search(12)}")
    sl.display()


if __name__ == "__main__":
    # Set seed for reproducibility
    random.seed(42)
    demo_skip_list()

