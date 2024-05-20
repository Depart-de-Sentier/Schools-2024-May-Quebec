# Spring-School-2024

Material and organization for the DdS 2024 Spring School

* [Course Logistics and Schedule](https://docs.google.com/presentation/d/1z3JZPQE9w0Nf2U1CT-5EqsDmDKvJgrcEDx-6g2oJPaQ/edit?usp=sharing)

## Getting help

> [!IMPORTANT]
> 🙋‍♀️⁉️🙋‍♂️ NO STUPID QUESTIONS \
> [Ask ANY Brightway/Premise/Wurst or Python question ANONYMOUSLY here!](https://forms.gle/rspm8uFJs8sJ5bZ37) \
> Answers will be posted to the Chat Room!

* [Chat Room (Matrix)](https://matrix.to/#/#dds-spring-school-quebec-2024:matrix.org)

## Infrastructure

* [Jupyter Hub server](https://hub.brightway.dev)

Restoring clean Brightway projects:

Wurst and Premise class:

```python
bw2io.restore_project_directory('/etc/data/ecoinvent-3.9.1-cutoff-bw2.tar.gz', overwrite_existing=True)
bw2data.projects.set_current('Quebec')
```

Brightway class:

```python
import bw2io as bi
import b2data as bd

PROJECT_NAME = "ecoinvent-3.10-cutoff BW25"  # You can change this
bi.restore_project_directory(
    fp='/etc/data/ecoinvent-3.10-cutoff-bw25.tar.gz', 
    project_name=PROJECT_NAME,  
    overwrite_existing=True
)
bd.projects.set_current(PROJECT_NAME)
```

## Guides and Documentation

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

### Testing your Package

* [pytest](https://docs.pytest.org/en/8.2.x/how-to/index.html)

### Packaging (=Releasing) your Package

* [packaging](https://packaging.python.org/en/latest/guides/)
