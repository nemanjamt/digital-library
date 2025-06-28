# OWASP Dependency Check

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


