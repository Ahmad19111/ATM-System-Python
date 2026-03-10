# Professionelle Bank-API (FastAPI und SQLite)

Diese professionelle RESTful API wurde mit FastAPI entwickelt und nutzt SQLite zur persistenten Datenspeicherung. Das Projekt implementiert eine saubere Architektur, die die Geschäftslogik von der Webschnittstelle trennt.

## Funktionen
- RESTful Endpunkte: Die API bietet Schnittstellen für Kontostandsabfragen, Einzahlungen, Auszahlungen und den Abruf von Kontoauszügen.
- Datenvalidierung: Eingehende Anfragen werden mithilfe von Pydantic-Modellen auf Richtigkeit geprüft.
- HTTP-Statuscodes: Die API kommuniziert über standardisierte Statuscodes, wie 404 für nicht gefundene Konten oder 400 bei unzureichendem Guthaben.
- Datenbank-Logging: Jede Transaktion wird mit Betrag, Typ und Zeitstempel in einer SQLite-Datenbank protokolliert.
- Fehlerbehandlung: Das System erkennt fehlende Konten und verhindert ungültige Operationen durch logische Prüfungen.



## Projektstruktur
- api_server.py: Enthält die FastAPI-Anwendung und alle Endpunkt-Definitionen.
- models/bank_account.py: Beinhaltet die BankAccount-Klasse mit der gesamten Geschäfts- und Datenbanklogik.
- database/: Enthält die Konfiguration für den Pfad zur SQLite-Datenbank.
- tests/: Beinhaltet automatisierte Test-Suites für die Überprüfung der API-Funktionalität.

## Ausfuehrungshinweise

1. Installation der notwendigen Bibliotheken:
   pip install fastapi uvicorn httpx pytest

2. Starten des Servers:
   uvicorn api_server:app --reload

3. Interaktive Dokumentation:
   Nach dem Start ist die Swagger-Benutzeroberfläche unter http://127.0.0.1:8000/docs erreichbar.

## Tests ausfuehren
Zur Überprüfung der Systemintegrität können die automatisierten Tests wie folgt gestartet werden:
python -m pytest