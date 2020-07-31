#!/usr/bin/python3

# parse keystone.common.wsgi and return number of successful login attempts
login_success = 0 # counter for successful logins

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if line is not equal to '- - - - -] Authorization failed.
        if line != "- - - - -] Authorization failed":
            login_success += 1 # this is the same as login_sucess = login_success + 1

print("The number of successful login attempts is", login_success)
