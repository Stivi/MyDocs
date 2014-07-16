#!/bin/bash


function push_to_file {
    echo push_to_file
}


function work {
    x=1
	while [ $x -le 52 ]
	do
		echo "access.log.$x"
		x=$(( $x + 1 ))
	done
}

#push_to_file

work
