#!/bin/bash

echo
echo "Checking build dependencies..."
echo

rpm -q rpm-build rsync python2 python2-sqlobject

if [ $? -ne 0 ]; then
	echo
	echo "ERROR: Build dependencies not met."
	echo
	echo "  Please ensure that the 'rpm-build', 'rsync', 'python2', and 'python2-sqlobject'"
	echo "  rpms are installed before building."
	echo
	echo "  NOTE:"
	echo "    If your RPM repositories do not include 'python2-sqlobject', you may install it"
	echo "    using pip:"
	echo
	echo "    'pip2 install sqlobject'"
	echo
	echo "  Once you are sure you have satisfied these requirements using either method,"
	echo "  you may build the RPM using the following command:"
	echo
	echo "  ./root/usr/bin/togo build package"
	echo
else
	echo
	echo "Attempting to build the togo RPM..."
	./root/usr/bin/togo build package
	echo
fi
