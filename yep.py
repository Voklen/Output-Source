import sys
x=""
y="\b"*16
print((x+'x=""'))
x="print(("
print((x+'''x+'x=""'))\nx="print(("\n''')*2,end="")
sys.stdout.write("\033[F") #back to previous line 
sys.stdout.write("\033[K")
x="print("