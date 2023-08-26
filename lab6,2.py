import re
def func1(text):

    pattern2=r'[A-Z]+'
    pattern3=r'[a-z]+'
    pattern4=r'[0-9]+'
    pattern5=r'[@ - / , .]+'
    match2=re.search(pattern2,text)
    match3=re.search(pattern3,text)
    match4=re.search(pattern4,text)
    match5=re.search(pattern5,text)
    if match2 and match3 and match4 and match5:
      
      print("Password Set Successfully")
    else: 
       print("Password Set Successfully")
text=str(input("Enter the string"))
func1(text)