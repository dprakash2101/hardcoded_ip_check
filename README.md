# Check for Hardcoded IPs

A GitHub Action to find hardcoded IP addresses in files. This action scans specified directories in your repository for hardcoded IP addresses and helps you maintain code quality and security.

## Features

- Checks for hardcoded IP addresses in specified directories.
- Customizable input for directory selection.
- Easy integration into your GitHub workflows.

## Languages Supported

This action checks for hardcoded IP addresses in the following file types:

- C# (`.cs`)
- Python (`.py`)
- JavaScript (`.js`)
- JSON (`.json`)
- Java (`.java`)
- TypeScript (`.ts`)

## Inputs

| Input         | Description                                                  | Required | Default |
|---------------|--------------------------------------------------------------|----------|---------|
| `directories` | Comma-separated list of directories to check (e.g., `src,app,config`). | No       | `.`     |

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
```
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This project is maintained by [dprakash2101](https://github.com/dprakash2101).
