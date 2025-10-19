"""
Visualization module for Skip List
Provides visual representation of the skip list structure
"""

from skip_list import SkipList


def visualize_skip_list_detailed(sl: SkipList) -> None:
    """
    Create a detailed ASCII visualization of the skip list structure.
    Shows the connections between nodes at different levels.
    
    Args:
        sl: SkipList instance to visualize
    """
    if sl.level == -1 or sl.header.forward[0] is None:
        print("\n[Empty Skip List]\n")
        return
    
    # Collect all nodes at level 0
    nodes = []
    current = sl.header.forward[0]
    while current:
        nodes.append(current)
        current = current.forward[0]
    
    if not nodes:
        print("\n[Empty Skip List]\n")
        return
    
    print("\n" + "="*80)
    print("DETAILED SKIP LIST VISUALIZATION")
    print("="*80)
    
    # Print each level
    for level in range(sl.level, -1, -1):
        print(f"\nLevel {level}:")
        print("-" * 80)
        
        # Build the visualization for this level
        current = sl.header.forward[level]
        node_positions = []
        
        # Find which nodes exist at this level
        while current:
            # Find position of this node in the base list
            for i, node in enumerate(nodes):
                if node.key == current.key:
                    node_positions.append((i, current))
                    break
            current = current.forward[level]
        
        # Create the visual representation
        line = "HEAD"
        for i, (pos, node) in enumerate(node_positions):
            # Add spacing
            if i == 0:
                line += " --> "
            else:
                prev_pos = node_positions[i-1][0]
                spacing = (pos - prev_pos - 1) * 8
                line += " " + "-" * spacing + " --> "
            
            line += f"[{node.key}]"
        
        line += " --> None"
        print(line)
    
    print("\n" + "="*80)
    print(f"Total nodes: {len(nodes)}")
    print(f"Maximum level: {sl.level}")
    print("="*80 + "\n")


def visualize_skip_list_compact(sl: SkipList) -> None:
    """
    Create a compact visualization showing node heights.
    
    Args:
        sl: SkipList instance to visualize
    """
    if sl.header.forward[0] is None:
        print("\n[Empty Skip List]\n")
        return
    
    # Collect all nodes with their max levels
    node_info = []
    current = sl.header.forward[0]
    
    while current:
        # Find max level for this node
        max_level = 0
        for level in range(sl.level + 1):
            temp = sl.header.forward[level]
            while temp:
                if temp.key == current.key:
                    max_level = level
                    break
                temp = temp.forward[level]
        
        node_info.append((current.key, current.value, max_level))
        current = current.forward[0]
    
    print("\n" + "="*80)
    print("SKIP LIST TOWER VISUALIZATION")
    print("="*80)
    print("\nEach node is shown as a tower with height = max level")
    print()
    
    # Find the maximum level for visualization
    max_display_level = max(info[2] for info in node_info)
    
    # Print from top level down
    for level in range(max_display_level, -1, -1):
        print(f"L{level}: ", end="")
        for key, value, max_level in node_info:
            if max_level >= level:
                print(f"[{key:3}]", end=" ")
            else:
                print("     ", end=" ")
        print()
    
    # Print keys at bottom
    print("     ", end="")
    for key, value, _ in node_info:
        print(f" {key:3} ", end=" ")
    print("\n")
    
    # Print statistics
    print("Node Details:")
    for key, value, max_level in node_info:
        print(f"  Key: {key:3} | Value: {value:15} | Max Level: {max_level}")
    
    print("\n" + "="*80 + "\n")


def demo_visualizations():
    """
    Demonstrate different visualization styles.
    """
    import random
    random.seed(42)
    
    print("\n" + "="*80)
    print("SKIP LIST VISUALIZATION DEMO")
    print("="*80 + "\n")
    
    sl = SkipList(max_level=4, p=0.5)
    
    # Insert some data
    data = [(3, "three"), (6, "six"), (7, "seven"), (9, "nine"), 
            (12, "twelve"), (17, "seventeen"), (19, "nineteen"), 
            (21, "twenty-one"), (25, "twenty-five")]
    
    print("Inserting data into skip list...")
    for key, value in data:
        sl.insert(key, value)
        print(f"  Inserted: {key} -> {value}")
    
    # Show standard display
    print("\n" + "="*80)
    print("1. STANDARD DISPLAY (Built-in)")
    print("="*80)
    sl.display()
    
    # Show detailed visualization
    print("\n" + "="*80)
    print("2. DETAILED VISUALIZATION")
    print("="*80)
    visualize_skip_list_detailed(sl)
    
    # Show compact visualization
    print("\n" + "="*80)
    print("3. TOWER VISUALIZATION")
    print("="*80)
    visualize_skip_list_compact(sl)
    
    # Demonstrate operations with visualization
    print("\n" + "="*80)
    print("4. OPERATIONS WITH VISUALIZATION")
    print("="*80 + "\n")
    
    print("Deleting key 7...")
    sl.delete(7)
    visualize_skip_list_compact(sl)
    
    print("\nInserting new key 15...")
    sl.insert(15, "fifteen")
    visualize_skip_list_compact(sl)


if __name__ == "__main__":
    demo_visualizations()

