#!/bin/sh

#Executing some extra commands, if file is found.
echo looking for extra.sh executable file in order to make some extra actions
file="extra.sh"
if [ -f "$file" ]
then
	echo "$file found."
	/bin/sh extra.sh
else
	echo "$file not found."
fi

#Installing requirements.
echo Installing user app requirements
pip install -r requirements.txt

# Starting django-queue-manager istance.
echo Starting Django Queue Manager istance
python /dqm_server.py


