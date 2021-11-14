# The name of your package
Name: togo

# A short summary of your package
Summary: A quick, easy, and powerful RPM authoring tool

# The version of your package
Version: 3.0

# The release number of your package
Release: 3

# Any license you wish to list
License: GNU GPL

# What group this RPM would typically reside in
Group: Applications/System

# Who packaged this RPM
Packager: Gene Reese <gene.reese@xirsix.com>

# The build architecture of this RPM (noarch/x86_64/i386/etc)
Buildarch: noarch

# You generally should not need to mess with this setting
Buildroot: %{_tmppath}/%{name}

# Change this extension to change the compression level in your RPM
# tar / tar.gz / tar.bz2
Source0: %{name}.tar.gz

# Required for building the togo RPM using itself
BuildRequires: rsync

# If this package has prerequisites, uncomment this line and
#  list them here - examples are already listed
Requires: bash, python3 >= 1, rpm-build, rsync

# A more verbose description of your package
%description
Create RPMs without devoting a lot of time into figuring out how to do it!

# You probably do not need to change this
%define debug_package %{nil}

%prep
%setup -q -c

%build

%install
rsync -a . %{buildroot}/

%clean
rm -rf %{buildroot}

%pre

%post

%preun

%postun
rm -rf ~/.togo

#%trigger

#%triggerin

#%triggerun

%changelog
* Thu Jun 24 2021 Gene Reese <gene.reese@xirsix.com>
- Modified togo to utilize python 3
- Suppressed a cleanup error message that occurs from a bug in sqlobject codebase

* Sun Oct 13 2019 Gene Reese <gene.reese@xirsix.com>
- Modified togo to explicitly use python2
- Modified installation script to use either the 'python2-sqlobject' rpm,
or the 'pip2' package - 'sqlobject'
- Updated togo package's dependencies to remove 'python-sqlobject' and 'sed'

* Sun Mar 18 2018 Gene Reese <gene.reese@xirsix.com>
- Added support for %config(noreplace) file flag

* Tue Jul 25 2017 Gene Reese <gene.reese@xirsix.com>
- Build package option will now also build the associated source RPM

* Thu Oct 20 2016 Gene Reese <gene.reese@xirsix.com>
- Minor changes to .rpmmacros in preparation of gpg signing support
- Added command line arguments to modify build version and release
- See 'togo build package -h' for more information
- Removed the use of sed from Togo

* Fri Sep 30 2016 Gene Reese <gene.reese@xirsix.com>
- Minor changes to logging output
- Added rysnc as a prerequisite for the build-togo.sh script

* Thu Sep 29 2016 Gene Reese <gene.reese@xirsix.com>
- Fixed an issue with AutoReqProv in the generated spec file which was
preventing the option from functioning properly. This fix will only apply to
newly generated spec files. If you need to disable automatic dependency checks
in your existing projects, please move the 'AutoReqProv: no' line above the
'description' directive in the 'spec/header'file of your project.
- Add BuildRequires for togo to its spec file

* Sat May 7 2016 Gene Reese <gene.reese@xirsix.com>
- Changed path of togo script
- Added a --nodeps flag to package building to disable automatic dependency
generation

* Sat Apr 16 2016 Gene Reese <gene.reese@xirsix.com>
- Added project management commands
- Changed project creation syntax
- Added project renaming functionality
- Added new dependency for togo (sed)

* Mon Aug 24 2015 Gene Reese <gene.reese@xirsix.com>
- Added file/directory permission support
- Togo now properly handles files/directories with spaces in them

* Mon May 25 2015 Gene Reese <gene.reese@xirsix.com>
- Fixed premature preference database connection close on some RHEL6.x systems
- Fixed argpase error checking for RHEL systems
- Fixed python bytecompile issue where bytecompiled python sources were not
being included and were causing "non-packaged files" errors
- Cosmetic configuration display fix

* Mon Mar 23 2015 Gene Reese <gene.reese@xirsix.com>
- Swapped out optparse (deprecated) for argparse
- Heavily modified database structure
- Removed interactive file flagging in exchange for command line file flagging

* Thu Mar 12 2015 Gene Reese <gene.reese@xirsix.com>
- Set default values for user and email address

* Tue Jun 17 2014 Gene Reese <gene.reese@xirsix.com>
- Corrected bug regarding storing symlinks in the file flag database
- Hid unnecessary debug output for several commands

* Sun Jun 15 2014 Gene Reese <gene.reese@xirsix.com>
- Added cascading exclude flags for directories

* Sun Jun 15 2014 Gene Reese <gene.reese@xirsix.com>
- Overhaul of file-related helper database information (see: https://github.com/genereese/togo)
- Removed _topdir and _usr directive definitions from ~/.rpmmacros
- Modified installation script to be less restrictive for other distros

* Wed Feb 19 2014 Gene Reese <gene.reese@xirsix.com>
- Had to update the changelog due to an apparent bug in rpmbuild on Fedora 20

* Wed Jan 29 2014 Gene Reese <gene.reese@xirsix.com>
- Moved source rsync function from 'build' into 'install'

* Tue Jan 28 2014 Gene Reese <gene.reese@xirsix.com>
- Re-formatted help display and options for easier reading/use
- Removed unused help options from display
- Removed explicit Provides: xyz from generated spec

* Wed Sep 18 2013 Gene Reese <gene.reese@xirsix.com>
- Fixed duplicate file table entries for flagged files

* Wed Sep 18 2013 Gene Reese <gene.reese@xirsix.com>
- Added transaction functionality to file table updates to vastly increase processing speed over large amounts of files
- Added a simple man-page

* Mon Sep 16 2013 Gene Reese <gene.reese@xirsix.com>
- Initial version.

%files
%attr(775, root, root) "/usr/bin/togo"
%attr(664, root, root) %doc "/usr/share/man/man1/togo.1.gz"

