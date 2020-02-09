import r2pipe
import argparse

def printFuncInfo(name, offset):
    print("function ->")
    print("\tName-> ", name)
    print("\tOffset-> ", offset)

def getFuncs(fileName):
    #Get functions from r2
    #the docs for r2pipe are located
    #at https://r2wiki.readthedocs.io/en/latest/home/radare2-python-scripting/
    r2 = r2pipe.open(fileName)
    r2.cmd("aaa")
    #The resolved json is a list
    #of objects each object is a r2 function def
    functionList = r2.cmdj("aflj")
    for i in functionList:
        name= i["name"]
        offset = i["offset"]
        printFuncInfo(name, offset)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help="The file to pase to r2")
    args = parser.parse_args()
    if args.filename:
        getFuncs(args.filename)
    else:
        print("Need filename")
        exit()

if __name__ == "__main__":
    main()
