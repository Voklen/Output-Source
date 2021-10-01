#initialize variables
x="";
y="'"*3+"<everything after line 8 column 32>";
z="";
# z+= is effectivly print()
z+=((x+"""<all previous lines>"""));x="z+=((x+"+"'"*3; # set x to different value for the next line
z+=((x+'''<previous 2 lines>''')*2).replace(x,'',1);
z+=y;
print(z)