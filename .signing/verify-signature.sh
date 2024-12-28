#!/bin/bash
set -e

PACKAGE="$1"
SIGNATURE="$2"

if [ -z "$PACKAGE" ] || [ -z "$SIGNATURE" ]; then
  echo "Usage: ./verify-signature.sh <package> <signature>"
  exit 1
fi

echo "Verifying signature..."
gpg --verify "$SIGNATURE" "$PACKAGE"
if [ $? -eq 0 ]; then
  echo "Signature verification succeeded!"
else
  echo "Signature verification failed!"
  exit 1
fi