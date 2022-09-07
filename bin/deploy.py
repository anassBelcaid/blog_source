#!/usr/bin/env python
"""
Script to deploy the source to github
"""

import argparse
import pathlib
from subprocess import check_output 
from shutil import rmtree, copytree
import os


#{{{ Parsing
#default parser
parser = argparse.ArgumentParser()

parser.add_argument("-m","--message",help=" Push message" )

#parse arguments
args = parser.parse_args()
#}}}

# Default path {{{ #
source = pathlib.Path("/home/anass/github/blog_source/")
blog   = pathlib.Path("/home/anass/github/anassBelcaid.github.io")
build_command = "bundle exec jekyll build"
# }}} Default path #

if __name__ == "__main__":
    
    #Changing the source directory
    print("change to the source")
    os.chdir(source)


    #Building the source
    print("Building")
    check_output(build_command.split())


    #Change to blog
    print("Chaning to blog")
    os.chdir(blog)

    #removing everything
    for item in blog.iterdir():
        if item.name ==".git":
            continue
        if os.path.isdir(item):
            rmtree(item)
        else:
            os.remove(item)

    #Copying the _site files into source
    print("Copying")
    copytree(source/"_site", os.getcwd(), dirs_exist_ok=True)


    #Pusing
    add_command = "git add ."
    check_output(add_command.split())


    #Pusing command
    print("Commiting")
    committing_command = ["git", "commit", "-m", args.message]
    check_output(committing_command)


    print("Pushing to original")
    check_output(["git", "push"])


    


    


