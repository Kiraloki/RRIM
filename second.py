import re
import requests
from bs4 import BeautifulSoup 

req = requests.get("https://github.com/") 

soup = BeautifulSoup(req.content,"html.parser")  

dict = {"sociallinks":[],"mail" :"" , "contact": ""}  

f_regex = "(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com\/(?P<profile>(?![A-z]+\.php)(?!marketplace|gaming|watch|me|messages|help|search|groups)[A-z0-9_\-\.]+)\/?" 
l_regex = "(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/(?P<company_type>(company)|(school))\/(?P<company_permalink>[A-z0-9-À-ÿ\.]+)\/?" 
p_regex = "(?:tel|phone|mobile):(?P<number>\+?[0-9. -]+)" 
m_regex = "(?:mailto:)?(?P<email>[A-z0-9_.+-]+@[A-z0-9_.-]+\.[A-z]+)" 

for link in soup.find_all('a'): 
    
    if(re.search(f_regex, link.get('href'))) :  
        dict["sociallinks"].append(link.get('href')) 

    if(re.search(l_regex, link.get('href'))): 
        dict["sociallinks"].append( link.get('href') )  
        
    if(re.search(m_regex, link.get('href'))) :  
        dict["mail"] = link.get('href')  
      

    if(re.search(p_regex, link.get('href')))  :  
        dict["contact"] = link.get('href') 
        
     
print(dict) 