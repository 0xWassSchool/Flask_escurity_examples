# File uploading

> Cos'e' un attacco di tipo File uploading?

Un attacco di File uploading e' un attacco che permette all'attaccante di caricare file diversi da tipo cui si aspetta il Server

> Quali modalita' di attacchi File uploading esistono?

1. Normal upload
2. File types
3. Config del server


> Normal upload:

Questo metodo si basa sul server che non controlla se il file e' in realta' quello che vuole ricevere

*Esempio*:

url: [POST] https://sitovulnerabile.com/upload

body:
file: shell.py

> File types

Questo metodo si basa su una errata validazione del file 

- File extenstion: Se la estensione del file non e' in quelle non accettate sara' possibile caricare il file senza nessun problema
- File extenstion obfuscation: La estensione e' nella lista nera quindi e' possibile provare a renderla offuscata
- File validation: Se il MIME della richieste e' l'unico campo di validazione del file potrebbe essere facilmente bypassabile

> Config del server

I config degli http servers sono dei file di configurazione per esempio nei server appache `.htaccess`, Questi nel lato di sicurezza servono per dare per esempio una lista di file accettati. Uno sviluppatore puo' caricare i suoi custom configs, questo potrebbe portare a molteplici vulnerabilita'

 # File uploading a cosa puo' portare?

1. L'attaccante puo' caricare ogni file che vuole sul server per esempio una Http Reverse Shell


# Tips per contrastare queste vulnerabilita'

- Controllare totalmente il file ( body e estensione, e non basarsi solo su header come il MIMETYPE )
- Non sovrascrivere i file di configurazione di un possibile Server se non si hanno le competenze adeguate