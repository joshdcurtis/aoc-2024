import sys

def is_safish(nums: list[int]) -> bool:
    if len(nums) < 3:
        return True

    decreasing = False
    skip_first = is_safe(nums[1:])

    if skip_first or nums[1] == nums[0]:
        return skip_first
    if nums[1] < nums[0]:
        decreasing = True

    for i in range(1,len(nums)):
        if (decreasing and not (nums[i-1] - 4 < nums[i] < nums[i-1]))\
            or (not decreasing and not (nums[i-1] < nums[i] < nums[i-1] + 4)):
            return is_safe(nums[:i-1] + nums[i:]) or (is_safe(nums[:i] + nums[i+1:]) if i < len(nums) - 1 else True)
    return True

def is_safe(nums: list[int]) -> bool:
    if len(nums) < 2:
        return True

    decreasing = False
    if nums[1] < nums[0]:
        decreasing = True
    
    for i in range(1,len(nums)):
        if (decreasing and not (nums[i-1] - 4 < nums[i] < nums[i-1]))\
            or (not decreasing and not (nums[i-1] < nums[i] < nums[i-1] + 4)):
            return False
    return True

def solution(input: str) -> tuple[str, str]:
    safe_reports = 0
    safish_reports = 0
    reports = input.splitlines()
    for report in reports:
        nums = [int(x) for x in report.split()]
        if is_safe(nums):
            safe_reports += 1
        if is_safish(nums):
            safish_reports += 1
        else:
            print("Found a report to be still unsafe after dampening:")
            print(nums)
    return str(safe_reports), str(safish_reports)

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
