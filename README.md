## README for "Spread The Code" Project
## Totally inspired by:
SpreadingTheWord using Python
This activity is part of Code the City's Aberdeen Python User Group (APUG), 14th February, 2024.

See the original code here:
https://github.com/carlosfmorenog/SpreadingTheWord


This is just a variant of most of the code. 
### Introduction
The "Spread The Code" project is a Python script designed to spread a code or message throughout Python files in a given directory and its subdirectories. The project includes a `malware.py` file that contains the spreading functionality.

### Usage
Follow the steps below to use the "Spread The Code" project:

1. **Clone the Repository:**
   ```
   git clone https://github.com/carlosfmorenog/SpreadingTheCode
   ```

2. **Navigate to the Project Directory:**
   ```
   cd SpreadingTheCode
   ```

3. **Execute the Spreading Script:**
   Open a Python environment and run the following code in the script:
   ```python
   !git clone https://github.com/carlosfmorenog/SpreadingTheCode
   import os
   filelist = os.listdir(os.path.abspath("SpreadingTheCode"))
   
   # Iterate filelist and find the .py files, then append them to a "filestoinfect" list.
   filestoinfect = []
   for name in filelist:
       if name[-3:] == ".py":
           filestoinfect.append(os.path.abspath("")+"/"+name)
   
   # Print the list of files to infect.
   print("List of files to infect:\n")
   print(filestoinfect)
   
   # Iterate filelist and print the subdirectories.
   print("\nSubdirectories:\n")
   for name in filelist:
       if os.path.isdir("SpreadingTheCode/"+name):
           print("SpreadingTheCode/"+name)
   
   # Implement the search function and print the list of files to spread the message into.
   def search(path):
       filestospreadmessage = []
       filelist = os.listdir(path)
       for name in filelist:
           if os.path.isdir("SpreadingTheCode/"+name):
               filestospreadmessage.extend(search(path+"/"+name))
           elif name[-3:] == ".py":
               filestospreadmessage.append(path+"/"+name)
       return filestospreadmessage
   
   filestospreadmessage = search(os.path.abspath("SpreadingTheCode"))
   print("\nList of files to spread the message into:\n")
   print(filestospreadmessage)
   ```

4. **Custom Variant - "Spread The Code":**
   - A variant of "Spread The Code" has been created, named `malware.py`.
   - It includes the `search()` and `spread()` functions.
   - The `spread()` function reads the content of `malware.py` and inserts it into other Python files, excluding itself.
   - Execute the script by running the provided code in the "My Variant of 'Spread The Code'" section.

### Important Note
Exercise caution when using this project, especially the spreading functionality, and ensure it is used responsibly and ethically. Avoid spreading messages or code that could cause harm or violate ethical standards.

### Disclaimer
This project is intended for educational purposes only. The authors are not responsible for any misuse or consequences arising from the use of this project.