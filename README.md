# mrjet

`mrjet` is a simple command-line tool for downloading funny movies.

## Installation

Install `mrjet` via PyPI:

```bash
pip install mrjet
```

Ensure you are using Python 3.6 or higher.

## Usage

Currently, `mrjet` supports a basic function: fetching content from a specified URL and saving it to an output directory.

### Basic Usage

```bash
mrjet --url <URL> --output_dir <directory>
```

- `--url`: The URL to process (required).
- `--output_dir`: The output directory (required).

#### Example

```bash
mrjet --url https://missav.ws/fc2-ppv-4635958 --output_dir movies/
```

This will process the content and save it to the `movies/` directory.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.