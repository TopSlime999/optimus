#!/usr/bin/env python


import sys
import time as t
import os


def handle_errors(file, message):
  sys.stdout.write(f" {file} {message}\n")


def initilize():
  try:
    test, var = sys.argv[1], sys.argv[2]
  except IndexError:
    sys.stdout.write(" Proper usage python [filename].py ['searched_term'] [mode (-D, -R, -F)] (if -F file to search.)\nex: python main.py 'Hello world' -R")
    sys.exit()

  if sys.argv[2].lower() not in ("-d", "-r", "-f"):
    sys.stdout.write(
        " Invalid usage. Valid modes are -D (search current directory), -R (search current and subdirectories), -F (search specific file).\n"
    )
    sys.exit()

  while sys.argv[2].lower() == "-f":
    try:
      test_var = sys.argv[3]
    except IndexError:
      sys.stdout.write(
          " Proper usage python [filename].py ['searched_term'] [mode (-D, -R, -F)] (if -F file to search.)"
      )
      sys.exit()
    break


def get_files(mode):
  cwd = os.getcwd()
  files = []
  if mode in ("-d", "-r"):
    for file in os.listdir(cwd):
      if os.path.isfile(file) and os.access(f"{cwd}/{file}", os.R_OK):
        files.append(f"{cwd}/{file}")

  if mode == "-r":
    num_subdirs = 0
    estimated_time = 0.0
    for dir in os.listdir(cwd):
      if os.path.isdir(dir):
        num_subdirs += 1
        # Assuming average file open/read time of 0.01 seconds
        estimated_time += 0.01 * len(os.listdir(f"{cwd}/{dir}"))

    sys.stdout.write(
        f"{num_subdirs} subdirectories will be searched. Estimated additional time: {estimated_time:.2f} seconds\n"
    )

    for dir in os.listdir(cwd):
      if os.path.isdir(dir):
        for sub_file in os.listdir(f"{cwd}/{dir}"):
          if os.path.isfile(f"{cwd}/{dir}/{sub_file}") and os.access(
              f"{cwd}/{dir}/{sub_file}", os.R_OK):
            files.append(f"{cwd}/{dir}/{sub_file}")
  return files


def search(files):
  to_be_searched = len(files)
  instances = []
  for file in files:
    start_time = t.time()
    if not os.path.isfile(file) or not os.access(file, os.R_OK):
      handle_errors(file,
                    "File found, but permission denied. OR non file found.")
      continue

    try:
      with open(file, "r", encoding="UTF-8") as searched_file:
        file_lines = searched_file.readlines()
        sys.stdout.write(
            f" searching {file} [{files.index(file) + 1}/{to_be_searched}]\n")
        for line in file_lines:
          if sys.argv[1] in line:
            instances.append(
                f"line {file_lines.index(line) + 1} contained '{sys.argv[1]}' in {file}\n"
            )
    except UnicodeDecodeError:
      handle_errors(file, "contains unreadable characters.")
    except:
      handle_errors(file, "is possibly empty")

    end_time = t.time()
    sys.stdout.write(
        f" SEARCH OF {file} COMPLETED TOOK {str(end_time - start_time)[0]} seconds\n"
    )

  return instances


def display_or_write(instances):
  num_instances = len(instances)
  if num_instances == 0:
    sys.stdout.write("No instances found.\n")
  elif num_instances <= 15:
    for instance in instances:
      sys.stdout.write(instance)
  else:

    write_to_file = input(
        f"{num_instances} instances found. Write to a file (y/n) or display all instances to terminal? (t): "
    ).lower()
    if write_to_file == "y":
      filename = input("Enter filename (including .txt): ")
      try:
        with open(filename, "w") as output_file:
          output_file.writelines(instances)
        sys.stdout.write(f"Instances written to {filename}.\n")
      except OSError as e:
        sys.stdout.write(f"Error writing to file: {e}\n")
    elif write_to_file == "t":
      for instance in instances:
        sys.stdout.write(instance)
    else:
      sys.stdout.write("Invalid choice. No instances displayed.\n")


def main():
  mode = sys.argv[2].lower()
  files = get_files(mode)
  sys.stdout.write(f"{len(files)} File[s] to be searched\n")
  instances = search(files)
  print(f"\n{t.time() - start_of_code}")
  display_or_write(instances)


if __name__ == "__main__":
  start_of_code = t.time()
  initilize()
  main()
