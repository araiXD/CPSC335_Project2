import heapq
import ast

def read_input_file(file_path):
    arrays = []
    array_lines = []
    collecting = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Start of array
            if line.startswith("Array_"):
                collecting = True
                # Save previous array if exists
                if array_lines:
                    array_text = ''.join(array_lines)
                    arrays.append(ast.literal_eval(array_text))
                    array_lines = []
                # Add first line of new array
                array_lines.append(line.split("=", 1)[1].strip())
            elif collecting and line:
                # Collect continuation lines
                array_lines.append(line)
            # Handle final array in file
        if array_lines:
            array_text = ''.join(array_lines)
            arrays.append(ast.literal_eval(array_text))
    return arrays    
    
def merge_sorted_list(all_lists):
    min_heap = []
    merged_list = []

    # Initialize heap with first element of each list
    for i, lst in enumerate(all_lists):
        if lst: # Check for empty
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    # Extract smallest element from the heap and add next element
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        # If there is a next, push it to the heap
        if element_index + 1 < len(all_lists[list_index]):
            next_value = all_lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_list

file_path = "in2c.txt"
all_lists = read_input_file(file_path)

for i, array_group in enumerate(all_lists, 1):
    result = merge_sorted_list(array_group)
    print(f"Array_{i}: {result}")