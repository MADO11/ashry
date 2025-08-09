# Ashry Project

This project provides a workaround for executing the `npx claude-code@latest` command, which fails when supplied with extensive or internationalized command-line arguments. It uses a Python wrapper to read agent and MCP lists from files, ensuring robust and reliable execution.

## Problem

The `claude-code` package has two key limitations:
1.  It does not correctly handle long, comma-separated lists of agent and MCP names, especially when they include internationalized characters.
2.  The package is not executable via `npx` due to a missing `bin` field in its `package.json`.

## Solution

This project implements a Python wrapper script, `run_claude_code.py`, that bypasses these issues. The script:
1.  Reads agent and MCP lists from `agents.txt` and `mcps.txt`.
2.  Cleans and sanitizes the lists to handle extra whitespace and empty entries.
3.  Executes the `claude-code` script using a locally installed `bun` dependency, ensuring the environment is correctly configured.

## Setup

1.  **Install Dependencies**:
    Install the required `npm` packages, including `bun` and `claude-code`:
    ```bash
    npm install
    ```

## Usage

1.  **Populate Agent and MCP Files**:
    -   Add your comma-separated agent names to `agents.txt`.
    -   Add your comma-separated MCP names to `mcps.txt`.

2.  **Run the Script**:
    Execute the wrapper script from the command line:
    ```bash
    python3 run_claude_code.py
    ```
