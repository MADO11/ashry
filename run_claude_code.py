import subprocess
import sys
import os
import re

def read_list_from_file(filename):
    """Reads a comma-separated list from a file, handling UTF-8 encoding."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return ""
            # Filter out empty strings that may result from multiple commas
            items = [item.strip() for item in content.split(',') if item.strip()]
            return ",".join(items)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Skipping this argument.")
        sys.exit(1)

def find_package_path(package_name):
    """Finds the path to an installed npm package."""
    try:
        # This is a simplification; a real implementation might need to search more robustly
        path = os.path.join('node_modules', package_name)
        if os.path.isdir(path):
            return path
    except Exception as e:
        print(f"Error finding package {package_name}: {e}")
    return None
def main():
    """Constructs and executes the npx command with arguments from files."""
    agent_list = read_list_from_file('agents.txt')
    mcp_list = read_list_from_file('mcps.txt')
    package_path = find_package_path('claude-code')

    if not package_path:
        print("Error: 'claude-code' package not found in node_modules.")
        sys.exit(1)

    command = ["../.bin/bun", "run", "index.ts", "--agent", agent_list, "--mcp", mcp_list]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, cwd=package_path)
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


