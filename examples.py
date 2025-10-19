"""
Usage Examples for Skip List Implementation
Assignment 359 - Topic 3

This file demonstrates various use cases and practical examples
of the skip list data structure.
"""

from skip_list import SkipList
import random


def example_1_basic_operations():
    """Example 1: Basic insert, search, and delete operations"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Operations")
    print("="*70 + "\n")
    
    sl = SkipList()
    
    # Insert some numbers
    print("Inserting numbers: 5, 2, 8, 1, 9, 3")
    for num in [5, 2, 8, 1, 9, 3]:
        sl.insert(num, f"value_{num}")
    
    sl.display()
    
    # Search for values
    print("Searching for key 8:", sl.search(8))
    print("Searching for key 10:", sl.search(10))
    
    # Delete a value
    print("\nDeleting key 5...")
    sl.delete(5)
    sl.display()


def example_2_dictionary_implementation():
    """Example 2: Using skip list as a dictionary"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Skip List as Dictionary")
    print("="*70 + "\n")
    
    # Create a phone book
    phonebook = SkipList()
    
    contacts = [
        ("Alice", "555-1234"),
        ("Bob", "555-5678"),
        ("Charlie", "555-9012"),
        ("Diana", "555-3456"),
        ("Eve", "555-7890")
    ]
    
    print("Building phonebook...")
    for name, number in contacts:
        phonebook.insert(name, number)
        print(f"  Added: {name} -> {number}")
    
    print("\nPhonebook structure:")
    phonebook.display()
    
    # Look up some contacts
    print("Looking up contacts:")
    print(f"  Alice's number: {phonebook.search('Alice')}")
    print(f"  Charlie's number: {phonebook.search('Charlie')}")
    print(f"  Frank's number: {phonebook.search('Frank')}")


def example_3_range_queries():
    """Example 3: Getting values in a range"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Range Queries")
    print("="*70 + "\n")
    
    sl = SkipList()
    
    # Insert random numbers
    numbers = random.sample(range(1, 100), 20)
    print(f"Inserting numbers: {sorted(numbers)}")
    for num in numbers:
        sl.insert(num, f"value_{num}")
    
    # Get all items in range
    print("\nAll items in skip list (sorted):")
    items = sl.get_all_items()
    
    # Find items in range [30, 60]
    range_items = [(k, v) for k, v in items if 30 <= k <= 60]
    print(f"\nItems in range [30, 60]:")
    for key, value in range_items:
        print(f"  {key} -> {value}")


def example_4_priority_queue():
    """Example 4: Using skip list for priority queue operations"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Priority Queue (Task Scheduler)")
    print("="*70 + "\n")
    
    # Task scheduler where priority is the key
    scheduler = SkipList()
    
    tasks = [
        (1, "Critical Bug Fix"),
        (5, "Code Review"),
        (3, "Write Documentation"),
        (2, "Database Backup"),
        (4, "Team Meeting")
    ]
    
    print("Adding tasks with priorities (1 = highest):")
    for priority, task in tasks:
        scheduler.insert(priority, task)
        print(f"  Priority {priority}: {task}")
    
    scheduler.display()
    
    print("Processing tasks in priority order:")
    for priority, task in scheduler.get_all_items():
        print(f"  [{priority}] {task}")


