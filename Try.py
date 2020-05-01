#!/usr/bin/env python3
# Beispieldatei Try-Email.py
 
import re 
s1 = 'abc'
s2 = '\a\a\a\a'
s1 = s1 + s1
print(s1)

pattern = r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+$'
email = input('Geben Sie ihre E-MAil-Adresse ein: ')

if re.match(pattern, email):
    print('Die Email-Adresse wurde korrekt eingegeben')
else:   
    print('Die Email-Adresse wurde fehlerhaft eingegeben, Bitte versuchen Sie es erneut')

    
s = 'home/Niklas.Karrasch/Data/Foto.jpg'
print(s)
spartion = s.split('/')
laenge = len(spartion)
print(spartion)
file = spartion[-1]
print(spartion[-1])
spartion = spartion.remove(spartion[-1])
print(type(spartion))
#path = spartion.join()
#print(path)

input('Druecken Sie return:')