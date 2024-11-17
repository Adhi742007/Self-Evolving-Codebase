import json
from code_generator import generate_code
from tester import run_tests
from version_control import commit_changes, revert_changes

def load_objectives():
    """Load user-defined objectives from a JSON file."""
    with open("objectives.json", "r") as file:
        return json.load(file)

def main():
    # Step 1: Load Objectives
    objectives = load_objectives()
    print("Loaded Objectives:", objectives)
    
    for task, details in objectives.items():
        print(f"\nProcessing Task: {task}")
        description = details["description"]
        print(f"Objective: {description}")
        
        # Step 2: Generate Code
        print("Generating new code...")
        success, new_code = generate_code(description)
        
        if not success:
            print(f"Failed to generate code for task: {task}")
            continue
        
        print("Generated Code:")
        print(new_code)
        
        # Step 3: Test the Code
        print("Testing the new code...")
        tests_passed = run_tests(new_code, task)
        
        if tests_passed:
            print("Tests Passed! Committing changes...")
            commit_changes(task, new_code)
        else:
            print("Tests Failed. Reverting changes...")
            revert_changes(task)
    
    print("\nAll tasks processed!")

if __name__ == "__main__":
    main()
