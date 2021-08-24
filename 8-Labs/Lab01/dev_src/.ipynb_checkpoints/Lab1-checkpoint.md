**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Laboratory 1](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab0/Lab1_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___


# <font color=darkred>Laboratory 1: A Notebook Like No Other!</font>



![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png) <br>


### Welcome to your first <span style='background:yellow'>Jupyter Notebook</span>. This is a medium that we will be using throughout the semester. 
___

## Why is this called a notebook?
### Because you can write stuff in it!

## Is that it?
### Nope! you can **write** and **run** <span style='background:yellow'>CODE</span> in this notebook! Plus a bunch of other cool stuff such as making graphs, running tests and simulations, adding images, and prepare documents (such as this one!). 



## <font color=purple>The Environment - Let's have a look around this window!</font>

![](https://i.pinimg.com/originals/db/db/ba/dbdbbad5798bfc3ff27a499dc5ca2b30.gif) <br>
<font color=gray>*Rami Malek in Mr. Robot*</font>

 
 
- The tabs:
    - File
    - Edit
    - View
    - Insert
    - Cell
    - Kernel
    
- The Icons:
    - Save
    - Insert Cell Below
    - Cut
    - Copy
    - Paste Cells Below
    - Move Up
    - Move Down
    - Run
    - Intruppt Kernel
    - Restart Kernel
    - Cell Type Selector (Dropdown list)

___

### The notebook consists of a sequence of cells. A cell is a multiline text input field, and its contents can be executed by using Shift-Enter, or by clicking Run in the menu bar. The execution behavior of a cell is determined by the cell’s type. 
### There are three types of cells: code cells, markdown cells, and raw cells. Every cell starts off being a code cell, but its type can be changed by using a drop-down on the toolbar (which will be “Code”, initially).
    


## Code Cells:

### A code cell allows you to edit and write new code, with full syntax highlighting and tab completion. The programming language you use depends on the kernel. What we will use for this course and the default kernel IPython runs, is Python code.
### When a code cell is executed, code that it contains is sent to the kernel associated with the notebook. The results that are returned from this computation are then displayed in the notebook as the cell’s output. The output is not limited to text, with many other possible forms of output are also possible, including matplotlib figures and HTML tables. This is known as IPython’s rich display capability.

## Markdown Cells:

### You can document the computational process in a literate way, alternating descriptive text with code, using rich text. In IPython this is accomplished by marking up text with the Markdown language. The corresponding cells are called Markdown cells. The Markdown language provides a simple way to perform this text markup, that is, to specify which parts of the text should be emphasized (italics), bold, form lists, etc. In fact, markdown cells allow a variety of cool modifications to be applied:


### If you want to provide structure for your document, you can use markdown headings. Markdown headings consist of 1 to 5 hash # signs followed by a space and the title of your section. (The markdown heading will be converted to a clickable link for a section of the notebook. It is also used as a hint when exporting to other document formats, like PDF.) Here is how it looks:

# # title
## ## major headings
### ### subheadings
#### #### 4th level subheadings
##### ##### 5th level subheadings


### These codes are also quite useful: 
- Use triple " * " before and after a word (without spacing) to make the word bold and italic <br>
B&I: ***string*** <br>

- __ or ** before and after a word (without spacing) to make the word bold <br>
Bold: __string__ or **string** <br>

- _ or * before and after a word (without spacing to make the word italic <br>
Italic: _string_ or *string* <br>

- Double ~ before and after a word (without spacing to make the word scratched <br>
Scratched: ~~string~~ <br>

- For line breaks use "br" in the middle of <> <br>

- For colors use this code: <font color=blue>Text</font> <br>
<font color=red>Text</font> <br>
<font color=orange>Text</font> <br>

- For indented quoting, use a greater than sign (>) and then a space, then type the text. The text is indented and has a gray horizontal line to the left of it until the next carriage return.
> here is an example of how it works!

- For bullets, use the dash sign (- ) with a space after it, or a space, a dash, and a space ( - ), to create a circular bullet. To create a sub bullet, use a tab followed a dash and a space. You can also use an asterisk instead of a dash, and it works the same.

- For numbered lists, start with 1. followed by a space, then it starts numbering for you. Start each line with some number and a period, then a space. Tab to indent to get subnumbering. <br>

    1. first
    2. second
    3. third
    4. ...

- For horizontal lines: Use three asterisks: ***
***
***
***

- For graphics, you can attach image files directly to a notebook only in Markdown cells. Drag and drop your images to the Mardown cell to attach it to the notebook.


![Anaconda.jpg](attachment:Anaconda.jpg)

- You can also use images from online sources be using this format:

![](put the image address here.image format) <br>


## Raw Cells:

### Raw cells provide a place in which you can write output directly. Raw cells are not evaluated by the notebook. 

## <font color=purple>Let's meet world's most popular python!</font>

![](https://media2.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif) <br>

### What is python?
> "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace." - Wikipedia @ https://en.wikipedia.org/wiki/Python_(programming_language)

### How to have access to it?

#### There are plenty of ways, from online compilers to our beloved Jupyter Notebook on your local machines. Here are a few examples of online compilers:
   a. https://www.programiz.com/python-programming/online-compiler/

   b. https://www.onlinegdb.com/online_python_compiler
   
   c. https://www.w3schools.com/python/python_compiler.asp
   
   d. https://repl.it/languages/python3

#### We can do the exact same thing in this notebook. But we need a CODE cell. 


```python
print("Hello World")
```

    Hello World


#### This is the classic "first program" of many languages! The script input is quite simple, we instruct the computer to print the literal string "hello world" to standard input/output device which is the console. Let's change it and see what happens:


```python
print("This is my first notebook!")
```

    This is my first notebook!


### How to save a notebook?


- __As a notebook file (.ipynb):__ <br>
    Go to File > Download As > Notebook (.ipynb)
    
- __As an HTML file (.html):__ <br>
    Go to File > Download As > HTML (.html)
    
- __As a Pdf (.pdf):__ <br>
    Go to File > Download As > PDF via LaTex (.pdf)
    or
    Save it as an HTML file and then convert that to a pdf via a website such as https://html2pdf.com/ 
    
*Unless stated otherwise, we want you to submit your weekly lab assignments in PDF and your exam and project deliverables in both PDF and .ipynb formats.*

![](https://i.pinimg.com/originals/1d/ae/c2/1daec2478020d74065a95359b6223283.gif) <br>
___

![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>

*This notebook was inspired by several blogposts including:* 

- __"Markdown for Jupyter notebooks cheatsheet"__ by __Inge Halilovic__ available at *https://medium.com/@ingeh/markdown-for-jupyter-notebooks-cheatsheet-386c05aeebed <br>
- __"Jupyter Notebook: An Introduction"__ by __Mike Driscoll__ available at *https://realpython.com/jupyter-notebook-introduction/ <br>


*Here are some great reads on this topic:* 
- __"Jupyter Notebook Tutorial: The Definitive Guide"__ by __Karlijn Willems__ available at *https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook <br>
- __"Introduction to Jupyter Notebooks"__ by __Quinn Dombrowski, Tassie Gniady, and David Kloster__ available at *https://programminghistorian.org/en/lessons/jupyter-notebooks <br>
- __"12 Things to know about Jupyter Notebook Markdown"__ by __Dayal Chand Aichara__ available at *https://medium.com/game-of-data/12-things-to-know-about-jupyter-notebook-markdown-3f6cef811707 <br>


*Here are some great videos on these topics:* 
- __"Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough"__ by __Corey Schafer__ available at *https://www.youtube.com/watch?v=HW29067qVWk <br>
- __"Quick introduction to Jupyter Notebook"__ by __Michael Fudge__ available at *https://www.youtube.com/watch?v=jZ952vChhuI <br>
- __"What is Jupyter Notebook?"__ by __codebasics__ available at *https://www.youtube.com/watch?v=q_BzsPxwLOE <br>

![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>


___
## Exercise: Let's see who you are! <br>




### Similar to the example, use a code cell and print a paragraph about you. You can introduce yourselves and write about interesting things to and about you!  




```python

```

![](https://i.pinimg.com/originals/84/44/f5/8444f53fa329b94ddd674ffb2e192fe8.png)
