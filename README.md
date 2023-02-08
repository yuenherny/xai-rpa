# Robotic Process Automation for Xircuits
This component library is for developers to use Xircuits with Python's open source RPA packages.

**Note: This is a work in progress at the moment. Some RPA functionalities might not be supported.**

## Supported RPA packages:
- [Tebelorg RPA-Python](https://github.com/tebelorg/RPA-Python)

## Prerequisites
Before you start, please refer to this [guide](https://xircuits.io/docs/Installation) to set up Xircuits.

## Installation
To use this component library, simply copy the directory / clone or submodule this repository to your working Xircuits project directory.

1. In `xai_components/xai_rpa` directory, clone:
    ```
    $ cd xai_components/xai_rpa
    $ git clone https://github.com/yuenherny/xai-rpa
    ```
    or at project root with Python environment activated, run:
    ```
    $ pip install xircuits
    $ xircuits-components --sublib rpa
    ```
2. At project root, install the required dependencies for RPA to work:
    ```
    $ cd ../..
    $ pip install -r xai_components/xai_rpa/requirements.txt
    ```
