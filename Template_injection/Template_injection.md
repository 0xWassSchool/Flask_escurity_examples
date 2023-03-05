# Template Injection


> Cos'e' un attacco di tipo Template Injection?

Un attacco di tipo Template Injection e' un attacco che prevede che l'attaccante esegua un payload del tipo di codice che possa essere PHP, Python e Ruby dipende dal web server cosa sfrutta


*Esempio*:

url: https://sito.com/content/?username={{app.config}}

Response:

I configs della web app ( in questo caso config della web app - flask )

# A cosa puo' portare un attacco di tipo Template Injection?

1. Puo' portare ad eseguire codice remoto quindi poter avere un controllo parziale sulla web app ed il server

# Tips per contrastare questa vulnerabilita'
- Filtrare gli input e non far che si possa eseguire qualsiasi tipo di codice 
- Encodare il risultato della query