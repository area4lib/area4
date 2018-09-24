# area4
Dividers in Python, the easy way!  Four different types.  [(As seen on PyPI!)](https://pypi.org/project/area4)  
*Version: 1.0.2*  
[![Known Vulnerabilities](https://snyk.io/test/github/RDIL/area4/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/RDIL/area4?targetFile=requirements.txt) ![](https://img.shields.io/badge/license-MIT-orange.svg) [![](https://img.shields.io/badge/pypi-1.0.2-purple.svg)](https://pypi.org/project/area4)  

## Example  
If you don't understand what we mean by dividers, fear not.  We mean dividers that divide text in the Python console, or anything you use the library for.  An example can be found [here](https://repl.it/@jumbocakeyumyum/area4tests).  

## Divider looks  
*The number before it is the number used in calling it, so for example if you want divider 1, it would be area4.divider1 or area4.div1().*  
1- Dashed  
2- Solid  
3- Dotted  
4- Black Squares  
And more coming soon!  

## Installing  
*You may install in one of the following ways:*  
* Through pip  
* Through requirements.txt  

### To install via pip  
To install via pip, open a terminal, and type the following command:  
```  
pip install area4  
```  
It should install.  

### To install via requirements.txt  
To use area4 as a dependency for your project, you can add the following line:  
```  
area4  
```  
You must have prior knowledge with using a requirements.txt file to take this path.  

## Using  
After you install the package (instructions above), you need to import it into any Python file that you will use it in.  You can do this by adding the following line to the top:  
```  
import area4  
```  
After doing so, you can use any of these methods to get a divider in your console:  

Just using plain print commands:  
```  
print(area4.divider1)  
print(area4.divider2)  
print(area4.divider3)  
print(area4.divider4)  
```  
Using functions:  
```  
area4.div1()
area4.div2()
area4.div3()
area4.div4()
```  
And if you want to you can check to make sure the library is working:  
```  
area4.area4info()
```  
