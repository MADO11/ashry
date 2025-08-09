import subprocess
import sys

def read_list_from_file(filename):
    """Reads a comma-separated list from a file, handling UTF-8 encoding."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        sys.exit(1)

def main():
    """Constructs and executes the npx command with arguments from files."""
    agent_list = read_list_from_file('agents.txt')
    mcp_list = read_list_from_file('mcps.txt')

    command = [
        "npx", "--package=claude-code@latest", "bun", "run", "index.ts",
        "--agent", agent_list,
        "--mcp", mcp_list
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Command executed successfully.")
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("stdout:", e.stdout)
        print("stderr:", e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

