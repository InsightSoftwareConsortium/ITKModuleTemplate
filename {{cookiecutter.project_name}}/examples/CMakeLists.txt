cmake_minimum_required(VERSION 3.10.2)
project({{ cookiecutter.module_name }}Examples)

find_package(ITK REQUIRED
  COMPONENTS
    ITKImageIO
    {{ cookiecutter.module_name }}
  )
include(${ITK_USE_FILE})

add_executable({{ cookiecutter.example_name }} {{ cookiecutter.example_name }}.cxx )
target_link_libraries({{ cookiecutter.example_name }} ${ITK_LIBRARIES})
