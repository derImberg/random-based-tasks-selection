# random-based-tasks-selection
## Was kann das Tool?
Dieses Tool wählt zufallsbasiert eine der Dinexite-Aufgaben aus, um immer wieder andere
Themen zu bearbeiten.

Abgeschlossene Aufgaben werden in einer Text-Datei gespeichert und werden 
nicht mehr berücksichtigt. Es ist möglich das Tool zu schließen
und an einem späteren Zeitpunkt weiter zu rechnen. 

Die Exel-Datei enthält die Liste aller Aufgaben mit einer eindeutigen Zuordnung innerhalb der Übung, 
sowie einer globalen fortlaufenden Nummer, zum Abgleich mit der Text-Datei.

Mit dem Restart-Button kann der aktuelle Fortschritt wieder gelöscht werden und es kann wieder
jede Aufgabe zufällig gewählt werden.

## Wie wird das Tool gestartet?

Nutze entweder eine IDE deiner Wahl (z.B. Pycharm) oder starte das Tool über die Konsole.
Überprüfe welche Python Version installiert ist oder lade die aktuelle Python Version herunter:

`python<Versionsnummer> random-based-tasks-selection.py`

Achte darauf, dass die notwendigen Pakete installiert sind. Falls nicht, kopiere folgenden Befehl
in die Konsole:
* Für tkinter: pip install tk
* Für pandas: pip install pandas

Solltest du die Anaconda-Distribution nutzen:
* Für tkinter: conda install -c anaconda tk
* Für pandas: conda install -c anaconda pandas



