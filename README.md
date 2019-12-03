## Implementation of a Database of European capitals


In this repository you can find in the folder named '''myfolder''' a file named ```capitals.py``` that implements the ```check_capital``` functions. These functions check if the given input is a valid name of an European state and return the respective capital. It is used in the ```main.py``` file to test if some states are in Europe. If you run the program, executing the main file with: ```python main.py``` you have to insert a positional argument and one optional to increase the output verbosity, So for example: 

```
$ python main.py [argv1]

- Capital
or Sorry, Honduras does not seem to be an European state

$ python main.py [argv1] -v

- The Eu state's capital of State is Capital

$ python main.py [argv1] -vv

Running main.py...
100% 
Extracting your input from csv file...
100%
Fiding matching value...
100%
Obtainng the name of the capital...
100%
Returning matched value...
100%
The Eu state's capital of Italy is Rome


```
