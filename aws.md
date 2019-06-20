# AWS

AWS provides several services with a free-tier and additional services are often available under AWS Educate Starter Account.

## Cloud 9
Provides a cloud based environment for programming. Make sure you save your work to GitHub or some other location

### Getting Started

1. [Instructor Only] [Setup Classroom](https://docs.aws.amazon.com/cloud9/latest/user-guide/setup-classroom.html)
2. As a student, you should get an email inviting you to join an "AWS Educate Classroom"
3. [Enter Classroom](https://docs.aws.amazon.com/cloud9/latest/user-guide/setup-classroom.html#setup-classroom-sign-in-classroom-student-first)
and follow the instructions to create your first environment.
    - Choose "Ubuntu Server" rather than "Amazon Linux" to make installing programs easier
4. Create your first program: File > New From Template > C++ File
5. Save your program: File > Save as "hello.cpp" in Folder "/HelloWorldProject"
6. Run your program: Run > Run with > C++
    - Next time you run the same program, you can use Run > Run Last
7. Learn more at [AWS Cloud9 Documentation](https://docs.aws.amazon.com/cloud9/)

### Saving to GitHub
When a Cloud9 environment is deleted, your programs in that environment will be deleted as well.
So, you **must** save your work to another location. You can use File > Download Project to save it to your local computer,
but a better way is to save it on GitHub
  1. Create a [GitHub](https://github.com/) username if you do not have one already
  2. On GitHub, create a new repository. Let's call it HelloWorldProject. Make this a private repository,
  so you can selectively share your work rather than making it public to the whole world
  3. On Cloud9 IDE, use the terminal (titled "bash")
  ```
  $ cd HelloWorldProject/
  $ git init
        Initialized empty Git repository in /home/ubuntu/environment/HelloWorldProject/.git/
  $ git add hello.cpp
  $ git config --global user.name "FirstName LastName"
  $ git config --global user.email "myemail@uw.edu" 
  $ git config credential.helper 'cache --timeout 7200'
  $ git commit -m "first commit"
  $ git remote add origin https://github.com/myGitHubUserName/HelloWorldProject.git
  $ git push -u origin master
        Username for 'https://github.com': myGitHubUserName
        Password for 'https://myGitHubUserName@github.com': 
        Counting objects: 3, done.
        Compressing objects: 100% (2/2), done.
        Writing objects: 100% (3/3), 334 bytes | 334.00 KiB/s, done.
        Total 3 (delta 0), reused 0 (delta 0)
        To https://github.com/myGitHubUserName/HelloWorldProject.git
         * [new branch]      master -> master
        Branch master set up to track remote branch master from origin.
```
  4. Confirm that your project has been uploaded by visiting https://github.com/myGitHubUserName/HelloWorldProject
  5. Make some changes to HelloWorldProject/hello.cpp using Cloud9 IDE
  ```
  $ git commit -a -m "Committing modified files already under source control."
  $ git push
  ```

### Loading a Project from GitHub
  1. On Cloud9 IDE, use the terminal (titled "bash")
  ```
  $ git clone https://github.com/myGitHubUserName/HelloWorldProject
        Cloning into 'HelloWorldProject'...
        Username for 'https://github.com': myGitHubUserName
        Password for 'https://myGitHubUserName@github.com': 
        remote: Enumerating objects: 3, done.
        remote: Counting objects: 100% (3/3), done.
        remote: Compressing objects: 100% (2/2), done.
        remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3)
  $ ls -al
        total 20
        drwxr-xr-x  4 ubuntu ubuntu 4096 Jun 20 19:29 .
        drwx------ 14 ubuntu ubuntu 4096 Jun 20 19:23 ..
        drwxr-xr-x  3 ubuntu ubuntu 4096 Jun 20 19:02 .c9
        drwxrwxr-x  3 ubuntu ubuntu 4096 Jun 20 19:29 HelloWorldProject
        -rw-r--r--  1 ubuntu ubuntu 569 Jun  3 09:22 README.md
  ```
  2. Make some changes to HelloWorldProject/hello.cpp using Cloud9 IDE
  ```
  $ cd HelloWorldProject
  $ git commit -a -m "Committing modified files already under source control."
  $ git push
  ```
  
### Setting up ssh for GitHub
  1. On Cloud9 IDE, use the terminal (titled "bash") to create an shh key-pair.
  The ssh key is for this instance only. If you delete this instance (or environment), you will need to
  repeat this step.
  ```
  $ ssh-keygen
        Generating public/private rsa key pair.
        Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): 
        Enter passphrase (empty for no passphrase): 
        Enter same passphrase again: 
        Your identification has been saved in /home/ubuntu/.ssh/id_rsa.
        Your public key has been saved in /home/ubuntu/.ssh/id_rsa.pub.
        The key fingerprint is:
        SHA256:7uvXOO7L2tqj/r6s+/4UweD4QqFLoHhX9A5t+eVEwRA ubuntu@ip-172-31-26-53
        The key's randomart image is:
        +---[RSA 2048]----+
        |    ..o . E+o.   |
        | . . o + = +.    |
        |. o . + B . =    |
        | . . . * o + .   |
        |      . S o o    |
        |       . .   .   |
        |        .  o.    |
        |       . ==..    |
        |       o@/#*.    |
        +----[SHA256]-----+
  $ ls -al ~/.ssh
        total 20
        drwxr-xr-x  2 ubuntu ubuntu 4096 Jun 20 19:57 .
        drwxr-xr-x 14 ubuntu ubuntu 4096 Jun 20 19:57 ..
        -rw-------  1 ubuntu ubuntu  991 Jun 20 19:55 authorized_keys
        -rw-------  1 ubuntu ubuntu 1679 Jun 20 19:57 id_rsa
        -rw-r--r--  1 ubuntu ubuntu  405 Jun 20 19:57 id_rsa.pub
  $ cat ~/.ssh/id_rsa.pub 
        ssh-rsa AAAAB....XnKyl RsZu9 ubuntu@ip-172-31-88-192
 ```
   2. On GitHub, Settings > SSH and GPG Keys > New SSH Key
        - Title: c9key
        - Key: copy-and-paste the above key starting with ssh-rsa
   3. Make some changes to HelloWorldProject/hello.cpp using Cloud9 IDE
   4. Push the modified project using ssh
   ```
  $ cd HelloWorldProject
  $ git commit -a -m "again"
        [master 16de09d] again
         1 file changed, 1 insertion(+), 1 deletion(-)
  $ git remote set-url origin git@github.com:myGitHubUserName/HelloWorldProject.git
  $ git push
        The authenticity of host 'github.com (192.30.253.113)' can't be established.
        RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
        RSA key fingerprint is MD5:16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
        Are you sure you want to continue connecting (yes/no)? yes
        Warning: Permanently added 'github.com,192.30.253.113' (RSA) to the list of known hosts.
        Counting objects: 6, done.
        Compressing objects: 100% (4/4), done.
        Writing objects: 100% (6/6), 618 bytes | 618.00 KiB/s, done.
        Total 6 (delta 0), reused 0 (delta 0)
        To github.com:myGitHubUserName/HelloWorldProject.git
           e111206..16de09d  master -> master
   ```
   2. When cloning a GitHub repository, you can now use: `git clone git@github.com:myGitHubUserName/HelloWorldProject.git`


### Setting up Toolchain
We would like to add some additional tools we can use

- CMake for building and testing: `sudo snap install cmake --classic`
- cppcheck for checking google-style compliance: `sudo snap install cppcheck`
- cpplint for static code analysis: `pip install cpplint`
- valgrind for memory leaks: `sudo snap install valgrind --classic`
- Update the list of packages: `sudo apt update`
- Clang for compiling and analyzing programs: `sudo apt install clang`
- Clang tools: `sudo apt install clang-tools`
- Clang tidy: `sudo apt install clang-tidy`
    
### Setting up CMake
CMake is used for compiling large projects. It is also used by CLion. A simple CMakeLists.txt file follows
```
project(hello)

set(CMAKE_CXX_STANDARD 11)

# Needed so clang-tidy knows how we compiled this project
# Generates the compile_commands.json file
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# have compiler give warnings, but not for signed/unsigned
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -Wextra -Wno-sign-compare")

add_executable(hello hello.cpp)

# First time compiling program, use:
# $ cmake CMakeLists.txt ; make clean; make
# If you changed .cpp files but not CmakeLists.txt, to recompile use:
# $ make
```

If you add files to the project, you will need to run `cmake CMakeLists.txt` again. If you have just modified
files, you can use `make` to create a new executable

### A Shell Script: simplecompile.sh
Shell scripts are programs that work as if we had typed the commands on the command line.

Create a new file `simplecompile.sh` using [this template](cpp/simplecompile.sh).
You can use `./simplecompile.sh` to compile your program and run checks using cppcheck, cpplint, valgrind and clang-tidy.

Modify `simplecompile.sh` as needed. For example, your programs probably does not need copyright notice, so
`-legal/copyright` flag is appropriate.

### Using Travis CI

** Travis CI only works on public repositories **

Travis CI is a continuous integration platorm that works with GitHub. When configured properly, every time you push your project to GitHub, Travis CI will compile and run it on a new virtual machine. This lets you see if your program actually works on another machine.

1. Login to Travis CI and "Activate the GitHub Apps integration"
To setup Travis CI, create a new file, `.travis.yml` in your project with the following content:
```
# Travis.ci file https://docs.travis-ci.com/user/tutorial/
# Continous integration

# Login to https://travis-ci.com/ using your github credentials
# Add this repository to travis
# Every time there is a commit, this script will be run and result emailed

language: cpp

dist: xenial

before_install:
  - sudo apt-get install valgrind
  - sudo apt-get install cppcheck
  - sudo -H pip install cpplint
  - sudo apt install clang-tidy
  - uname -a
  - cppcheck --version
  - pip show cpplint
  - g++ --version
  - valgrind --version


script:
    - ./simplecompile.sh
    - echo "Travis CI is done!"
 ```
 
Cloud9 normally hides files that start with `.`, to make them visible click on the `gear icon` next to
`C and C++  Spaces: 4` at the boottom right of `hello.cpp` (or any file really) and select `Show Invisibles`

3. Add this new file to your git repository and push it to GitHub
```
   $ git add .travis.yml
   $ git commit -a -m "added travis"
   $ git push
```
4. Login to Travis CI. Select your repository. You might have to choose More Options > Trigger Build to get the compilation started the first time around.



    
  