def example_5_student_grades():
    """Example 5: Student grade management system"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Student Grade Management")
    print("="*70 + "\n")
    
    grades = SkipList()
    
    # Insert student scores
    students = [
        (95, "Alice"),
        (87, "Bob"),
        (92, "Charlie"),
        (78, "Diana"),
        (88, "Eve"),
        (95, "Frank"),  # Same score as Alice
        (82, "Grace")
    ]
    
    print("Recording student grades:")
    # Use score as key, but handle duplicates by making composite keys
    for i, (score, name) in enumerate(students):
        # Use (score, i) as key to handle duplicates
        composite_key = f"{score:03d}_{i}"
        grades.insert(composite_key, (score, name))
        print(f"  {name}: {score}")
    
    print("\nStudents ranked by grade (highest to lowest):")
    all_grades = grades.get_all_items()
    for key, (score, name) in reversed(all_grades):
        print(f"  {score} - {name}")
    
    # Find students above 90
    print("\nStudents with A grades (90+):")
    for key, (score, name) in all_grades:
        if score >= 90:
            print(f"  {name}: {score}")


def example_6_time_series_data():
    """Example 6: Time series data storage"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Time Series Data (Temperature Log)")
    print("="*70 + "\n")
    
    temp_log = SkipList()
    
    # Simulate temperature readings (timestamp, temperature)
    import time
    base_time = 1640000000  # Some base timestamp
    
    readings = [
        (base_time + 0, 22.5),
        (base_time + 60, 22.7),
        (base_time + 120, 23.1),
        (base_time + 180, 23.4),
        (base_time + 240, 23.2),
        (base_time + 300, 23.0),
    ]
    
    print("Recording temperature readings:")
    for timestamp, temp in readings:
        temp_log.insert(timestamp, temp)
        print(f"  Time {timestamp}: {temp}°C")
    
    print("\nTemperature timeline:")
    for timestamp, temp in temp_log.get_all_items():
        print(f"  {timestamp} -> {temp}°C")
    
    # Search for specific timestamp
    search_time = base_time + 120
    print(f"\nTemperature at time {search_time}: {temp_log.search(search_time)}°C")


def example_7_performance_comparison():
    """Example 7: Compare skip list vs list performance"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Performance Comparison")
    print("="*70 + "\n")
    
    import time
    
    n = 1000
    data = list(range(n))
    random.shuffle(data)
    
    # Skip List
    sl = SkipList()
    start = time.time()
    for num in data:
        sl.insert(num, num)
    sl_insert_time = time.time() - start
    
    start = time.time()
    for _ in range(100):
        sl.search(random.randint(0, n))
    sl_search_time = time.time() - start
    
    # Regular sorted list
    sorted_list = []
    start = time.time()
    for num in data:
        sorted_list.append(num)
        sorted_list.sort()
    list_insert_time = time.time() - start
    
    start = time.time()
    for _ in range(100):
        target = random.randint(0, n)
        # Binary search
        left, right = 0, len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid] == target:
                break
            elif sorted_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    list_search_time = time.time() - start
    
    print(f"Operations on {n} elements:")
    print(f"\nInsertion (keeping sorted order):")
    print(f"  Skip List: {sl_insert_time:.4f}s")
    print(f"  Sorted List: {list_insert_time:.4f}s")
    print(f"  Speedup: {list_insert_time/sl_insert_time:.2f}x")
    
    print(f"\nSearch (100 random searches):")
    print(f"  Skip List: {sl_search_time:.4f}s")
    print(f"  Binary Search: {list_search_time:.4f}s")
    print(f"  Ratio: {sl_search_time/list_search_time:.2f}x")


def example_8_concurrent_simulation():
    """Example 8: Simulate concurrent-like operations"""
    print("\n" + "="*70)
    print("EXAMPLE 8: Simulated Concurrent Operations")
    print("="*70 + "\n")
    
    sl = SkipList()
    
    print("Simulating interleaved insert/delete operations:")
    operations = [
        ('insert', 5, 'five'),
        ('insert', 3, 'three'),
        ('insert', 7, 'seven'),
        ('search', 5, None),
        ('delete', 3, None),
        ('insert', 9, 'nine'),
        ('search', 3, None),
        ('insert', 1, 'one'),
    ]
    
    for op, key, value in operations:
        if op == 'insert':
            sl.insert(key, value)
            print(f"  INSERT {key} -> {value}")
        elif op == 'delete':
            result = sl.delete(key)
            print(f"  DELETE {key} -> {'Success' if result else 'Failed'}")
        elif op == 'search':
            result = sl.search(key)
            print(f"  SEARCH {key} -> {result}")
    
    print("\nFinal state:")
    sl.display()


def run_all_examples():
    """Run all examples"""
    print("\n" + "="*70)
    print("SKIP LIST USAGE EXAMPLES")
    print("Assignment 359 - Topic 3")
    print("="*70)
    
    random.seed(42)  # For reproducibility
    
    example_1_basic_operations()
    example_2_dictionary_implementation()
    example_3_range_queries()
    example_4_priority_queue()
    example_5_student_grades()
    example_6_time_series_data()
    example_7_performance_comparison()
    example_8_concurrent_simulation()
    
    print("\n" + "="*70)
    print("All examples completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_examples()

