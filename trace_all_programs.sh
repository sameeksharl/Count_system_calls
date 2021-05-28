!/bin/bash
# traces all the programs at once using strace
(mkdir -p launch_at_once) && (strace -c -o launch_at_once/firefox.txt firefox | strace -c -o launch_at_once/libreoffice.txt libreoffice | strace -c -o launch_at_once/gedit.txt gedit | strace -c -o launch_at_once/rhythmbox.txt rhythmbox-client --play | strace -c -o launch_at_once/ping.txt ping 127.0.0.1 | strace -c -o launch_at_once/wireshark.txt wireshark | strace -c -o launch_at_once/redis.txt redis-benchmark | strace -c -o launch_at_once/ls.txt ls .. | strace -c -o launch_at_once/cat.txt cat trace_all_programs.sh | strace -c -o launch_at_once/ps.txt ps -e)

