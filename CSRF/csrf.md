# CSRF

> Cos'e' un attacco di tipo CSRF?

Un attacco di tipo CSRF e' un attacco che prevede che l'utente esegua una azione che in realta' non voleva / doveva eseguire per esempio il cambio di una email o una transazione bancaria

*Esempio*:

Attaccante manda alla vittima un link: 
http://attacckersite.it/

dentro il sito l'attccante ha scritto un preciso codice html per fare in modo che la vittima cliccando sul link invii una richiesta al sito prefissato dall'attaccante 


# A cosa puo' portare un attacco di tipo CSRF?

1. Cambio di dati utente senza il volere di farlo ( Emeail, Password, Username )
2. Eseguire azioni invonotarie e qundi mettere a rischio dati sensibilit


# Tips per contrastare queste vulnerabilita'
- Token CSRF sono dei token che vengono generati lato server e vengono usati per richieste di alto calibro 
- Fare dei controlli sulla sorgente del sito
- Sfruttare il SameCookie ( https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions )
