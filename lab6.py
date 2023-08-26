import re
def func1(text):
   
   pattern1=r'[(?][0-9]{3}[)?]\-[0-9]{3}\-[0-9]{4}'
   pattern2=r'[0-9]{3}-[0-9]{3}-[0-9]{4}'
   match1=re.search(pattern1,text)
   match2=re.search(pattern2,text)
   if match1 or match2:
      
    print("Valid phn number")
   else:
    print("Invalid phn number")
text=str(input("Enter the number"))
func1(text)

 