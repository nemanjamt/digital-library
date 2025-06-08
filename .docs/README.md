# 🛡️ Project Security Pipeline Documentation

## 📂 Documentation Structure

📁 [.docs](https://github.com/nemanjamt/digital-library/tree/main/.docs)  
├── [Zap api scan example.html](https://github.com/nemanjamt/digital-library/blob/main/.docs/Zap%20api%20scan%20example.html)  
├── [Zap full scan example.html](https://github.com/nemanjamt/digital-library/blob/main/.docs/Zap%20full%20scan%20example.html)  
├── GPG Application signing.md  
│   ├── [🇬🇧 English version](https://github.com/nemanjamt/digital-library/blob/main/.docs/GPG%20Application%20signing.md#-english)  
│   └── [🇷🇸 Srpska verzija](https://github.com/nemanjamt/digital-library/blob/main/.docs/GPG%20Application%20signing.md#-srpski)  
├── OWASP Dependecy check.md  
│   ├── [🇬🇧 English version](https://github.com/nemanjamt/digital-library/blob/main/.docs/OWASP%20Dependecy%20check.md#-english)  
│   └── [🇷🇸 Srpska verzija](https://github.com/nemanjamt/digital-library/blob/main/.docs/OWASP%20Dependecy%20check.md#-srpski)  
├── OWASP Zap.md  
│   ├── [🇬🇧 English version](https://github.com/nemanjamt/digital-library/blob/main/.docs/OWASP%20Zap.md#-english)  
│   └── [🇷🇸 Srpska verzija](https://github.com/nemanjamt/digital-library/blob/main/.docs/OWASP%20Zap.md#-srpski)  
├── [README.md](https://github.com/nemanjamt/digital-library/blob/main/.docs/README.md)  
└── SonarQube.md  
    ├── [🇬🇧 English version](https://github.com/nemanjamt/digital-library/blob/main/.docs/SonarQube.md#-english)  
    └── [🇷🇸 Srpska verzija](https://github.com/nemanjamt/digital-library/blob/main/.docs/SonarQube.md#-srpski)


> 📄 Each pipeline stage is documented in its own file. Click the links above to explore each document.

---

## 🔒 Security Pipeline Overview

Our security pipeline helps ensure your application remains secure throughout the development process by leveraging industry-standard tools. These tools are orchestrated via Docker containers, each responsible for a specific phase of analysis and reporting.

### ✅ Tools Used

- [OWASP ZAP](https://owasp.org/www-project-zap/)
- [SonarQube](https://www.sonarsource.com/products/sonarqube/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [GPG Signing](https://gnupg.org/)

### 📋 Pipeline Stages

1. **Endpoint Security Testing**  
   ZAP runs two scans:
   - API Scan ([example](https://github.com/your-org/your-repo/blob/main/.docs/Zap%20api%20scan%20example.html))
   - Full Scan ([example](https://github.com/your-org/your-repo/blob/main/.docs/Zap%20full%20scan%20example.html))

2. **Static Code Analysis**  
   SonarQube is used to inspect your code and highlight issues.

3. **Dependency Vulnerability Scanning**  
   Detects known vulnerable dependencies using OWASP Dependency-Check.

4. **Packaging and GPG Signing**  
   Your app is packed and cryptographically signed using GPG. A public key and signature are provided so that integrity can be verified.

5. **Final Report Generation**  
   A combined report is created, aggregating results from all tools.

---

## 🇷🇸 Verzija na srpskom

# 🛡️ Dokumentacija o sigurnosnom pipelinu

## 📂 Struktura dokumentacije

.docs <br>
├── Zap API Primer Skeniranja.html <br>
├── Zap Puni Sken Primer.html <br>
├── GPG Potpisivanje Aplikacije.md <br>
├── OWASP Provera Zavisnosti.md <br>
├── OWASP ZAP.md <br>
├── README.md <br>
└── SonarQube.md <br>

> 📄 Svaka faza pipelina je opisana u posebnom fajlu. Pogledajte linkove iznad za više informacija.

---

## 🔒 Pregled sigurnosnog pipelina

Naš sigurnosni pipeline štiti vašu aplikaciju tokom razvoja koristeći dobro poznate alate. Svaki alat se pokreće u sopstvenom Docker kontejneru i ima jasno definisanu ulogu.

### ✅ Korišćeni alati

- [OWASP ZAP](https://owasp.org/www-project-zap/)
- [SonarQube](https://www.sonarsource.com/products/sonarqube/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [GPG Potpisivanje](https://gnupg.org/)

### 📋 Faze pipelina

1. **Testiranje sigurnosti krajnjih tačaka**  
   Pokreću se dve ZAP provere:
   - API skeniranje ([primer](https://github.com/your-org/your-repo/blob/main/.docs/Zap%20api%20scan%20example.html))
   - Puno skeniranje ([primer](https://github.com/your-org/your-repo/blob/main/.docs/Zap%20full%20scan%20example.html))

2. **Analiza statičkog koda**  
   SonarQube analizira vaš kod i identifikuje probleme.

3. **Skeniranje zavisnosti**  
   Otkrivanje poznatih ranjivosti u korišćenim zavisnostima.

4. **Pakovanje i GPG potpisivanje**  
   Aplikacija se pakuje i kriptografski potpisuje. Dostavljamo javni ključ i potpis za verifikaciju integriteta.

5. **Kreiranje konačnog izveštaja**  
   Kombinovani izveštaj na osnovu svih prethodnih faza.

---

