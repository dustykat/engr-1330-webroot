**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Lab5](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab5/Lab5_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 5: Working with Files </font>


```python
# Preamble script block to identify host, user, and kernel
import sys
! hostname
! whoami
print(sys.executable)
print(sys.version)
print(sys.version_info)
```

    ip-172-26-4-2
    sensei
    /opt/jupyterhub/bin/python3
    3.8.5 (default, May 27 2021, 13:30:53) 
    [GCC 9.3.0]
    sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)


## Full name: 
## R#: 
## Title of the notebook:
## Date:
___

![](https://thumbs.gfycat.com/PaleGargantuanCooter-size_restricted.gif) <br>


### <font color=purple>Background</font>

A computer file is a computer resource for recording data discretely (not in the secretive context, but specifically somewhere on a piece of hardware) in a computer storage device. Just as words can be written to paper, so can information be written to a computer file. Files can be edited and transferred through the internet on that particular computer system.

There are different types of computer files, designed for different purposes. A file may be designed to store a picture, a written message, a video, a computer program, or a wide variety of other kinds of data. Some types of files can store several types of information at once.

By using computer programs, a person can open, read, change, save, and close a computer file. Computer files may be reopened, modified, and copied an arbitrary number of times.

Typically, files are organised in a file system, which keeps track of where the files are located on disk and enables user access. 

### <font color=purple>File system</font>

In computing, a file system or filesystem, controls how data is stored and retrieved. 
Without a file system, data placed in a storage medium would be one large body of data with no way to tell where one piece of data stops and the next begins. 
By separating the data into pieces and giving each piece a name, the data is isolated and identified. 
Taking its name from the way paper-based data management system is named, each group of data is called a “file”. 
The structure and logic rules used to manage the groups of data and their names is called a “file system”.

### <font color=purple>Path</font>

A path, the general form of the name of a file or directory, specifies a unique location in a file system. A path points to a file system location by following the directory tree hierarchy expressed in a string of characters in which path components, separated by a delimiting character, represent each directory. The delimiting character is most commonly the slash (”/”), the backslash character (”\”), or colon (”:”), though some operating systems may use a different delimiter.
Paths are used extensively in computer science to represent the directory/file relationships common in modern operating systems, and are essential in the construction of Uniform Resource Locators (URLs). Resources can be represented by either absolute or relative paths.
As an example consider the following two files:

1. /Users/theodore/MyGit/@atomickitty/hurri-sensors/.git/Guest.conf 
2. /etc/apache2/users/Guest.conf

They both have the same file name, but are located on different paths. 
Failure to provide the path when addressing the file can be a problem. 
Another way to interpret is that the two unique files actually have different names, and only part of those names is common (Guest.conf)
The two names above (including the path) are called fully qualified filenames (or absolute names), a relative path (usually relative to the file or program of interest depends on where in the directory structure the file lives. 
If we are currently in the .git directory (the first file) the path to the file is just the filename.

We have experienced path issues with dependencies on .png files - in general your JupyterLab notebooks on CoCalc can only look at the local directory which is why we have to copy files into the directory for things to work.

### <font color=purple>File Types</font>

1. Text Files. Text files are regular files that contain information readable by the user. This information is stored in ASCII. You can display and print these files. The lines of a text file must not contain NULL characters, and none can exceed a prescribed (by architecture) length, including the new-line character.  The term text file does not prevent the inclusion of control or other nonprintable characters (other than NUL). Therefore, standard utilities that list text files as inputs or outputs are either able to process the special characters gracefully or they explicitly describe their limitations within their individual sections.

2. Binary Files. Binary files are regular files that contain information readable by the computer. Binary files may be executable files that instruct the system to accomplish a job. Commands and programs are stored in executable, binary files. Special compiling programs translate ASCII text into binary code.  The only difference between text and binary files is that text files have lines of less than some length, with no NULL characters, each terminated by a new-line character.

3. Directory Files. Directory files contain information the system needs to access all types of files, but they do not contain the actual file data. As a result, directories occupy less space than a regular file and give the file system structure flexibility and depth. Each directory entry represents either a file or a subdirectory. Each entry contains the name of the file and the file's index node reference number (i-node). The i-node points to the unique index node assigned to the file. The i-node describes the location of the data associated with the file. Directories are created and controlled by a separate set of commands.

### <font color=purple>File Manipulation</font>

For this laboratory we will learn just a handfull of file manipulations which are quite useful. Files can be "created","read","updated", or "deleted" (CRUD). 

___
### Example: Create a file, write to it. 

Below is an example of creating a file that does not yet exist.
The script is a bit pendandic on purpose.

First will use some system commands to view the contents of the local directory


```python
import sys
! del  myfirstfile.txt  # delete file if it exists, Use rm -f on Mac 
%pwd  # list name of working directory, note it includes path, so it is an absolute path
```




    'C:\\Users\\Farha'




```python
# create file example
externalfile = open("myfirstfile.txt",'w') # create connection to file, set to write (w), file does not need to exist
mymessage = 'message in a bottle' #some object to write, in this case a string
externalfile.write(mymessage)# write the contents of mymessage to the file
externalfile.close() # close the file connection
```

At this point our new file should exist, lets list the directory and see if that is so

Sure enough, its there, we will use a `bash` command `cat` to look at the contents of the file.


```python
! type myfirstfile.txt
```

    message in a bottle


Thats about it, use of system commands, of course depends on the system, the examples above should work OK on CoCalc or a Macintosh; on Winderz the shell commands are a little different.  If you have the linux subsystem installed then these should work as is.

___
### Example: Read from an existing file. 

We will continue using the file we just made, and read from it the example is below


```python
# read file example
externalfile = open("myfirstfile.txt",'r') # create connection to file, set to read (r), file must exist
silly_string = externalfile.read() # read the contents
externalfile.close() # close the file connection
print(silly_string)
```

    message in a bottle


___
#### Example: Update a file.

This example continues with our same file, but we will now add contents without destroying existing contents. The keyword is `append`


```python
externalfile = open("myfirstfile.txt",'a') # create connection to file, set to append (a), file does not need to exist
externalfile.write('\n') # adds a newline character
what_to_add = 'I love rock-and-roll, put another dime in the jukebox baby ... \n' 
externalfile.write(what_to_add) # add a string including the linefeed
what_to_add = '... the waiting is the hardest part \n' 
externalfile.write(what_to_add) # add a string including the linefeed
mylist = [1,2,3,4,5] # a list of numbers
what_to_add = ','.join(map(repr, mylist)) + "\n" # one way to write the list
externalfile.write(what_to_add)
what_to_add = ','.join(map(repr, mylist[0:len(mylist)])) + "\n" # another way to write the list
externalfile.write(what_to_add)
externalfile.close()
```

As before we can examine the contents using a shell command sent from the notebook.


```python
! type myfirstfile.txt
```

    message in a bottle
    I love rock-and-roll, put another dime in the jukebox baby ... 
    ... the waiting is the hardest part 
    1,2,3,4,5
    1,2,3,4,5


___
A little discussion on the part where we wrote numbers

>    what_to_add = ','.join(map(repr, mylist[0:len(mylist)])) + "\n"

Here are descriptions of the two functions `map` and `repr`

`map(function, iterable, ...)` Apply `function` to every item of iterable and return a list of the results. 
If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. 
If one iterable is shorter than another it is assumed to be extended with None items. 
If function is None, the identity function is assumed; if there are multiple arguments, `map()` returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). 
The iterable arguments may be a sequence or any iterable object; the result is always a list.

`repr(object)` Return a string containing a printable representation of an object. 
This is the same value yielded by conversions (reverse quotes). 
It is sometimes useful to be able to access this operation as an ordinary function. 
For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to `eval()`, otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. 
A class can control what this function returns for its instances by defining a `repr()` method.

What they do in this script is important. 
The statement:

    what_to_add = ’,’.join(map(repr, mylist[0:len(mylist)])) + "\n"
    
is building a string that will be comprised of elements of mylist[0:len(mylist)].
The `repr()` function gets these elements as they are represented in the computer, the delimiter a comma is added using the join method in Python, and because everything is now a string the

    ... + "\n"
    
puts a linefeed character at the end of the string so the output will start a new line the next time something is written.

___
#### Example: Delete a file

Delete can be done by a system call as we did above to clear the local directory

In a JupyterLab notebook, we can either use

    import sys
    ! del  myfirstfile.txt  # delete file if it exists, Use rm -f on Mac

or

    import os
    os.remove("myfirstfile.txt")

they both have same effect, both equally dangerous to your filesystem.


Learn more about CRUD with text files at https://www.guru99.com/reading-and-writing-files-in-python.html

Learn more about file delete at https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/
    


```python
# import os
file2kill = "myfirstfile.txt"
try:
    os.remove(file2kill) # file must exist or will generate an exception
except:
    pass # example of using pass to improve readability
print(file2kill, " missing or deleted !")
```

    myfirstfile.txt  missing or deleted !


___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>


*Here are some great reads on this topic:* 
- __"Python Classes and Objects"__ available at *https://www.geeksforgeeks.org/python-classes-and-objects/<br>
- __"Object-Oriented Programming (OOP) in Python 3"__ by __David Amos__ available at *https://realpython.com/python3-object-oriented-programming/ <br>
- __"Python File Operations – Read and Write to files with Python"__ available at *https://www.journaldev.com/14408/python-read-file-open-write-delete-copy <br>

*Here are some great videos on these topics:* 
- __"Python OOP Tutorial 1: Classes and Instances"__ by __Corey Schafer__ available at *https://www.youtube.com/watch?v=ZDa-Z5JzLYM <br>
- __"Python Object Oriented Programming (OOP) - For Beginners"__ by __Tech With Tim__ available at *https://www.youtube.com/watch?v=JeznW_7DlB0 <br>
- __"Python Classes and Objects || Python Tutorial || Learn Python Programming"__ by __Socratica__ available at *https://www.youtube.com/watch?v=apACNr7DC_s <br>
- __"Python Tutorial: File Objects - Reading and Writing to Files"__ by __Corey Schafer__ available at *https://www.youtube.com/watch?v=Uh2ebFW8OYM <br>

___
![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>


## Exercise: Your Favorite Quotation! <br>

- create a text file, name it __"MyFavoriteQuotation"__.
- Write __your favorite quotation__ in the file.
- Read the file.
- Add this string to it in a new line : "And that's something I wish I had said..."
- Show the final outcome.


```python
# create the "My Favorite Quotation" file:
externalfile = open("MyFavoriteQuotation.txt",'w')         # create connection to file, set to write (w)
myquotation = 'The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness. For he is truly his brother’s keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know my name is the Lord when I lay my vengeance upon you.' #My choice: quotation from Pulp Fiction
externalfile.write(myquotation)# write the contents of mymessage to the file
externalfile.close() # close the file connection
#Let's read the file
#! type MyFavoriteQuotation.txt 
# Let's add the string
externalfile = open("MyFavoriteQuotation.txt",'a')  #create connection to file, set to append (a)
externalfile.write('\n') # adds a newline character
what_to_add = "And that's something I wish I had said ... \n"
externalfile.write(what_to_add)
externalfile.close()
#Let's read the file one last time
! type MyFavoriteQuotation.txt 
```

    The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness. For he is truly his brother’s keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know my name is the Lord when I lay my vengeance upon you.
    And that's something I wish I had said ... 


![](https://quotefancy.com/media/wallpaper/3840x2160/6361186-George-Bernard-Shaw-Quote-Life-isn-t-about-finding-yourself-Life.jpg)


```python

```
