import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
uscore=0
cscore=0
userchoice1=input("ENTER YOUR 1st CHOICE").lower()
if(userchoice1=="rock"):
  print(f"You chose: {rock}")
elif(userchoice1=="paper"):
  print(f"You chose: {paper}")
elif(userchoice1=="scissors"):
  print(f"You chose: {scissors}")
else:
  print("enter correct choice")
list=[rock,paper,scissors]
r=random.randint(0,2)
comchoice1=list[r]
print(f"\n Computer chose: {comchoice1}")
if(userchoice1=="rock" or userchoice1=="paper" or userchoice1=="scissors"):
  if (userchoice1=="rock" and r==0) or (userchoice1=="paper" and r==1) or (userchoice1=="scissors" and r==2):
    cscore=cscore
    uscore=uscore
  elif (userchoice1=="rock" and r==2) or (userchoice1=="paper" and r==0) or (userchoice1=="scissors" and r==1):
    cscore=cscore
    uscore=uscore+1
  else:
    cscore=cscore+1
    uscore=uscore
  print(f"\nCOMPUTER SCORE:{cscore}\nYOUR SCORE:{uscore}")


userchoice2=input("ENTER YOUR 2nd CHOICE").lower()
if(userchoice2=="rock"):
  print(f"You chose: {rock}")
elif(userchoice2=="paper"):
  print(f"You chose: {paper}")
elif(userchoice2=="scissors"):
  print(f"You chose: {scissors}")
list=[rock,paper,scissors]
r=random.randint(0,2)
comchoice2=list[r]
print(f"\n Computer chose: {comchoice2}")
if(userchoice2=="rock" or userchoice2=="paper" or userchoice2=="scissors"):
  if (userchoice2=="rock" and r==0) or (userchoice2=="paper" and r==1) or (userchoice2=="scissors" and r==2):
    cscore=cscore
    uscore=uscore
  elif (userchoice2=="rock" and r==2) or (userchoice2=="paper" and r==0) or (userchoice2=="scissors" and r==1):
    cscore=cscore
    uscore=uscore+1
  else:
    cscore=cscore+1
    uscore=uscore
  print(f"\nCOMPUTER SCORE:{cscore}\nYOUR SCORE:{uscore}")

userchoice3=input("ENTER YOUR 3rd CHOICE").lower()
if(userchoice3=="rock"):
  print(f"You chose: {rock}")
elif(userchoice3=="paper"):
  print(f"You chose: {paper}")
elif(userchoice3=="scissors"):
  print(f"You chose: {scissors}")
list=[rock,paper,scissors]
r=random.randint(0,2)
comchoice3=list[r]
print(f"\n Computer chose: {comchoice3}")
if(userchoice3=="rock" or userchoice3=="paper" or userchoice3=="scissors"):
  if (userchoice3=="rock" and r==0) or (userchoice3=="paper" and r==1) or (userchoice3=="scissors" and r==2):
    cscore=cscore
    uscore=uscore
  elif (userchoice3=="rock" and r==2) or (userchoice3=="paper" and r==0) or (userchoice3=="scissors" and r==1):
    cscore=cscore
    uscore=uscore+1
  else:
    cscore=cscore+1
    uscore=uscore
  print(f"\nCOMPUTER SCORE:{cscore}\nYOUR SCORE:{uscore}")
if(cscore>uscore):
  print("              COMPUTER WON               ")
else:
  print("                YOU WIN                  ")
