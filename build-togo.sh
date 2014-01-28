#!/bin/bash

echo
echo "Checking build dependencies..."
echo

rpm -q rpm-build python-sqlobject

if [ $? -ne 0 ]; then
	echo
	echo "ERROR: Build dependencies not met."
	echo
	echo "  Please ensure the above packages are installed before building."
	echo
else
	echo
	echo "Attempting to build the togo RPM..."
	./root/usr/local/bin/togo -bp
	echo
fi
