# General Information

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

NOTE: Changing file ownership here works, but can cause auditing (RMP -V) to fail. This is not an issue unless you audit your environments and a near future version of Togo will add user/group support directly to remedy this.

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
