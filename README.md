pybright
========

Integration of [CA Brightside](https://www.ca.com/us/products/ca-brightside.html) to Python.

Features
--------
        
* Allow calling Brighside commands without any boilerplate code - just one function `bright(command)`
* Output is converted to Python data structures
  * Lists or dictionaries
* Automatic error handling - failures are reported as exception (as a Python developer would expect)


Usage
-----

### List all my jobs and their return code

```python
    from pybright.cli import bright

    for job in bright("zos-jobs list jobs"):
        print(f"{job['jobname']} {job['jobid']} {job['retcode']}")
```

Prints:

        PLAPE03A JOB20471 CC 0000
        PLAPE03A JOB20380 CC 0000
        PLAPE03A JOB17519 ABEND S222
        PLAPE03A JOB17460 ABEND S222


### List my failed jobs

```python
    for job in bright("zos-jobs list jobs"):
        if job['retcode'] not in ['CC 0000', None]:
            print(f"{job['jobname']} {job['jobid']} {job['retcode']}")
```            

Prints:

        PLAPE03A JOB17519 ABEND S222
        PLAPE03A JOB17460 ABEND S222


### Print SYSOUT of failed API Layer started tasks:

```python
    for job in bright("zos-jobs list jobs --prefix MAS* --owner MASSERV"):
        if job['retcode'] not in ['CC 0000', None]:
            print(f"{job['jobname']} {job['jobid']} {job['retcode']}")
            for spool_file in bright(f"zos-jobs list spool-files-by-jobid {job['jobid']}"):
                if spool_file['ddname'] == 'SYSOUT':
                    sysout = bright(f"zos-jobs view spool-file-by-id {job['jobid']} {spool_file['id']}")
                    print(sysout)
```            

Prints:

        MASDDS1 STC03252 CC 0101
        ...
        JVMJZBL2007E Stack trace follows:
        java.io.FileNotFoundException: runtime/CA/MFSJDISV (EDC5129I No such file or directory.)
                at java.util.zip.ZipFile.open(Native Method)
                at java.util.zip.ZipFile.<init>(ZipFile.java:241)
                at java.util.zip.ZipFile.<init>(ZipFile.java:171)
                at java.util.jar.JarFile.<init>(JarFile.java:179)
                at java.util.jar.JarFile.<init>(JarFile.java:116)  
        ...      


### Issue a console command

```python
        jobname = "MASAGW1"
        bright(f'zos-console issue command --sysplex-system ca31 "S {jobname}"')
```        

See full example at [start_api_layer.py](examples/start_api_layer.py).


Installation
------------

### Requirements

 - Python 3.6 or higher
 - CA Brightside - Community Edition


### Installing CA Brightside

1. Request access to z/OSMF as described here: https://docops.ca.com/ca-brightside-enterprise-and-essentials/1-0/en/installing/prerequisites/z-osmf-configuration-overview/configure-z-osmf-security

2. Issue the following command to set the npm registry to the CA Brightside scoped package:

        npm config set @brightside:registry https://api.bintray.com/npm/ca/brightside

3. To install CA Brightside, issue the following command:

        npm install -g @brightside/core@next

4.  To create a `zosmf` profile, issue the following command. Refer to the available options in the help text to define your profile:

        bright profiles create zosmf-profile --help    

    Example for CA32 system:

        bright profiles create zosmf-profile ca32 --host ca32.ca.com --port 1443 --user <userid> --pass <password> --reject-unauthorized false --overwrite  


Full installation instructions are at <https://docops.ca.com/ca-brightside-community-edition/1-0/en/installing/install-ca-brightside>.

### Installing pybright

    pip install pybright


Licence
-------

MIT

Authors
-------

pybright was written by [Petr Plavjanik](plavjanik@gmail.com).
