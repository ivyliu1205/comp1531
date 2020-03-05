# Lab 02 ( Due Week 02, Sunday, 11:59 pm )
### 12 marks ( + 4 marks bonus )
# Aim
Become familiar with:
 - Python data structures - lists, dictionaries and tuples    
 - Writing functions
 - Built-in  functions in Python

# Lab instructions

In this lab, you have been given a number of exercises to help you become familiar with the Python programming language.  Some of these exercises are optional exercises, which carry a bonus mark.  

This lab must be completed and solution must be uploaded to GitHub by Sunday, 11:59 pm, week 02. Tutors will check the time-stamp, when the lab is marked in week 03 lab session. Tasks in this lab must be completed individually.

## Setup Instructions: 
This lab uses the  `pytest`  package ( which you will learn about later on ) and some plugins to test the programming exercises.

You will need to install these packages in order to run the tests. To do this, you will use a  *virtual environment* which is essentially a nice way to separate python modules you only need for specific projects.

Please read  [How to setup a Virtual Environment](https://webcms3.cse.unsw.edu.au/COMP1531/18s2/resources/19969)  to get help set up and give some more information about virtual environments.

The below commands will set up your  _virtual environment._  Please refer to

```bash
virtualenv --python=/usr/bin/python3 venv
. venv/bin/activate
pip3 install -r requirements.txt 
```
## Tasks:  

Complete the following exercises and demo them to your tutor to get marked. The process to import the starter code is the same as last week. Go to  [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs](https://cgi.cse.unsw.edu.au/~cs1531/18s1/github/run.cgi/labs), select  **lab02**  and click  **Import**.

*Students who have still not been acquired an Education pack can download the starter code from webcms3*

**Exercise 1:**  
Complete each of the following lines with one line of Python code **(3 Marks)**

Given a list of numbers (e.g., numbers = [2, 4, -23, 2, 95, 21]), return:

 - reverse of the list
 - largest number
 - minimum number
 - sum of the numbers
 - numbers sorted in descending order
 - average of the numbers
The starter code for this exercise is in the  `numbers_list.py`  file. 

**Exercise 2:**  
* Write a Python program which given a list of numbers finds (and returns) the second smallest number in the list   **(2 Marks)**

 * ***Bonus Extension:***  Write a Python program which given a list of numbers finds (and returns) the kth smallest number in the list   **(2 Marks)**
 
**Exercise 3:**  
* Given a paragraph of text, count the number of times each character occurs in the text, and print each character and its count (in any order).  **(2 Marks)**
* Now, implement the above program so that it works in a case-insensitive manner with the alphabets **(2 Marks)**
* ***Bonus Extension:*** Now, print the list in the descending order of the count (case-insensitive) **(2 Marks)**
The starter code for this exercise is in the  `count.py`  file. 


_Do:_ count_char_ordered('Hello,World!')  
_Output:_  
l 3  
o 2  
h 1  
e 1  
w 1  
r 1  
d 1  
! 1  

**Exercise 4:**  Fibonacci extension - Print the nth number in the fibonacci series given the index n  **(3 Marks)**
 
Last week, you were asked to complete a Python exercise that produced a list of Fibonacci numbers of size  _n_, where n is provided. In this exercise, you are required to write a program that reads a number n and print the nth number in the Fibonacci series. The program must make use of a  **recursive function**  to implement this task. The function should return the number instead of printing it. Hence, reading the user input and printing the number should be handled outside the function.

The Fibonacci series in this program should start from one. The first 10 numbers are shown below:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55….

The number at index 1 is 1 and the number at index 3 is 2. So, the number at index 10 would be 55.

_Input:_  5  
_Output:_  5

The starter code for this exercise is in the  `fibonacci.py`  file. Please complete your solution within this file. Do not change the function name because it is required during the tests.

## Testing

Please implement all of the function skeletons provided in the starter code.  Once completed, you can now run the tests by simply running

```bash
pytest
```
