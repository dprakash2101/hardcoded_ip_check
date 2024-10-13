# Check for Hardcoded IPs

<img src="images/icon.jpeg" alt="Check for Hardcoded IPs Icon" style="width: 150px; height: auto;"/>

A GitHub Action to find hardcoded IP addresses in files. This action scans specified directories in your repository for hardcoded IP addresses and helps you maintain code quality and security.

## Features

- Checks for hardcoded IP addresses in specified directories.
- Customizable input for directory selection.
- Supports user-defined file extensions for checking.
- Option to combine user-defined extensions with default ones.
- Easy integration into your GitHub workflows.

## What's New

- **File Extension Support**: You can now specify which file types to scan for hardcoded IP addresses.
- **Combine Extensions Option**: A new option allows users to combine their specified extensions with the default extensions for a more comprehensive check.


## Default Languages Supported

This action checks for hardcoded IP addresses in the following file types:

- C# (`.cs`)
- Python (`.py`)
- JavaScript (`.js`)
- JSON (`.json`)
- Java (`.java`)
- TypeScript (`.ts`)

## Inputs

| Input               | Description                                                                                           | Required | Default               |
|---------------------|-------------------------------------------------------------------------------------------------------|----------|-----------------------|
| `directories`       | Comma-separated list of directories to check (e.g., `src,app,config`).                              | Yes       | `.`                   |
| `extensions`        | Comma-separated list of file extensions to check (e.g., `.cs,.py,.js`).                             | No       | (empty, checks defaults) |
| `combine_extensions`| Set to `true` if you want to combine the provided extensions with the default ones.                  | No       | `false`               |


## Usage

### Example Workflow

To use this action in your workflow, create a `.github/workflows/ip-check.yml` file in your repository:

```yaml
name: Check for Hardcoded IPs

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  check-ips:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Run IP Check
        uses: dprakash2101/hardcoded_ip_check@v1.0.0  # Use the latest version
        with:
          directories: 'src, app, config'  # Specify directories to check
          extensions: '.cs,.py'  # Optionally specify extensions to check
          combine_extensions: 'true'  # Set to true to combine with default extensions

```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This project is maintained by [Devi Prakash Kandikonda](https://github.com/dprakash2101).
