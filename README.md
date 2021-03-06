# Userguide
_____________________________________________________________________________________________________________________

edjuSQL wurde entwickelt, um Studierenden beim erlernen von SQL zu helfen.
Die folgende Anleitung soll beim Umgang mit dem Tool helfen und so den Einstieg erleichtern. Dabei wird auf die Grundlegende Funktionalität eingegangen.
Um den Studenten in Zukunft den Einstieg so einfach wie möglich zu machen, wird es (vorraussichtlich) zum nächsten Semester einen fertig eingerichteten Jupyterhub Server geben, auf dem sich die Studenten direkt einloggen können. Dadurch soll die doch recht 


# Jupyter und IPython
_____________________________________________________________________________________________________________________

IPython ist eine Python-Bibliothek, die ursprünglich dazu gedacht war, die standard Konsole zu verbessern. Im Jahr 2011, zehn Jahre nach der ersten Veröffentlichung, wurde das IPython Notebook vorgestellt. Diese webbasierte Schnittstelle zu IPython
kombiniert Code, Text, mathematische Ausdrücke, Inline-Plots, interaktive Diagramme, Widgets,
grafische Oberflächen und Weiteres in einem eigenständigen, gemeinsam nutzbaren Webdokument. Diese
Plattform bietet einen idealen Zugang zu interaktivem wissenschaftlichem Rechnen und Datenanalyse.
IPython ist für Forscher, Ingenieure, Datenwissenschaftler  und Studenten zu einer attraktiven Arbeitsumgebung geworden. 

Innerhalb weniger Jahre erlangte IPython eine sehr starke Popularität unter Wissenschaftlern und Experten in der Entwicklergemeinschaft. Mit der Zeit wurden - neben Python - 
immer mehr Programmiersprachen untestützt. Im Jahr 2014 gaben die IPython-Entwickler das Jupyter-Projekt bekannt,
eine Initiative, die ins Leben gerufen wurde, um die Implementierung des Notebooks zu verbessern und es 'by design' sprachunabhängig zu gestalten. Der Name des Projekts spiegelt die Bedeutung von drei der wichtigsten Sprachen wider: Julia, Python und R.
Das Jupyter Notebook ist eine webbasierte interaktive Umgebung, die Code und Rich Text kombiniert,
Bilder, Videos, Animationen, mathematische Gleichungen, Diagramme, Karten, interaktive Figuren und
Widgets und grafische Benutzeroberflächen in einem einzigen Dokument. 
Selbst dieses Dokument wurde im Jupyter Notebook erstellt.


# Installation
_____________________________________________________________________________________________________________________


Bevor es los gehen kann, müssen zunächst die Voraussetzungen geschaffen werden. Hierzu zählt die Installation von:

-Python

-Jupyter

-cx_Oracle

-Oracle Instant Client

-Watchguard

-Sonstiges


## Python
_____________________________________________________________________________________________________________________
Je nach Betriebssystem kann es Unterschiede bei der Installation geben. Eine sehr gute Anleitung zur Installation von Python findet man z.B. hier: https://realpython.com/installing-python/

## Jupyter
_____________________________________________________________________________________________________________________
Bei der Installation von Jupyter steht man vor der Entscheidung, ob man 'von Hand' alle notwendigen Pakete über z.B. pip installiert, oder ob man das recht umfangreiche Programmpaket 'Anaconda' der Firma Continuum einrichtet. Auf der Jupyter Homepage wird zur Installation von Anaconda geraten. Folgende Links können hierzu hilfreich sein: https://repo.continuum.io/ & https://jupyter.org/install

## cx_Oracle
_____________________________________________________________________________________________________________________
Ähnlich dem JDBC Treiber, ist cx_Oracle ein Datenbanktreiber, welcher für die Interaktion zwischen einem Programm und einer Oracle Datenbank verwendet werden kann. cx_Oracle ist sehr gut dokumentiert. Auf den folgenden Seiten findet man alle notwendigen Informationen und weitere Hinweise: https://oracle.github.io/python-cx_Oracle/ & https://cx-oracle.readthedocs.io/en/latest/index.html

## Oracle Instant Client
_____________________________________________________________________________________________________________________
Oracle Instant Client beinhaltet verschiedene Tools und Bibliotheken zum Erstellen von Anwendungen auf einer Oracle Datenbank.
Beim setzen der entsprechenden Umgebungsvariable ist darauf zu achten, dass keine anderen Oracle Anwendungen vorher gefunden werden können.
Anschließend kann es hilfreich sein im Hauptordner einen Unterordner mit dem Namen 'network' anzulegen ,darin den Ordner 'admin' zu erstellen und eine Datei mit dem Namen 'tnsnames.ora' anzulegen. Die Datei kann für die Spezifikation der Verbindungsparameter genutzt werden. 
Weitere Informationen zu diesem recht umfangreichen Programmpaket sind hier zu finden: https://docs.oracle.com/cd/E83411_01/OREAD/installing-oracle-database-instant-client.htm#OREAD348

