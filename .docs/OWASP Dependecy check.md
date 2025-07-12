# OWASP Dependency Check
**Command:**
```bash
/usr/share/dependency-check/bin/dependency-check.sh \
  --project DIGITAL_LIBRARY_PROJECT \
  --scan /src \
  --format ALL \
  --out /reports \
  --nvdApiKey <API_KEY>
```

## Description:
This command analyzes all project dependencies to find security vulnerabilities (CVEs).

It uses the NVD (National Vulnerability Database) as a data source, with the nvdApiKey used as the access key.

The tool scans the entire /src directory.

It generates reports in all available formats (JSON, XML, SARIF, CSV) and saves them in the /reports folder.

When the scan is finished, it creates a file: /.done/dependency-scan.done.
Other services use this file for synchronization.

The scan is run from a Docker container defined in the owasp-dependency-check service.

## Logs and Reports:
Reports are stored in the following folder (relative to /src):
../.dependency-check/reports/

Logs are not explicitly defined at the moment, but they can be viewed in the container output, or configured additionally if needed.
<br><br><br>


# OWASP provjera zavisnosti
## Komanda:
```bash
/usr/share/dependency-check/bin/dependency-check.sh \
  --project DIGITAL_LIBRARY_PROJECT \
  --scan /src \
  --format ALL \
  --out /reports \
  --nvdApiKey <API_KEY>
```
  
## Opis:

Analizira sve projektne zavisnosti radi otkrivanja bezbjednosnih ranjivosti (CVEs).

Koristi NVD (National Vulnerability Database) kao izvor podataka, koristeci nvdApiKey kao API kljuc za pristup istoj.

Skenira cijeli direktorijum /src.

Generiše izveštaje u svim dostupnim formatima (JSON, XML, SARIF, CSV) u /reports.

Označava završetak skeniranja kreiranjem fajla /.done/dependency-scan.done, koji druge komponente koriste za sinhronizaciju.

Pokreće se iz Docker kontejnera definisanog u servisu owasp-dependency-check.

## Logovi i Izveštaji:

Izvještaji se nalaze u direktorijumu(u odnosu na src): ../.dependency-check/reports/

Logovi trenutno nisu eksplicitno navedeni, ali se standardno mogu vidjeti  iz izlaza kontejnera ili dodatno konfigurisati.


