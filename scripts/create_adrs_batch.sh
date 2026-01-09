#!/usr/bin/env bash
set -euo pipefail

DATE="$(date +%Y-%m-%d)"

# ADR skeleton list (starting at ADR-004)
# Add/remove items as needed, but keep numbering stable.
declare -A ADRS=(
  ["004"]="cloud-provider-enablement-and-key-security"
  ["005"]="evaluation-and-regression-testing-policy"
  ["006"]="persona-binding-and-mode-governance"
  ["007"]="memory-persistence-and-drift-control"
)

# Ensure ADR directory exists
mkdir -p ./ADR

for NUM in $(printf "%s\n" "${!ADRS[@]}" | sort); do
  TITLE="${ADRS[$NUM]}"
  FILE="./ADR/ADR-${NUM}-${TITLE}.md"

  if [[ -f "$FILE" ]]; then
    echo "Skipping existing ADR-${NUM}: $FILE"
    continue
  fi

  cat > "$FILE" <<EOM
---
id: "ADR-${NUM}"
title: ""
type: "adr"
status: "draft"
version: "v0.1"
canonical: true
scope: "io-iii"
audience: "internal"
created: "${DATE}"
updated: "${DATE}"
tags: []
roles_focus: []
provenance: "human"
---

# ADR-${NUM} — 

## Context

_TODO_

## Decision

_TODO_

## Decision Drivers

_TODO_

## Options Considered

_TODO_

## Consequences

_TODO_

## Related

EOM

  echo "Created $FILE"
done

echo "✅ ADR batch skeleton creation complete."
