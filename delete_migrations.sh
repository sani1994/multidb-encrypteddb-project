#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

printf '%s%s%s%s' "$(tput setaf 1)" "$(tput bold)" "DO NOT RUN THIS SCRIPT TO ANY SERVER." "$(tput sgr0)"
printf "\nDo you want to ${RED}DELETE${NC} all migrations files (Y/n)? "


delete_migrations_files() {
  pwd=`pwd`
  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
  find . -path "*/migrations/*.pyc" -delete
  cd ../fblibs/final/
  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
  find . -path "*/migrations/*.pyc" -delete
  cd ${pwd}
}
read answer

if [ "$answer" != "${answer#[Yy]}" ]; then
  delete_migrations_files
  printf "${GREEN}All migrations files are deleted${NC}.\n"
else
  printf "${GREEN}Skipped delete migrations files.${NC}\n"
fi

python manage.py shell << EOF
exit()
EOF

printf "\nDo you want to ${RED}DELETE${NC} all migrations entry from ${GREEN}database${NC} (Y/n)? "
read db_answer

if [ "$db_answer" != "${db_answer#[Yy]}" ]; then
python manage.py shell << EOF
from django.db.migrations.recorder import MigrationRecorder
MigrationRecorder.Migration.objects.all().delete()
exit()
EOF
  printf "${GREEN}All migrations entries are deleted from database.${NC}\n"
else
  printf "${GREEN}Skipped delete entries from database.${NC}\n"
fi
