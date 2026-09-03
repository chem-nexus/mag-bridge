#!/bin/bash
# World-A hydration. Runs from /docker-entrypoint-initdb.d when /data/db is empty — which, with the
# tmpfs data dir, is EVERY container start → the DB is always rebuilt from the seed files (files are
# the source of truth). Each seed JSON becomes a collection named after the file (stem = collection).
set -euo pipefail

DB="${MONGO_INITDB_DATABASE:-magbridge_testdata}"
shopt -s nullglob

count=0
for f in /seed/*.json; do
  coll="$(basename "$f" .json)"
  echo "[seed] importing ${f} -> ${DB}.${coll}"
  mongoimport --db "$DB" --collection "$coll" --file "$f" \
    --jsonArray --mode upsert --upsertFields _id
  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  echo "[seed] WARNING: no /seed/*.json found — is ../magbridge-tests/seed mounted and populated?"
else
  echo "[seed] done — ${count} collection(s) hydrated into ${DB}"
fi
