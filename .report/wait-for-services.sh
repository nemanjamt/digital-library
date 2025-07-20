#!/bin/bash
rm -f /.done/sonarscanner.done

until [[ -f /.done/sonarscanner.done && -f /.done/dependency-scan.done ]]
do 
 echo 'Waiting for sonarscanner to finish...';
 sleep 5;

done;
echo 'Starting report generation...';