# GPACalculater
A small piece of software to calculate your 4.0 GPA from US GPA or Syrian GPA.  
# GPA Input method 
You can use this code to calculate your 4.0 GPA from a CSV file which contains your grades and your credit hour pre subject.
The only requirement is that you have two columns in the CSV file on for grades and the other for credit hour and then each row contains a subject data.
* Example1 CSV file of Syrian grades:
| Physics     | 80 | 2 |
| Mathematics | 95 | 4 |
| Programming | 60 | 3 |
In this table we have the first column is subject name (optional) the second column the grade the third column credit hour for this subject.
* Example1 CSV file of US grades:
| Physics     | B+ | 2 |
| Mathematics | A+ | 4 |
| Programming | D- | 3 |

# Usage 
* Convert US Grad to 4.0 GPA  
Here I have a cvs file with name 'us_marks.csv' the working directory of this script.    
In this file I have the subject name in the first column,
the grade/mark in the second column and the credit hour for the subject in the third column.
```python
from GPACalculator import GPACalculator
from USGPAConverter import USGPAConverter
calc = GPACalculator('us_marks.csv',1,2)
print(calc.CalculateGPA(USGPAConverter()))
```
* Convert Syrian Grad to 4.0 GPA  
Here I have a cvs file with name 'syrian_marks.csv' the working directory of this script.  
In this file I have the subject name in the first column, 
the grade/mark in the second column and the credit hour for the subject in the third column.
```python
from GPACalculator import GPACalculator
from SyrianGPAConverter import SyrianGPAConverter
calc = GPACalculator('syrian_marks.csv',1,2)
print(calc.CalculateGPA(SyrianGPAConverter()))
```
# Notes
This code is tested on windows machine with python 3.6
# License

Copyright (c) 2018 Ahmad Bashar Eter  

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
