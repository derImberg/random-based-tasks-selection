# random-based-tasks-selection
English version below
## Was kann das Tool?
Dieses Tool wählt zufallsbasiert eine der Aufgaben aus, die in der Excel-Datei 'Aufgabenliste.xlsx'
enthalten ist.

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

## What can the tool do?
This tool randomly selects one of the tasks contained in the Excel file 'Aufgabenliste.xlsx'.
file.

Completed tasks are saved in a text file and are not considered anymore. 
no longer taken into account. It is possible to close the tool
and continue calculating at a later time. 

The exel file contains the list of all tasks with a unique assignment within the exercise, 
as well as a global consecutive number, for comparison with the text file.

With the Restart button the current progress can be deleted again and each task can be randomly selected again.
each task randomly.

## How to start the tool?

Use either an IDE of your choice (e.g. Pycharm) or start the tool via the console.
Check which Python version is installed or download the latest Python version:

`python<version number> random-based-tasks-selection.py`.

Make sure that the necessary packages are installed. If not, copy the following command
into the console:
* For tkinter: pip install tk
* For pandas: pip install pandas

If you are using the Anaconda distribution:
* For tkinter: conda install -c anaconda tk
* For pandas: conda install -c anaconda pandas

