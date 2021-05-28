import matplotlib.pyplot as plt
import operator
from collections import Counter
print("\n\n1.Get details when all applications were launched at once")
print("2.Get details when applications were launched one by one\n\n")
print("Enter your choice : ")
r=int(input())
if(r==1):
    while True:
        
        print("\n\n1.View system call occcurences\n")
        print("2.View most frequently used system calls and Time spent on locking\n")
        print("3.View most infrequently used system calls\n")
        print("4.Graphical analysis\n")
        print("Enter 0 to exit\n")
        select=int(input("Enter your choice : "))
     
        if select==0:
            print("\nEXITING...\n\n")
            break
        
        elif select==1:
            
            freq_time=dict()
            def systemcall_occurences(filename, application):
                f = open(filename,'r')
                data = []
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                #print(modified_data)
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
            
                system_call_name = []
                no_of_calls = []
                for i in graph_data:
                    if i[-1] in freq_time.keys():
                        freq_time[i[-1]][0]+=1
                        freq_time[i[-1]][1]+=float(i[1])
                    else:
                        freq_time[i[-1]]=[1,float(i[1])]
            
         
            systemcall_occurences('launch_at_once/firefox.txt', 'Firefox')
            systemcall_occurences('launch_at_once/libreoffice.txt', 'LibreOffice')
            systemcall_occurences('launch_at_once/gedit.txt', 'Gedit')
            systemcall_occurences('launch_at_once/rhythmbox.txt', 'RhythmBox')
            systemcall_occurences('launch_at_once/ping.txt', 'Ping Command')
            systemcall_occurences('launch_at_once/wireshark.txt', 'Wireshark')
            systemcall_occurences('launch_at_once/redis.txt', 'Redis Benchmark')
            systemcall_occurences('launch_at_once/ls.txt', 'ls Command')
            systemcall_occurences('launch_at_once/cat.txt', 'cat Command')
            systemcall_occurences('launch_at_once/ps.txt', 'ps Command')
            print(freq_time)
            
        elif select==2:
            freq_time=dict()
            futex=[0,0]
            first_pair=[]
            max_syscall=[]
            max_syscalll_count=[]
            files=['Firefox','LibreOffice','Gedit','RhythmBox','Ping Command','Wireshark', 'Redis Benchmark','ls Command', 'ps Command','cat Command']
            def System_calls(filename, application):
                
                data = []
                f = open(filename,'r')
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
                system_call_name = []
                no_of_calls = []
                for i in graph_data:
                    no_of_calls.append(int(i[3]))
                    system_call_name.append(i[- 1])
                for i in graph_data:
                    if i[-1] in freq_time.keys():
                        if(i[-1]=='futex'):
                            futex[0]+=1
                            futex[1]+=float(i[0])
                        
                        freq_time[i[-1]][0]+=1
                        freq_time[i[-1]][1]+=float(i[1])
                    else:
                        freq_time[i[-1]]=[1,float(i[1])]
                max_syscall.append(system_call_name[no_of_calls.index(max(no_of_calls))])
                max_syscalll_count.append(max(no_of_calls))
                most_pop=dict(Counter(max_syscall))
                map_of_result = dict(sorted(most_pop.items(),key = operator.itemgetter(1),reverse=True ))
                pairs_iterator = iter(map_of_result)
                first_pair1 = next(pairs_iterator)
                first_pair.append(first_pair1)
            System_calls('launch_at_once/firefox.txt', 'Firefox')
            System_calls('launch_at_once/libreoffice.txt', 'LibreOffice')
            System_calls('launch_at_once/gedit.txt', 'Gedit')
            System_calls('launch_at_once/rhythmbox.txt', 'RhythmBox')
            System_calls('launch_at_once/ping.txt', 'Ping Command')
            System_calls('launch_at_once/wireshark.txt', 'Wireshark')
            System_calls('launch_at_once/redis.txt', 'Redis Benchmark')
            System_calls('launch_at_once/ls.txt', 'ls Command')
            System_calls('launch_at_once/ps.txt', 'ps Command')
            System_calls('launch_at_once/cat.txt', 'cat Command')
            print('\n')
            print("Most frequently used systemcall among all applicatin is "+first_pair[-1])
            print('\n')
            print("Highest no of System calls is made by the application "+files[max_syscalll_count.index(max(max_syscalll_count))]+  " and the system call is "+max_syscall[max_syscalll_count.index(max(max_syscalll_count))])
            print("\nTime spent on locking and its occurences\n")
            print(str(futex[1])+" secs  ",futex[0])           
        elif select==3:
            final=dict()
            def infrequent_systemcalls(filename, application):
                data = []
                f = open(filename,'r')
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
                    system_call_name = []
                    no_of_calls = []
                for i in graph_data:
                    no_of_calls.append(int(i[3]))
                    system_call_name.append(i[- 1])
                for i in range(len(system_call_name)):
                    if(system_call_name[i] not in final.keys()):
                        final[system_call_name[i]]= no_of_calls[i]
                    else:
                        final[system_call_name[i]]+= no_of_calls[i]
                map_of_result = {system_call_name[i]: no_of_calls[i] for i in range(len(system_call_name))}
                map_of_result = dict(sorted(map_of_result.items(),key = operator.itemgetter(1) ))
                dict_items = map_of_result.items()
                print("Infrequent system calls in "+application+" and its occurence")
                first_ten_infrequent_calls = list(dict_items)[:10]
                print(first_ten_infrequent_calls)
                print('\n\n\n\n\n')
            infrequent_systemcalls('launch_at_once/firefox.txt', 'Firefox')
            infrequent_systemcalls('launch_at_once/libreoffice.txt', 'LibreOffice')
            infrequent_systemcalls('launch_at_once/gedit.txt', 'Gedit')
            infrequent_systemcalls('launch_at_once/rhythmbox.txt', 'RhythmBox')
            infrequent_systemcalls('launch_at_once/ping.txt', 'Ping Command')
            infrequent_systemcalls('launch_at_once/wireshark.txt', 'Wireshark')
            infrequent_systemcalls('launch_at_once/redis.txt', 'Redis Benchmark')
            infrequent_systemcalls('launch_at_once/ls.txt', 'ls Command')
            infrequent_systemcalls('launch_at_once/cat.txt', 'cat Command')
            infrequent_systemcalls('launch_at_once/ps.txt', 'ps Command')
            print("\nMost infrequently used systemcalls are")
            for i,k in final.items():
                if(k==1):
                    print(i)
                    
        elif select==4:
            print("1.View all the graphs at once\n")
            print("2.Graph menu\n")
            print("Enter 0 to exit\n")
            option=int(input("Enter your choice:"))
            def plot_graph(filename, application):
                data = []
                f = open(filename,'r')
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
                    system_call_name = []
                    no_of_calls = []
                for i in graph_data:
                    system_call_name.append(i[len(i) - 1])
                    no_of_calls.append(int(i[len(i) - 2]))
                map_of_result = {system_call_name[i]: no_of_calls[i] for i in range(len(system_call_name))}
                map_of_result = dict(sorted(map_of_result.items(),key = operator.itemgetter(1), reverse=True))
                print(map_of_result)
                plt.figure(figsize = (10,10))
                plt.bar(list(map_of_result.keys())[:10],list(map_of_result.values())[:10], color = 'g', label = 'Top 10 System Calls for ' + application)
                plt.xlabel('System Call Names', fontsize = 12)
                plt.ylabel('No.of calls', fontsize = 12)
                plt.title(('Top 10 System Calls for ' + application), fontsize = 20)
                plt.legend()
                plt.show()
                print('\n\n\n\n\n')
            if option==0:
                break
            elif option==1:
                plot_graph('launch_at_once/firefox.txt','Firefox')
                plot_graph('launch_at_once/libreoffice.txt','LibreOffice')
                plot_graph('launch_at_once/gedit.txt','Gedit')
                plot_graph('launch_at_once/rhythmbox.txt','RhythmBox')
                plot_graph('launch_at_once/ping.txt','Ping Command')
                plot_graph('launch_at_once/wireshark.txt','Wireshark')
                plot_graph('launch_at_once/redis.txt','Redis Benchmark')
                plot_graph('launch_at_once/ls.txt','ls Command')
                plot_graph('launch_at_once/cat.txt','cat Command')
                plot_graph('launch_at_once/ps.txt','ps Command')
            elif option==2:
                print("Graph menu")
                print("1.Firefox\n2.LibreOffice Writer\n3.Gedit\n4.RythmBox\n5.Ping\n6.Wireshark\n7.Redis benchmark\n8.ls command\n9.cat command\n10.ps command\nEnter 0 to exit\n")
                choice=int(input("Enter your choice:"))
                if choice==1:
                    plot_graph('launch_at_once/firefox.txt','Firefox')
                elif choice==2:
                    plot_graph('launch_at_once/libreoffice.txt','LibreOffice')
                elif choice==3:
                    plot_graph('launch_at_once/gedit.txt','Gedit')
                elif choice==4:
                    plot_graph('launch_at_once/rhythmbox.txt','RhythmBox')
                elif choice==5:
                    plot_graph('launch_at_once/ping.txt','Ping Command')
                elif choice==6:
                    plot_graph('launch_at_once/wireshark.txt','Wireshark')
                elif choice==7:
                    plot_graph('launch_at_once/redis.txt','Redis Benchmark')
                elif choice==8:
                    plot_graph('launch_at_once/ls.txt','ls Command')
                elif choice==9:
                    plot_graph('launch_at_once/cat.txt','cat Command')
                elif choice==10:
                    plot_graph('launch_at_once/ps.txt','ps Command')
                else:
                    break
