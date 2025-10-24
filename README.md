
## Link naar repo en SSH key
- https://github.com/ihssane-1103386/Security5
- git@github.com: ihssane-1103386/Security5.git

## Installatie:
1. python -m venv .venv 
2. source venv/bin/activate (mac en linux) of: .venv\Scripts\Activate.ps1 (windows)
3. pip install -r requirements.txt 
4. start python app.py en klik op de http://127.0.0.1:5000/ link in de terminal

## Gebruiksaanwijzing: 
1. **Sleutel genereren:** 
- Klik op "genereer nieuwe sleutel", Je kan de output ook kopiëren door op "kopieer sleutel" te klikken.
2. **Tekst encrypten:** 
- Voer een tekst in, klik dan op "versleutelen". Je kunt de output kopiëren door op "kopieer resultaat" te klikken.
3. **Tekst decrypten:** 
- Voer de gekopieerde output van de versleuteling in het Tekst veld, en klikt daarna op "ontsleutelen". Het originele bericht wordt weergegeven onder "Resultaat".
- **(Zorg ervoor dat dezelfde key aanwezig is, en niet verwijderd of opnieuw gegenereerd wordt).**

## Methode & encryptie:
De applicatie maakt gebruik van symmetrische encryptie, wat betekent dat dezelfde sleutel wordt gebruikt voor zowel het versleutelen als ontsleutelen van een bericht.

Voor de encryptie is de Python cryptography library gebruikt.
Ik heb gebruik gemaakt van html, css, en een flask-app waar de cryptography is toegevoegd.
Er is geen database aanwezig, dus de keys worden niet in het systeem zelf opgeslagen. 
Wel is er een stukje javascript toegevoegd aan de html-pagina, om de output te kunnen kopiëren naar je klembord. 
De cryptography die ik heb gebruikt implimenteert zelf al veel beveiliging over  het versleutelde bericht, maar de key mag niet openbaar gemaakt worden. 

### Ik heb gebruik gemaakt van "Fernet": 

- Waarom Fernet? 
- - Veilig, betrouwbaar en goed gedocumenteerd.
- - Fernet zorgt ervoor dat je je bericht makkelijk kan versleutelen en ontsleutelen.
- - Combineert automatisch AES-encryptie (geheime gegevens versleutelen)
- - HMAC-authenticatie (controleren dat de data niet gewijzigd is). 
- - Voegt een IV toe, zodat hetzelfde bericht altijd anders wordt versleuteld.

### AES
AES (advanced encryption standards). 
Dat is een wereldwijd gebruikte encryptie algorithme. Het versleutelt data in blokjes van 128 bits (16 bytes).
Deze 16 bytes worden in een soort vierkant van 4×4 geplaatst, dat een state matrix genoemd wordt. 
In die matrix voert AES verschillende wiskundige bewerkingen uit om de data te versleutelen, zoals bv het verschuiving en mengen van de bytes.
De sleutellengte kan 128, 192 of 256 bits zijn. Hoe langer de sleutel, hoe moeilijker het is om de versleuteling te kraken. Fernet gebruikt 256-bit AES, wat extra veilig is.

### HMAC
HMAC (Hash-based message authentication) authenticatie. Dit is belangrijk om er zeker van te zijn dat de sleutel en versleutelde tekst niet aangepast zijn tijdens het versturen. 
HMAC heeft 2 onderdelen; een key en een hash-functie. Met fernet wordt er standaard gebruik gemaakt van de HMAC-SHA256 functie, zodat er eerst wordt gecontroleerd of de encryptie klopt en niet aangepast is, voordat het bericht ontsleuteld wordt. 

### Proces van Fernet
1. Een Fernet encryptie begint dus bij het aanmaken van een sleutel (die gebruikt wordt voor het versleutelen en ontsleutelen van een bericht --> symmetrische encryptie). 
2. Daarna wordt de oorspronkelijke tekst door de AES versleuteld met gebruik van de key en een IV (initialization vector --> zorgt ervoor dat hetzelfde stukje tekst altijd anders wordt versleuteld).
3. Een HMAC wordt berekend over het versleutelde bericht, met inclusief een tijdstempel, dit maakt het mogelijk om later te controleren of een bericht nog geldig is.
4. Er wordt met dit alles een fernet token gemaakt, die dan verzonden kan worden. 
5. Voordat het bericht wordt ontsleuteld, wordt er eerst door de HMAC gecontroleerd of alles nog klopt. Als er toch nog iets aangepast is, is het niet mogelijk om het bericht te ontsleutelen. 
Als alles wel klopt, wordt het bericht ontsleuteld met dezelfde sleutel en IV, en wordt het originele bericht getoond. 

### Kerckhoffs’s Principe:
Deze principe houdt in dat een veilig encryptiesysteem niet afhankelijk mag zijn van geheimhouding van de code of het algoritme, maar dat de veiligheid alleen moet afhangen van de sleutel.
- Ik gebruik openbare, vertrouwde algoritmen: AES en HMAC via de Python cryptography library, die open-source is.
- Iedereen kan dus zien hoe Fernet werkt, omdat het openbare informatie is. 
- De veiligheid van de versleuteling hangt af van de sleutel die de gebruiker genereert. De sleutel wordt niet opgeslagen in een database, alleen de gebruiker heeft toegang tot de sleutel. Dus zelfs als iemand anders toegang heeft tot de code of het algoritme, 
kan het bericht nogsteeds niet ontsleuteld worden. 

  
  
## bronnen: 
- https://www.geeksforgeeks.org/computer-networks/advanced-encryption-standard-aes/
- https://www.okta.com/identity-101/hmac/
- https://cryptography.io/en/latest/fernet/
- https://masteringjs.io/tutorials/fundamentals/copy-to-clipboard#:~:text=To%20copy%20text%20from%20an,current%20selection%20to%20the%20clipboard.
- https://www.geeksforgeeks.org/python/fernet-symmetric-encryption-using-cryptography-module-in-python/
- https://chatgpt.com/share/68f7f0f3-becc-8013-bdc0-72145e5a8936
- https://chatgpt.com/share/68f7f720-34e4-8013-9429-5fcc7ed05782


