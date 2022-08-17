ch = input("ENTER:")
out = ""
for i in range(0,len(ch),2):
    out += ch[i]*int(ch[i+1])
    
print(out)
