""" 
filesplitter by Yankeevic. 20170606
splists a file and generates as many files as pairs of even-odd lines

MODULES:
    cefpython3 (57.0)
    named-constants (1.0)
    pip (9.0.1)
    setuptools (28.8.0)
    six (1.10.0)
    wxPython (4.0.0a3)

TODO:
    Error management 
    big file management. 
    Additional checks and guards ?
    Add to source control
"""
import os
import sys
#https://stackoverflow.com/questions/291740/how-do-i-split-a-huge-text-file-in-python
import mmap
#https://stackoverflow.com/questions/19684434/best-way-to-check-function-arguments-in-python
import getopt 
#https://stackoverflow.com/questions/2682745/how-to-create-a-constant-in-python/19306516#19306516
from named_constants import Constants 

class UserMessages(Constants):
    MSG1 = "File generated =>"
    MSG2 = "Number of files generated: "
    MSG3 = "File size in bytes: "

class ErrorMessages(Constants):
    ERR1 = "WARNING: Missing argument=> -i 'c:\inputfile.txt'  "
    ERR2 = "WARNING: The file does not exist => "
    
class Parameters:
    def __init__(self, filename):
        self.filename  = filename
        #self.outputpath = outputpath
        
def main():
    version = '1.0'
    params = checkarguments()
    getfilesize(params)
    splitfile(params)
    
def checkarguments():
    if len(sys.argv) < 3:
        print(ErrorMessages.ERR1)
        sys.exit(-1)
    print('ARGV      :', sys.argv[1:])
    options, remainder = getopt.getopt(sys.argv[1:], 
                                             'i:v', 
                                            ['inputfile=','version=', ])
    print ('OPTIONS   :', options)
    for opt, arg in options:
        if opt in ('-i', '--input'):
            filename = arg
#        elif opt in ('-o', '--outputpath'):
#            outputpath = arg
        elif opt == '--version':
            version = arg
    #check if file exists.
    if not os.path.isfile(filename):
       print(ErrorMessages.ERR2,'"',filename, '"')
       sys.exit(-1)
    return Parameters(filename)

#file size for Big file management
def getfilesize(parameters):
   with open(parameters.filename,"rb") as fr:
       fr.seek(0,2) # move to end of the file
       size=fr.tell()
       print(UserMessages.MSG3, size)
       return fr.tell()
       
def splitfile(parameters):
    #splitpoint =  parameters.filename.rfind(".")
    #orginalfilename = parameters.filename.split(".")
    orginalfilename = parameters.filename.rsplit(".",1)
    try:
        with  open(parameters.filename, "r") as fhand:
            linecount=0
            filecount=0
            #se recorre el fichero linea a linea
            for line in fhand:
                linecount += 1 #contador de lineas
                #En las lineas pares se rellena y se cierra el fichero.
                if (linecount % 2 == 0):  #print "linea PAR"
                    with open(newfilename,"ab") as fw:
                        fw.write(bytes(line, 'utf-8'))
                        fw.close()
                #En las lineas impares se crea el fichero con la primera parte.       
                else:   #print "linea IMPAR"
                    filecount +=1 #contador de ficheros que se generan.
                    newfilename = orginalfilename[0]+ \
                                              "_{id}.".format(id=str(filecount))+ \
                                              orginalfilename[1]
                    #fullpath = parameters.outputpath + newfilename
                    with open(newfilename,"ab") as fw:
                        fw.seek(0) 
                        fw.truncate()# truncate original if present
                        fw.write(bytes(line, 'utf-8'))
                        print( UserMessages.MSG1,"'",newfilename,"'")
            print( UserMessages.MSG2, filecount)
            fhand.close()
    except OSError as err:
        print("OS error: {0}".format(err))
        sys.exit(-1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(-1)
        #raise
        
#entry point 
if __name__ == "__main__":
    main()          



