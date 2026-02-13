# Kidney Disease Classification using CNN

Dieses Projekt nutzt Deep Learning zur Klassifizierung von Nierenerkrankungen basierend auf Bilddaten.

## Worflows

1. Update config.yml
2. Update secrets.yml [Optional]
3. Update params.yml
4. Update entity 
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yml
10. app.py


## 🚀 How to run?

### Voraussetzungen
Stelle sicher, dass du [Anaconda](https://www.anaconda.com/) oder [Miniconda](https://docs.conda.io/en/latest/miniconda.html) auf deinem System installiert hast.

### SCHRITT 01 - Repository klonen
Klonen Sie das Projekt und navigieren Sie in das Projektverzeichnis:

```bash
    git clone https://github.com/Rustyfull/kidney-disease-classification.git
```
```bash
  cd kidney-disease-classification
````
### SCHRITT 02 - Conda Umgebung erstellen
Erstellen Sie eine isolierte Umgebung mit Python 3.8:
```bash
    conda create -n cnncls python=3.8 -y
```
Aktivieren Sie die Umgebung
```bash
    conda activate cnnls
```

### SCHRITT 03 - Abhängigkeiten installieren
Installieren Sie alle notwendigen Bibliotheken aus der requirements.txt
```bash
    pip install -r requirements
```

### SCHRITT 04 - Anwendung starten
Führen Sie die Flask-Applikation aus:
```bash
    python app.py
```
Öffnen Sie nun ihren Browser unter [localhost:5000](http://localhost:5000)

