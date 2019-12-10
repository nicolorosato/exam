Welcome to the repository exam! 
The team NMTP is pleased to have You here!

Before starting using the program, please follow the instructions: 

1.	From your terminal, go into ‘scripts’ directory and ran dbmanager.py. 		Here you can add a username with the relative password. With the 		arguments -a and -p. The new user will be saved in a database called 		data.db. Your password will be hashed, salted, and iterated 100000 		times ;) 

2.	After this step, you exit the ‘scripts’ directory and you return to the 	‘exam’ one. Now you execute ‘main.py’. The main function requires the 		following arguments: 
	-c to check the username 
	-p to check the password 
	- ‘state’(positional) to return the state’s capital name. 
	Only European states are allowed. Note well, the name of the state 		should start with a capital letter, i.e. Italy or France, not Italy or 		france. Wrong states will not considered valid. In this case, will 		be displayed an error message. 
	
	Optional arguments: 
	- v to increase the output verbosity. 
	-vv to obtain more debug information. 

Regarding point 2, you are allowed to obtain the capital’s state name only and only if your username and password are correct. Otherwise you will receive the message: ‘wrong username or wrong password’ and no output will be showed regarding the capital’s state name. 

Have a nice one! 

