If you have any questions, problems, suggestions, or just plain like the software, please email me at gene.reese@xirsix.com to let me know; I base how much work I put in on my projects off how many people find them useful.

If you find Togo useful, please also consider upvoting my post at StackOverflow to spread the word about it:
http://stackoverflow.com/questions/880227/what-is-the-minimum-i-have-to-do-to-create-an-rpm-file

---

### What is Togo?
Want to create an RPM to deploy your software and don't want to spend hours learning how to do it? -or maybe you're already familiar with the process, but just want it to feel more clean and organized?

Use Togo! You can have **your first RPM** built and ready to install **in less than 5 minutes.** (Scroll down for a super-fast example.)

Who might find Togo useful?
* A sysadmin who has a script or group of scripts he wants to add to a yum repository
* A developer who has pre-compiled binaries he wants to package up and install on several systems
* Anyone who wants to keep track of everything on their system(s) with RPM
* 
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

##### More Information
* [About Togo](./docs/about.md)
* [Detailed Example](./docs/detailed-example.md)
* [General](./docs/general.md)
