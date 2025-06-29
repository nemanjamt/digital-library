# SonarQube 

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
