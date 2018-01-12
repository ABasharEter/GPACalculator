#GPA Calculater
# Copyright (c) 2018 Ahmad Bashar Eter

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class SyrianGPAConverter():
    def convert(self,mark):
		#Graduate marks convert method from: https://www.foreigncredits.com/resources/Grade-Conversion/
        mark = int(mark)
        if(mark>=95):
            return 'A+'
        if(mark>=85):
            return 'A'
        if(mark>=75):
            return 'B+'
        if(mark>=65):
            return 'B'
        if(mark>=60):
            return 'C'
        return 'F'
		
if __name__=='__main__':
	#This piece of code is for testing. You can use  it as a usage example.
    #Here I have a cvs file with name 'syrian_marks.csv' the workign directory of this script
    #In this file I have the subject name in the first column, 
    # the grade/mark in the second column and the credit hour for the subject in the third column.
	
	from GPACalculator import GPACalculator
    calc = GPACalculator('syrian_marks.csv',1,2)
    print(calc.CalculateGPA(SyrianGPAConverter()))

