# Optimus  

Don't ask why we named it that... 

**Features:**

* **Multiple Search Modes:**
    * `-D`: Search the current directory only.
    * `-R`: Search the current directory and all subdirectories recursively.
* **Error Handling:**
    * Provides clear messages for missing arguments, invalid modes, inaccessible files, and non-textual content.
* **Search Progress:**
    * Displays the number of files to be searched.
    * Estimates search time for recursive searches.
    * Shows individual file search completion time.
* **Output Options:**
    * Displays up to 15 found instances in the terminal by default.
    * Prompts for writing all instances to a user-specified file for larger results.

**Installation**

1. Save the script as a Python file (e.g., `pysearch.py`).
2. Make the script executable using `chmod +x pysearch.py`. (Optional but recommended for convenience)

**Example**

```bash
./pysearch.py hello_world -R
```

* **Notes**
    * Will soon add option to read specific file, and view lines in terminal.
    * improvements to code logic and speed.
