Files are named locations on disk to store related information. They are used to permanently
store data in a non-volatile memory (e.g. hard disk).
In Python, files are treated in two modes as text or binary. The file may be in the text or binary
format, and each line of a file is ended with the special character.
Hence, in Python, a file operation takes place in the following order:
Open a file
Read or write (perform operation)
Close the file
1. Working of open() function
We use open () function in Python to open a file in read or write mode. As explained above,
open ( ) will return a file object. To return a file object we use open() function along with two
arguments, that accepts file name and the mode, whether to read or write. So, the syntax
being: open(filename, mode). There are three kinds of mode, that Python provides and how
files can be opened:
• “ r “, for reading.
• “ w “, for writing.
• “ a “, for appending.
• “ r+ “, for both reading and writing

2. Working of read() mode
There is more than one way to read a file in Python. If you need to extract a string that contains
all characters in the file then we can use file.read(). The full code would work like this:
Code:
file = open("file.text", "r") # Python code to illustrate read() mode
print file.read()

3. Creating a new file
The new file can be created by using one of the following access modes with the function
open().
x: it creates a new file with the specified name. It causes an error a file exists with the same
name.
a: It creates a new file with the specified name if no such file exists. It appends the content to
the file if the file already exists with the specified name.
w: It creates a new file with the specified name if no such file exists. It overwrites the existing file.

4. Creating a file using write() mode
Code:
file = open('file.txt','w') # Python code to create a file 
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
