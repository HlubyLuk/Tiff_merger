#!/usr/bin/env sh

shopt -s nullglob

iter_over_directories() {
	local arr=(${1}/*)
	local files=()
	for i in ${arr[@]} ; do
		if [[ -f ${i} && ${i##*\.} = "tif" ]]; then
			files+=("${i}")
		fi
		if [[ -d ${i} ]]; then
			iter_over_directories ${i}
		fi
	done

	local count=${#files[@]}
	if [[ ${count} -gt "2" ]]; then
		printf "dir: %s\n" ${1}
		printf "call..."
		printf "python %s %s" ${files[@]:0:$count} "output.tif"
		printf "\n"
		printf "\n"
	elif [[ ${count} -eq "1" ]]; then
		printf "dir: %s\n" ${1}
		printf "call... rename file to output.tif\n"
		printf "\n"
	#else
	#	printf "no tif file found\n"
	fi
}


iter_over_directories ${1:-.}

shopt -u nullglob
