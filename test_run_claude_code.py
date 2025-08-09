import unittest
from unittest.mock import patch, mock_open
import run_claude_code
import os

class TestRunClaudeCode(unittest.TestCase):

    def test_read_list_from_file_valid(self):
        m = mock_open(read_data="agent1,agent2,agent3")
        with patch('builtins.open', m):
            result = run_claude_code.read_list_from_file("dummy_path")
            self.assertEqual(result, "agent1,agent2,agent3")

    def test_read_list_from_file_with_whitespace(self):
        m = mock_open(read_data=" agent1 , agent2,agent3 ")
        with patch('builtins.open', m):
            result = run_claude_code.read_list_from_file("dummy_path")
            self.assertEqual(result, "agent1,agent2,agent3")

    def test_read_list_from_file_with_empty_items(self):
        m = mock_open(read_data="agent1,,agent2, ,agent3")
        with patch('builtins.open', m):
            result = run_claude_code.read_list_from_file("dummy_path")
            self.assertEqual(result, "agent1,agent2,agent3")

    def test_read_list_from_file_internationalized(self):
        m = mock_open(read_data="مرحبا,עולם")
        with patch('builtins.open', m):
            result = run_claude_code.read_list_from_file("dummy_path")
            self.assertEqual(result, "مرحبا,עולם")

    def test_read_list_from_file_empty(self):
        m = mock_open(read_data="")
        with patch('builtins.open', m):
            result = run_claude_code.read_list_from_file("dummy_path")
            self.assertEqual(result, "")

    @patch('sys.exit')
    def test_read_list_from_file_not_found(self, mock_exit):
        with patch('builtins.open', side_effect=FileNotFoundError):
            run_claude_code.read_list_from_file("non_existent_path")
            mock_exit.assert_called_with(1)

    @patch('subprocess.run')
    @patch('run_claude_code.find_package_path', return_value='/fake/path/to/claude-code')
    @patch('run_claude_code.read_list_from_file')
    def test_main_function(self, mock_read_list, mock_find_package, mock_subprocess_run):
        mock_read_list.side_effect = ["agent1,agent2", "mcp1,mcp2"]
        run_claude_code.main()
        mock_subprocess_run.assert_called_with(
            ["../.bin/bun", "run", "index.ts", "--agent", "agent1,agent2", "--mcp", "mcp1,mcp2"],
            check=True, capture_output=True, text=True, cwd='/fake/path/to/claude-code'
        )

