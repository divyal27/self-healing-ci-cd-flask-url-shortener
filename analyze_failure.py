import sys

def main():
    log = sys.stdin.read()
    print("=== Self-healing analysis ===")

    if "ModuleNotFoundError" in log:
        print("Hint: A module is missing. Check requirements.txt and install it with pip.")

    if "AssertionError" in log:
        print("Hint: A test assertion failed. Re-run 'python -m pytest' locally and fix the failing test.")

    if "Could not open requirements file" in log:
        print("Hint: requirements.txt is missing or in the wrong place. Keep it in the repo root and commit it.")

    print("=== End of analysis ===")

if __name__ == "__main__":
    main()

