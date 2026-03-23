#!/usr/bin/python3

# INET4031
# David Meng
# 3/22/2026 Created
# 3/23/2026 Last Modified

#REPLACE THIS COMMENT - identify what each of these imports is for.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        #Looks if there is a hashtage # at each start of every line.
        match = re.match("^#",line)

        #Removes the extra unnecessary space and splits into other pieces for every colon.
        fields = line.strip().split(':')

        #Checking if the line has a hashtage or if there is any missing fields, skips if did not meet requirements, or match.
        if match or len(fields) != 5:
            continue

        #Pulls specific user information from the list. Formats information for passwd.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Splits groups by commas if the user belongs to more groups.
        groups = fields[4].split(',')

        #Prints information that a new account is being processed.
        print("==> Creating account for %s..." % (username))
        #Creating a new command for a new user without a password.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #Prints out a new command and tells the OS to execute the command.
        #print(cmd)
        #os.system(cmd)

        #Printing out the process for a new password.
        print("==> Setting the password for %s..." % (username))
        #RCreaes a new command which can help set up the password automatically through the passwd tool.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Prints out the command and tells the OS to execute the command.
        #print(cmd)
        #os.system(cmd)

        for group in groups:
            #Checking if the following group field has a dash, if not, the user will be added.
            #If there is a dash, it skips the group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
