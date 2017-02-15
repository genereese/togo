#!/bin/bash

echo
echo "Checking build dependencies..."
echo

rpm -q rpm-build python-sqlobject rsync

if [ $? -ne 0 ]; then
	echo
	echo "ERROR: Build dependencies not met."
	echo
	echo "  Please ensure that the 'rpm-build','python-sqlobject', and 'rsync'"
	echo "  rpms are installed before building."
	echo
	echo "  If you have satisfied these requirements via some other means"
	echo "  (easy_install, etc.) you may try to build the RPM using:"
	echo
	echo "  ./root/usr/bin/togo build package"
	echo
else
	echo
	echo "Attempting to build the togo RPM..."
	./root/usr/bin/togo build package
	echo
fi
