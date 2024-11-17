import git

REPO_PATH = "./"  # Path to project repository

def commit_changes(task, code):
    """Commits the changes to the Git repository."""
    try:
        repo = git.Repo(REPO_PATH)
        with open(f"{task}.py", "w") as file:
            file.write(code)
        repo.index.add([f"{task}.py"])
        repo.index.commit(f"Updated {task} with new code.")
        print("Changes committed successfully.")
    except Exception as e:
        print(f"Error during commit: {e}")

def revert_changes(task):
    """Reverts changes for the specified task."""
    try:
        repo = git.Repo(REPO_PATH)
        repo.git.checkout(f"{task}.py")
        print("Reverted changes successfully.")
    except Exception as e:
        print(f"Error during revert: {e}")
