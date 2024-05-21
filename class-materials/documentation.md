### Documenting Python Code (=your Package)

Did you ever wonder how [the Brightway documentation](https://docs.brightway.dev/en/latest/) (or Pandas/NumPy/SciPy... documentation) is built?

The answer is: the [Sphinx documentation generator](https://www.sphinx-doc.org/en/master/)! \
This tool _automatically_ builds fancy documntation websites... as long as you properly document your Python source-code.

To do that, you must:

1. Choose a [Python docstring](https://peps.python.org/pep-0257/#what-is-a-docstring) style (@michaelweinold recommends [the NumPy Style](https://numpydoc.readthedocs.io/en/latest/format.html))
2. Document your functions, classes and methods!

You can also add more extensive descriptions (text with images, tables, etc.) to the documentation. \
All you have to do is write your content in [MyST Markdown files](https://myst-parser.readthedocs.io/en/latest/index.html).

To get an idea of how you must structure your documentation, you can have a look at [the Brightway documentation repository.](https://github.com/brightway-lca/brightway-documentation/tree/main/source)