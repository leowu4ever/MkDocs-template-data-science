---
hide:
  - navigation
---

# mkdocs-template
This repo is created to demonstrate how I put together a documentation in MkDocs with several essential components.

## Steps to set up MkDocs
pip install -r requirements.txt

## Documentation structure
```mermaid
%%{init: {'theme':'default'}}%%
flowchart
subgraph readme
mermaid[mermaid diagram]
end
docstring[Docstrings]
demo[Demo notebooks]
doc[MkDocs documentation]

readme --mkdocs-include & mkdocs-mermaid--> doc
docstring --mkdocstrings--> doc
demo --mkdocs-jupyter--> doc
```
