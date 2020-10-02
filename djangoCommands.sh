#!/bin/bash

# alias penv="source ../venv/Scripts/activate"
# alias runserver="py manage.py runserver"
# alias migrate="py manage.py migrate"
# alias makemigrations="py manage.py makemigrations"

if [ -z $1 ]
then
  echo "Type an argument. Posible arg: env run migrate mkmigrations"
fi

COMMAND=${1}

case $COMMAND in
	"env")
		# For make this command run the djangoCommands.sh script has to be executed in with source
		source ../venv/Scripts/activate;;
	"run")
		py manage.py runserver;;
	"migrate")
		py manage.py migrate;;
	"mkmigrations")
		py manage.py makemigrations;;
	*)
		echo "Command not supported. Posible arg: env run migrate mkmigrations";;
esac