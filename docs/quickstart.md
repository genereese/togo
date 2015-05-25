#### Togo 2.x Changes

There were many syntax changes to allow for flagging of files via the command line as well as some database changes. Any project created with Togo 1.x will need to have its project database updated using 'togo file database --init'. Unfortunately, you will also need to re-flag your project files and set your excludes, etc. again.

### Quick-start Guide
#### Installation
Clone the repo, run the build script, and install the RPM

```
$ git clone https://github.com/genereese/togo.git

$ cd togo; ./build-togo.sh

$ sudo yum localinstall ./rpms/*.rpm
```

#### Configuration
Now that togo is installed, let's configure it.

```bash
$ togo configure -n "Your Name" -e "your_email@address.com"
```

### Super-Fast Example

1) Create the project directory using the script:
```bash
$ togo create my-project; cd my-project
```
2) Copy your files into the build root:
```bash
$ mkdir -p root/usr/local/bin; touch root/usr/local/bin/example_file
```

3) Exclude the the ownership of '/usr', '/usr/local', and '/usr/local/bin' from your RPM:
```bash
$ togo file exclude root/usr/local/bin
...
```

4) Modify the spec to change your version/release/summary, etc.
```bash
$ vi spec/header
```
5) Build the RPM
```bash
$ togo build package
```
-and your RPM is spit out into the rpms directory.


### Detailed Example
Once togo is configured, you can create your first project. To do this, move to the desired parent directory and run togo with the 'create' option. Whatever you pass as the argument will be the name of your new RPM. You can change it later, but it's easiest to start out with the proper name:

```bash
# Create a parent directory for your RPM projects
$ mkdir -p /home/username/rpms

# Change to that directory
$ cd /home/username/rpms

# Run togo with 'create' to create a new package
$ togo create my-package-name
```

#### Directory Structure Overview
You will now notice a new directory under your current directory called 'my-package-name' (or whatever you named it). Change into this directory to get started.

```bash
$ cd my-package-name
```

Here you will notice several directories. The main ones you will be concerned with for a 'quick start' are the 'root' and 'spec' directories.

##### The 'root' Directory
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

Togo will automatically add every file/directory under the ./root directory into the RPM. This means that your RPM, by default, will claim ownership of all files and folders in the ./root directory.

Technically speaking, there is currently nothing wrong with this, but common practice is to have each file/directory on the filesystem owned by only a single RPM.

So, for this example, you will want to exclude '/usr', '/usr/local', and '/usr/local/bin'. This is actually very easy as the exclude process will cascade up the directory tree:

```bash
$ togo file exclude root/usr/local/bin
```

-and, of course, if you want to remove a file from your RPM, simply remove it from the ./root directory tree and it will be removed from the RPM.

Technically, you may now build your RPM with 'togo build package', but you will probably want to update your version information, description, compression, etc. first:

```bash
$ vi spec/header
```

Once you have modified your header file, simply run 'togo build package' from your togo package directory to create the RPM:

```bash
$ togo build package
Generating spec file: generated.spec

Generating metadata using: generated.spec

Cleaning Metadata
  Removing old files from:
    ./meta/*

Creating Metadata Structure
  Creating directory structure under: /home/greese/Desktop/rpm/my-package-name/meta
    Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD'
    Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/RPMS'
    Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/SOURCES'
    Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/SPECS'
    Creating dir '/home/greese/Desktop/rpm/my-package-name/meta/redhat/SRPMS'
    Linking generated.spec to /home/greese/Desktop/rpm/my-package-name/meta/redhat/SPECS/generated.spec

Creating Compressed Source
  Compressing...
    Done


Building the package...

Setting Up Environment Variables
  Setting gpg key macros

Building the RPM
==================================

Executing:
time rpmbuild --define '_topdir /home/greese/Desktop/rpm/my-package-name/meta/redhat' -bb ./meta/redhat/SPECS/*.spec

Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.6lw4hN
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ rm -rf my-package-name-1.0
+ /usr/bin/mkdir -p my-package-name-1.0
+ cd my-package-name-1.0
+ /usr/bin/tar -xf /home/greese/Desktop/rpm/my-package-name/meta/redhat/SOURCES/my-package-name.tar
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.NqxIsx
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ cd my-package-name-1.0
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.iqMHDh
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ '[' /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.i386 '!=' / ']'
+ rm -rf /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.i386
++ dirname /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.i386
+ mkdir -p /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT
+ mkdir /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.i386
+ cd my-package-name-1.0
+ rsync -a . /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.i386/
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/brp-compress
+ /usr/lib/rpm/brp-strip /usr/bin/strip
+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
+ /usr/lib/rpm/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-java-repack-jars
Processing files: my-package-name-1.0-1.noarch
Provides: my-package-name = 1.0-1
Requires(interp): /bin/sh /bin/sh /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(pre): /bin/sh
Requires(post): /bin/sh
Requires(preun): /bin/sh
Requires(postun): /bin/sh
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.i386
Wrote: /home/greese/Desktop/rpm/my-package-name/meta/redhat/RPMS/noarch/my-package-name-1.0-1.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.EhMra2
+ umask 022
+ cd /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILD
+ cd my-package-name-1.0
+ rm -rf /home/greese/Desktop/rpm/my-package-name/meta/redhat/BUILDROOT/my-package-name-1.0-1.i386
+ exit 0

real	0m0.112s
user	0m0.033s
sys	0m0.012s

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
