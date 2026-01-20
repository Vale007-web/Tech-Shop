# Tech-Shop - E-commerce

Progetto: realizzazione di un e-commerce, sviluppato con Python e Django.

## Descrizione del progetto
Applicazione web per la vendita online di prodotti, con catalogo, filtri di ricerca, ordinamento e gestione del carrello e degli ordini.

L'e-commerce che ho realizzato si distingue innanzitutto tra le schede del browser grazie ad una favicon del logo; il sito si presenta in tutte le pagine, grazie a base.html, con una navbar in alto e un footer in basso.
La navbar contiene il logo e il nome del negozio, la barra di ricerca dei prodotti, e i link al carrello con popup col numero di prodotti al suo interno (che scompare se ci si reca nel carrello stesso), e al login. Se loggati, scompare il link per il login; quindi compaiono il link alle informazioni del proprio account, quello agli ordini effettuati, e quello per il logout.

Nella pagina di login, l'utente può accedere inserendo username e password.
Se non ha ancora un'account, trova nella stessa pagina un'invito a creare un'account tramite un link alla pagina di registrazione. Lì potrà registrarsi inserendo username, email e password; quest'ultima deve essere inserita due volte, se corrisponde e tutte le informazioni inserite rispetta i requisiti di sicurezza richiesti, allora il sistema permette all'utente di procedere con la registrazione.
A registrazione avvenuta l'utente viene reindirizzato alla home, loggato.

Nella pagina del carrello, se l'utente ha aggiunto dei prodotti, vengono visualizzati in riga; per ogni prodotto viene visualizzata la sua immagine, il nome, la quantità, il prezzo della singola unità, il prezzo del totale delle unità di quel prodotto; inoltre sono presenti anche due pulsanti per aumentare e diminuire la quantità di quel prodotto, e uno per eliminare tutte le quantità di quel prodotto.
Sotto i prodotti nel carrello compare il prezzo totale di tutto il carrello, e un pulsante che permette di procedere all'ordine.

Procedendo all'ordine, l'utente viene reindirizzato alla pagina di checkout, dove dovrà inserire le sue informazioni di spedizione: nome, cognome, indirizzo, città e CAP. Se l'utente che effettua l'ordine non è loggato, allora tra le informazioni richieste in fase di checkout comparirà anche l'email.
Accanto al form di checkout è presente anche una sintesi del carrello.

Quando l'utente clicca su "Invia ordine", l'ordine viene registrato e l'utente viene reindirizzato in una pagina di ringraziamento, che lo informa che l'ordine è stato correttamente inviato, comunicandogli il numero di riferimento ordine. Nella stessa pagina è presente anche un pulsante che invita a continuare lo shopping e reinderizza alla home del sito.

Nella navbar, accedendo alla pagina degli ordini, l'utente può vedere la lista degli ordini effettuati. Di ogni ordine visualizza numero, data, nome e prezzo totale.

Nella home del sito (home.html) vengono visualizzati i prodotti disponibili nel database in delle card disposte in griglia. Ogni card mostra l'immagine del prodotto, il nome, parte della descrizione e il prezzo; se un prodotto risulta esaurito, viene mostrato nella card al posto del prezzo.
A sinistra dei prodotti mostrati, è presente una sidebar per filtrare i prodotti per categoria (oltre alla barra di ricerca nella navbar), e sotto invece un menu a discesa per metterli in ordine di nome o prezzo, crescente o decrescente.

Cliccando su uno dei prodotti nella home, si viene reindirizzati alla pagina di quel singolo prodotto; mostra l'immagine del prodotto, la descrizione completa, le specifiche del prodotto, il prezzo e la disponibilità, oltre al pulsante per aggiungere il prodotto al carrello. Quì, a differenza della home, il prezzo viene sempre mostrato. Sotto, però, viene dettagliata la disponibilità; viene visualizzato il numero di pezzi ancora disponibili di quel prodotto; se rimangono poche scorte di quel prodotto (meno di 10), viene mostrato invece un messaggio che invita ad affrettarsi per l'acquisto, perchè il prodotto sta per terminare; se invece le scorte di quel prodotto sono terminate, allora anche quì come nella home viene mostrato "Esaurito", e scompare il pulsante per aggiungere il prodotto al carrello.


## Tecnologie utilizzate
- Python
- Django
- HTML / CSS
- Javascript
- SQLite

## Installazione
1. Clonare o scaricare la repository
2. Creare un ambiente virtuale
3. Installare le dipendenze:
   pip install -r requirements.txt
5. Eseguire le migrazioni:
   python manage.py migrate
7. Avviare il server:
   python manage.py runserver

## Funzionalità implementate
- Visualizzazione prodotti
- Ricerca prodotti
- Filtro per categoria
- Ordinamento crescente e decrescente: nome, prezzo
- Dettaglio prodotto
- Carrello
- Modulo di checkout ordine
- Login/logout
- Registrazione
- Profilo
