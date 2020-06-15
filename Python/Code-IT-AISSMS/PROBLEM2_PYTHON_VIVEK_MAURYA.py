from collections import defaultdict 
s1= "sproutswisdom"
s2="wisdomsproutsisawesome"
'''
s1 = "hihelloeveryone"
s2 ="everyonehihello"

s1 = "helloworld"
s2 = "hiworldhihello"

s1= "aissms"
s2 = "ioit"
'''

s1 = list(s1)
s2 = list(s2)
index = 0

def def_value(): 
    return 0
      
letter_count_s1 = defaultdict(def_value) 
letter_count_s2 = defaultdict(def_value)

for s1 in s1:
    letter_count_s1[str(s1)] = letter_count_s1[str(s1)] + 1
      
for s2 in s2:
    letter_count_s2[str(s2)] = letter_count_s2[str(s2)] + 1

for key in letter_count_s1:
    if(letter_count_s1[key] <= letter_count_s2[key]):
        index +=1
    
if(index == (len(letter_count_s1))):
    print("True")
else:
    print("False")


