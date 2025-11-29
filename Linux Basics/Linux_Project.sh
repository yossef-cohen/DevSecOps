#!/bin/bash

find_ip(){
	ip=$1
	regex='(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
	full_ip="($regex\.$regex\.$regex\.$regex)"
	if [[ $ip =~ $full_ip ]]; then
		echo "${BASH_REMATCH[1]}"
		return 0
	fi
	
}

error="(error|
warning|
not found|
No such file or directory|
permission denied|
invalid argument|
too many arguments|
numerical argument required|
bad substitution|
bad file descriptor|
is a directory|
is not a directory|
is not a function|
readonly variable|
unary operator expected|
binary operator expected|
unexpected token|
unexpected EOF)"

find_error(){
	err=$1
	if [[ "$err" =~ $error ]]; then	
		echo "${BASH_REMATCH[1]}"
		return 0
	fi
}


i=1
banana="$(date).rep"
exec 3< /var/log/syslog
while read -u 3 line
do 
	err=$(find_error "$line")
	ip=$(find_ip "$line")
	ip="${ip//[[:space:]]/}"
	if [[ -n "$ip" && -n $err ]]; then    # print only if IP is not empty
		echo "$ip and $err in line $i, good good" >> "$banana"
	fi	
	i=$((i+1))

done
exec 3<&-
