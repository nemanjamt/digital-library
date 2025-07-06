# 🛡️ Security Pipeline Outline & Threat Mitigation
<a id="english"></a>

## 🔧 Overview
This pipeline integrates automated security checks into your CI/CD flow using containerized tools to protect applications from a range of cybersecurity threats across multiple stages of the software development lifecycle.

## 1. Endpoint Security Testing (OWASP ZAP)
### 🧪 Description:
ZAP performs:

- API Scan: Targets your API endpoints.

- Full Scan: Crawls and fuzzes the entire application surface.

### 🛡️ Threats Mitigated:
- Injection attacks (SQL, XSS)

- Broken authentication

- Security misconfigurations

- Sensitive data exposure

- Unvalidated redirects and forwards

- Insecure API implementations

## 2. Static Code Analysis (SonarQube)
### 🧪 Description:
Analyzes source code for bugs, code smells, and vulnerabilities using static analysis techniques.

### 🛡️ Threats Mitigated:
- Logic flaws

- Hardcoded secrets and credentials

- Insecure functions or unsafe libraries

- Buffer overflows, race conditions

- Insufficient input validation

## 3. Dependency Vulnerability Scanning (OWASP Dependency-Check)
### 🧪 Description:
Scans third-party libraries and frameworks for known vulnerabilities by checking against public CVE databases.

### 🛡️ Threats Mitigated:
- Supply chain attacks

- Zero-day vulnerabilities in dependencies

- Outdated or unpatched libraries


## 4. Packaging and GPG Signing
### 🧪 Description:
Signs the final artifact with GPG. Verifiers can confirm the origin and integrity using the public key and signature.

### 🛡️ Threats Mitigated:
- Tampering during deployment or distribution

- Man-in-the-middle (MITM) attacks

- Repackaged malware-injected binaries

- Impersonation attacks

## 5. Final Report Generation
### 🧪 Description:
Collates results from all tools into a single unified report for analysis, auditing, and traceability.

### 🛡️ Benefits:
- Improved visibility of risks

- Easier audit trails for compliance (e.g., ISO 27001, SOC2)

- Centralized decision-making support

<br/>

# 🛡️ Pregled sigurnosnog pipeline-a i zaštita od pretnji

<a id="srpski"></a>

## 🔧 Opšti Opis
Ovaj sigurnosni pajplajn integriše automatizovane bezbednosne provere u CI/CD tok razvoja koristeći Docker kontejnere sa specijalizovanim alatima. Svaka faza štiti aplikaciju od različitih tipova sajber pretnji tokom razvoja i distribucije softvera.

## 1. Testiranje bezbednosti krajnjih tačaka (OWASP ZAP)
### 🧪 Opis:
ZAP vrši:

- API skeniranje: testira REST/HTTP API krajnje tačke.

- Puno skeniranje: skenira ceo interfejs aplikacije.

### 🛡️ Pretnje protiv kojih štiti:
- SQL i XSS injekcije

- Pogrešna autentifikacija i sesije

- Neispravne sigurnosne konfiguracije

- Izlaganje osetljivih podataka

- Nedovoljna validacija unosa

- Nesigurne API implementacije

## 2. Statička Analiza Koda (SonarQube)
### 🧪 Opis:
Analizira izvorni kod i pronalazi ranjivosti, bagove i loše prakse u pisanju koda.

### 🛡️ Pretnje protiv kojih štiti:
- Logičke greške

- Hardkodovane lozinke i tajne

- Upotreba nesigurnih funkcija

- Prelivi bafera i trke procesa

- Nedovoljna obrada korisničkog unosa

## 3. Skeniranje Ranljivosti u Zavistnostima (OWASP Dependency-Check)
### 🧪 Opis:
Skener detektuje poznate ranjivosti u biblioteka koristeći CVE bazu podataka.

### 🛡️ Pretnje protiv kojih štiti:
- Napadi kroz lanac snabdevanja (Supply Chain)

- Poznate ranjivosti u bibliotekama

- Upotreba zastarelih/nezakrpljenih zavisnosti

## 4. Pakovanje i GPG Potpisivanje
### 🧪 Opis:
Aplikacija se pakuje i digitalno potpisuje pomoću GPG ključa. Objavljuje se javni ključ i potpis radi provere integriteta.

### 🛡️ Pretnje protiv kojih štiti:
- Izmena fajlova u transportu

- Man-in-the-middle (MITM) napadi

- Lažni (maliciozni) binarni fajlovi

- Imitacija autora softvera

## 5. Generisanje Završnog Izveštaja
### 🧪 Opis:
Konsoliduje rezultate iz svih alata u jedinstven izveštaj za pregled i dalje delovanje.

### 🛡️ Prednosti:
- Puna vidljivost nad ranjivostima

- Lakša revizija i usklađenost sa standardima (ISO 27001, SOC 2 itd.)

- Jasna baza za donošenje bezbednosnih odluka
---