# SSRF ( Server-side request forgery )


> Cos'e' un attacco di tipo SSRF? 

Un attacco di tipo SSRF e' un attacco che punta a far inviare al server delle richieste http indesiderate, queste richieste possono essere sia interne che esterne


> Quali tipi di attacchi SSRF esistono?
1. Attacchi sul server stesso
2. Attacchi contro server esterni

> Attacchi sul server stesso

*Esempio*:

Richiesta reale:

```
POST /prodotti HTTP/1.1
Content-Type: application/x-www-form-urlencoded

prodotto=https://api.com/prodotto/?p=iphone12max
```

Richiesta contraffatta:

```
POST /prodotti HTTP/1.1
Content-Type: application/x-www-form-urlencoded

prodotto=http://127.0.0.1:5000/admin
```

> Attacchi contro server esterni

```
POST /prodotti HTTP/1.1
Content-Type: application/x-www-form-urlencoded

prodotto=http://server-attaccante/admin
```

# A cosa puo' portare un attacco di tipo SSRF?

1. A fare in modo che l'attaccante abbia accesso a risorse del sito protette


# Tips per contrastare questa vulnerabilita'
- Filtrare il tipo di input o query
- Encodare il data
- Usare headers di sicurezza specifici auth headers
