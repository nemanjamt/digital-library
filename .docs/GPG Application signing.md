# 🔐 GPG Application Signing

<a id="english"></a>

This stage ensures the application's integrity and authenticity by using GPG to sign the built `.tgz` package. [Link to full script](https://github.com/your-org/your-repo/blob/main/.signing/sign.sh)

### Steps:
#### 1. Checks for required tools (`gpg`, `npm`).
```bash
# Check if GPG is installed
if ! command -v gpg &> /dev/null; then
echo "GPG is not installed. Please install GPG and try again."
exit 1
fi
# Check if npm is installed
if ! command -v npm &> /dev/null; then
echo "npm is not installed. Please install npm and try again."
exit 1
fi
```
#### 2. Ensures a GPG key exists or generates a new one using `$GPG_NAME` and `$GPG_EMAIL`.
```bash
# Check if the key exists
if ! gpg --list-keys "$GPG_EMAIL" > /dev/null 2>&1; then
  echo "GPG key not found. Creating a new one..."
  cat > gen-key-script <<EOF
    %no-protection
    %echo Generating a GPG key
    Key-Type: RSA
    Key-Length: 4096
    Subkey-Type: RSA
    Subkey-Length: 4096
    Name-Real: $GPG_NAME
    Name-Email: $GPG_EMAIL
    Expire-Date: 0
    %commit
    %echo Key creation complete
EOF
  gpg --batch --generate-key gen-key-script
  rm gen-key-script
else
  echo "GPG key already exists for $GPG_EMAIL."
fi
```
#### 3. Installs dependencies and builds the app with `npm`.
```bash
npm install
if [ $? -ne 0 ]; then
  echo "npm install failed. Exiting."
  exit 1
fi

npm run build
if [ $? -ne 0 ]; then
  echo "Build failed. Exiting."
  exit 1
fi
```
#### 4. Packages the app using `npm pack`.
```bash
PACKAGE_TGX=$(npm pack --silent)
if [ $? -ne 0 ]; then
  echo "npm pack failed. Exiting."
  exit 1
fi
```
#### 5. Signs the `.tgz` archive using GPG with a detached signature.
```bash
# Move the package to the signing output directory
mv "$PACKAGE_TGX" "$OUTPUT_DIR/"

SIGNATURE_NAME="${PACKAGE_TGX}.sig"
# Sign the package
echo "Signing the package $PACKAGE_TGX"
gpg --batch --yes --passphrase $GPG_PASSPHRASE --detach-sign --output "$OUTPUT_DIR/$SIGNATURE_NAME" "$OUTPUT_DIR/$PACKAGE_TGX"
```
#### 6. Exports the public key.
```bash
echo "Exporting public key..."
gpg --armor --export "$GPG_EMAIL" > ./$OUTPUT_DIR/public-key.asc
```
#### 7. Verifies the signature and prints validation status.
```bash
gpg --verify "$OUTPUT_DIR/$SIGNATURE_NAME" "$OUTPUT_DIR/$PACKAGE_TGX" 2>&1 | tee "$OUTPUT_DIR/verify.log" 
echo "Verifying signature..."

if cat "$OUTPUT_DIR/verify.log" | grep -q "Good signature"; then
  echo "✅ Signature is valid."
  rm -f "$OUTPUT_DIR/verify.log"
else
  echo "❌ Signature verification failed!"
  cat verify.log
  exit 1
fi
echo "Signature verification complete."
```
#### 8. Moves the signature and package to `.report/general-report/`.
```bash
mv "$OUTPUT_DIR/" "$FINAL_REPORT_DIR/"
echo "Package, signature and public key moved to $FINAL_REPORT_DIR"
```

### Output files:
- `<package>.tgz` - application package
- `<package>.tgz.sig` - package signature
- `public-key.asc` - public key for signature verification

---
<br><br>

<a id="srpski"></a>

# 🔐 GPG Potpisivanje aplikacije


