import os
import math

def is_complex_arithmetic(input_data):
    return '^' in input_data or input_data.strip().startswith('sqrt')

def perform_complex_arithmetic(input_data):
    try:
        if input_data.strip().startswith('sqrt'):
            _, num = input_data.strip().split()
            result = math.sqrt(float(num))
        else:
            base, _, exp = input_data.strip().partition('^')
            result = math.pow(float(base), float(exp))
        return f"RESULT: {result}"
    except Exception as e:
        return f"ERROR: {str(e)}"

# Step 1: Read input
with open('input.txt', 'r') as f:
    input_data = f.read().strip()

# Step 2: Validate using Java
os.system(f"java validate \"{input_data}\" > temp_validation.txt")
with open("temp_validation.txt", 'r') as f:
    validation_result = f.read().strip()

# Step 3: Check logic using Prolog
os.system(f"swipl -s logic_check.pl -g \"validate('{input_data}')\" -t halt. > logic_output.txt")
with open("logic_output.txt", 'r') as f:
    logic_result = f.read().strip()

# Step 4: Decide how to process
if validation_result != "VALID" or logic_result != "OK":
    output = "ERROR: Invalid input or disallowed operation."
else:
    if is_complex_arithmetic(input_data):
        output = perform_complex_arithmetic(input_data)
    else:
        os.system(f"calculator.exe \"{input_data}\" > result.txt")
        with open("result.txt", 'r') as f:
            output = f.read().strip()

# Step 5: Write to output.txt
with open("output.txt", 'w') as f:
    f.write(output)

print("Operation complete. Result written to output.txt")
