#Importo la libreria g2d
import lib.g2d as g2d

#Definisco le coordinate degli sprite sheet
CELL = 32

#Definisco la direzione, dove ogni direzione ha 2 frame
_FROG_FRAMES = {
    "up":    (0, 1, 0),
    "down":  (0, 1, 1),
    "left":  (0, 1, 2),
    "right": (0, 1, 3)
}

#Definisco le costanti di gioco
STEP        = 40 #Pixel per ogni salto
ANIM_STICKS = 6  #Frame in cui si mostra il frame di salto

#Classe che rappresenta la classe della rana controllata dal giocatore
class Giocatore:
    #Costruzione del personaggio
    def __init__(self, _start_x: int, _start_y: int):
        self._x = _start_x
        self._y = _start_y
        self._dir   = "up"  #Direzione corrente
        self._frame = 0     #0 = fermo, 1 = in salto
        self._anim  = 0     #Contatore tick animazione
        self._vite  = 3
        self._vivo  = True
        self._start_x = _start_x
        self._start_y = _start_y

    #Definisco le proprietà d'accesso
    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def w(self) -> int:
        return CELL

    @property
    def h(self) -> int:
        return CELL

    @property
    def vite(self) -> int:
        return self._vite

    @property
    def vivo(self) -> bool:
        return self._vivo

    #Gestione dell'input leggendo i tasti premuti spostando la rana di un passo
    def gestisci_input(self, canvas_w: int, canvas_h: int) -> None:
        #Controllo per non accettare input durante il salto
        if self._anim > 0:
            return

        #Controlli per indicare la direzione della rana
        moved = False
        if g2d.key_pressed("ArrowUp"):
            self._dir = "up"
            self._y   = max(0, self._y - STEP)
            moved = True
        elif g2d.key_pressed("ArrowDown"):
            self._dir = "down"
            self._y   = min(canvas_h - CELL, self._y + STEP)
            moved = True
        elif g2d.key_pressed("ArrowLeft"):
            self._dir = "left"
            self._x   = max(0, self._x - STEP)
            moved = True
        elif g2d.key_pressed("ArrowRight"):
            self._dir = "right"
            self._x   = min(canvas_w - CELL, self._x + STEP)
            moved = True

        #Controllo se la rana e in movimento
        if moved:
            self._frame = 1
            self._anim  = ANIM_STICKS

    #Aggiornamento
    #Avanzamento dell'animazione di salto
    def aggiorna(self) -> None:
        if self._anim > 0:
            self._anim -= 1
            if self._anim == 0:
                self._frame = 0

    #Spostamento orizontale della rana usato da tronchi/tartarughe
    def trascinato(self, dx: int) -> None:
        self._x += dx

    #Scala di una vita e riposizionamento della rana
    def muori(self) -> None:
        self._vite -= 1
        if self._vite <= 0:
            self._vivo = False
        else:
            self.respawn()

    #Riporto la rana alla posizione di partenza
    def respawn(self) -> None:
        self._x     = self._start_x
        self._y     = self._start_y
        self._dir   = "up"
        self._frame = 0
        self._anim  = 0

    #Rettangolo di collisione della rana
    def rettangolo(self) -> tuple[int, int, int, int]:
        margin = 4
        return (self._x + margin, self._y + margin,
                CELL - margin * 2, CELL - margin *2)

    #Disegno la rana sullo schermo
    def disegna(self) -> None:
        col0, col1, row = _FROG_FRAMES[self._dir]
        col = col1 if self._frame == 1 else col0
        clip_x = col * CELL
        clip_y = col * CELL

        g2d.draw_image("frogger.png",
                       (self._x, self._y),
                       (clip_y, clip_y),
                       (CELL, CELL))