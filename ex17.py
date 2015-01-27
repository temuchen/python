from sys import argv
from os.path import exists

script,from_file,to_file=argv

print "Copy from %s to %s"%(from_file,to_file)

input=open(from_file) #create a object named "input" by file class.
indata=input.read() #call the "read" method,return a string to indata.

print "The input file is %d bytes long "%len(indata)

print "Ready,hit RETURN to continue,CTRL-C to abort."
raw_input()

output=open(to_file,'w')
output.write(indata)

print "Alright,all done."

output.close()
input.close()