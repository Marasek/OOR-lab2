# -*- coding: utf-8 -*-
import Queue
from threading import Thread

# tworzy przykład
q = Queue.LifoQueue() #LIFO- Last in first out; czyli liczby pokazują się od największej
#FIFO- First in first out

# dodaje pozycje do kolejki
for i in range(10):
    q.put(i) #elementy są dodawane na koniec kolejki (get() usuwa z koleji)

def dane_z_kolejki():
    while not q.empty(): # sprawdza czy kolejka nie jest pusta
        print q.get() # drukuje element z kolejki
        q.task_done() # określa czy element się wykonał
        
for i in range(2): # liczba wątków
    t1 = Thread(target = dane_z_kolejki) 
    t1.start() # start wątku
    
q.join() # działa z q.task_done
         # przede wszystkim q.join() utrzymuje rozmiar koleji

