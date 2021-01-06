#!/usr/bin/env bash

i=701
for file in cards/*; do
	ssh evanbrug@lxplus$i.cern.ch ./public/MG5_aMC_v2_7_3/bin/mg5_aMC public/cards/$file
	i=$((i+1))
done
