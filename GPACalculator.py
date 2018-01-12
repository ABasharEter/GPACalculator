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

import csv
class GPACalculator():
    def __init__(self,marks_csv_filepath=None,marks_column=0,credit_hours_column=1):
        self.marks_csv_filepath = marks_csv_filepath
        self.marks_column = marks_column
        self.credit_hours_column = credit_hours_column
        self.__us4grade={'A+':4,'A':4,'A-':3.7,'B+':3.3,'B':3,'B-':2.7,'C+':2.3,'C':2,'C-':1.7,'D+':1.3,'D':1,'D-':0.7,'F':0}
        
    def us_to_4_grade(self,mark):
        return self.__us4grade[mark]

    def CalculateGPA(self,to_us_coverter):
        csvdata = []
        with open(self.marks_csv_filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            csvdata = list(reader)
        totw = 0.0
        GPA = 0.0
        for l in csvdata:
            m = l[self.marks_column]
            w = int(l[self.credit_hours_column])
            m = to_us_coverter.convert(m)
            m = self.us_to_4_grade(m)
            totw += w
            GPA += m*w
        GPA /=totw
        return GPA