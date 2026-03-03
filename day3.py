
#string creation
teju ='Data Analyst'
raki ="Data Analyst"

pooja = '''writing a string in multi lines in triple single quotes are called as multi line strings in python.
pooja is working as data analyst in mnc company'''

print (teju)
print (raki)
print(pooja)

print(teju,raki,pooja)

# indexing and slicing of strings
text = "python is fun to learn"
print(text[1]) #postivie indexing left to right
print (text[-1]) # negative indexing right to left 
print (text[0:6]) #slicing
print (text[10:]) #slicing from index 10 to end
print(text[:]) # full string
print (text[::-1])# reverse the string 
print(text[::2]) #step slicing every 2nd character 
print (text[1::2]) # step slicing every 2nd character starting from index 1    
print (text [0:6:2]) # step slicing with step variable greater the lenght of string
print (text[-1:-6:-1]) # reverse slicing 

srivani ="da"
hussain="de"
print (srivani + hussain) # concentation of strings
print (srivani + " @ " + hussain) # concentation with special character
print (" ".join ([srivani,hussain])) # concentation using join function 
print (srivani * 5) # repetition of strings
print (len (srivani)) # lenght of string 
print (srivani in hussain) # membership operator
print (srivani not in hussain) # membership operator 