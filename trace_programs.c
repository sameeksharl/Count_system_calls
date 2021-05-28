#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	// coloring convention : '\e[<fg_bg>;2;<R>;<G>;<B>m' ; 38 for fg ; 48 for bg

	int choice, option;
	printf("\n\n\n\t\t*************** WELCOME ***************\n\n");
	printf("ANALYSE APPLICATIONS AND PROCESSES TO GET REAL TIME STATS & SUMMARY\n\n");
	do
	{
		printf("\nChoose any one option :\n");
		printf("1. Trace all processes at once\n");
		printf("2. Launch processes one by one and trace them\n");
		printf("3. Get an information on the threads created by different processes\n");
		printf("Enter 0 to exit....\n");
		printf("Enter your choice : ");
		scanf("%d", &option);
		switch(option)
		{
			case 0:
			{
				printf("\n\e[38;2;255;0;0mEXITING...\e[38;2;255;255;255m\n\n");
				return 0;
			}
			case 1:
			{
				system("bash trace_all_programs.sh");
				printf("\e[38;2;0;255;0mTraced all applications successfully\e[38;2;255;255;0m\n\n");
				break;
			}
			case 2:
			{
				{
					do
					{
						printf("\e[38;2;255;255;0m\n\n\t\tMENU:\n\n");
						printf("Enter 1 to launch firefox\nEnter 2 to launch LibreOffice Writer\nEnter 3 to open a new text editor window(gedit)\nEnter 4 to launch RythmBox\nEnter 5 to start pinging operation\nEnter 6 to launch Wireshark\nEnter 7 to run redis benchmark on redis\nEnter 8 to run the ls command\nEnter 9 to run the cat command\nEnter 10 to run the ps command\n\e[38;2;255;0;0mEnter 0 to exit\e[38;2;255;255;255m\n");
						scanf("%d", &choice);
		
						switch(choice)
						{
							case 0 :
							{
								printf("\n\e[38;2;255;0;0mEXITING...\e[38;2;255;255;255m\n\n");
								return 0;
							}
							case 1: 
							{
								printf("Launching firefox ... \n");
								system("strace -c -o firefox.txt firefox");
								printf("\n\n\e[38;2;0;255;0mTraced process 'firefox' successfully...\e[38;2;255;255;0m\n");
								break;
							}
							case 2: 
							{
								printf("Launching LibreOffice writer ... \n");
								system("strace -c -o libreoffice.txt libreoffice");
								printf("\n\n\e[38;2;0;255;0mTraced process 'libreoffice' successfully...\e[38;2;255;255;0m\n");
								break;
							}
							case 3: 
							{
								printf("Launching gedit ... \n");
								system("strace -c -o gedit.txt gedit");
								printf("\n\n\e[38;2;0;255;0mTraced process 'gedit' successfully...\e[38;2;255;255;0m\n");
								break;
							}
							case 4: 
							{
								int stop;
								printf("Launching RythmBox ... \n");
								system("strace -c -o rhythmbox.txt rhythmbox-client --play");
								printf("Playing the most recent song...\n");
								printf("Enter 0 if you wish to stop the song :");
								scanf("%d", &stop);
								if( stop == 0)
								{
									system("rhythmbox-client --stop");
									printf("\e[38;2;255;255;0mMusic stopped...\e[38;2;255;255;255m\n");
								}
								printf("\e[38;2;0;255;0mTraced process 'rythmbox' successfully...\e[38;2;255;255;255m\n");
								break;
							}
							case 5: 
							{
								char dest[100];
								char BUF[1000];
								printf("Enter the destination where you want to ping : ");
								scanf("%s", dest);
								snprintf(BUF, sizeof(BUF), "strace -c -o ping.txt ping %s", dest);
								printf("Running ping operation (Pinging from host to %s) ... \n", dest);
								system(BUF);
								printf("\n\n\e[38;2;0;255;0mTraced process 'ping' successfully...\e[38;2;255;255;0m\n");
								break;
							}
							case 6: 
							{
								printf("Launching wireshark ... \n");
								system("strace -c -o wireshark.txt wireshark");
								printf("\n\n\e[38;2;0;255;0mTraced process 'wireshark' successfully...\e[38;2;255;255;0m\n");
								break;
							}
							case 7: 
							{
								printf("Running redis benchmark on redis ... \n");
								system("strace -c -o redis.txt redis-benchmark");
								printf("\n\n\e[38;2;0;255;0mTraced process 'redis-benchmark' successfully...\e[38;2;255;255;0m\n");
								break;
							}
							case 8: 
							{
								char command[200];
								char BUF[1000];
								int yes;
								printf("Do you want to directly run the ls command or pass some parameters with it?\n");
								printf("Enter 1 if you want to add parameters and 0 if you don't wish to do so : ");
								scanf("%d", &yes);
								if(yes == 1)
								{
									printf("Enter the additional parameters you would like to pass with ls : ");
									scanf("%s", command);
									printf("Running the ls %s command ... \n", command);
									snprintf(BUF, sizeof(BUF), "strace -c -o ls.txt ls %s", command);
									system(BUF);
									printf("\n\n\e[38;2;0;255;0mTraced process 'ls %s' successfully...\e[38;2;255;255;0m\n", command);
								}
								else if (yes == 0)
								{
									printf("Running the ls command ... \n");
									system("strace -c -o ls.txt ls");
									printf("\n\n\e[38;2;0;255;0mTraced process 'ls' successfully...\e[38;2;255;255;0m\n");
								}
								else
								{
									printf("\n\e[38;2;255;0;0mNOT A VALID CHOICE !\e[38;2;255;255;255m\n");
								}
								break;
							}
							case 9: 
							{
								char BUF[1000];
								char filename[100];
								printf("These are the files present in the current directory :\n");
								system("ls -l");
								printf("\n\n\nSelect any one of them to be displayed using cat command...\n");
								printf("Enter the name of the file : ");
								scanf("%s", filename);
								printf("Displaying the contents of %s using cat command...\n", filename);
								snprintf(BUF, sizeof(BUF), "strace -c -o cat.txt cat %s", filename);
								system(BUF);
								printf("\n\n\e[38;2;0;255;0mTraced process 'cat %s' successfully...\e[38;2;255;255;0m\n", filename);
								break;
							}
							case 10: 
							{
								char command[200];
								int yes;
								char BUF[1000];
								printf("Do you want to directly run the ps command or pass some parameters with it?\n");
								printf("Enter 1 if you want to add parameters and 0 if you don't wish to do so : ");
								scanf("%d", &yes);
								if(yes == 1)
								{
									printf("Enter the additional parameters you would like to pass with ps : ");
									scanf("%s", command);
									printf("Running the ps %s command ... \n", command);
									snprintf(BUF, sizeof(BUF), "strace -c -o ps.txt ps %s", command);
									system(BUF);
									printf("\n\n\e[38;2;0;255;0mTraced process 'ps %s' successfully...\e[38;2;255;255;0m\n", command);
								}
								else if (yes == 0)
								{
									printf("Running the ps command ... \n");
									system("strace -c -o ps.txt ps");
									printf("\n\n\e[38;2;0;255;0mTraced process 'ps' successfully...\e[38;2;255;255;0m\n");
								}
								else
								{
									printf("\n\e[38;2;255;0;0mNOT A VALID CHOICE !\e[38;2;255;255;255m\n");
								}
								break;
							}
							default :
							{
								printf("\n\e[38;2;255;0;0mNOT A VALID CHOICE !\e[38;2;255;255;255m\n");
								printf("\e[38;2;0;255;0mPlease re-enter your choice !\e[38;2;255;255;255m\n\n");
							}
			
						}
	
					}
					
					while(choice != 0);
				}
				break;
			}
			case 3 :
			{
				printf("\n\nChoose an application:\n1.Firefox\n2.Gedit\n3.Redis-benchmark\n4.Ping\n5.Rhythmbox\n\n");
				printf("Enter your choice : ");
				int application;
				scanf("%d", &application);
				switch(application)
				{
					case 1:
					{
						printf("\e[38;2;255;255;0mThese are the threads created by the application firefox where SID represents the thread ID\e[38;2;255;255;255m\n\n");
						system("ps -F -T -m -p $(pidof firefox | awk '{print $1}') ; echo '\e[38;2;255;255;0m\nThe total number of threads created by firefox are : \e[38;2;255;255;255m'; ps hH p $(pidof firefox | awk '{print $1}') | wc -l");
						break;
					}
					case 2:
					{
						printf("\e[38;2;255;255;0mThese are the threads created by the application gedit where SID represents the thread ID\e[38;2;255;255;255m\n\n");
						system("ps -F -T -m -p $(pgrep gedit) ; echo '\e[38;2;255;255;0m\nThe total number of threads created by gedit are : \e[38;2;255;255;255m'; ps hH p $(pgrep gedit) | wc -l");
						break;
					}
					case 3:
					{
						printf("\e[38;2;255;255;0mThese are the threads created by the application redis-server where SID represents the thread ID\e[38;2;255;255;255m\n\n");
						system("ps -F -T -m -p $(pgrep redis-server) ; echo '\e[38;2;255;255;0m\nThe total number of threads created by redis-server are : \e[38;2;255;255;255m'; ps hH p $(pgrep redis-server) | wc -l");
						break;
					}
					case 4:
					{
						printf("\e[38;2;255;255;0mThese are the threads created by the command ping where SID represents the thread ID\e[38;2;255;255;255m\n\n");
						system("ps -F -T -m -p $(pgrep ping) ; echo '\e[38;2;255;255;0m\nThe total number of threads created by ping command are : \e[38;2;255;255;255m'; ps hH p $(pgrep ping) | wc -l");
						break;
					}
					case 5:
					{
						printf("\e[38;2;255;255;0mThese are the threads created by the application rhythmbox where SID represents the thread ID\e[38;2;255;255;255m\n\n");
						system("ps -F -T -m -p $(pgrep rhythmbox) ; echo '\e[38;2;255;255;0m\nThe total number of threads created by rhythmbox are : \e[38;2;255;255;255m'; ps hH p $(pgrep rhythmbox) | wc -l");
						break;
					}
					default:
					{
						printf("Invalid choice!");
						break;
					}
				}
				break;
				
			}
			
			default:
			{
				printf("\n\e[38;2;255;0;0mNOT A VALID CHOICE !\e[38;2;255;255;255m\n");
				printf("\e[38;2;0;255;0mPlease re-enter your choice !\e[38;2;255;255;255m\n\n");
			}
			
		}
		
	}
	
	while(option != 0);

	printf("\n\e[38;2;255;0;0mEXITING...\e[38;2;255;255;255m\n\n");
	return 0;
}


/*
Commands used:
1. To launch an application type: the application name
2. To get pID of that process type : sh -c 'echo $$; exec <application name>'
3. Run strace on that pID and save the result to a text file : strace -c -p <pID> -o applicationname.txt
4. To kill that process type: kill(<pID)
5. To get an info on threads use the command: ps -F -T -m -p <pID> --> in the output SID corrresponds to threadID
6. To get name of these threads use : pthread_getname_np() -> not required can experiment if you wish  
*/
				
