# Python Geldautomaten-Simulation (ATM System)

Eine modulare, objektorientierte Geldautomaten-Simulation, entwickelt mit Python und SQLite.

## Funktionen
- Sicherer Login: Überprüft den Benutzernamen und erstellt eine Sitzung.
- Transaktionen: Sicheres Ein- und Auszahlen von Geld.
- Datenbankintegration: Nutzt SQLite zur Speicherung von Konten und zur Protokollierung des Transaktionsverlaufs.
- Kontoauszug: Exportiert einen formatierten Kontoauszug als `.txt`-Datei für den Benutzer.
- Saubere Architektur: Logisch aufgeteilt in Module (Models, Database, Scripts).

## Projektstruktur
- `main.py`: Der Einstiegspunkt und die Benutzeroberfläche.
- `models/`: Enthält die Klasse `BankAccount` (Geschäftslogik).
- `database/`: Verwaltet den dynamischen Pfad zur Datenbank.
- `scripts/`: Hilfsskripte zum Einrichten und Füllen der Datenbank (`setup_database.py` etc.).

## Ausführungshinweise
1. Klonen Sie das Repository auf Ihren lokalen Rechner.
2. Stellen Sie sicher, dass Python installiert ist.
3. Beim ersten Start muss die Datenbank initialisiert werden:
   ```bash
   python scripts/setup_database.py