Ova faza osigurava integritet i autentičnost aplikacije pomoću GPG potpisivanja `.tgz` paketa. [Link do kompletne scripte](https://github.com/your-org/your-repo/blob/main/.signing/sign.sh)

### Koraci:
#### 1. Proverava da li su `gpg` i `npm` instalirani.
```bash
# Check if GPG is installed
if ! command -v gpg &> /dev/null; then
echo "GPG is not installed. Please install GPG and try again."
exit 1
fi
# Check if npm is installed
if ! command -v npm &> /dev/null; then
echo "npm is not installed. Please install npm and try again."
exit 1
fi
```
#### 2. Proverava da li postoji GPG ključ ili kreira novi pomoću `$GPG_NAME` i `$GPG_EMAIL`.
```bash
# Check if the key exists
if ! gpg --list-keys "$GPG_EMAIL" > /dev/null 2>&1; then
  echo "GPG key not found. Creating a new one..."
  cat > gen-key-script <<EOF
    %no-protection
    %echo Generating a GPG key
    Key-Type: RSA
    Key-Length: 4096
    Subkey-Type: RSA
    Subkey-Length: 4096
    Name-Real: $GPG_NAME
    Name-Email: $GPG_EMAIL
    Expire-Date: 0
    %commit
    %echo Key creation complete
EOF
  gpg --batch --generate-key gen-key-script
  rm gen-key-script
else
  echo "GPG key already exists for $GPG_EMAIL."
fi
```
#### 3. Instalira zavisnosti i build-uje aplikaciju pomoću `npm`.
```bash
npm install
if [ $? -ne 0 ]; then
  echo "npm install failed. Exiting."
  exit 1
fi

npm run build
if [ $? -ne 0 ]; then
  echo "Build failed. Exiting."
  exit 1
fi
```
#### 4. Pakuje aplikaciju pomoću `npm pack`.
```bash
PACKAGE_TGX=$(npm pack --silent)
if [ $? -ne 0 ]; then
  echo "npm pack failed. Exiting."
  exit 1
fi
```
#### 5. Potpisuje `.tgz` datoteku koristeći GPG (odvojen potpis).
```bash
# Move the package to the signing output directory
mv "$PACKAGE_TGX" "$OUTPUT_DIR/"

SIGNATURE_NAME="${PACKAGE_TGX}.sig"
# Sign the package
echo "Signing the package $PACKAGE_TGX"
gpg --batch --yes --passphrase $GPG_PASSPHRASE --detach-sign --output "$OUTPUT_DIR/$SIGNATURE_NAME" "$OUTPUT_DIR/$PACKAGE_TGX"
```
#### 6. Eksportuje javni ključ.
```bash
echo "Exporting public key..."
gpg --armor --export "$GPG_EMAIL" > ./$OUTPUT_DIR/public-key.asc
```
#### 7. Verifikuje potpis i prikazuje status validacije.
```bash
gpg --verify "$OUTPUT_DIR/$SIGNATURE_NAME" "$OUTPUT_DIR/$PACKAGE_TGX" 2>&1 | tee "$OUTPUT_DIR/verify.log" 
echo "Verifying signature..."

if cat "$OUTPUT_DIR/verify.log" | grep -q "Good signature"; then
  echo "✅ Signature is valid."
  rm -f "$OUTPUT_DIR/verify.log"
else
  echo "❌ Signature verification failed!"
  cat verify.log
  exit 1
fi
echo "Signature verification complete."
```
#### 8. Premešta potpis i paket u `.report/general-report/`.
```bash
mv "$OUTPUT_DIR/" "$FINAL_REPORT_DIR/"
echo "Package, signature and public key moved to $FINAL_REPORT_DIR"
```

### Izlazne datoteke:
- `<package>.tgz` - sam paket aplikacije
- `<package>.tgz.sig` - potpis paketa aplikacije
- `public-key.asc` - javni kljuc za verifikaciju potpisa aplikacije
