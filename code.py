# Kaun Banega Crorepati Project
ques = ["MCQ.1 Which of the following corresponds to ‘ek bataa do’?",'''MCQ.2 Which of the following gods is also known as ‘Gauri Nandan’?''','''MCQ.3 In the game of ludo the discs or tokens are of how many colours?''','''MCQ.4 Which of these are names of national parks located in Madhya Pradesh?''','''MCQ.5 Where was the BRICS summit held in 2014?''','''MCQ.6 Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?''','''MCQ.7 Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?''','''MCQ.8 The wife of which of these famous sports persons was once captain of Indian volleyball team?''','''MCQ.9 Starting with the earliest, arrange the following events in Narendra Modi’s life in chronological order. FFF (Fastest Finger First)''','''MCQ.10 Which of these terms can only be used for women?''']
opt = {4:["(A) Krishna and Kanhaiya","(B) Kanha and Madhav","(C) Ghanshyam and Murari","(D) Girdhar and Gopal"],5:["(A) Brazil","(B) India","(C) Russia","(D) China"],6:["(A) P.B. Shelley","(B) Alfred Tennyson","(C) W.B. Yeats","(D) T.S. Elliot"],7:["(A) Anandiben Patel","(B) Vasundhara Raje Scindia","(C) Uma Bharti","(D) Mamata Banerjee"],8:["(A) K.D.Jadav","(B) Dhyan Chand","(C) Prakash Padukone","(D) Milkha Singh"],9:["(A) CM of Gujarat","(B) Took oath as","(C) Joined BJP","(D) Became RSS Pracharak"],10:["(A) Dirghaayu","(B) Suhagan","(C) Chiranjeevi","(D) Sushil"],1:["(A) Pura","(B) Sawa","(C) Adha","(D) Pauna"],2:["(A) Agni","(B) Indra","(C) Hanuman","(D) Ganesha"],3:["(A) One","(B) Two","(C) Three","(D) Four"]}
answers = {1:"C",2:"D",3:"D",4:"A",5:"A",6:"C",7:"A",8:"D",9:"DCAB",10:"B"}
print("Welcome to Kaun banega Crorepati season 8")
Amount = 0
ans = answers.values()
def Amount_increment(n,A):
  if n>=1 and n<=3:
    A+=1000
  elif n==4:
    A+=2000
  elif n==5:
    A+=5000
  elif n==6:
    A+=10000
  else:
    A*=2
  return A  
for i in ques:
  print(i)
  print(opt[(ques.index(i))+1])
  a = input("Enter a option = ")
  if a==answers[(ques.index(i))+1]:
    print("option is correct\nProceed to the next question")
    c = (ques.index(i))+1  
    n = input("Do you want to proceed(y/n)? ")
    Amount = Amount+Amount_increment(c,Amount)
    while n!="y" and n!="n":
      print("Enter a valid output")
      n = input("Do you want to proceed(y/n)? ")
    else:
      if n=="y":
        pass
      elif n =="n":
        print(f"your final winning amount is {Amount}")
        break
        
    
      
  elif a in "ABCD".replace(answers[(ques.index(i))+1],""):
    print("Sorry But you lose")
    print(f"your final winning amount is {Amount}")
    break

  else:
    print("enter a valid output")
    print("Please restart the game")
    break

