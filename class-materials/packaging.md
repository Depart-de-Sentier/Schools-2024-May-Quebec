# Python Library and Packaging Basics


> [!IMPORTANT]
> **Prerequisites**:
> * A local Python installation (see [the docs](https://docs.brightway.dev/en/latest/content/installation/index.html)).
> * A text editor with code support. We recommend you use [VSCode](https://code.visualstudio.com/).
> * [Github account](https://github.com/).
> * [ReadTheDocs account](https://about.readthedocs.com/) - use your Github account for Single Sign-On.
> * [PyPI Test account](https://test.pypi.org/).

Creating a Python package is pretty easy, and we have templates to make common things even easier. However, it is easy to get frustrated, as small changes can break things. Please follow these steps carefully and in order:

[Primary step-by-step guide on BASIC packaging at `packaging.python.org`](https://packaging.python.org/en/latest/tutorials/packaging-projects/) \
[Primary step-by-step guide on ADVANCED packaging at `packaging.python.org`](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/#publishing-package-distribution-releases-using-github-actions-ci-cd-workflows)


## Terminology

### Module

[Module](https://packaging.python.org/en/latest/glossary/#term-Pure-Module)

> A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.
> - [Python Documentation](https://docs.python.org/3/tutorial/modules.html)

### Package

[(Import) Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package)

### `__init__.py`-File

> The `__init__.py` files are required to make Python treat directories containing the file as packages (...) \
> - [Python Documentation](https://docs.python.org/3/tutorial/modules.html#packages)


## Creating a Virtual Environment

> [!WARNING]
> DO NOT mix the use of Conda and `venv`/`pip`! In this course, we will use `venv`/`pip` exclusively.

Follow the [official Python `venv` documentation](https://docs.python.org/3/library/venv.html) to set up a virtual environment.

## Install Build Tools

In order to build a Python package, you need to install a few tools:

```bash
pip install build setuptools twine cruft
```

## Create a Python Package (based on [the Brightway template](https://github.com/brightway-lca/cookiecutter-brightwaylib))

We have created a "template repository" that you can use to instantly create the structure of a Brightway-related Python package: [`cookiecutter-brightwaylib`](https://github.com/brightway-lca/cookiecutter-brightwaylib).

> [!NOTE]
> The tool used to create the template is called [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/). \
> The tool used to create your project based on the template is called [`cruft`](https://cruft.github.io/cruft/)

Navigate to your desired directory and run the following command:

```bash
cruft create https://github.com/brightway-lca/cookiecutter-brightwaylib
```

You will be guided through a series of questions, which will determine the name of your package, the author, the license, etc.

> [!WARNING]
> In this example, the package is called `bw_test`. You will need to use a different name for your package!
> This is because packages on PyPi Test (just like on "regular" PyPi) must have unique names.
> There is already a package called `wurst` in the Brightway ecosystem... so why not `sauerkraut`, or `beer`?

## Make Edits to your Package

You have now created the basic structure of your package.

The most simple edit you can make is to add a "Hello, world!" function to your package. You can therefore add the function

```python
def hello_world():
    print("Bonjour, le monde!") # we are in Quebec, after all
```

to a __module__ called `printing.py`:.

```
.
├── .github/
│   └── ...
├── bw_test/
│   ├── __init__.py
│   └── printing.py
├── docs/
│   ├── content/
│   │   └── ...  
│   ├── conf.py
│   ├── environment.yaml
│   └── index.md
├── tests\/
│   └── ...
├── .gitignore
├── .readthedocs.yaml
├── pyproject.toml
├── MANIFEST.in
├── README.md
└── ...
```

In order to make the function available to the user, you need to add it to the `__all__` import of the `__init__.py` file:

```python
# https://docs.python.org/3/reference/import.html#regular-packages
"""
`bw_test` is a Python package for testing purposes.
"""

# https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
__all__ = (
    "__version__",
    "printing",
)

__version__ = "0.0.1"
```

## Build your Package

In order to "ship" your package to other users via the PyPi repository, you need to "build" it first. This will create a "wheel" file (`.whl`) of your package, that can be uploaded to PyPi. The tool used to build the package is called `setuptools`. It is defined in the `pyproject.toml` file.

```bash
python3 -m build --wheel
```

This will create a `dist` directory with the wheel file in it.

## Set up `twine`

Create [an API token at PyPI Test](https://pypi.org/help/#apitoken). This will allow you to upload your package directly to PyPi Test using `twine`.

Create a file called `~/.pypirc` with the following content:

> [!IMPORTANT]
> PyPi may change the "_" in package names to a minus/dash "-". In this case, the package name is `bw-test`, but the repository name is `bw_test`.

```
[distutils]
  index-servers =
    testpypi
    bw-test

[testpypi]
  username = __token__
  password = # either a user-scoped token or a project-scoped token you want to set as the default
[bw-test]
  repository = https://test.pypi.org/legacy/
  username = __token__
  password = <API_TOKEN>
```

__NOW__ you are set! You can upload the package to PyPi Test using `twine`:

```bash
twine upload -r testpypi --repository bw-test dist/*
```

## Installing your Package from PyPi Test

You can now install your package from PyPi Test [using a special `pip install` command](https://packaging.python.org/en/latest/guides/using-testpypi/#using-testpypi-with-pip):

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ bw_test
```

## Installing your Package Locally

You can also install your package locally (directly from your computer), [using a special `pip install` command](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-e):

```bash
pip install --editable <PATH_TO_PACKAGE_DIRECTORY>
```

The `--editable` flag will install the package in "editable" mode, meaning that you can make changes to the package and they will be immediately available to the user. Amazing! We will try this out together.
