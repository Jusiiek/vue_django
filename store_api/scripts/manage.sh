#!/bin/bash

set -e

COMMAND=$1
FIXTURE=${2:-""}

cd "$(dirname "$0")/.."

APPS=$(cat scripts/apps.txt)

case $COMMAND in
  make)
    echo "📦 Making migrations..."
    for app in $APPS; do
      python manage.py makemigrations $app
    done
    ;;

  migrate)
    echo "📂 Applying migrations..."
    python manage.py migrate
    ;;

  rollback)
    echo "🔙 Rolling back last migration..."
    for app in $APPS; do
      python manage.py migrate $app zero
    done
    ;;

  load)
    if [[ -z "$FIXTURE" ]]; then
      echo "⚠️  Please provide fixture name (without .json)."
      exit 1
    fi

    FIXTURE_PATH="fixtures/.${FIXTURE}.json"

    if [[ ! -f "$FIXTURE_PATH" ]]; then
      echo "❌ Fixture file not found: $FIXTURE_PATH"
      exit 1
    fi

    echo "📥 Loading fixture: $FIXTURE_PATH"
    python manage.py loaddata "$FIXTURE_PATH"
    ;;

  *)
    echo "Usage: ./scripts/manage.sh [make|migrate|rollback|load] [fixture_name]"
    exit 1
    ;;
esac
