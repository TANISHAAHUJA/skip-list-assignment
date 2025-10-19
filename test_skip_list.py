"""
Unit tests for Skip List implementation
"""

import unittest
import random
from skip_list import SkipList, SkipNode


class TestSkipNode(unittest.TestCase):
    """Test cases for SkipNode class"""
    
    def test_node_creation(self):
        """Test node creation with different levels"""
        node = SkipNode(5, "five", 3)
        self.assertEqual(node.key, 5)
        self.assertEqual(node.value, "five")
        self.assertEqual(len(node.forward), 4)  # level 3 means 4 pointers (0-3)
    
    def test_node_forward_pointers(self):
        """Test that forward pointers are initialized to None"""
        node = SkipNode(10, "ten", 2)
        self.assertTrue(all(ptr is None for ptr in node.forward))


class TestSkipList(unittest.TestCase):
    """Test cases for SkipList class"""
    
    def setUp(self):
        """Set up test fixtures"""
        random.seed(42)  # For reproducibility
        self.sl = SkipList(max_level=4, p=0.5)
    
    def test_empty_skip_list(self):
        """Test empty skip list"""
        self.assertEqual(len(self.sl), 0)
        self.assertIsNone(self.sl.search(1))
        self.assertEqual(self.sl.get_all_items(), [])
    
    def test_insert_single_element(self):
        """Test inserting a single element"""
        self.sl.insert(5, "five")
        self.assertEqual(len(self.sl), 1)
        self.assertEqual(self.sl.search(5), "five")
    
    def test_insert_multiple_elements(self):
        """Test inserting multiple elements"""
        data = [(3, "three"), (1, "one"), (4, "four"), (2, "two")]
        for key, value in data:
            self.sl.insert(key, value)
        
        self.assertEqual(len(self.sl), 4)
        self.assertEqual(self.sl.search(1), "one")
        self.assertEqual(self.sl.search(2), "two")
        self.assertEqual(self.sl.search(3), "three")
        self.assertEqual(self.sl.search(4), "four")
    
    def test_insert_maintains_sorted_order(self):
        """Test that insertions maintain sorted order"""
        keys = [9, 3, 7, 1, 5, 2, 8, 4, 6]
        for key in keys:
            self.sl.insert(key, str(key))
        
        items = self.sl.get_all_items()
        sorted_keys = [item[0] for item in items]
        self.assertEqual(sorted_keys, sorted(keys))
    
    def test_update_existing_key(self):
        """Test updating value for existing key"""
        self.sl.insert(5, "five")
        self.assertEqual(self.sl.search(5), "five")
        
        self.sl.insert(5, "FIVE")
        self.assertEqual(self.sl.search(5), "FIVE")
        self.assertEqual(len(self.sl), 1)  # Length should not change
    
    def test_search_nonexistent_key(self):
        """Test searching for nonexistent key"""
        self.sl.insert(5, "five")
        self.assertIsNone(self.sl.search(10))
    
    def test_delete_existing_key(self):
        """Test deleting existing key"""
        self.sl.insert(5, "five")
        self.assertTrue(self.sl.delete(5))
        self.assertIsNone(self.sl.search(5))
        self.assertEqual(len(self.sl), 0)
    
    def test_delete_nonexistent_key(self):
        """Test deleting nonexistent key"""
        self.sl.insert(5, "five")
        self.assertFalse(self.sl.delete(10))
        self.assertEqual(len(self.sl), 1)  # Length should not change
    
    def test_delete_from_empty_list(self):
        """Test deleting from empty list"""
        self.assertFalse(self.sl.delete(1))
    
    def test_multiple_deletions(self):
        """Test multiple deletions"""
        data = [(i, str(i)) for i in range(10)]
        for key, value in data:
            self.sl.insert(key, value)
        
        self.assertEqual(len(self.sl), 10)
        
        # Delete even numbers
        for i in range(0, 10, 2):
            self.assertTrue(self.sl.delete(i))
        
        self.assertEqual(len(self.sl), 5)
        
        # Verify odd numbers still exist
        for i in range(1, 10, 2):
            self.assertEqual(self.sl.search(i), str(i))
        
        # Verify even numbers are gone
        for i in range(0, 10, 2):
            self.assertIsNone(self.sl.search(i))
    
    def test_contains_operator(self):
        """Test __contains__ operator"""
        self.sl.insert(5, "five")
        self.assertTrue(5 in self.sl)
        self.assertFalse(10 in self.sl)
    
    def test_large_dataset(self):
        """Test with larger dataset"""
        n = 100
        data = list(range(n))
        random.shuffle(data)
        
        # Insert in random order
        for key in data:
            self.sl.insert(key, str(key))
        
        self.assertEqual(len(self.sl), n)
        
        # Verify all elements
        for key in range(n):
            self.assertEqual(self.sl.search(key), str(key))
        
        # Verify sorted order
        items = self.sl.get_all_items()
        sorted_keys = [item[0] for item in items]
        self.assertEqual(sorted_keys, list(range(n)))
    
    def test_duplicate_insertions(self):
        """Test that duplicate insertions update values"""
        for _ in range(3):
            self.sl.insert(5, "five")
        
        self.assertEqual(len(self.sl), 1)
        self.assertEqual(self.sl.search(5), "five")
    
    def test_random_operations(self):
        """Test random sequence of operations"""
        random.seed(123)
        operations = []
        
        # Generate random operations
        for _ in range(50):
            op = random.choice(['insert', 'search', 'delete'])
            key = random.randint(1, 20)
            operations.append((op, key))
        
        # Execute operations
        inserted_keys = set()
        for op, key in operations:
            if op == 'insert':
                self.sl.insert(key, str(key))
                inserted_keys.add(key)
            elif op == 'search':
                result = self.sl.search(key)
                if key in inserted_keys:
                    self.assertIsNotNone(result)
            elif op == 'delete':
                self.sl.delete(key)
                inserted_keys.discard(key)
        
        # Verify final state
        self.assertEqual(len(self.sl), len(inserted_keys))
        for key in inserted_keys:
            self.assertTrue(key in self.sl)
    
    def test_string_keys(self):
        """Test skip list with string keys"""
        sl = SkipList()
        words = ["apple", "banana", "cherry", "date", "elderberry"]
        
        for word in words:
            sl.insert(word, len(word))
        
        self.assertEqual(len(sl), 5)
        self.assertEqual(sl.search("banana"), 6)
        self.assertEqual(sl.search("date"), 4)
        
        # Verify sorted order
        items = sl.get_all_items()
        sorted_words = [item[0] for item in items]
        self.assertEqual(sorted_words, sorted(words))


