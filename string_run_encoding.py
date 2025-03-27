def string_run_encoding(S):
    if not S:
        return "Empty String"
    
    result = []
    count = 1

    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{S[i - 1]}")
            else:
                result.append(S[i - 1])
            count = 1

    # Process last run
    if count > 1:
        result.append(f"{count}{S[-1]}")
    else:
        result.append(S[-1])

    return "".join(result)

# while True:
#     sample = input("Enter a string (or 'exit' to stop): ")
#     if sample.lower() == 'exit':
#         break
#     print(f'"{sample}" becomes "{string_run_encoding(sample)}"')

samples = [
    "ddd",
    "heloooooooo there",
    "choosemeeky and tuition-free"
]

for sample in samples:
    print(f'"{sample}" becomes "{string_run_encoding(sample)}"')