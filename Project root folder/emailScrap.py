import re 
import json
Email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Human_regex = r'\.'
fo = open("websiteData.txt", encoding="utf8")
data = fo.read()
lst = re.findall(Email_regex,data)
email_dict = {}
for i in lst:
    email_dict[i] = {}
    email_dict[i]['Occurance'] = lst.count(i)
    name = i.split("@")[0]
    if re.findall(Human_regex,name) or len(name) > 8:
        email_dict[i]['EmailType'] = "Human"
    else:
        email_dict[i]['EmailType'] = "Non-Human"
    
# print(email_dict)
json_data = json.dumps(email_dict,sort_keys=False, indent=4)
# print(json_data)
fo.close()
fw=open('result.json','w')
fw.write(json_data)
fw.close()



    
  
 