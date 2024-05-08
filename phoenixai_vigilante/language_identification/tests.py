import shutil
import unittest
import os

from .parsers import identify_languages_and_frameworks

class TestIdentifyLanguagesAndFrameworks(unittest.TestCase):

    def test_identify_languages_and_frameworks(self):
        # Create a temporary directory structure with project sample files

        # For demonstration purposes, we'll simulate a Python project
        project_directory = '/tmp/sample_project'
        if not os.path.exists(project_directory):
            os.makedirs(project_directory)

        
        open(os.path.join(project_directory, 'app.py'), 'a').close() # python file
        open(os.path.join(project_directory, 'index.html'), 'a').close() # html file
        open(os.path.join(project_directory, 'script.js'), 'a').close() # javascript file


        # Identify languages and frameworks in the sample project directory
        languages, frameworks = identify_languages_and_frameworks(project_directory)

        # Print relevant information
        print("Identified Languages:", languages)
        print("Identified Frameworks:", frameworks)
        print("Project Directory:", project_directory)
        print("Files in Project Directory:", os.path.join(project_directory))

        # check if Python and HTML are identified 
        self.assertIn('Python', languages)
        self.assertIn('HTML', languages)
        self.assertIn('JavaScript', languages)
        self.assertIn('Django', frameworks)

        #  Clean up the temporary directory
        shutil.rmtree(project_directory)


if __name__ == '__main__':
    unittest.main()


