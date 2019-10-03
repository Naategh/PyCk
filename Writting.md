#How to learn from these scripts
This repository was created with the intention of being a source 
that can be learned from. This file serves to be a rough map of 
what scripts people should look into for learning. 

##Simple examples
Some good scripts to use as a starting reference point when building
your own tools are `sniff.py` `postexfil.py` `sysInfo.py` and `xorCrypt.py`.
These scripts are all fairly small scripts that exemplify some simple python features.

##Web
If you want to learn about writting web tools then take a look at
`Site_Tester.py` `XssTester.py` `admin_panel_finder.py` and `postexfil.py`

All of these scripts deal with either scanning or implimenting web server functions.

##Some notes about writting reuseable code
Writing your own code and tools is good, but writing code and tools that 
can also be useful as modules too, not just standalone tools, is better.
The simpliest way to do this is impliment the main logic of a program in
a function and then create a `main()` function that does argument parseing and 
passing to the logic function.
For example
```
def logicCode(x, z):
    return(x, z)

def main():
   //Do ArgParse
   print(logicCode(x, z)

if __name__ == "__main__":
    main()
```
This way you can use the logic implimented in logicCode in other scripts.
Writting modular code is a good mindset to get into when writting security tools because modilarity can lead to making automation easier.
