# ft_package

This is a simple Python package named `ft_package` that includes a basic module with a function to count occurrences in a list.

## Installation

### Prerequisites

- Python 3.x installed
- pip package manager installed

### Build and Install

1. Build the package:

    ```bash
    python3 setup.py sdist bdist_wheel
    ```
    
    or

    ```bash
    python setup.py sdist bdist_wheel
    ```

2. Install the package:

    ```bash
    pip install --upgrade ./dist/ft_package-0.0.1.tar.gz
    ```

    or

    ```bash
    pip install --upgrade ./dist/ft_package-0.0.1-py3-none-any.whl
    ```

## Usage

After installation, you can use the `count_in_list` function from the `ft_package.my_module` module in your Python scripts or interactive environments.

Example:

```python
from ft_package.my_module import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## Uninstallation

```bash
pip uninstall ft_package
rm -rf build dist ft_package.egg-info
```
