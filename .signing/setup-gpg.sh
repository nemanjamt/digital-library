#!/bin/bash
set -e

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