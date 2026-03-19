#!/usr/bin/python3

# INET4031
# Joel Abbe
# 03/19/2026


import os  #Allows us to run linux commands within the script
import re  #Allows us to work with regular expressions
import sys #Allows access to system-specific parameters and functions


def main():
    for line in sys.stdin:
        #This looks to see if the line starts with a "#", they will be ignored by the script
        #The important part is WHY it is looking for a particular characer- what is that character being used for?
        match = re.match("^#",line)

        #This removes the extra spaces, splits the input line using ":"
        fields = line.strip().split(':')

        #Looks at the line and will skip if it is incorrectly formatted, and if records are not valid it won't continue.
        #Match looks at the comments and the fields looks at the number
        if match or len(fields) != 5:
            continue

        #The username looks at the user input, when finish the gecos acts as a holder of information
        #gecos is simmlar to /etc/passwd(hold information)
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This split is being done because it splits the groups field into a list of groups
        #A user can be added to mutiple groups if chosen
        groups = fields[4].split(',')

        #Prints the progress so the Admin knows which user is being created
        print("==> Creating account for %s..." % (username))
        #cmd contains the linux command to create a new user. 
        #Builds on the adduser with no password set, and uses gecos to store user data(name,passwd,etc)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print(cmd)
        #os.system(cmd)

        #Prints the progress so the admin knows which password is being set up for which user
        print("==> Setting the password for %s..." % (username))
        #Sets the user to enter the password twice in the command line
        #Echo send the password input and applies it to the specific user
        #cmd contains the linux command used to set the users passwrd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print(cmd)
        #os.system(cmd)

        for group in groups:
            #The if statement is looking for "-".  If the input doesn't have it, the user will be added to that group
            #If the value has"-" no group will be assigned
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                #os.system(cmd)

if __name__ == '__main__':
    main()
