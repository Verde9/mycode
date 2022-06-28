#!/usr/bin/env python3

def main():

    log= "WARNING keystone.common.wsgi [req-10b2861f-a302-4767-b484-39731f9371a8 - - - - -] Authorization failed. The request you have made requires authentication. from 172.16.1.5"
    
    log_list = log.split(" ")
    
    print(log_list[-1])
    

main()    
