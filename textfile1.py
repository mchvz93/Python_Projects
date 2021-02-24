def main ():
	outfile = open(r"c:\Users\Marco\Desktop\Python Text files\philo.txt", 'w') # raw string---> will the \ as it is and not as escape keys
	
	outfile.write('John Locke\n')  #you need the \n to seperate each piece of data eg Jon LockeDavid HumeEdmund Burke
	outfile.write('David Hume\n')
	outfile.write('Edmund Burke\n')
	
	outfile.close()

main()
