# Directory traversal

> Cos'e' un attacco di tipo Directory traversal?

Un attacco di tipo Directory traversal e' un attacco che punta a avere accesso a fare un list di ua dir specifica

*Esempio*

url: https://sito.com/prodotto?file=../../../etc/password

response: 
Il list dir della cartella /etc/password

# A cosa puo' portare un attacco di tipo Directory traversal? 
1. Avere un list delle potenziali directory attaccate
2. Ottenere molteplici informazioni sulla struttura totale della web app


# Tips per contrstare questa vulnerabilita'
- Filtare gli input utente
- Appendare il risultato della query a una dir esistente
 