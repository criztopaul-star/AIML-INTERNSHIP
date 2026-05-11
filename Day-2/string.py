#Count number of characters in a string.
a=input("Enter the string: ")
s=len(a)
print("Number of characters in string is:",s)

#Reverse a string
b=input("Enter the string: ")
print("The reverse of string is: ",b[::-1])

#Check if a string is palindrome
c=input("Enter a string: ")
s=c[::-1]
if c==s:
    print("The String is Palindrome")
else:
    print("The String is not Palindrome")

#Count vowels and consonants in a string
d=input("Enter the string: ")
vcount=0
ccount=0
for i in d:
    if i in "aeiouAEIOU":
        vcount+=1
    elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        ccount+=1
    else:
        continue
print("Number of vowels is:",vcount)
print("Number of consonants is:",ccount)
        

#Convert string to uppercase and lowercase.
e=input("Enter the string: ")
f=""
for l in e:
    if ord(l)>=65 and ord(l)<=90:
        g=l.lower()
        f=f+g
    elif ord(l)>=97 and ord(l)<=122:
        h=l.upper()
        f=f+h
    else:
        f=f+l
print("The swapped Character string is:",f)
        
        
#Remove spaces from a string.
j = input("Enter the String: ")
y = j.replace(" ", "")
print("The string after removing spaces:", y)

#Replace a word in a sentence.
o = input("Enter the String: ")
rep = input("Enter the word to be replaced: ")
sub = input("Enter the replacement word: ")
words = o.split()
new = ""
for w in words:
    if w == rep:
        new += sub + " "
    else:
        new += w + " "

print("The replaced string is:", new.strip())

#Count frequency of each character.
stri=input("Enter the String: ")
histogram = {}
for char in stri:
    if char in histogram:
        histogram[char.lower()] += 1
    else:
        histogram[char.lower()] = 1
print(histogram)

#Extract substring from a string.
st=input("Enter the String: ")
start=int(input("Enter Starting index: "))
end=int(input("Enter Ending index: "))
print(st[start:end+1:1])

#Check if two strings are anagrams.
st1=input("Enter the String: ")
st2=input("Enter the String: ")
hist1 = {}
hist2 = {}
for char in st1:
    if char.lower() in hist1:
        hist1[char.lower()] += 1
    else:
        hist1[char.lower()] = 1
for char in st2:
    if char.lower() in hist2:
        hist2[char.lower()] += 1
    else:
        hist2[char.lower()] = 1
if hist1==hist2:
    print("The strings are anagram")
else:
    print("The Strings are not anagram")