if(r==2):
    '''
    one by one
    '''
    while True:
        
        print("\n\n1.View system call occcurences\n")
        print("2.View most frequently used system calls and Time spent on locking\n")
        print("3.View most infrequently used system calls\n")
        print("4.Graphical analysis\n")
        select=int(input("Enter your choice:"))
     
        if select==0:
            print("\nEXITING..\n\n")
            break
        
        elif select==1:
            
            freq_time=dict()
            def systemcall_occurences(filename, application):
                f = open(filename,'r')
                data = []
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                #print(modified_data)
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
            
                system_call_name = []
                no_of_calls = []
                for i in graph_data:
                    if i[-1] in freq_time.keys():
                        
                        freq_time[i[-1]][0]+=1
                        freq_time[i[-1]][1]+=float(i[1])
                    else:
                        freq_time[i[-1]]=[1,float(i[1])]
            
         
            systemcall_occurences('firefox.txt', 'Firefox')
            
            systemcall_occurences('libreoffice.txt', 'LibreOffice')
            systemcall_occurences('gedit.txt', 'Gedit')
            systemcall_occurences('rhythmbox.txt', 'RhythmBox')
            systemcall_occurences('ping.txt', 'Ping Command')
            systemcall_occurences('wireshark.txt', 'Wireshark')
            systemcall_occurences('redis.txt', 'Redis Benchmark')
            systemcall_occurences('ls.txt', 'ls Command')
            systemcall_occurences('cat.txt', 'cat Command')
            systemcall_occurences('ps.txt', 'ps Command')
            print(freq_time)
            
        elif select==2:
            freq_time=dict()
            futex=[0,0]
            first_pair=[]
            max_syscall=[]
            max_syscalll_count=[]
            files=['Firefox','LibreOffice','Gedit','RhythmBox','Ping Command','Wireshark', 'Redis Benchmark','ls Command', 'ps Command','cat Command']
            def System_calls(filename, application):
                
                data = []
                f = open(filename,'r')
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
                system_call_name = []
                no_of_calls = []
                for i in graph_data:
                    no_of_calls.append(int(i[3]))
                    system_call_name.append(i[- 1])
                for i in graph_data:
                    if i[-1] in freq_time.keys():
                        if(i[-1]=='futex'):
                            futex[0]+=1
                            futex[1]+=float(i[0])
                        
                        freq_time[i[-1]][0]+=1
                        freq_time[i[-1]][1]+=float(i[1])
                    else:
                        freq_time[i[-1]]=[1,float(i[1])]
                max_syscall.append(system_call_name[no_of_calls.index(max(no_of_calls))])
                max_syscalll_count.append(max(no_of_calls))
                most_pop=dict(Counter(max_syscall))
                map_of_result = dict(sorted(most_pop.items(),key = operator.itemgetter(1),reverse=True ))
                pairs_iterator = iter(map_of_result)
                first_pair1 = next(pairs_iterator)
                first_pair.append(first_pair1)
            System_calls('firefox.txt', 'Firefox')
            System_calls('libreoffice.txt', 'LibreOffice')
            System_calls('gedit.txt', 'Gedit')
            System_calls('rhythmbox.txt', 'RhythmBox')
            System_calls('ping.txt', 'Ping Command')
            System_calls('wireshark.txt', 'Wireshark')
            System_calls('redis.txt', 'Redis Benchmark')
            System_calls('ls.txt', 'ls Command')
            System_calls('ps.txt', 'ps Command')
            System_calls('cat.txt', 'cat Command')
            print('\n')
            print("Most frequently used systemcall among all applicatin is "+first_pair[-1])
            print('\n')
            print("Highest no of System calls is made by the application "+files[max_syscalll_count.index(max(max_syscalll_count))]+  " and the system call is "+max_syscall[max_syscalll_count.index(max(max_syscalll_count))])
            print("\nTime spent on locking and its occurences\n")
            print(str(futex[1])+" secs  ",futex[0])             
        elif select==3:
            final=dict()
            def infrequent_systemcalls(filename, application):
                data = []
                f = open(filename,'r')
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
                    system_call_name = []
                    no_of_calls = []
                for i in graph_data:
                    no_of_calls.append(int(i[3]))
                    system_call_name.append(i[- 1])
                for i in range(len(system_call_name)):
                    if(system_call_name[i] not in final.keys()):
                        final[system_call_name[i]]= no_of_calls[i]
                    else:
                        final[system_call_name[i]]+= no_of_calls[i]
                map_of_result = {system_call_name[i]: no_of_calls[i] for i in range(len(system_call_name))}
                map_of_result = dict(sorted(map_of_result.items(),key = operator.itemgetter(1) ))
                dict_items = map_of_result.items()
                print("Infrequent system calls in "+application+" and its occurence")
                first_ten_infrequent_calls = list(dict_items)[:10]
                print(first_ten_infrequent_calls)
                print('\n\n\n\n\n')
            infrequent_systemcalls('firefox.txt', 'Firefox')
            infrequent_systemcalls('libreoffice.txt', 'LibreOffice')
            infrequent_systemcalls('gedit.txt', 'Gedit')
            infrequent_systemcalls('rhythmbox.txt', 'RhythmBox')
            infrequent_systemcalls('ping.txt', 'Ping Command')
            infrequent_systemcalls('wireshark.txt', 'Wireshark')
            infrequent_systemcalls('redis.txt', 'Redis Benchmark')
            infrequent_systemcalls('ls.txt', 'ls Command')
            infrequent_systemcalls('cat.txt', 'cat Command')
            infrequent_systemcalls('ps.txt', 'ps Command')
            print("\nMost infrequently used systemcalls are")
            for i,k in final.items():
                if(k==1):
                    print(i)
                    
        elif select==4:
            print("1.View all the graphs at once\n")
            print("2.Graph menu\n")
            print("Enter 0 to exit\n")
            option=int(input("Enter your choice:"))
            def plot_graph(filename, application):
                data = []
                f = open(filename,'r')
                for row in f:
                    row = row.split('\t')
                    data.append(row[0])
                data.pop();
                data.pop();
                modified_data = data[2:]
                graph_data = []
                for i in modified_data:
                    graph_data.append(i.strip().split())
                    system_call_name = []
                    no_of_calls = []
                for i in graph_data:
                    system_call_name.append(i[len(i) - 1])
                    no_of_calls.append(int(i[len(i) - 2]))
                map_of_result = {system_call_name[i]: no_of_calls[i] for i in range(len(system_call_name))}
                map_of_result = dict(sorted(map_of_result.items(),key = operator.itemgetter(1), reverse=True))
                print(map_of_result)
                plt.figure(figsize = (10,10))
                plt.bar(list(map_of_result.keys())[:10],list(map_of_result.values())[:10], color = 'g', label = 'Top 10 System Calls for ' + application)
                plt.xlabel('System Call Names', fontsize = 12)
                plt.ylabel('No.of calls', fontsize = 12)
                plt.title(('Top 10 System Calls for ' + application), fontsize = 20)
                plt.legend()
                plt.show()
                print('\n\n\n\n\n')
            if option==0:
                break
            elif option==1:
                plot_graph('firefox.txt','Firefox')
                plot_graph('libreoffice.txt','LibreOffice')
                plot_graph('gedit.txt','Gedit')
                plot_graph('rhythmbox.txt','RhythmBox')
                plot_graph('ping.txt','Ping Command')
                plot_graph('wireshark.txt','Wireshark')
                plot_graph('redis.txt','Redis Benchmark')
                plot_graph('ls.txt','ls Command')
                plot_graph('cat.txt','cat Command')
                plot_graph('ps.txt','ps Command')
            elif option==2:
                print("Graph menu")
                print("1.Firefox\n2.LibreOffice Writer\n3.Gedit\n4.RythmBox\n5.Ping\n6.Wireshark\n7.Redis benchmark\n8.ls command\n9.cat command\n10.ps command\nEnter 0 to exit\n")
                choice=int(input("Enter your choice:"))
                if choice==1:
                    plot_graph('firefox.txt','Firefox')
                elif choice==2:
                    plot_graph('libreoffice.txt','LibreOffice')
                elif choice==3:
                    plot_graph('gedit.txt','Gedit')
                elif choice==4:
                    plot_graph('rhythmbox.txt','RhythmBox')
                elif choice==5:
                    plot_graph('ping.txt','Ping Command')
                elif choice==6:
                    plot_graph('wireshark.txt','Wireshark')
                elif choice==7:
                    plot_graph('redis.txt','Redis Benchmark')
                elif choice==8:
                    plot_graph('ls.txt','ls Command')
                elif choice==9:
                    plot_graph('cat.txt','cat Command')
                elif choice==10:
                    plot_graph('ps.txt','ps Command')
                else:
                    break
                    
            
