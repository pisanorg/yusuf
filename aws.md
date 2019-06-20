# AWS

AWS provides several services with a free-tier and additional services are often available under AWS Educate Starter Account.

## Cloud 9
Provides a cloud based environment for programming. Make sure you save your work to GitHub or some other location

### Getting Started

1. [Instructor Only] [Setup Classroom](https://docs.aws.amazon.com/cloud9/latest/user-guide/setup-classroom.html)
2. As a student, you should get an email inviting you to join an "AWS Educate Classroom"
3. [Enter Classroom](https://docs.aws.amazon.com/cloud9/latest/user-guide/setup-classroom.html#setup-classroom-sign-in-classroom-student-first)
and follow the instructions to create your first environment,
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
        Initialized empty Git repository in /home/ec2-user/environment/HelloWorldProject/.git/
  $ git add hello.cpp
  $ git config --global user.name "FirstName LastName"
  $ git config --global user.email "myemail@uw.edu" 
  $ git config credential.helper 'cache --timeout 7200
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
        drwxr-xr-x  4 ec2-user ec2-user 4096 Jun 20 19:29 .
        drwx------ 14 ec2-user ec2-user 4096 Jun 20 19:23 ..
        drwxr-xr-x  3 ec2-user ec2-user 4096 Jun 20 19:02 .c9
        drwxrwxr-x  3 ec2-user ec2-user 4096 Jun 20 19:29 HelloWorldProject
        -rw-r--r--  1 ec2-user ec2-user  569 Jun  3 09:22 README.md
  ```
  2. Make some changes to HelloWorldProject/hello.cpp using Cloud9 IDE
  ```
  $ cd HelloWorldProject
  $ git commit -a -m "Committing modified files already under source control."
  $ git push
  ```
  

  
