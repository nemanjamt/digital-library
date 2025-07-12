# SonarQube 

**Command:**

```bash
sonar-scanner \
  -Dsonar.projectKey=<project_key> \
  -Dsonar.sources=./src \
  -Dsonar.host.url=http://sonarqube:9000 \
  -Dsonar.login=$SONAR_TOKEN
```
## Description:
This command runs an analysis of the project's source code to find problems related to code quality, security issues, bugs, and duplicated code.

SonarQube is a server that hosts a web interface and stores the analysis results.

SonarScanner is a tool used to send the source code to the SonarQube server for analysis.

The authentication token (SONAR_TOKEN) is generated and used to connect securely to the SonarQube server.

The analysis starts after the SonarQube server is up and running.

## Logs and Reports:
The analysis results can be viewed on the SonarQube web interface (port 9000).
In the report generation script, it uses this endpoint:
http://sonarqube:9000/api/hotspots/search

The SonarScanner service writes the analysis status to a file:
/.done/sonarscanner.done
This file is used for synchronization with other services.



**Komanda:**

```bash
sonar-scanner \
  -Dsonar.projectKey=<project_key> \
  -Dsonar.sources=./src \
  -Dsonar.host.url=http://sonarqube:9000 \
  -Dsonar.login=$SONAR_TOKEN
```

## Opis:

Pokreće analizu izvornog koda projekta radi pronalaženja slučajeva vezanih za kvalitet koda, bezbjednosnih ranjivosti, bug-ova i koda koji se ponavlja.

Sonarqube je server koji hostuje web interfejs i čuva rezultate analiza.

Sonarscanner je alat koji se koristi za slanje izvornog koda na SonarQube server radi analize.

Token za autentifikaciju (SONAR_TOKEN) se generiše i koristi za autorizaciju prema SonarQube serveru.

Analiza se pokreće nakon što je SonarQube server dostupan.

## Logovi i Izveštaji:

Rezultati analize su dostupni na SonarQube web interfejsu na portu 9000, dok konkretno u skripti za generisanje izvještaja , gađa se endpoint
http://sonarqube:9000/api/hotspots/search

Sonarscanner servis zapisuje status završene analize u fajl /.done/sonarscanner.done, koji služi za sinhronizaciju sa ostalim servisima.
