# Commands for local development

## Prerequisites

- [Python](https://www.python.org/) 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Virtual Environment Commands

### Initialize the virtual environment

On Windows:

```cmd
.\scripts\init-venv.bat
```

On macOS/Linux:

```bash
./scripts/init-venv.sh
```

Then, you can configure the virtual environment in Cursor (VS Code) to run the code directly in the IDE.

### Enter the virtual environment

On Windows:

```cmd
.\scripts\enter-venv.bat
```

On macOS/Linux:

```bash
./scripts/enter-venv.sh
```

### Add the package (after entering the virtual environment)

```bash
uv add <package_name>
```

### Remove the package (after entering the virtual environment)

```bash
uv remove <package_name>
```

If you need other commands, please refer to the [uv documentation](https://docs.astral.sh/uv/getting-started/features/).

<br />
<br />

## Run the server

Ensure that you are in the `app` directory, and entered the virtual environment.

### Run the MCP server (with inspector)

```bash
mcp dev run_mcp.py
```

### Run the MCP server (without inspector)

```bash
uv run run_mcp.py
```

### Run the overall server (FastAPI + MCP server)

```bash
uv run run_server.py
```

<br />
<br />

## pytest Commands

### Run all tests without entering the virtual environment

On Windows:

```cmd
.\scripts\pytest.bat
```

On macOS/Linux:

```bash
./scripts/pytest.sh
```

### Run the test (after entering the virtual environment)

Assume that you are in the `app` directory.

To run all tests:

```bash
pytest
```

To run a specific test, for example:

```bash
pytest tests/foo.py::test_bar -v
```

If you need to view more detailed logs, you can use the command with `-s` and `-vv`:

```bash
pytest -s tests/foo.py::test_bar -vv
```
