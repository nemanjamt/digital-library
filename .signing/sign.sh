#!/bin/bash
set -e

# Output directory for signing artifacts
OUTPUT_DIR=".signing/app_signature"
FINAL_REPORT_DIR=".report/general-report"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"
# Check if GPG is installed
if ! command -v gpg &> /dev/null; then
  echo "GPG is not installed. Please install GPG and try again."
  exit 1
fi

# Check if Final Report directory exists
if [ ! -d "$FINAL_REPORT_DIR" ]; then
  echo "Final report directory does not exist. Creating it..."
  exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
  echo "npm is not installed. Please install npm and try again."
  exit 1
fi

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

# Install dependencies
echo "Installing npm dependencies..."

npm install
if [ $? -ne 0 ]; then
  echo "npm install failed. Exiting."
  exit 1
fi

# Build the npm app
echo "Building npm app..."

npm run build
if [ $? -ne 0 ]; then
  echo "Build failed. Exiting."
  exit 1
fi

# Pack npm app and create a tarball
echo "Packing npm app..."

PACKAGE_TGX=$(npm pack --silent)
if [ $? -ne 0 ]; then
  echo "npm pack failed. Exiting."
  exit 1
fi

# Move the package to the signing output directory
mv "$PACKAGE_TGX" "$OUTPUT_DIR/"

SIGNATURE_NAME="${PACKAGE_TGX}.sig"
# Sign the package
echo "Signing the package $PACKAGE_TGX"
gpg --batch --yes --passphrase $GPG_PASSPHRASE --detach-sign --output "$OUTPUT_DIR/$SIGNATURE_NAME" "$OUTPUT_DIR/$PACKAGE_TGX"


# Export the generated public key in ASCII format
echo "Exporting public key..."
gpg --armor --export "$GPG_EMAIL" > ./$OUTPUT_DIR/public-key.asc

echo "Signing complete. Artifacts are in $OUTPUT_DIR/"

# Verify the signature
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

# Move the package and signature to the reports directory
mv "$OUTPUT_DIR/" "$FINAL_REPORT_DIR/"
echo "Package, signature and public key moved to $FINAL_REPORT_DIR"

# Clean up
rm -f -R "$OUTPUT_DIR"
echo "Temporary files cleaned up."
