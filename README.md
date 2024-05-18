# Excel Autostart

## Altes Autostart-Skript löschen

Das alte Skript im Autostart für Chrome wird nicht mehr benötigt. Mit dem Befehl kannst du es löschen:
```bash
sudo rm /etc/xdg/autostart/chromium.desktop
```
(Kann sein, dass du die Datei ohne "p" erstellt hast; dann lass es auch im Befehl oben weg)

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

-   In der Datei `firefox.desktop`, ersetze in der letzten Zeile `pi` durch den Benutzernamen, den du eingerichtet hast (falls du ihn nicht weißt: steht z.B. in der Kommandozeile vor dem @).

## Installation
Installiere alle notwendigen Bibliotheken mit
```bash
bash install.sh
```
(Wenn ein Fehler wegen fehlender Rechte auftritt, probiere den gleichen Befehl mit `sudo` am Anfang aus). Das Skript kopiert auch die Datei `firefox.desktop` an die richtige Stelle, sodass Firefox automatisch startet. Starte den Pi neu und teste, ob der Autostart funktioniert.