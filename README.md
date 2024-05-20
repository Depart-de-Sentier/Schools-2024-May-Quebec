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

## Guides and documentation

* [pytest](https://docs.pytest.org/en/8.2.x/how-to/index.html)
* [packaging](https://packaging.python.org/en/latest/guides/)
