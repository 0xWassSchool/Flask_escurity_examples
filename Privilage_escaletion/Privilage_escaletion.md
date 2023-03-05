# Privilage escaletion - NO ESEMPIO

> Cos'e' un attacco di tipo Privilage escaletion? 

Un attacco di tipo Privilage escaletion si divide in due rami Privilage escaletion verticale e orizzontale.


> Privilage escaletion verticale 

L'attaccante puo' accedere a degli endpoints protetti o eseguire azioni nel sit, senza avere nessun permesso iniziale

url: https://sito.com/admin

oppure

url: https://sito.com/admin?admin=true


> Privilage escaletion orizzontale 

L'attaccante puo' accedere a degli endpoints protetti o eseguire azioni nel sit, con dei privilegi iniziali

url: https://sito.com/aggiunngi-prodotto/?categoria=informatica&name=pc ( l'utente puo' aggiungere prodtto solo nella sezione casa)


# Tips per contrastare questa vunlerabilita'
- Usare sistemi come cookie o headers negli endpoints che devono essere **protetti**
- Non avere fiducia sulla gestione
