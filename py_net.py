"""
Python use .dll, and test on .NET Framework dll, System.dll
1. sys.path.append() :append  .dll path
2. clr.AddReference :add .dll lib
3. import: heer we test import IO from System

Example:

import sys
sys.path.append("C:\Path\to\your\assemblies")

clr.AddReference('MyAssembly')
from MyAssembly import MyClass

MyClass.does_something()

This assumes that in the C:\Path\to\your\assemblies folder you have a MyAssembly.dll file.

So the 'trick' is that you have to add your assemblies folder to the sys.path before clr.AddReference.
"""
import sys, clr
sys.path.append(r'C:\Users\koala\Documents\Visual Studio 2017\Projects\Gofer_net_lib\Gofer_net_lib\bin\Debug\netstandard1.4')
clr.AddReference(r'Gofer_net_lib')
clr.AddReference(r'Interop.Microsoft.Office.Interop.Excel')
from Gofer_net_lib import test
import Microsoft.Office.Interop.Excel as Excel
calc=test()
res=calc.add(5,8)
print(res)
sys.path.append(r'C:\Program Files (x86)\Reference Assemblies\Microsoft'
                r'\Framework\.NETFramework\v4.0\Profile\Client')
clr.AddReference(r'System')
from System import IO
path=r'C:\Users\koala\Documents\Visual Studio 2013\Projects\jlxl\jlxl\bin\Debug\datafile'
files=IO.Directory.GetFiles(path, "*.csv") # this is like in C#
for f in files:
    print(f)