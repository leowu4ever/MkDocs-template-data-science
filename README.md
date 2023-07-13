# MkDocs template for data science projects

[Link to the template](https://leowu4ever.github.io/mkdocs-template/)

## Overview
This repository is created to demonstrate how I put together documentation for data science projects by utilising MkDocs with several essential extensions. Comprehensive documentation should cover the information for different aspects. The proposed template has three pages including the home page, API page and demo page.

The home page serves as a starting point for the project by covering some of the key information, such as the introduction, system diagram and usage guide. It aims to help the audience quickly grasp the overview of the system. The next page is the API page which presents docstrings. It is ideal for those who want to figure out how to exactly use or configure APIs. The last page is the demo page which displays Jupyter notebook demos and it is very beneficial and would be greatly appreciated. To seamlessly integrate these three pages in MkDocs, requires some very specific packages so that all pages can be rendered and presented nicely. In the following section, I will explain what dependencies are needed and how to configure them properly.

## Components
Three packages are needed including [mkdocstrings](https://pypi.org/project/mkdocstrings-python/), [mkdocs-jupyter](https://pypi.org/project/mkdocs-jupyter/0.16.1/) and [mkdocs-mermaid](https://pypi.org/project/mkdocs-mermaid2-plugin/). It is quite obvious to tell what job each package does from their names. 

- Mkdocstrings picks up all the docstrings written and format them professionally. It provides great flexibility in controlling how the docstrings are displayed.
- Mkdocs-jupyter helps to render Jupyter notebook but it would have difficulties with certain types of outputs, such as interactive plots created by Plotly. 
- Mkdocs-mermaid enables mermaid diagrams rendering. Mermaid diagram is a markdown-based diagram generation tool that allows you to generate various kinds of diagrams using markdown language. The illustration below is created using Mermaid.

```mermaid
%%{init: {'theme':'default'}}%%
flowchart BT

home[home page]
api[API page]
demo[demo page]
mermaid[(mermaid diagram)]
docstring[(Docstrings)]
jupyter[(jupyter notebooks)]
template([mkdocs template for ds project])
theme[theme]

home -->template
api-->template
demo-->template
mermaid --mkdocs-mermaid--> home
docstring --mkdocstrings--> api
jupyter --mkdocs-jupyter--> demo
theme --mkdocs-material-->template
```

## Usage
### Setup
You need to make sure Python 3.10.8 is installed.
- Install all dependencies.
  - pip install -r requirements.txt.
- Navigate to a desired directory and initialise MkDocs project named 'xxx'.
  - mkdocs new 'xxx'
  - cd 'xxx'
  - You should be able to see a folder named 'docs' and mkdocs.yml file.

Now the barebone of the template is already in place. The below shows how to create and configure the home page, API page and demo page.

- Home page
  - Create a markdown file in the '/docs' folder and reference it in the nav section in the mkdocs.yml file. See line 35 in the mkdocs.yml file.
  - Write on the markdown file like how you usually would do it in a readme file.
- API page
  - Make sure python scripts are documented with docstrings.
  - Create a markdown file in docs and reference it in the nav section in the mkdocs.yml file. See lines 36-39 in the mkdocs.yml file.- Demo page
  - Each markdown file can associate with at least one module. To include a module, it follows a convention that is very similar to relative importing. For example, the first line in 'car.md' (:::src.car) means including go up two levels and include all docstrings in the car.py module.
- Demo page
  - Create a folder named notebooks inside the docs folder. Place the demo notebook in the notebooks folder. Referernce it in the nav section in the mkdocs.yml file. See lines 40-41.

### Deploy the doc
To deploy the documentation in github, you can follow the instructions below.

https://squidfunk.github.io/mkdocs-material/publishing-your-site/
