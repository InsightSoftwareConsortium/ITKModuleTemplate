cmake_minimum_required(VERSION 3.22.1...3.29.0 FATAL_ERROR)
project({{ cookiecutter.module_name }})

set({{ cookiecutter.module_name }}_LIBRARIES {{ cookiecutter.module_name }})

if(NOT ITK_SOURCE_DIR)
  find_package(ITK REQUIRED)
  list(APPEND CMAKE_MODULE_PATH ${ITK_CMAKE_DIR})
  include(ITKModuleExternal)
else()
  set(ITK_DIR ${CMAKE_BINARY_DIR})
  itk_module_impl()
endif()

itk_module_examples()