## Watchguard
_____________________________________________________________________________________________________________________
Um auch ausserhalb des HWR Netzwerks Zugriff auf die Oracle Instanz zu bekommen, muss der Watchguard client installiert werden. Eine detaillierte Anleitung ist unter https://www.it.hwr-berlin.de/anleitungen/vpn/ zu finden. 

## Sonstiges
_____________________________________________________________________________________________________________________
Einige der benötigten Python Module sind in der requirements.txt hinterlegt. Sie können über pip mit dem befehl

pip install -r requirements.txt

installiert werden. 


An dieser Stelle soll erwähnt werden, dass hier nur ein kleiner Überblick gegeben wurde. Die genannten Webseiten sind jedoch gute Anlaufstellen für weitere Recherchen. Folgend ist eine Liste zusammengestellt, welche weitere notwendige Python Module nennt:

### Jupyter Widgets
_____________________________________________________________________________________________________________________
ipywidgets bieten die Möglichkeit innerhalb der Jupyter Umgebung mit interaktiven Kontrollelementen (Widgets) zu arbeiten. Diese Widgets lassen sich zu komplexen User Interfaces zusammenstellen. 

### SQLAlchemy
_____________________________________________________________________________________________________________________
SQLAlchemy wird von vielen Webseiten, unter anderem auch bekannten wie z.B. Yelp!, reddit und DropBox genutzt. SQLAlchemy besteht aus zwei verschiedenen Komponenten, dem so genannten Core und dem ORM. Der Kern selbst ist ein voll ausgestattetes SQL-Abstraktionstool, welches eine Abstraktionsschicht über eine Vielzahl von DBAPI-Implementierungen bereitstellt, sowie eine SQL Expression Language. Der Object- relationale Mapper (ORM) ist ein optionales Paket, das auf dem Core aufbaut. Viele Anwendungen basieren ausschließlich auf dem Core und verwenden das SQL-Expressionssystem, um eine präzise und genaue Kontrolle über Datenbankinteraktionen zu gewährleisten.

# edjuSQL
_____________________________________________________________________________________________________________________

Das Modul qedjuQSL ist im Rahmen des Kurses 'Projekt Software Engineering' entstanden. Es soll Studenten die Möglichkeit bieten, SQL- Abfragen auf Richtigkeit zu prüfen. Hierfür gibt der Student seine Oracle Zugangsdaten ein und kann über ein Dropdown- Menü die zu bearbeitende Aufgabe auswählen. In einem Textfeld kann nun die SQL- Abfrage geschrieben werden. Nachdem der 'Check'- Button gedrückt wurde wird im Hintergrund die Abfrage überprüft und der Student bekommt das entsprechende Ergebnis ausgegeben. query_checker muss wie jedes andere Modul zunächst importiert werden. Der Aufruf "qc.disp()" lässt das Widget erscheinen: (Abbildung 1: Das Widget in Aktion)
![query_checker_widget.png](https://github.com/Salbinus/edjuSQL/edit/master/query_checker_widget.png)
Das Modul bietet in Verbindung mit der Erweiterung IPython-sql die Möglichkeit, direkt im Notebook SQL-Abfragen zu schreiben und sich die Ergebnisse anzeigen zu lassen. Hierfür muss die Funktion "get_creds()" zunächst instanziiert werden und der Instanz wird der Connectionstring als Wert zugewiesen. Das folgende Beispiel soll das verdeutlichen:

![My image](https://github.com/Salbinus/edjuSQL/edit/master/ipython_sql.png)

# Ressources
_____________________________________________________________________________________________________________________

Die initiale Idee zur Umsetzung kam durch folgende Blogposts von Danielle Chou und Sayat Satybaldiyev: 
- https://medium.com/@ZymergenTechBlog/tips-for-developing-user-facing-tools-in-jupyter-notebooks-1d71aa46aef7
- https://towardsdatascience.com/jupyter-magics-with-sql-921370099589


Diese Arbeit wäre jedoch nicht entstanden ohne all die anderen Quellen. Das Buch 'IPython Interactive Computing and Visualization Cookbook', von Cyrille Rossant(2018), war als weiterfürende Literatur essentiell.

Ganz allgemein sind natürlich die offiziellen Docs zu nennen:
- https://cx-oracle.readthedocs.io/en/latest/
- https://docs.python.org/3/

Für die Verbindung zwischen Python und Oracle war die Seite von Julian Dyke sehr hilfreich:
- http://www.juliandyke.com/Research/Development/UsingPythonWithOracle.php
Großer Dank gilt auch für Jason Grout, der innerhalb kürzester Zeit auf ein meine Frage geantwortet hat:
- https://github.com/jupyter-widgets/ipywidgets/issues/2291

