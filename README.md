# Robotic Process Automation for Xircuits
This component library is for developers to use Xircuits with Python's open source RPA packages.

**Note: This is a work in progress at the moment. Some RPA functionalities might not be supported.**

## Supported RPA packages:
- [Tebelorg RPA-Python](https://github.com/tebelorg/RPA-Python)>=1.48.0

## Prerequisites
Before you start, please refer to this [guide](https://xircuits.io/docs/Installation) to set up Xircuits.

## Installation
To use this component library, simply copy the directory / clone or submodule this repository to your working Xircuits project directory.

1. At your project root:
    ```
    $ git clone https://github.com/yuenherny/xai-rpa.git
    ```
2. Install the required dependencies for RPA to work:
    ```
    pip install -r <PATH/TO/XAI-RPA>/requirements.txt
    ```

## Examples
This section provides brief explanation and things to take note of in selected examples.

### RpaClickAndHover
This example demonstrates left click and hover capability of the RPA bot.

1. The element identifiers used in this example are:
    - HTML `title`: Text button
    - HTML `href`: Image button
2. The **hover** action is on the GitHub icon at the bottom of the webpage.
