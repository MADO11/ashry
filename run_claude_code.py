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
        "npx", "claude-code@latest",
        "--agent", agent_list,
        "--mcp", mcp_list
    ]

    subprocess.run(command)

if __name__ == "__main__":
    main()
