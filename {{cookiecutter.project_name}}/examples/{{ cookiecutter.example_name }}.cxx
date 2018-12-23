/*=========================================================================
 *
 *  Copyright Insight Software Consortium
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0.txt
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *=========================================================================*/

#include "itk{{cookiecutter.filter_name}}.h"

#include "itkCommand.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"


int main( int argc, char * argv[] )
{
  if( argc < 4 )
    {
    std::cerr << "Missing parameters." << std::endl;
    std::cerr << "Usage: " << argv[0]
      << " inputImage"
      << " outputImage"
      << " parameters" << std::endl;
    return EXIT_FAILURE;
    }


  // Please, write a complete, self-containted and useful example that
  // demonstrate a class when being used along with other ITK classes or in
  // the context of a wider or specific application.


  return EXIT_SUCCESS;
}
