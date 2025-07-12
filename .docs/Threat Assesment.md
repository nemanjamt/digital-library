# 🛡️ Security Pipeline Outline & Threat Mitigation  
<a id="english"></a>

## 🔧 Overview  
This pipeline integrates automated security checks into your CI/CD flow using containerized tools to protect applications from a range of cybersecurity threats across multiple stages of the software development lifecycle.

---

## 1. Endpoint Security Testing (OWASP ZAP)  
### 🧪 Description:  
ZAP performs:  
- API Scan: Targets your API endpoints.  
- Full Scan: Crawls and fuzzes the entire web application surface.

### ⚔️ Attacks mitigated:  
- **LDAP Injection:** where malicious input manipulates backend queries or commands.  
- **Cross-Site Request Forgery (CSRF):** Tricks authenticated users into submitting unwanted actions.  
- **Insecure Direct Object References (IDOR):** Unauthorized data access by manipulating URLs or parameters.  
- **Security Misconfigurations:** Incorrect settings that expose sensitive information or functionality (e.g., open debug endpoints).  
- **Sensitive Data Exposure:** Detection of unencrypted or improperly handled secrets, passwords, tokens, or personal data.  
- **Broken Authentication and Session Management:** Weak login/session controls leading to session hijacking or account compromise.  
- **Directory Traversal:** Accessing restricted files by manipulating file paths.  
- **Unvalidated Redirects and Forwards:** Redirecting users to malicious sites or unintended pages.

### 🛡️ Threats mitigated:  
- Broken authentication/session control risks.  
- Security misconfigurations leading to privilege escalation or information leaks.  
- Exposure of sensitive data (PII, credentials).  
- Unvalidated redirects enabling phishing or malware distribution.  
- Vulnerable or misconfigured API endpoints allowing unauthorized operations.

---

## 2. Static Code Analysis (SonarQube)  
### 🧪 Description:  
Analyzes source code for bugs, code smells, and vulnerabilities using static analysis techniques without executing the code.

### ⚔️ Attacks mitigated:  
- **Buffer Overflows:** Memory corruption vulnerabilities that can lead to arbitrary code execution.  
- **Race Conditions:** Flaws due to improper timing or concurrent access to shared resources.  
- **Insufficient Input Validation:** Leads to injection attacks and logic bypass.  
- **Use of Unsafe Functions:** Functions prone to vulnerabilities like string overflows, improper sanitization.  
- **Hardcoded Secrets:** Embedded passwords, API keys, tokens in codebase.

### 🛡️ Threats mitigated:  
- Logical flaws that could cause incorrect behavior or security bypass.  
- Exposure of secrets increasing risk of compromise.  
- Use of deprecated or insecure APIs.  
- Code complexity and smells that increase maintenance risks and hidden vulnerabilities.

---

## 3. Dependency Vulnerability Scanning (OWASP Dependency-Check)  
### 🧪 Description:  
Scans third-party libraries and frameworks for known vulnerabilities by checking against public CVE databases and advisories.

### ⚔️ Attacks mitigated:  
- **Supply Chain Attacks:** Exploiting vulnerable or malicious dependencies to compromise the software.  
- **Known Exploits:** Using known CVEs that attackers can exploit remotely or locally.

### 🛡️ Threats mitigated:  
- Use of outdated or unpatched third-party components.  
- Transitive dependencies introducing unknown risks.  
- Vulnerabilities with no vendor patches requiring mitigation or replacement.

---

## 4. Packaging and GPG Signing  
### 🧪 Description:  
Signs the final artifact with GPG. Verifiers can confirm origin and integrity using the public key and signature.

### 🛡️ Attacks mitigated:  
- **Tampering During Deployment:** Unauthorized changes to binaries or packages in transit or storage.  
- **Man-in-the-Middle (MITM) Attacks:** Intercepting and modifying packages.  
- **Repackaged Malware:** Injecting malicious code into legitimate software distributions.  
- **Impersonation Attacks:** Faking software publisher identities to distribute malware.

---

## 5. Final Report Generation  
### 🧪 Description:  
Combines results from all tools into a single unified report for analysis, auditing, and traceability.

### 🛡️ Benefits:  
- Improved visibility of risks and vulnerabilities.  
- Easier audit trails for compliance frameworks (e.g., ISO 27001, SOC 2).  
- Centralized decision-making support for prioritizing fixes.

---

<br/>

<a id="srpski"></a>

# 🛡️ Pregled sigurnosnog pipeline-a i zaštita od pretnji  

## 🔧 Opšti Opis  
Ovaj sigurnosni *pipeline* integriše automatizovane bezbednosne provere u CI/CD tok razvoja koristeći *Docker* kontejnere sa specijalizovanim alatima. Svaka faza štiti aplikaciju od različitih tipova sajber pretnji tokom razvoja i distribucije softvera.

