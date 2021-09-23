x=""
y="abc" #replace abc with everything after Line 6 Column 31
z=""
z+=(x+'x="";')
x="z+=(x+'''"
z+=(x+'''x+'x="";'));x="z+=(";''')*2
print(z)