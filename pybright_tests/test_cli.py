from pprint import pprint
from subprocess import CalledProcessError
from unittest.mock import Mock

import pytest

from pybright import cli
from pybright.cli import BrightCallError, _version, bright, version


def mock_bright_response(response=None, side_effect=None):
    cli._call_command_and_parse_json = Mock(return_value=(response, None), side_effect=side_effect)


def test_version():
    mock_bright_response({'success': True, 'message': 'Version displayed',
                          'stdout': '1.0.2-next.201806261725\n', 'stderr': '', 'data': {'version': '1.0.2-next.201806261725\n'}})

    assert _version() == "1.0.2-next.201806261725"
    assert _version() == version()


def test_bright_syntax_error():
    mock_bright_response(side_effect=CalledProcessError(1, 'bright --rfj szos-jobs list jobs', output="""{
  "success": false,
  "message": "Command syntax invalid",
  "stdout": "",
  "stderr": "\\nSyntax Error:\\nYou specified the following unknown values: \\"list\\", \\"jobs\\".\\n\\n Could not interpret them as a group, command name, or positional option.\\n\\nUse \\"bright szos-jobs list jobs --help\\" to view command description, usage, and options.\\n",
  "data": [
    {
      "message": "You specified the following unknown values: \\"list\\", \\"jobs\\".\\n\\n Could not interpret them as a group, command name, or positional option.\\n",
      "optionInError": "unknown"
    }
  ]
}"""))

    with pytest.raises(BrightCallError) as excinfo:
        bright('bright --rfj syntax error')
    excinfo.value.returncode == 1


if __name__ == '__main__':
    pytest.main([__file__])
