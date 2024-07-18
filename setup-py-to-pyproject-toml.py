#!/usr/bin/env python3

# This script will convert setup.py to pyproject.toml
# for ITK remote modules. It will also update the
# itk version to 5.4.* in the dependencies section.

import os
import re
import sys
import argparse

def setup_py_to_pyproject_toml(setup_python_path):
    if not os.path.exists(setup_python_path):
        print('setup.py file not found')
        sys.exit(1)

    with open(setup_python_path, 'r') as f:
        setup_py = f.read()

    project_name = re.search(r'name\s*=\s*[\'"]([^\'"]*)[\'"]', setup_py).group(1)
    project_version = re.search(r'version\s*=\s*[\'"]([^\'"]*)[\'"]', setup_py).group(1)
    project_description = re.search(r'description\s*=\s*[\'"]([^\'"]*)[\'"]', setup_py).group(1)
    project_author = re.search(r'author\s*=\s*[\'"]([^\'"]*)[\'"]', setup_py).group(1)
    project_author_email = re.search(r'author_email\s*=\s*[\'"]([^\'"]*)[\'"]', setup_py).group(1)
    project_url = re.search(r'url\s*=\s*r?[\'"]([^\'"]*)[\'"]', setup_py).group(1)
    project_classifiers = re.findall(r'classifiers\s*=\s*\[([^\]]*)\]', setup_py, re.DOTALL)
    project_classifiers = project_classifiers[0].replace('\n', '').replace(' ', '').replace('"', '').split(',')
    project_packages = re.findall(r'packages\s*=\s*\[([^\]]*)\]', setup_py, re.DOTALL)
    project_packages = project_packages[0].replace('\n', '').replace(' ', '').replace('"', '').split(',')
    project_install = re.findall(r'install_requires\s*=\s*\[([^\]]*)\]', setup_py, re.DOTALL)

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

    deps = [eval(str(d).strip()) for d in project_install]
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