If you have any questions, problems, suggestions, or just plain like the software, please email me at gene.reese@xirsix.com to let me know; I base how much work I put in on my projects off how many people find them useful.

# What is Togo?
Want to create an RPM to deploy your software and don't want to spend hours learning how to do it?

Use Togo! You can have **your first RPM** built and ready to install **in less than 5 minutes.**

Who might find Togo useful?
* A sysadmin who has a script or group of scripts he wants to add to a yum repository
* A developer who has pre-compiled binaries he wants to package up and install on several systems
* Anyone who wants to keep track of everything on their system(s) with RPM

# Getting Started
### Installation
Clone the repo, run the build script, and install the RPM

```
$ git clone https://github.com/genereese/togo.git

$ cd togo; ./build-togo.sh

$ sudo yum localinstall ./rpms/*.rpm
```

### Configuration
Now that togo is installed, let's configure it.

```bash
$ togo --configure
```

You will be prompted for your name and an email address. This information is only used to populate some default variables in your RPM configuration file (known as a '.spec' file), and is not used for any other purpose.

# Super-Fast Example

1) Create the project directory using the script:
```bash
$ togo -c my-project; cd my-project
```
2) Copy your files into the build root:
```bash
$ mkdir -p root/usr/local/bin; cp /path/to/myfile root/usr/local/bin/
```
3) Flag the file(s) and/or directories to include them in the RPM
```bash
$ togo -f root/usr/local/bin/myfile
```
4) Modify the spec to change your version/release/summary, etc.
```bash
$ vi spec/header
```
5) Build the RPM
```bash
$ togo -bp
```
-and your RPM is spit out into the rpms directory.


# Detailed Example
Once togo is configured, you can create your first project. To do this, move to the desired parent directory and run togo with the '-c' option. Whatever you pass as the argument will be the name of your new RPM. You can change it later, but it's easiest to start out with the proper name:

```bash
# Create a parent directory for your RPM projects
$ mkdir -p /home/username/rpms

# Change to that directory
$ cd /home/username/rpms

# Run togo with a -c to create a new package
$ togo -c my-package-name
```

### Directory Structure Overview
You will now notice a new directory under your current directory called 'my-package-name' (or whatever you named it). Change into this directory to get started.

```bash
$ cd my-package-name
```

Here you will notice several directories. The main ones you will be concerned with for a 'quick start' are the 'root' and 'spec' directories.

#### The 'root' Directory
The 'root' directory represents your RPMs expanded files.

For example, say you developed a script called 'stat.sh' that polls the host machine for statistical information. You would like to place this script in an RPM and make sure that users on the system have access to it.

Typically, for custom scripts, I want them to go under '/usr/local/bin'. So, I create that directory structure under the 'root' directory, then place my 'stat.sh' script in it:

```bash
# Create the directory structure I want to see when my RPM is installed
$ mkdir -p root/usr/local/bin

# Place my pretend script in the appropriate location
$ touch root/usr/local/bin/stat.sh
```

If you're not sure where you should place your files, have a look at the Filesystem Hierarchy Standard (http://www.pathname.com/fhs/pub/fhs-2.3.html).

After you copy your files into your root directory structure, you will need to flag them to ensure they are included in your package. You accomplish this with the '-f' option.

You may individually flag files or you may flag entire directories. If you flag a directory, you will not need to flag the files in that directory as they will automatically be included. You just want to make sure that you are not flagging directories which are owned by other packages (such as /etc).

```bash
# Flag the stat.sh file
$ togo -f root/usr/local/bin/stat.sh

Options:
--------
1) REGULAR
2) %config
3) %doc

-1) Clear all flags from this item

0) Cancel

Please select a flag to apply:
```

We want to flag the 'stat.sh' script as a regular file, so we enter option '1'.

```bash

...

Please select a flag to apply: 1
 Applied REGULAR flag to: /usr/local/bin/stat.sh
```

Technically, you may now build your RPM with 'togo -bp', but you will probably want to update your version information, description, compression, etc. first:

```bash
$ vi spec/header
```

Once you have modified your header file, simply run 'togo -bp' from your root package directory to create the RPM:

