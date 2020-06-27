# Generate Markdown Template

This raw script generates the markdown template required for each community on the list, this is to simplify [contributions](../CONTRIBUTING.md#new-community), not an all-powerful generator.

## Requirements

- `python >= 3.6`
- `requests`

## Usage

Run with `python3 /path/to/get_template.py`. You'll be asked to enter the details about the community. At every input to move to the next query simply hit `Enter`. In the end you'll be given a generated template which you only need to copy and propose file change from a pull request.

![Screenshot of template script](../images/screenshots/screenshot_01.png)

**Note:** This script is relatively bare-bone, there is no strong validation check, it only spews out whatever you type in.
