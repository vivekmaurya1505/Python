'''#! python3'''
#Link->https://www.udemy.com/course/automate/learn/lecture/3470534#overview
#Install: pip install pyperclip
import re
import pyperclip

# TODO: Create a regex for phone numbers
Phone_Regex = re.compile(r'''
# 415-555-0000, 555-0000,(415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|\(\d\d\d\))?        #area code (optional)
(\s|-)        #first separator
\d\d\d        #first 3 digits
-        #separator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x)        #extension word-part (optional)
  (\d{2,5}))?       #Extension number-part (optinal)
)  
''', re.VERBOSE)

# TODO: Create a regex for email addresses
Email_Regex = re.compile(r'''
# Some.+_thing@(\d{2,5})?.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+    # Domain name part

''',re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
Extract_Phone = Phone_Regex.findall(text)
Extract_Email = Email_Regex.findall(text)


All_Phone_Number = []
for Phone_Number in Extract_Phone:
    All_Phone_Number.append(Phone_Number[0])

'''Copy This line of contact for input after that run the code and we can paste result anywhere 

Cyril Wynn cwynn63@outlook.com 405-918-3937
Sidney Lara sidneyl@hotmail.com 464-390-2264
Pasquale Larson larso56@msn.com 242-726-1488
Olen Fuentes ofuentes67@verizon.net 662-743-9060
'''    

# TODO: copy the extracted email/phone to the clipboard

Results = "\n".join(All_Phone_Number) + '\n' + '\n'.join(Extract_Email)
pyperclip.copy(Results)

print(Extract_Phone)
#Output: [('405-918-3937', '405', '405', '-', '', '', '', '', ''), ('464-390-2264', '464', '464', '-', '', '', '', '', ''),
#('242-726-1488', '242', '242', '-', '', '', '', '', ''), ('662-743-9060', '662', '662', '-', '', '', '', '', '')]
print(Extract_Email)
#output: ['cwynn63@outlook.com', 'sidneyl@hotmail.com', 'larso56@msn.com', 'ofuentes67@verizon.net']
print(All_Phone_Number)
#Output:['405-918-3937', '464-390-2264', '242-726-1488', '662-743-9060']
print(Results)
'''Output: 405-918-3937
464-390-2264
242-726-1488
662-743-9060
cwynn63@outlook.com
sidneyl@hotmail.com
larso56@msn.com
ofuentes67@verizon.net
'''
