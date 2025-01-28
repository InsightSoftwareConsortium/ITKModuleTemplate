#!/usr/bin/env python3

# This script will convert setup.py to pyproject.toml
# for ITK remote modules. It will also update the
# itk version to 5.4.* in the dependencies section.

import os
import re
import sys
import argparse
import runpy
from packaging.version import Version


def make_shim():
    mydict = {}

    def setup_shim(**kwargs):
        mydict.update(kwargs)

    return mydict, setup_shim

def setup_py_to_pyproject_toml(setup_python_path):
    if not os.path.exists(setup_python_path):
        print('setup.py file not found')
        sys.exit(1)

    import setuptools
    import skbuild
    capture, shim = make_shim()
    setuptools.setup = shim
    skbuild.setup = shim

    runpy.run_path(setup_python_path)

    # with open(setup_python_path, 'r') as f:
    #     setup_py = f.read()

    project_name = capture['name']
    current_version = Version(capture['version'])
    project_version = f'{current_version.major}.{current_version.minor + 1}.0'
    project_description = capture['description']
    project_author = capture['author']
    project_author_email = capture['author_email']
    project_url = capture['url']
    project_classifiers = capture['classifiers']
    project_packages = capture['packages']
    project_install = capture['install_requires']

    # Load the file "./{{cookiecutter.project_name}}/pyproject.toml" as the pyproject.toml template
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_file = os.path.join(script_dir, '{{cookiecutter.project_name}}', 'pyproject.toml')
    with open(template_file, 'r') as f:
        template = f.read()

    # Replace placeholders in the template with the extracted data
    template = template.replace('{{ cookiecutter.python_package_name }}', project_name)
    template = template.replace('version = "0.1.0"', f'version = "{project_version}"')
    template = template.replace('{{ cookiecutter.project_short_description }}', project_description)
    template = template.replace('{{ cookiecutter.full_name }}', project_author)
    template = template.replace('{{ cookiecutter.email }}', project_author_email)
    template = template.replace('{{ cookiecutter.download_url }}', project_url)

    setup_dirname = os.path.dirname(setup_python_path)
    if os.path.exists(os.path.join(setup_dirname, 'README.md')):
        template = template.replace('README.rst', 'README.md')

    deps = [str(d).strip() for d in project_install]
    new_deps = []
    for dep in deps:
        if '==' in dep or '>=' in dep:
            if '>=' in dep:
                split_dep = dep.split('>=')
            else:
                split_dep = dep.split('==')
            if 'itk' in split_dep[0] and split_dep[1][0] == '5':
                new_deps.append(f'{split_dep[0]} == 5.4.*')
            else:
                new_deps.append(dep)
        else:
            new_deps.append(dep)
    new_deps_str = ''
    for dep in new_deps:
        new_deps_str += f'    "{dep}",\n'
    template = template.replace('    "itk == 5.4.*",\n', new_deps_str)

    # Write the converted data to the new pyproject.toml file
    with open('pyproject.toml', 'w') as f:
        f.write(template)


def main():
    parser = argparse.ArgumentParser(description='Convert setup.py to pyproject.toml')
    parser.add_argument('setup_python_path', help='Path to the setup.py file')
    args = parser.parse_args()

    setup_py_to_pyproject_toml(args.setup_python_path)

    # Remove setup.py file
    os.remove(args.setup_python_path)

if __name__ == '__main__':
    main()
