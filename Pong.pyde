x=60
y=60
xrect2=0
xrect1=0
xVers=1
yVers=1
raggio=35
xracc=0
xracc2=0
yracc=0
score1=0
score2=0

def setup():
    background(13,255) #coloro lo sfondo
    size(900,600) #dimensione della finestra
    
    
def draw():
    global x,y,xVers,yVers,raggio,xracc,xracc2,yracc,score1,score2,rect1,rect2 #dichiaro le variabili
    
    
    background(13,255)
    fill(255,255,255) #coloro lo sfondo
    ellipse(x,y,raggio,raggio) #creo la pallina
    
#Dimensioni delle racchette
    rect(xracc,575,100,25)
    rect(xracc2,yracc,100,25)


    if (y+25>height-25) and (x+25)>xracc and (x-25)<(xracc+100) :
        yVers  = -1 #allontano la pallina e cambia direzione
        score1 = score1 + 1 #aumento i punti
        
    if (y-25<25) and (x+25)>xracc2 and (x-25)<(xracc2+100) :
        yVers = +1 #allontano la pallina e cambia direzione
        score2 = score2 + 1 #aumento i punti
    
   
        
        
        
        
    if (x+25 > width or x-25 < 0): #se la palla tocca su o giu'
        xVers = xVers * (-1) #allontano la pallina e cambia direzione
    
   
   
    if (y+25 > height or y-25 < 0): #se la palla tocca a destra o sinistra
        yVers = yVers * (-1) #allontano la pallina e cambia direzione


        
        

#Coordinate per fare muovere la pallina
    x += 3*xVers
    y += 3*yVers



    
    fill(255,128,128) #colore punteggio
    textSize(20) #grandezza testo punteggio
    text(score1,10,400) #assegno posizione e valore al punteggio
    
    fill(255,128,128) #colore
    textSize(20) #grandezza testo punteggio
    text(score2,0,40) #assegno posizione e valore al punteggio   
    
    
def keyPressed():
    global xracc,xracc2
    if  keyCode == LEFT:
        xracc = xracc-20 
    if  keyCode == RIGHT:
        xracc = xracc+20
        
    if key== "a":
        xracc2 = xracc2-20
    if key== "d":
        xracc2 = xracc2+20
