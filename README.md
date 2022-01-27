ITKModuleTemplate
=================

[![][gha-img]][gha-link]

[gha-img]: https://github.com/InsightSoftwareConsortium/ITKModuleTemplate/actions/workflows/build-test-package.yml/badge.svg
[gha-link]: https://github.com/InsightSoftwareConsortium/ITKModuleTemplate/actions/workflows/build-test-package.yml


Overview
--------

This is a module for the [Insight Toolkit (ITK)](http://itk.org) for
segmentation and registration. It is designed to work with the ITK
modular system.

This module is a template to be used as a starting point for a new ITK
module.

Getting Started
---------------

The following will get an external module started in a new repository:

    python -m pip install cookiecutter
    python -m cookiecutter gh:InsightSoftwareConsortium/ITKModuleTemplate
    # Fill in the information requested at the prompts

Reasonable defaults will be provided for all of the parameters. The
parameters are:

<dl>
<dt>full_name</dt>
<dd>Your full name.</dd>

<dt>email</dt>
<dd>Your email.</dd>

<dt>project_name</dt>
<dd>This is a name for the project, which is <i>ITK</i> followed by the module
name, by convention. Examples include <i>ITKIsotropicWavelets</i> or
<i>ITKBoneMorphometry</i>.<dd>

<dt>module_name</dt>
<dd>This is the name of the module. Since this is an external module, it
does not start with the <i>ITK</i> prefix. It is in CamelCase, by convention.
Examples include <i>IsotropicWavelets</i> and <i>BoneMorphometry</i>.<dd>

<dt>filter_name</dt>
<dd>The skeleton of an <code>itk::ImageToImageFilter</code> will be created by default.
Optionally specify this value, if you will be adding an
<code>itk::ImageToImageFilter</code> to your module.</dt>

<dt>python_package_name</dt>
<dd>This is the name of the Python package that will be created from the
module. By convention, this is <i>itk-<project_name in lower case></i>
For example, <i>itk-isotropicwavelets</i> or <i>itk-bonemorphometry</i>.</dd>

<dt>download_url</dt>
<dd>This is the download url added to the Python package metadata. This can
be the GitHub repository URL.</dd>

<dt>project_short_description</dt>
<dd>A short description to use in the project README, module Doxygen
documentation, and Python package documentation.</dd>

<dt>project_long_description</dt>
<dd>A long description to use in the project README, module Doxygen
documentation, and Python package documentation.</dd>
</dl>

The output of the cookiecutter is a buildable ITK external module with
example classes. Remove or replace the classes with your new classes.
Push your new module to GitHub, and enable builds on
[CircleCI](https://circleci.com/), [TravisCI](https://travis-ci.org/),
and [AppVeyor](https://www.appveyor.com/).

Documentation on [how to populate the
module](https://itk.org/ITKSoftwareGuide/html/Book1/ITKSoftwareGuide-Book1ch9.html#x50-1430009)
can be found in the [ITK Software
Guide](https://itk.org/ITKSoftwareGuide/html/).

To improve the discoverability of your module on GitHub, first push the
associated repository, then add
[itk-module](https://github.com/topics/itk-module) to the project's
[GitHub Topics](https://help.github.com/articles/about-topics/) .

Remote Module
-------------

After an [Insight Journal](http://www.insight-journal.org/) article has
been submitted, the module can be included in ITK as a [remote
module](https://itk.org/ITKSoftwareGuide/html/Book1/ITKSoftwareGuide-Book1ch9.html#x55-1640009.7).
Add a file in "ITK/Modules/Remote" called "YourModule.remote.cmake", for
this module it would be "ExternalExample.remote.cmake" with the
followlowing contents:

    itk_fetch_module(MyModule
      "A description of the a module."
      GIT_REPOSITORY http://github.com/myuser/ITKMyModule.git
      GIT_TAG abcdef012345
      )

CI Testing and Python Packages
------------------------------

Continuous integration service configurations are included to build
and test the C++ core of packages across platforms and build binary
Python packages for Linux, macOS, and Windows. These packages can be
[downloaded](https://itkpythonpackage.readthedocs.io/en/master/Build_ITK_Module_Python_packages.html#github-automated-ci-package-builds)
and [uploaded to the Python Package Index
(PyPI)](https://itkpythonpackage.readthedocs.io/en/master/Build_ITK_Module_Python_packages.html#upload-the-packages-to-pypi).

ITKv4 Branch
------------

In the transition to the major release of ITKv5 your module might want
to be compatible with both versions: ITKv4 and ITKv5. In order to do
that, keep the master branch for development with ITKv5, and create
another branch, named `ITKv4`, or `release`, that is compatible with the
version 4.13 of ITK. For examples and updated information on how to do
this: please [check the discourse
conversation](https://discourse.itk.org/t/itk-external-module-github-builds-for-4-x-and-5-x/900).

License
-------

This software is distributed under the Apache 2.0 license. Please see
the *LICENSE* file for details.

Authors
-------

-   Bradley Lowekamp
-   Matt McCormick
-   Jean-Baptiste VIMORT
