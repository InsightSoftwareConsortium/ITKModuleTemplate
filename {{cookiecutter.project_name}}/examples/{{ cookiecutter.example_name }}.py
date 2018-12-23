#!/usr/bin/env python

# Copyright Insight Software Consortium
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Run with:
# ./{{ cookiecutter.example_name }}.py <InputImageFile> <OutputImageFile>
# <Parameters>
# e.g.
# ./{{ cookiecutter.example_name }}.py MyImage.mha Output.mha 2 0.2
# (A rule of thumb is to set the Threshold to be about 1 / 100 of the Level.)
#
#  parameter_1: absolute minimum...
#        The assumption is that...
#  parameter_2: controls the..
#        A tradeoff between...

import sys
import itk

import numpy as np


if len(sys.argv) != 4:
    print('Usage: ' + sys.argv[0] +
          ' <InputFileName> <OutputFileName> <Parameters>')
    sys.exit(1)

# Please, write a complete, self-containted and useful example that
# demonstrate a class when being used along with other ITK classes or in
# the context of a wider or specific application.