---

## 1. Testiranje bezbednosti krajnjih tačaka (OWASP ZAP)  
### 🧪 Opis:  
ZAP vrši:  
- API skeniranje: testira REST/HTTP API krajnje tačke.  
- Puno skeniranje: skenira ceo web interfejs aplikacije.

### ⚔️ Napadi protiv kojih štiti:  
- **Injekcioni napadi:** SQL injekcija, XSS, komandna injekcija, LDAP injekcija — gde zlonamerni unos menja upite ili komande.  
- **CSRF:** Prisiljavanje prijavljenog korisnika na neželjene akcije.  
- **IDOR:** Neautorizovan pristup podacima promenom URL ili parametara.  
- **Sigurnosne konfiguracije:** Pogrešne postavke koje otkrivaju osetljive informacije ili funkcionalnosti.  
- **Izlaganje osetljivih podataka:** Nešifrovani ili neadekvatno zaštićeni podaci kao što su lozinke, tokeni.  
- **Pokvarena autentifikacija i upravljanje sesijama:** Slabi mehanizmi koji omogućavaju preuzimanje naloga.  
- **Prelazak kroz direktorijume:** Pristup zaštićenim fajlovima menjajući putanju.  
- **Nevalidni preusmerioci i prosleđivanja:** Usmeravanje korisnika na maliciozne sajtove.

### 🛡️ Pretnje protiv kojih štiti:  
- Slaba autentifikacija i kontrola sesija.  
- Pogrešne sigurnosne konfiguracije koje mogu dovesti do eskalacije privilegija.  
- Izlaganje ličnih i poverljivih podataka.  
- Nevalidni preusmerioci koji mogu omogućiti fišing ili distribuciju malvera.  
- Ranjivi ili pogrešno konfigurisani API-jevi.

---

## 2. Statička Analiza Koda (SonarQube)  
### 🧪 Opis:  
Analizira izvorni kod i pronalazi ranjivosti, *code smells* i loše prakse u pisanju koda bez pokretanja programa.

### ⚔️ Napadi protiv kojih štiti:  
- **Prelivi bafera:** Greške u memoriji koje mogu dovesti do izvršavanja proizvoljnog koda.  
- **Utrka u pristupu resursima (race conditions).**  
- **Nedovoljna validacija unosa:** Omogućava injekcije i zaobilaženje logike.  
- **Upotreba nesigurnih funkcija:** Funkcije koje su podložne greškama u sanitizaciji ili memoriji.  
- **Zakucane lozinke i tajne:** Lozinke, API ključevi u kodu.

### 🛡️ Pretnje protiv kojih štiti:  
- Logičke greške koje mogu izazvati neispravan rad ili bezbednosne propuste.  
- Izlaganje poverljivih podataka.  
- Upotreba zastarelih ili nesigurnih API-ja.  
- Kompleksnost koda koja povećava rizik od grešaka i ranjivosti.

---

## 3. Skeniranje ranjivosti u zavisnostima (OWASP Dependency-Check)  
### 🧪 Opis:  
Skener detektuje poznate ranjivosti u bibliotekama koristeći bazu CVE podataka i obaveštenja.

### ⚔️ Napadi protiv kojih štiti:  
- **Napadi kroz lanac snabdevanja:** Iskorišćavanje ranjivih ili malicioznih zavisnosti za kompromitovanje softvera.  
- **Poznate ranjivosti:** Eksploatacije ranjivosti za koje već postoje javno poznata rešenja.

### 🛡️ Pretnje protiv kojih štiti:  
- Upotreba zastarelih ili nezakrpljenih komponenti.  
- Indirektne zavisnosti koje uvode nepoznate rizike.  
- Ranjivosti za koje nema dostupnih zakrpa.

---

## 4. Pakovanje i GPG potpisivanje  
### 🧪 Opis:  
Softver se pakuje i digitalno potpisuje GPG ključem radi verifikacije integriteta i izvora.

### 🛡️ Napadi protiv kojih štiti:  
- **Izmena fajlova u transportu:** Neovlašćene izmene softvera tokom prenosa ili skladištenja.  
- **Man-in-the-middle (MITM) napadi:** Presretanje i modifikovanje paketa.  
- **Repakovanje malicioznim kodom:** Ubacivanje malvera u legitimne fajlove.  
- **Imitacija autora:** Lažno predstavljanje izvora softvera.

---

## 5. Generisanje završnog izveštaja  
### 🧪 Opis:  
Konsoliduje rezultate iz svih alata u jedinstven izveštaj za pregled, reviziju i donošenje odluka.

### 🛡️ Prednosti:  
- Puna vidljivost ranjivosti i rizika.  
- Jednostavnija revizija za usklađenost sa standardima (ISO 27001, SOC 2 itd.)  
- Centralizovana podrška za donošenje bezbednosnih odluka i prioriteta.