# Excel Autostart


## Herunterladen

Klone das Repository hier mit dem Befehl
```bash
git clone https://github.com/johboe/excel_autostart.git
```
und gehe in das Verzeichnis mit
```bash
cd excel_autostart
```

## Notwendige Anpassungen

-   In der Datei `config.py`: Passe `excel_url`, `username` und `password` an. Das sollte entweder über eine grafische Oberfläche gehen, wenn du die Datei über den Explorer öffnest, oder alternativ über die Kommandozeile mit nano:
    ```bash
    nano config.py
    ```

-   In der Datei `firefox.desktop`, ersetzt in der letzten Zeile `pi` durch den Benutzernamen, den du eingerichtet hast (falls du ihn nicht weißt: steht z.B. in der Kommandozeile vor dem @).

## Installation
Installiere alle notwendigen Bibliotheken mit
```bash
bash install.sh
```
Das Skript kopiert auch die Datei `firefox.desktop` an die richtige Stelle, sodass Firefox automatisch startet.