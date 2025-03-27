#Algorihm 1
import ast

def read_input_file(file_path):
    input_groups = []
    current_group = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.lower().startswith("array") and "a =" in line:
                # Extract and store the string array A
                a_data = line.split("=", 1)[1].strip()
                current_group['A'] = ast.literal_eval(a_data)

            elif line.lower().startswith("array") and "b =" in line:
                # Extract and store the list of words B
                b_data = line.split("=", 1)[1].strip()
                current_group['B'] = ast.literal_eval(b_data)
                input_groups.append(current_group)
                current_group = {}

    return input_groups

def Algorithm1(inputA, inputB):
    full_string = inputA[0]
    output_order = []
    output_array = []

    for word in inputB:
        index = full_string.find(word)
        if index != -1:
            output_order.append(index)
            output_array.append(word)

    # Sort by index order
    combined = list(zip(output_order, output_array))
    combined.sort()

    if combined:
        output_order, output_array = zip(*combined)
        return list(output_order), list(output_array)
    else:
        return [], []

# Main execution
file_path = "in2a.txt"
input_groups = read_input_file(file_path)

for i, group in enumerate(input_groups, 1):
    output_indices, output_words = Algorithm1(group['A'], group['B'])
    print(f"--- Result for array {i} ---")
    print("Output_order:", output_indices)
    print("Output_array:", output_words)
