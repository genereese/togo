#!/bin/bash

echo
echo "Checking build dependencies..."
echo

rpm -q rpm-build python-sqlobject

if [ $? -ne 0 ]; then
	echo
	echo "ERROR: Build dependencies not met."
	echo
	echo "  Please ensure that the 'rpm-build' and 'python-sqlobject' rpms"
	echo "  are installed before building."
	echo
	echo "  If you have satisfied these requirements via some other means"
	echo "  (easy_install, etc.) you may try to build the RPM using:"
	echo
	echo "  ./root/usr/local/bin/togo build package"
	echo
else
	echo
	echo "Attempting to build the togo RPM..."
	./root/usr/local/bin/togo build package
	echo
fi
