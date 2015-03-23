### What is Togo?
Want to create an RPM to deploy your software and don't want to spend hours learning how to do it? -or maybe you're already familiar with the process, but just want it to feel more clean and organized?

Use Togo! You can have **your first RPM** built and ready to install **in less than 5 minutes.** (Scroll down for a super-fast example.)

Who might find Togo useful?
* A sysadmin who has a script or group of scripts he wants to add to a yum repository
* A developer who has pre-compiled binaries he wants to package up and install on several systems
* Anyone who wants to keep track of everything on their system(s) with RPM


#####GET STARTED: [View the Quick-start Guide](./quickstart.md)

### Philosophy

Traditionally, RPM creation has been overly complicated. Best practices are largely non-existent and documentation mainly consists of either incredibly dry reading, or random anecdotes from people who have done it their own way. Togo seeks to help both new-comers and experienced RPM builders standardize and organize their build process by making it as simple and reproducible as possible.

Other softwares have tried to bundle the packaging process into a more generic wrapper to accomodate multiple distros (debian packages, etc.), but this process dilutes the specialization that goes into focusing on a single package format.

Togo only handles RPMs, and it handles them well. By automating the most complex and time-consuming tasks (setting up your build environment, bundling and tarring source files, generating your spec file and file lists), Togo deals with all the stupid crap that you don't want to and lets you focus on your software.
