import sys
import os
import random
version = str("0.0.1")
edition = str("Development")
#choose words to say
greetings = ["Hey!","Hiya!","What's up?","Hello!","Hey!","Hullo!","Sup!","Heya!","What's good?",]
need = ["Need","Want", "Require","Would you like"]
lookats = ["a looking-at", "a checkup", "an exam", "an examination","a system check","a helping hand"]

#print(rand.greetings + rand.need + str("a") + rand.lookats + str("?"))
greet = str(random.choice(greetings))
want = str(random.choice(need))
exam = str(random.choice(lookats))
#+ str(" ") +
print("Doctor Py Version: "+version+", "+edition+" Edition.")
print("")
print("")
print(greet + str(" ") + want +  str(" ") + exam + str("?"))
print("(y/n)")
print("")
x = str(input(">"))

if x.lower() =="n":
    END

input("END OF CODE")
