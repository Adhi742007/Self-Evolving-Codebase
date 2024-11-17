import subprocess

def run_tests(new_code, task_name):
    """
    Runs a set of unit tests on the generated code.
    Returns True if all tests pass; otherwise, False.
    """
    try:
        # Save the code to a temporary file
        test_file = f"{task_name}_test.py"
        with open(test_file, "w") as file:
            file.write(new_code)
        
        # Run pytest on the temporary file
        result = subprocess.run(["pytest", test_file], capture_output=True, text=True)
        print(result.stdout)
        return result.returncode == 0  # Return True if all tests pass
    except Exception as e:
        print(f"Error during testing: {e}")
        return False
