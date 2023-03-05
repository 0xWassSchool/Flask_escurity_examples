# OS Injection ( Command injection )


> Cos'e' un attacco di tipo OS injection? 

Un attacco di tipo Os injection e' un attacco che prevede che l'attaccante inserisca dei comandi che andranmo eseguiti sull'os. Questa problematica e' sopratutto riscontrata nell'URL 


*Esempio*:

url: `https://sito.com/prodotto/?name=echo ciao && ls`

Response: 

```
Prodotto non trovato

Ciao 

ls della dir
```

# A cosa puo' portare un attacco del tipo OS Injection? 
1. Eseguire comandi all'interno del OS
2. Poter controllare parzialmente o totalmente ( dipende dai permessi ) un web server


# Tips per contrastare questa vulnerailta'
- Controllare il tipo della query 
- Controllare se ci sono spazi o simboli come &, |