class TestSkipListPerformance(unittest.TestCase):
    """Performance-related tests for Skip List"""
    
    def test_level_distribution(self):
        """Test that random level generation follows expected distribution"""
        sl = SkipList(max_level=10, p=0.5)
        levels = [sl.random_level() for _ in range(1000)]
        
        # Most nodes should be at level 0
        level_0_count = levels.count(0)
        self.assertGreater(level_0_count, 400)  # Should be around 50%
        
        # Higher levels should be progressively rarer
        max_level = max(levels)
        self.assertLessEqual(max_level, 10)


def run_performance_test():
    """
    Run a simple performance comparison between skip list operations
    """
    import time
    
    print("\n" + "="*60)
    print("PERFORMANCE TEST")
    print("="*60 + "\n")
    
    sl = SkipList()
    n = 10000
    
    # Test insertion time
    print(f"Testing with {n} elements...")
    keys = list(range(n))
    random.shuffle(keys)
    
    start = time.time()
    for key in keys:
        sl.insert(key, str(key))
    insert_time = time.time() - start
    
    print(f"Insertion time: {insert_time:.4f} seconds")
    print(f"Average per insertion: {(insert_time/n)*1000:.4f} ms")
    
    # Test search time
    search_keys = random.sample(range(n), 1000)
    start = time.time()
    for key in search_keys:
        sl.search(key)
    search_time = time.time() - start
    
    print(f"\nSearch time (1000 searches): {search_time:.4f} seconds")
    print(f"Average per search: {(search_time/1000)*1000:.4f} ms")
    
    # Test deletion time
    delete_keys = random.sample(range(n), 1000)
    start = time.time()
    for key in delete_keys:
        sl.delete(key)
    delete_time = time.time() - start
    
    print(f"\nDeletion time (1000 deletions): {delete_time:.4f} seconds")
    print(f"Average per deletion: {(delete_time/1000)*1000:.4f} ms")
    
    print(f"\nFinal skip list size: {len(sl)}")
    print(f"Maximum level reached: {sl.level}")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Run unit tests
    print("Running unit tests...\n")
    unittest.main(argv=[''], verbosity=2, exit=False)
    
    # Run performance test
    random.seed(42)
    run_performance_test()

