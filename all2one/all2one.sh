#!/bin/bash


push_to_file() {
    echo push_to_file $1
}


work() {
    x=1
	while [ $x -le 52 ]
	do
		push_to_file access.log.$x
		x=$(( $x + 1 ))
	done
}

#push_to_file

work
