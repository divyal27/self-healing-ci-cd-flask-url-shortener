import sys

def main():
    log = sys.stdin.read()
    print("=== Self-healing analysis ===")
    if "pytest" in log:
        print("Hint: Tests failed. Run 'python -m pytest' locally and fix failing tests.")
    if "Could not open requirements file" in log:
        print("Hint: requirements.txt missing or wrong path. Check file name and location.")
    print("=== End of analysis ===")

if __name__ == "__main__":
    main()
