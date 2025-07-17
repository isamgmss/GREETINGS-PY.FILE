import time
tp=(time.strftime('%H hrs : %M min : %S sec '))
print((tp))
import time
print(f'YOUR TIME {tp}')
tp=int(time.strftime('%H'))
if(tp<11):
    print("Good Morning")

elif(tp==12):
    print("Good Noon")
    
elif(tp>12 and tp<19):
    print("Good Evening") 
       
else:
    print("Good Night") 
