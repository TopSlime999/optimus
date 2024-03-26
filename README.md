# optimus
dont ask why I named it that...

Features:

    Multiple Search Modes:
        -D: Search the current directory only.
        -R: Search the current directory and all subdirectories recursively.
    Error Handling:
        Provides clear messages for missing arguments, invalid modes, inaccessible files, and non-textual content.
    Search Progress:
        Displays the number of files to be searched.
        Estimates search time for recursive searches.
        Shows individual file search completion time.
    Output Options:
        Displays up to 15 found instances in the terminal by default.
        Prompts for writing all instances to a user-specified file for larger results.

Installation

    Save the script as a Python file (e.g., pysearch.py).
    Make the script executable using chmod +x pysearch.py. (Optional but recommended for convenience)

Example:

*./file_search.py hello_world -R*

This command searches for the term "hello_world" in the current directory and all subdirectories recursively.

Additional Notes:

    The script assumes UTF-8 encoding for files.
    For very large numbers of found instances (> 15), the script offers the option to write them to a file instead of displaying them all in the terminal.
    will soon add ability for individual files to be searched, and direct viewing of the lines. 

