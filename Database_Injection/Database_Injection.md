# Database injection 


> Cos'e' un attacco di tipo Database injection?

Un attacco di tipo Database injection e' un attacco che prevede che il payload della richiesta sia indirizzato al database com l'ausilio di comandi per il caso di database SQL o di azioni come shell commands nel caso di MongoDB

> Vettori di attacco:
1. Commenti
2. Comandi

> SQL injection 

Un attacco che prevede la SQL injection e' un attacco che sfrutta la struttura SQL ovvero la injection di comandi 

*Esempio*:

url: https://sito.com/prodotto?categoria=Prodotti comandi da eseguire

> No SQL databases
> 
Un attacco che prevede che venga attaccato un Database NOSQL potrebbe risultare piu' complicato, perche' potrebbe essere che un database come per dire mongo non sia usabile la struttura SQL infatti per provare un attacco di questo tipo e' usuale attaccare la shell del databsae

*Esempio*:

url: https://sito.com/prodotto?categoria=show-dbs

response:

Database1
Database2


# A cosa puo' portare un attacco di tipo Databsae injection? 

1. Avere accesso alla parte di storage della web app ovvero gli account degli utenti o anche dati molto sensibili\
2. Poter sovrascrivere un intero database o cambiare i suoi parametri di sicurezza come ip accettati o user permission


# Tips per contrastare questa vulnerabilita'
- Filtrare gli input ( non accettare keywords come SELECT, ADD )
- Rendere il database un posto sicuro con per dire opzioni di sicurezza aggiuntive sul suo contenuto