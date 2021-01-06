#!/usr/bin/env bash

# seq: START STEP LAST
for x in $(seq 500 500 3500); do
	for y in $(seq 50 20 150); do
		sed "s/{X}/$x/g; s/{Y}/$y/g" monosbb-template.cmnd > cards/monosbb-$x-$y.cmnd
		echo created monosbb-$x-$y.cmnd
	done
done
