from turtle import *
shape("turtle")
speed(2)

for n in range(3, 5):
     for i in range(3, 6):

        left(180-(180*(n-2)/n))
        forward(150)
left(90)        
forward(150)
for m in range(5, 7):
    for x in range(4, 9):
        left(180-(180*(m-2)/m))
        forward(150)    
left(60)
forward(150)
for i in range(6):
    m =7
    left(180-(180*(m-2)/m))
    forward(150)   

mainloop()



