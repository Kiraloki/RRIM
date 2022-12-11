
import re ; 

def check(phone_number) : 
   
    phone_regex = '^(\+?\d{1}?[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$';  
    match = re.search(phone_regex, phone_number)
    if (match):
        print("yes ! it is valid") 
    else : 
        print("Invalid")
    
check('2124567890') 
check('212-456-7890') 
check('(212)456-7890') 
check('(212)-456-7890') 
check('212.456.7890') 
check('212 456 7890') 
check('+12124567890') 
check('+12124567890') 
check('+1 212.456.7890') 
check('+212-456-7890') 
check('1-212-456-7890')
    
