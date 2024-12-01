from collections import Counter
import sys

# sys.argv[0] is the script name itself
# sys.argv[1] would be the first argument (in this case, the input file path)
def solution(input: str) -> tuple[str, str]:
    list_a = []
    list_b = []
    lines = input.splitlines()
    for line in lines:
        num_1, num_2 = line.split()
        list_a.append(int(num_1))
        list_b.append(int(num_2))

    list_a.sort()
    list_b.sort()
    frequencies = Counter(list_b)

    distance = 0
    similarity = 0
    for i in range(len(lines)):
        id_a = list_a[i]
        id_b = list_b[i]
        distance += abs(id_a - id_b)
        similarity += id_a * frequencies[id_a]

    return str(distance), str(similarity)

def main():
    # Check if an argument was passed
    if len(sys.argv) < 2:
        print("Error: No input file provided")
        sys.exit(1)
    
    # Get the input file path
    input_file_path = sys.argv[1]
    
    # Read the input file
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            results = solution(content)
            for result in results:
                print(result)
    except FileNotFoundError:
        print(f"Error: File {input_file_path} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
