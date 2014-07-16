#!/bin/bash


push_to_file() {
    cat $1 >> out.log
}


work() {
    counter=52
	until [ $counter -lt 1 ]; do
		push_to_file access.log.$counter
		let counter-=1
	done
}


work
