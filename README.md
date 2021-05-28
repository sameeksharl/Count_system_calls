# Count_system_calls

It is a simple program that counts the number of system calls used by any application and summarizes the result at the end. The summary includes stating about the most frequently used applications across applications, most infrequently used system calls, time spent in locking and threads created by each process.

How to run?

Required tools (On Ubuntu 18.04):
1. Wireshark 
2. Systemtap
3. Matplotlib
4. Redis-server

How to run?
Step 1: gcc trace_programs.c
Step 2 : python3 get_result.py)
topsys.stp can be run in another terminal simultaneously (however, it's just an additional feature and not a requirement)
