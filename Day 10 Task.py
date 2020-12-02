#Day 10 Task

#1
import re
def check(string):
    pattern = re.compile(r'[^a-zA-Z0-9.]')
    string = pattern.search(string)
    return not bool(string)
print(check("abcVUn12"))    #output = True
print(check("&*%^(!"))      #output = False

#2
def match(text):
    pattern = 'ab'
    res = re.search(pattern,text)
    if res:
        print("found")
    else:
        print("not found")
match("abs")        #output = found
match("triceps")     #output = not found

#3
def end(txt):
    res = re.findall("\d$",txt)
    if res:
        print("ends with number: ",res)
    else:
        print("does not ends with number")
end("abc7")                  #output = ends with number:  ['7']
end("3def")                  #output = does not ends with number


#4
def check_nums(s):
    results = re.findall(r"(\d{1,3})",s)
    print(results)
check_nums("girish10 prakash25 irfan30 bill300")    #output = ['10', '25', '30', '300']


#5
def check_text(words):
    res = re.findall("[A-Z]",words)
    if res:
        print(res)
        print("There is a match")
    else:
        print("No match found")
check_text("ABC")              #output = ['A', 'B', 'C']
                                #There is a match


