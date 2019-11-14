## Prof. Inserire QUI il significato di queste variabili globali
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
## Prof. In effetti lo sfondo definito qui viene immediatamente sovrascritto da quello che fai in draw
    size(900,600) #dimensione della finestra
    
    
def draw():
    global x,y,xVers,yVers,raggio,xracc,xracc2,yracc,score1,score2,rect1,rect2 #dichiaro le variabili
    
    
    background(13,255)
    fill(255,255,255) #coloro lo sfondo
    ellipse(x,y,raggio,raggio) #creo la pallina
    
#Dimensioni delle racchette
    rect(xracc,575,100,25)
## Prof. Avrei usato una variabile o il conto espicito per il calcolo della y della racchetta in basso. Se cambi la dimensione della finestra, non funziona

    rect(xracc2,yracc,100,25)

## Prof. Non è chiaro cosa sia 25. La pallina ha raggio 35. Infatti cambia direzione prima di toccare gli oggetti
## Prof. Il giocatore in alto non fa punti
    if (y+25>height-25) and (x+25)>xracc and (x-25)<(xracc+100) :
        yVers  = -1 #allontano la pallina e cambia direzione
        score1 = score1 + 1 #aumento i punti
        
    if (y-25<25) and (x+25)>xracc2 and (x-25)<(xracc2+100) :
        yVers = +1 #allontano la pallina e cambia direzione
        score2 = score2 + 1 #aumento i punti
    
   
        
        
        
## Prof. Non è chiaro cosa sia 25. La pallina ha raggio 35. Infatti cambia direzione prima di toccare gli oggetti
## Prof. la coordinata x controlla i lati e non su e giù
      
    if (x+25 > width or x-25 < 0): #se la palla tocca su o giu'
        xVers = xVers * (-1) #allontano la pallina e cambia direzione
    
   
## Prof. la coordinata y controlla su e giù e non i lati

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
## Prof. Le racchette escono dal campo di gioco
    global xracc,xracc2
    if  keyCode == LEFT:
        xracc = xracc-20 
    if  keyCode == RIGHT:
        xracc = xracc+20
        
    if key== "a":
        xracc2 = xracc2-20
    if key== "d":
        xracc2 = xracc2+20
