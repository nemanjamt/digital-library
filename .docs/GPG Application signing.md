# 🔐 GPG Application Signing

## 🇬🇧 English

This stage ensures the application's integrity and authenticity by using GPG to sign the built `.tgz` package.

### Steps:
1. Checks for required tools (`gpg`, `npm`).
2. Ensures a GPG key exists or generates a new one using `$GPG_NAME` and `$GPG_EMAIL`.
3. Installs dependencies and builds the app with `npm`.
4. Packages the app using `npm pack`.
5. Signs the `.tgz` archive using GPG with a detached signature.
6. Exports the public key.
7. Verifies the signature and prints validation status.
8. Moves the signature and package to `.report/general-report/`.

### Artifacts:
- `<package>.tgz`
- `<package>.tgz.sig`
- `public-key.asc`

---
---

# 🔐 GPG Potpisivanje aplikacije

## 🇷🇸 Srpski

Ova faza osigurava integritet i autentičnost aplikacije pomoću GPG potpisivanja `.tgz` paketa.

### Koraci:
1. Proverava da li su `gpg` i `npm` instalirani.
2. Proverava da li postoji GPG ključ ili kreira novi pomoću `$GPG_NAME` i `$GPG_EMAIL`.
3. Instalira zavisnosti i build-uje aplikaciju pomoću `npm`.
4. Pakuje aplikaciju pomoću `npm pack`.
5. Potpisuje `.tgz` fajl koristeći GPG (odvojen potpis).
6. Eksportuje javni ključ.
7. Verifikuje potpis i prikazuje status validacije.
8. Premešta potpis i paket u `.report/general-report/`.

### Artefakti:
- `<package>.tgz`
- `<package>.tgz.sig`
- `public-key.asc`
