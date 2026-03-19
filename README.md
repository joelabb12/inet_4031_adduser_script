# inet_4031_adduser_script

## Program Description
This program automates the process of adding users to a Linux system. Instead of having to manually create an account, set a password, and assign it to a group, the script reads the user information from an input file and performs the tasks efficiently. A System Admin would need to manually create users using Linux commands, using adduser to create the user, passwd to create a password, and adduser username groupname to place them into a group. The script automates those commands, it creates the user, builds the password, and adds it to a group listed in the input file. 


## Program User Operation
The user creates an input file that contains one line for each account that is being created. Each line needs to follow the required format so the script can correctly read the name, password, name information, and group. Once that is correctly done, the script, which runs on the command line, reads the input line by line. Each valid line creates what the user inputted, like the user account, password, and the listed group. The script will skip any invalid lines or comment lines. 


## Input File Format
This is the expected format:

username:password:last name:first name:groups

The username

- Name for the new account

The Password

 - Password set for the new user
   
The Last Name

 - Last name set for the user
   
The First Name

- First name set for the user
  
Groups

- group information


If the user does not have all 5 fields, it is skipped. If the user is intentionally skipping a line in the input file, they need to add "#" at the beginning of the line. The script will ignore it. 


## Command Execution

To run this program, please remember to move into the directory containing the files. The Python file may need to be made executable before running it directly. Once that is done, the script can be run from the command line.

Below is the code that runs the script:

./create-users.py < create-users.input

The "<"symbol is redirecting the contents of the create-users.Input the file into the program so the script can read each line through the input. 


## Dry Run
A dry run allows the user to test the script without making changes to the system. In the script, commenting on the lines that are "os.cmd()" will not make any changes to the system. The system will only print the commands and actions it would perform, like creating users, setting passwords, and groups. 
t
