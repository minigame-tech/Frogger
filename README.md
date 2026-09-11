# 🐸 Frogger - Python Remake

Un remake del classico videogioco **Frogger** sviluppato in **Python**, utilizzando la libreria **Pygame** per la gestione del comparto audio e il modulo **g2d** per la gestione della logica grafica e dei cicli di gioco.

## 🚀 Funzionalità Principali
- Logica di gioco fedele all'originale (movimento della rana, ostacoli, fiumi e strade).
- Effetti sonori dinamici gestiti tramite Pygame.
- Rendering grafico leggero e strutturato tramite g2d.

## 🛠️ Installazione e Avvio
Per giocare al titolo in locale, assicurati di avere Python installato sul tuo computer, dopodiché:

1. Clona il repository o scarica i file del progetto.
2. Installa la dipendenza audio (Pygame):
   ```bash
   pip install pygame
   ```
3. Avvia il gioco eseguendo il file principale:
   ```bash
   python main.py
   ```

## 📈 Roadmap

### 🎨 Comparto Animazioni
- [ ] **Splash Screen:** Introduzione animata automatica all'avvio del gioco tramite doppio click.
- [ ] **Transizioni Menu:** Animazioni fluide alla pressione dei tasti nei menu principali.
- [ ] **Tutorial Intelligente:** Schermata con spiegazione dei comandi visibile solo alla prima partita in assoluto (saltabile) e disattivata nei riavvii rapidi post-morte.

### 💾 Salvataggio Dati (Database)
- [ ] **Accesso stile Netflix:** Interfaccia grafica all'avvio (`menu_accesso.py` e `grafica_accesso.py`) per caricare il proprio profilo o crearne uno nuovo se non esiste.
- [ ] **Persistenza:** Tracciamento automatico del nome utente e del numero di partite giocate nel database locale (SQLite).
- [ ] **Statistiche e Record:** Salvataggio permanente del miglior punteggio assoluto e del record giornaliero dinamico.

## 📄 Licenza
Questo progetto è rilasciato sotto i termini della licenza **MIT**. Consulta il file `LICENSE` per maggiori dettagli.