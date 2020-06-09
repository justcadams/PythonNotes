# Programming and Source Code Management <sub>[[1]](#References)</sub>
## Computer Programs

A program makes a computer usable. Without a program, a computer, even the most powerful one, is nothing more than an object. Programs are the physical manifestation of the Turing Machine mathematical model, which defines a device that is capable of the following:

1. Reading the symbol at the current location.
2. Performing a calculation, which generates a symbol and/or a movement instruction.
3. Moving left or right a discrete number of symbols.
4. Writing the symbol at the current location.

This mathematical abstraction is ultimately a computer and the program is the infinite tape of symbols. A modern computer is no different. It repeats steps 1-4 until it is shutdown. Modern computers now have a substantial number of hardware components that handle difficult calculations, but they only generate two symbols 0 or 1. It may even consume enough power in the processor to match the power density of a jet engine. However, all classical computers are Turing Machines.

## Topic 1 - Programming Basics

### Natural Language (Reactive Adaptive Language)

Any language is a means for expressing and recording thoughts. There are currently 7,117 known living natural languages. Many more languages have perished to documented history.

![Language Tree](images/Language-Tree-Minna-Sundberg.jpg)Illustration by Linguist Minna Sundberg <sub>[[2]](#References)</sub>

There are so many languages around us that we are even capable of expressing our deepest feelings very precisely without saying even one word. Another language you use each day is your native language. This language is an intimate relationship involving reading, writing, and speaking to others to relate your thoughts, opinions, questions, and ideas.

This language also systematically biases your thought process. As a matter of using language, we become biased by its use. So, it is important to recognize that bias is intrinsically human, and it is always acceptable to create constructive conversation questioning our biases.

### Formal Language (Communication by Construction)

Similarly processors (Turing Machines) only understand their personal machine code, which is known as an Instruction List (IL). Different processors may understand different instructions depending on the size of their ILs.

There are even dynamic processors using Field Programmable Gate Arrays (FPGAs) that can change their IL as they execute instructions. This does not allow a computer to create a new language. However, it is the first step to designing dynamic language processing systems and it provides the system a substantial amount of security. So, formal languages are constructed for the specific system or communications channel.

Example: [x86 Processor Instruction List](https://en.wikipedia.org/wiki/X86_instruction_listings) <sub>[[3]](#References)</sub>

Natural language developed through the process of human adaptation to their environment, while formal language is designed by humans.

### Artificial Intelligence Language (Active Adaptive Language)

There is a rapidly developing form of communication developing within artificial intelligence. Active Adaptive Language (AAL) modifies the system that stores the language and modifies the language itself to continuously search for the best language for the chosen communications channel. This is the very best form of language discovered to date. It resembles how human language evolves over time. Hoewever, in most cases human language evolves as a reaction to the environment.

### Components of a Language

* Alphabet

	A set of symbols used to build words of a certain language (e.g., Binary {0,1}, Latin alphabet {A,B,C,...,x,y,z}, Cyrillic {А,Б,Ч,Д,...,у,ү,в,э}, Kanji {})

* Lexis

	A set of words that comprises the language.

		English: {a,aa,aaa,aaaa,aachen,aaes,aaf,aah,aalborg,aalesund,aalii,aalst,aalto,aam,aap,aar,aarau,aardvark,...,zymology,zymolysis,zymometer,zymosis,zymotic,zymurgy,zyrian,zyryan,zyryenian,zyzzyva,zyzzyvas,z,zz,zzz}.

* Syntax

	A set of formal or informal rules used to determine if a certain string of words forms a valid sentence.

		Valid: Python is a high-level language, which means it is human readable.

		Invalid: Python is a high level language that reads good.
		Notice the sentence above has one spelling mistake (high level) and one misuse of a modifier (good).

* Semantics

	A set of formal or informal rules that determines if a phrase makes sense.

		Valid: If you prove me wrong, then I will eat my hat.

		Invalid: If I prove you right, then the hat will eat us.
	
	Although the second sentence is fanciful and fun, it is also absurd.

Note: A processors instruction list is the alphabet of a machine language because it is the "smallest symbol" the computer is capable of understanding (Turing Machine Abstraction).

### High-Level Language vs Low Level Language

A high-level language is a human readable programming language, which contains symbols, words, and syntax that resembles a natural language.

Examples: C++, C#, Java, and Python

Note: A program written in a high-level language is called a source code. Similarly, the file containing the source code is called a source file.

A low-level language is a machine readable programming language, which contains machine code or assembly language.

### Compilation vs Interpretation

For the source code written in a high-level language to transform in to the machine code of a low-level language, the following must be correct in all cases:

* Alphabetically - The code must be written in a recognizable script, such as Roman, Cyrillic, etc.
* Lexically - The code must use the dictionary of reserved keywords to accomplish the intended task.
* Syntactically - Each language has syntax rules that must be strictly adhered to.
* Semantically - The output of the program must make sense to the user.

There are two different ways of transforming a program from a high-level programming language into an assembly language:

Compilation - The source code is translated in to a .exe file (Windows), which contains the machine code. This executable file is usable by all processors that use the same instruction list.

Interpretation - Executing source code for an interpreted language requires an interpreter to generate machine code for the system. This interpreter is necessary on any machine that attempts to run the interpreted programming language source code.

|	|Compilation|Interpretation|
|---|-----------|--------------|
|   Advantage   | * the execution of the translated code is faster.| * You can run the code as soon as you complete it - there are no additional phases of translation. |
|   Advantage   |  Only the user has to have the compiler - the end-user may use the code without it. |  the code is stored using programming language, not the machine one - this means that it can be run on computers using different machien languages; you don't compile your code seperately for each different architecture |
|   Advantage   | The translated code is stored using machine language - as it very hard to undsertand it, your own inventions and programming tricks are likely to remain your secret.  |	|
| Disadvantage | The compilation itself may be a very time-consuming process - you may not be able to run your code immediately after any ammendment | Don't expect that interpretation will ramp your code to high speed - your code will share the computer's power with the interpreter, so it can't be really fast. |
| Disadvantage | You have to have as many compilers as hardware platforms you want your code to be run on. | Both you and the end user have to have the interpreter to run your code. |

This means that Python is an interpreted language. If you want to program in Python, then you will need the Python interpreter. Interpreted languages are tradtionally called scripting languages and the source code is called a script.

### What does an interpreter do?

A source file containing the source code you want to execute is read by an interpreter from left to right and top to bottom. The first step to interpretation is ensuring that the source code is alphabetically, lexically, syntactically, and semantically correct (many semantics problems are logic errors, which will not prevent execution). If a compiler finds an error, then interpretation is complete. The only result is an error message, which points to the line that failed. The error message may also contain the fault that caused the error. The most interesting part of interpreting code is that each line is executed individually, which forces the first line to execute close to the number of lines in the code and the last line to execute once if there are no errors.

### What is Python and who created it?

Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.

Python was created by Guido van Rossum, born in 1956 in Haarlem, the Netherlands. Guido and his friends had a penchant for British comedy and pizza. So, Python was named after Monty Python and The Flying Circus, (This explains why I became a programmer. I do indeed enjoy pizza, and I watched Monty Python religiously in my youth).

### Programming, A Hobby

In December 1989, I was looking for a "hobby" programming project that would keep me occupied during the week around Christmas. My office (...) would be closed, but I had a home computer, and not much else on my hands. I decided to write an interpreter for the new scripting language I had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers. I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus). 

-Guido van Rossum

#### Guido's Goals: A Vision for Unity

* an easy and intuitive language just as powerful as those of the major competitors
* open source, so anyone can contribute to its development
* code that is as understandable as plain English
* suitable for everyday tasks, allowing for short development times

After 20 years this vision has brought together the global community to create one of the largest and most diverse open source programming language libraries.

#### Python Advantages: Simple Objectives

* Easy to learn
* Easy to teach
* Easy to use
* Easy to understand
* Easy to obtain, install, and deploy

#### Python Alternatives

    Perl - a scripting language originally authored by Larry Wall;
    Ruby - a scripting language originally authored by Yukihiro Matsumoto.

### Python Requirements Components

* Python requires a text editor
* A console from which to launch the interpreter and source code.
* Python Interpreter translares source code in to machine code
* Python Debugger reports errors as they occur.
* Read, Execute, Print, and Loop / Integrated Development and Learning Environment (REPL/IDLE) These systems provide a shell with which developers can explore the Python programming language, tools, and libraries.

# Programming & Source Code Management
	A way to track changes in files. Standard practice require tracking each change, file name, and the person responsible for that change.
* Source Code Information Recorded by Source Code Managers
  * Change
  * File
  * Person
  * Version

## Git:
	Git (/ɡɪt/) is a distributed version-control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.

Revature url for gitlab: https://gitlab.com/revature_batches/2005-may19-richard

### Git Commands:
* git clone <url> 				- Copies a remote repository
* git status 					- Displays local branch changes in comparison to HEAD
* git add 						- Stages branch for commit by adding files / file changes/updates the local repository
* git commit -m "message" 		- Saves changes to be added to the remote repository.
* git pull origin master 		- Pulls the remote master repository 
* git push origin master		- Update the remote master repository
* git branch -b 				- Creates and checks out a branch
* git fetch 					- Retrieves the 
* git checkout master 			-
	(not allowed during training)
* credential manager  		- Windows program for handling usernames and passwords.
	(delete login information if it is incorrect)

### Branching:
	By making a new branch or copy of the repository inside of the repository, I can keep my work separate from other work.

* Master Branch <- Protected branch that houses the canonical app
* Dev/Staging <- A more experimental application
* Feature Branches <- A branch off of dev that we use to develop a new feature.

## Bash Commands:
* mkdir - Make a directory
* cd - Change a directory
* ls - List the files in the current directory

## Programming Language
	A programming language is a language that allows us to communicate with a computer and tell it what to do.

### High vs Low

#### Low-level programming language
	Machine-code, assembly, etc.

#### High-level programming language
	Closer to natural language. We can communicate in a formal language that appears to be natural, and it can translate that language to a lower-level language.
	Python, Java, C#, C, C++, JS, Basic

### Translation
	When you compile a high-level language into something the machine can acutally use.
* Compilation
  * You run a program that will create machine code out of the high-level program you wrote and you end up with an executable file for THAT machine that you can run.
  * C - When you compile a C program it only works on the machine that you used to compile.
  * Java - Runtime Environment - Compiles your code into Java code that can run on a Java Runtime Environment
* Interpretation
  * You run a progam that will read your code line by line and transform that code into machine code on the fly. 
  * Python and JavaScript are both interpreted languages.

### REPL Shell - Read Evaluate Print Loop (REPL)
	Read, Evaluate, Print, Loop (REPL) shell programs can be run from the command line. They are used as a syntax test bed when there is no other available system for testing your code.

	The code is ephemeral, which prevents us from saving it anywhere while working in a test environment.

### Identifiers
	An identifier is a string of alphanumeric characters that begins with an alphabetic character or an underscore character that are used to represent various programming elements such as variables, functions, arrays, structures, unions and so on. Actually, an identifier is a user-defined word.

### Keywords
	A built-in command or word in the programming language. Keywords can be commands or parameters. Every programming language has a set of keywords that cannot be used as variable names. Keywords are sometimes called reserved names.

### Types
	 A primitive or data structure that functions the same as another.

# Python Programming Language
	
	Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming.

## Python Topics

[Python Flashcards](https://quizlet.com/jameshambley1)<sub>[[4]](#References)</sub> created by user jamesshambley1 on Quizlet

### Primitive Variables
#### Int
	Int in python is arbitrarily long. Limited by the machine that is running the code.
#### Float
	Which can be written in scientific notation
### Complex
	1+j is 1+i in math.
### String literals
	'str'
	"str"
	'''str'''
### Boolean
	True and False
## Truthy and Falsey Values
	All values are inherently considered true or false.
### Falsey values:
* None
* False
* 0, 0.0, 0j, Decimal(0), Fraction(0,1)
* '', ", ''''''
* (), [], {}, set(), range(0)

### Truthy values:
	Almost everything else...

## Lambda (Programming) - Wikipedia

	In computer programming, an anonymous function (function literal, lambda abstraction, or lambda expression) is a function definition that is not bound to an identifier. Anonymous functions are often arguments being passed to higher-order functions, or used for constructing the result of a higher-order function that needs to return a function.[1] If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function. Anonymous functions are ubiquitous in functional programming languages and other languages with first-class functions, where they fulfill the same role for the function type as literals do for other data types.

	Anonymous functions originate in the work of Alonzo Church in his invention of the lambda calculus, in which all functions are anonymous, in 1936, before electronic computers.[2] In several programming languages, anonymous functions are introduced using the keyword lambda, and anonymous functions are often referred to as lambdas or lambda abstractions. Anonymous functions have been a feature of programming languages since Lisp in 1958, and a growing number of modern programming languages support anonymous functions.

## Reflection

	To display all values in a library using reflection.
	1. Import the library.
	2. print(dir(library))

## Slicing
	# Code
	a = [1, 2, 3, 4, 5, 6, 7, 8]
	a[1:4]

Output: [2, 3, 4]

	# Code
	a[1:4:2]

Output: [2, 4]

	a[::-1]

Output: [8, 7, 6, 5, 4, 3, 2, 1]

	t = (2, 5, 7, 9, 10, 11, 12)
	t[2:4]

Output: (7, 9)
	
	a = [1, 2, 3, 4, 5]
	sliceObj = slice(1, 3)
	a[sliceObj]

Output: [2, 3]

	colors = ['red', 'green', 'blue', 'yellow'， 'white', 'black']
	colors[-1]

Output: 'black'

	colors[-2]
	
Output: 'white'

	colors[-6]

Output: 'red'

	nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
	some_nums = nums[2:7]
	some_nums

Output: [30, 40, 50, 60, 70]

	nums[0:4]

Output: [10, 20, 30, 40]

	nums[:5]

Output: [10, 20, 30, 40, 50]

	nums[-3:]

Output: [70, 80, 90]

	nums[1:-1]

Output: [20, 30, 40, 50, 60, 70, 80]
	
	nums[-3:8]

Output: [70, 80]

	nums[-5:-1]

Output: [50, 60, 70, 80]

	nums[:-2]

Output: [10, 20, 30, 40, 50, 60, 70]

	nums[::2]

Output: [10, 30, 50, 70, 90]

	nums[1::2]
	
Output: [20, 40, 60, 80]

## Reading and Writing Files Input/Ouput

### Open a file

    open(filename, mode, encoding)
    filename - String containing the path to the file including the name
    mode - “r” read, “w” write, “a” append, “x” exclusive file creation (if the file exists this fails), “+” open a file for updating (reading and writing)
    encoding - “t” opens in text mode, “b” opens in binary mode

#### Example One

    file_object = open("gitnotes.txt", "r")
    text = file_object.read()

Output: The entire files contents…

#### Example Two

    A simple way to open a file line by line is the following:
    
    for line in f = open("demofile.txt", "r").readline()
    print(line + ‘\n’)
    f.close()

Don’t forget to close the file!

Output:\
First line\
Second line\
Third line\
etc...

#### Example Three

A more elegant way to open a file so you don’t have to worry about closing the file is the following:

    filepath = 'somepath/somefile.txt’'
    with open(filepath) as fp:
        line = fp.readline()
    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1

Output:\
Line 1: First Line\
Line 2: Second Line\
Line 3: Third Line\
etc...
              
This will close the file at the most reasonable time within your code, and it is standard practice in Python. (I am not sure what PyLint does to this syntax).

Remember to apply the appropriate mode and encoding whenever opening a file no matter what method you choose.

### Underscore Character

Example: _function()

Indicates to the programmer that a function is used by the class alone, and not by anything existing outside of the class.

This is similar to a private function.

### Python Operators

Python operators are stored in a recursive tree containing a key, level, and operation function. The functions are stored in a dictionary, which allows the system O(1) look up time. The recursive tree handles operations using the following telescoping function:

T(n) = 2T(n/2) + n2

### Abstract Functions/Methods



### Abstract Class



### Dictionary



### Extensibility



### Scalability



### Tuples



### Logging

Critical - Application is crashing

	logging.critical('bad news')

Error - Error was raised and handled

	logging.error('hopefully you can recover')

Warning - Something might break

	logging.warning('these are dangerous... ask NASA')

Info - Flow of an application

	logging.info('log input output')

Debug - All of your print statements that you use to figure out what is happening.

	logging.debug('learning and testing')

Note: Trace does not exist in Python.\
Trace - Log all information that enters or exits a function.


### Scope

Built-in

Global

Local

Non-Local

### Testing

Testing is the most important part of development. Comprehensive tests can ensure that your system works under any and all circumstances. It will reveal bugs before they become problems.

#### Functional Testing

Testing the functionality of code.

#### Unit Testing
Testing the smallest unit of code.
Usually:

* Functions
* Methods
* Code Blocks

#### Integration Testing



#### End to End Testing

Testing a part of the code from the standpoint of the user to determine whether a feature works.\

Automation Notes:

* In web development you can use Selenium to simulate a user and perform a use case for your project and see that it works.
* In Python 

#### Non-Functional Testing

Testing things that aren't a part of the functionality of the application.

* Stress Testing
* User Acceptance Testing
* Compliance Testing
* Load Testing
* Performance Testing

# Python Certification
## Exam Objectives

### The test candidate should demonstrate the sufficient knowledge of the following concepts:

1. The fundamentals of computer programming, i.e. how the computer works, how the program is executed, how the programming language is defined and constructed, what the difference is between compilation and interpretation, what Python is, how it is positioned among other programming languages, and what distinguishes the different versions of Python;

2. The basic methods of formatting and outputting data offered by Python, together with the primary kinds of data and numerical operators, their mutual relations and bindings; the concept of variables and variable naming conventions; the assignment operator, the rules governing the building of expressions; the inputting and converting of data;

3. Boolean values to compare difference values and control the execution paths using the if and if-else instructions; the utilization of loops (while and for) and how to control their behavior using the break and continue instructions; the difference between logical and bitwise operations; the concept of lists and list processing, including the iteration provided by the for loop, and slicing; the idea of multi-dimensional arrays;

4. The defining and using of functions – their rationale, purpose, conventions, and traps; the concept of passing arguments in different ways and setting their default values, along with the mechanisms of returning the function’s results; name scope issues; new data aggregates: tuples and dictionaries, and their role in data processing;

5. Python modules: their rationale, function, how to import them in different ways, and present the content of some standard modules provided by Python; the way in which modules are coupled together to make packages; the concept of an exception and Python’s implementation of exceptions, including the try-except instruction, with its applications, and the raise instruction; strings and their specific methods, together with their similarities and differences compared to lists;

6. The fundamentals of OOP (Object Oriented Programming) and the way they are adopted in Python, showing the difference between OOP and the classical, procedural approach; the standard objective features: inheritance, abstraction, encapsulation, and polymorphism, along with Python-specific issues like instance vs. class variables, and Python’s implementation of inheritance; objective nature of exceptions; Python’s generators (the yield instruction) and closures (the lambda keyword); the means Python developers can use to process (create, read, and write) files.


# References

[1.](https://edube.org/study/pe1) <cite>Python Essentials 1" Python Essentials - Part 1. https://edube.org/study/pe1. Accessed 31 May 2020.</cite>

[2.](https://www.salto-youth.net/tools/otlas-partner-finding/download/4896/annexBabelBooks.pdf) <cite>Sundberg, Minna. SALTO-
YOUTH-PARTNER - Otlas - The Partner-Finding Tool. https://www.salto-\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;youth.net/tools/otlas-partner-finding/. Accessed 31 May 2020.</cite>

[3.](https://en.wikipedia.org/wiki/X86_instruction_listings) <cite>“X86 Instruction Listings.” Wikipedia, 24 May 2020. Wikipedia,\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://en.wikipedia.org/w/index.php?title=X86_instruction_listings&oldid=958566320.</cite>


[4.](https://quizlet.com/279308046/flashcards)<cite>“Python Flashcards.” Quizlet. quizlet.com, https://quizlet.com/291523268/python-flash-cards/. Accessed 31 May\ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2020.
</cite>

[5.](https://wordpress.com/support/markdown-quick-reference/) “Markdown Quick Reference Cheat Sheet.” Support, 19 Nov. 2013. wordpress.com,\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://wordpress.com/support/markdown-quick-reference/.

# MongoDB

## MongoDB Resources

MongoDB provides three resources to handle database management.

* mongoDB Compass Desktop Application
* PyMongo API Development Library
* mongoDB Atlas HTML5 Web Application
  * Database as a service
  * Allows easy setup and database management
  * Free-Enterprise Service Tiers allow for easy scaling to industry demands
  * 

## Tools Overview