```bash
$ togo -bp

Updating file list...
Cleaning Metadata
==================================
 Removing old files from:
   ./meta/*

Creating Metadata Structure
==================================
 Creating directory structure under: /home/greese/Desktop/rpm/my-package-name/meta
   Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD'
     Linking /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD to /home/greese/Desktop/rpm/my-package-name/meta/usr/src/redhat/BUILD
   Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/RPMS'
     Linking /home/greese/Desktop/rpm/my-package-name/meta/redhat/RPMS to /home/greese/Desktop/rpm/my-package-name/meta/usr/src/redhat/RPMS
   Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/SOURCES'
     Linking /home/greese/Desktop/rpm/my-package-name/meta/redhat/SOURCES to /home/greese/Desktop/rpm/my-package-name/meta/usr/src/redhat/SOURCES
   Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/SPECS'
     Linking /home/greese/Desktop/rpm/my-package-name/meta/redhat/SPECS to /home/greese/Desktop/rpm/my-package-name/meta/usr/src/redhat/SPECS
   Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/SRPMS'
     Linking /home/greese/Desktop/rpm/my-package-name/meta/redhat/SRPMS to /home/greese/Desktop/rpm/my-package-name/meta/usr/src/redhat/SRPMS
   Linking generated.spec to /home/greese/Desktop/rpm/my-package-name/meta/redhat/SPECS/generated.spec

Creating Compressed Source
==================================
 Compressing...
  Done

Setting Up Environment Variables
==================================
 Setting '%_usr' macro
 Setting gpg key macros

 Building the RPM
==================================
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.KEo3YD
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ rm -rf my-package-name-1.0
+ /usr/bin/mkdir -p my-package-name-1.0
+ cd my-package-name-1.0
+ /usr/bin/tar -xf /home/greese/Desktop/rpm/my-package-name/meta/redhat/SOURCES/my-package-name.tar
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.mlcEGy
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ cd my-package-name-1.0
+ rsync -a . /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.x86_64/
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.7FgAyt
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ cd my-package-name-1.0
+ /usr/lib/rpm/brp-compress
+ /usr/lib/rpm/brp-strip /usr/bin/strip
+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
Processing files: my-package-name-1.0-1.noarch
Provides: my-package-name my-package-name = 1.0-1
Requires(interp): /bin/sh /bin/sh /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(pre): /bin/sh
Requires(post): /bin/sh
Requires(preun): /bin/sh
Requires(postun): /bin/sh
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.x86_64
Wrote: /home/greese/Desktop/rpm/my-package-name/meta/redhat/RPMS/noarch/my-package-name-1.0-1.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.1HQDWj
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ cd my-package-name-1.0
+ rm -rf /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.x86_64
+ exit 0

real	0m0.217s
user	0m0.072s
sys	0m0.083s

Any generated RPMs are in: ./rpms
```

If all went well, you should either see your RPM in ./rpms, or you'll see an error message as to why the build failed:

```bash

$ rpm -qip rpms/my-package-name-1.0-1.noarch.rpm
 
Name        : my-package-name
Version     : 1.0
Release     : 1
Architecture: noarch
Install Date: (not installed)
Group       : Applications/System
Size        : 0
License     : GNU GPL
Signature   : (none)
Source RPM  : my-package-name-1.0-1.src.rpm
Build Date  : Mon 16 Sep 2013 08:53:52 PM CDT
Build Host  : devel
Relocations : (not relocatable)
Packager    : Gene Reese <gene.reese@xirsix.com>
Summary     : None
Description :
None
```

### Additional Information

#### The 'spec' Directory
The 'spec' directory contains templates of the different sections of the RPM '.spec' file. These sections include RPM information (such as version numbers and author information) as well as basic setup and cleanup instructions.

##### header
This file contains the basic information about your RPM. If you need to change the version/release of your RPM, you can do it here. You will also need to update the 'Summary' and 'License' fields for your RPM.

##### pre
This file is an empty shell script that may be used to ensure certain things are done before your RPM is installed.

Examples include:

  * User creation
  * Gathering of host information
  * Starting/Stopping services

##### post
This file is an empty shell script that may be used to ensure certain things are done after your RPM is installed.

Examples include:

  * Starting/Stopping services
  * Altering configuration files
  * Changing file/directory ownership/permissions

##### preun
This file is an empty shell script that may be used to ensure certain things are done before your RPM is removed from a system.

Examples include:

  * Stopping services before they are removed
  * Checking the current state of a system before RPM removal

##### postun
This file is an empty shell script that may be used to ensure certain things are done after your RPM is removed from a system.

Examples include:

  * Restarting services which may have partially depended on your RPM
  * Performing final cleanup of files not included in your RPM (like log files) or modifications of config files you may have altered when you installed your RPM.

##### changelog
This is your changelog for your RPM. The script provides a structure that you may use, but you may change this to whatever format you would like.

##### tigger, triggerin and triggerun
These sections allow your RPM to perform actions based on the state changes of other packages on the system.

For example, if you wanted something about your package to change if the user installs sendmail, you may perform those actions in these files.

If you need to add more than a single trigger, you may do so in these files; the file structure simply breaks the spec file up into more readable/maintainable sections.

For more details, you may read up on triggers, here:

http://rpm.org/api/4.4.2.2/triggers.html
