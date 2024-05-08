import os

def identify_languages_and_frameworks(project_directory):
    """
    Identify the primary language(s) and associated frameworks used in the project


    Args: 
    - project_directory: The project directory  of the project to analyze

    Returns:
    - A list of identified languages and frameworks

    """


    # Set of identified languages and frameworks
    identified_languages = set()
    identified_frameworks = set()


    # Map of file extensions to languages and frameworks
    language_map = {
        '.py': 'Python',
        '.java': 'Java',
        '.c': 'C',
        '.cpp': 'C++',
        '.js': 'JavaScript',
        '.html': 'HTML',
        '.css': 'CSS',
        '.sql': 'SQL',
        '.go': 'Go',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
        '.xml': 'XML',
        '.yaml': 'YAML',
        '.yml': 'YAML',
        '.json': 'JSON',
        '.txt': 'Text',
    }
    framework_map = {
        "React": "Javascript",
        "Next.js": "JavaScript",
        "Vue.js": "JavaScript",
        "Angular": "JavaScript",
        "Nuxt.js": "JavaScript",
        "Express": "JavaScript",
        "Django": "Python",
        "Flask": "Python",
        "Express": "JavaScript",
        "Rails": "Ruby",
        "Laravel": "PHP",
        "Spring":"Java",
        "Hibernate":"Java",
        "Flutter": "Java",
        "Kotlin": "Java",

        
    }

    # Check the language_map dictionary
    # print("Language map:", language_map)


   
    # iterate through files in the given project directory
    for root, _, files in os.walk (project_directory):
        for filename in files:
            # get the file extension
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower() # Convert to lowercase for case-insensitive matching

            print(f"File: {filename}, Extension: {file_extension}")

            # check if the file extension is in the language_map
            if file_extension in language_map:
                # Get the language/framework associated with the file extension
                language = language_map[file_extension]
                # print("Language before:", language) 
                identified_languages.add(language)

    # Check for frameworks used in the language_map
    for framework, language in framework_map.items():
        if language in identified_languages:
            identified_frameworks.add(framework)

        # print(f"Identified Languages: {identified_languages}")
        # print(f"Identified Frameworks: {identified_frameworks}")


    return list(identified_languages), list(identified_frameworks)
        

def is_language(language):
    """
    Check if the provided string represents a programming language


    Args:
    - language: The string to check

    Returns:
    - True if the string represents a programming language, False otherwise

    """

    # List of programming languages
    programming_languages = [
        "Python",
        "Java",
        "c",
        "c++",
        "Javascript",
        "html",
        "css",
        "sql",
        "go",
        "ruby",
        "php",
        "swift",
        "kotlin",
        "xml",
        "yaml",
        "yml",
        "json",
        "text"
    ]

    # Check if the string is a programming language
    return language in programming_languages

