import lib.g2d as g2d

#Costanti sprite sheet
C          = 32
SPRITE     = "frogger.png"
BACKGROUND = "frogger-bg.png"

#Clip degli elementi grafici usati nel menu
_LOGO_CLIP   = (0,    8*C, 7*C,  C)   #Scritta FROGGER      (224×32)
_CIRCLE_BTN  = (4*C,  6*C,  C,   C)   #Cerchio giallo/viola (32×32)
_SNAKE_CLIP  = (0,    7*C, 5*C,  C)   #Serpente verde       (160×32)
_CROC_CLIP   = (5*C,  7*C, 5*C,  C)   #Coccodrillo          (160×32)
_FROG_CLIP   = (2*C,  0,    C,   C)   #Rana ferma           (cursore / decorazione)
_TURTLE_CLIP = (6*C,  5*C,  C,   C)   #Tartaruga verde      (coordinata corretta)

#Dimensioni dell'area cliccabile di ogni bottone
_BTN_W, _BTN_H = 260, 48

#Posizioni Y dei centri dei 3 bottoni
_BTN0_CY = 254 #GIOCA
_BTN1_CY = 324 #COME SI GIOCA
_BTN2_CY = 394 #ESCI

_BTNS = [_BTN0_CY, _BTN1_CY, _BTN2_CY]

#Classe che rappresenta il menu principale
class MainMenu:
    def __init__(self, canvas_w: int, canvas_h: int):
        self._cw = canvas_w
        self._ch = canvas_h

        self._voce_sel  = 0      #0 = GIOCA, 1 = COME SI GIOCA, 2 = ESCI
        self._anim_tick = 0
        self._mostra_istruzioni = False

        #Segnali letti dal main loop dopo ogni chiamata alla funzione aggiorna()
        self._avvia = False
        self._esci  = False

    #Segnali pubblici
    @property
    def avvia(self) -> bool:
        return self._avvia

    @property
    def esci(self) -> bool:
        return self._esci

    #Aggiornamento
    def aggiorna(self) -> None:
        self._avvia     = False
        self._esci      = False
        self._anim_tick += 1

        if self._mostra_istruzioni:
            #Qualsiasi tasto/click chiude le istruzioni
            if g2d.key_pressed("Enter") or g2d.key_pressed("Escape") \
                    or g2d.key_pressed("Spacebar") or g2d.mouse_clicked():
                self._mostra_istruzioni = False
        else:
            self._gestisci_tastiera()
            self._gestisci_mouse()

    def _gestisci_tastiera(self) -> None:
        if g2d.key_pressed("ArrowUp"):
            self._voce_sel = (self._voce_sel - 1) % 3
        elif g2d.key_pressed("ArrowDown"):
            self._voce_sel = (self._voce_sel + 1) % 3

        if g2d.key_pressed("Enter") or g2d.key_pressed("Spacebar"):
            self._conferma()

    def _gestisci_mouse(self) -> None:
        if not g2d.mouse_clicked():
            return

        mx, my = g2d.mouse_pos()
        bx = self._cw // 2 - _BTN_W // 2
        for i, cy in enumerate(_BTNS):
            if bx <= mx <= bx + _BTN_W:
                if cy - _BTN_H // 2 <= my <= cy + _BTN_H // 2:
                    self._voce_sel = i
                    self._conferma()
                    return

    def _conferma(self) -> None:
        if self._voce_sel == 0:
            self._avvia = True
        elif self._voce_sel == 1:
            self._mostra_istruzioni = True
        else:
            self._esci = True

    #Disegno del main menu
    def disegna(self) -> None:
        g2d.clear_canvas()
        self._disegna_sfondo()
        self._disegna_logo()
        self._disegna_sottotitolo()
        self._disegna_tartarughe()
        self._disegna_bottone("  GIOCA  ",        _BTN0_CY, self._voce_sel == 0)
        self._disegna_bottone(" COME SI GIOCA ",  _BTN1_CY, self._voce_sel == 1)
        self._disegna_bottone("   ESCI   ",       _BTN2_CY, self._voce_sel == 2)
        self._disegna_cursore_rana()
        self._disegna_decorazioni_basse()

        if self._mostra_istruzioni:
            self._disegna_schermata_istruzioni()

    def _disegna_sfondo(self) -> None:
        g2d.draw_image(BACKGROUND, (0, 0))
        g2d.set_color((0, 0, 0, 140))
        g2d.draw_rect((0, 0), (self._cw, self._ch))

    def _disegna_logo(self) -> None:
        logo_w = _LOGO_CLIP[2]
        logo_x = self._cw // 2 - logo_w // 2
        logo_y = 40

        g2d.draw_image(SPRITE, (logo_x, logo_y),
                       (_LOGO_CLIP[0], _LOGO_CLIP[1]),
                       (_LOGO_CLIP[2], _LOGO_CLIP[3]))
        g2d.draw_image(SPRITE, (logo_x - C - 8, logo_y),
                       (_FROG_CLIP[0], _FROG_CLIP[1], (C, C)))
        g2d.draw_image(SPRITE, (logo_x + logo_w + 8, logo_y),
                       (_FROG_CLIP[0], _FROG_CLIP[1]), (C, C))

    def _disegna_sottotitolo(self) -> None:
        g2d.set_color((0, 255, 200))
        g2d.draw_text("Usa le frecce  •  INVIO per confermare",
                      (self._cw // 2, 110), 18)

    def _disegna_tartarughe(self) -> None:
        y = 170
        for i in range(8):
            g2d.draw_image(SPRITE, (i * (C + 8) + 24, y),
                           _TURTLE_CLIP[0], _TURTLE_CLIP[1], (C, C))