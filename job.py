#!/usr/local/bin/python3.8
#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	JOB PROCESSING
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-10-22
#* PURPOSE	JOB SPAWNER
#* FILE		JOB.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-10-22 - LHAYNIE - INITIAL VERSION
#**********************************************************
#Copyright 2020 Haynie IPHC, LLC
#Developed by Haynie Research & Development, LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.#
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
import sys
import os
import subprocess

if len(sys.argv) == 1:
    args = sys.argv
    print("No arguments provided.")
    exit(0)
elif len(sys.argv) == 2:
    args = sys.argv
    arg1 = sys.argv[1]
    print("Submitting job with no retry attempts.")
elif len(sys.argv) == 3:
    args = sys.argv
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print("Submitting job with " + arg2 + " retry attempts.")
else:
    print("No option provided, use --help for options.")
    exit(0)

counter = 0
attempts = 3
result = None
output = ""
error = ""

def submit (cmd):
    job = subprocess.Popen(cmd,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=True,
                           universal_newlines=True)
    std_out, std_err = job.communicate()
    return job.returncode, std_out, std_err

if len(sys.argv) > 2:
    attempts = float(arg2)
else:
    attempts = 0

print("Job: " + arg1 + "\n")

while (counter <= attempts):
    result, output, error = submit(arg1)
    counter += 1
    if result == 0:
        print("Return code: {}".format(result));
        print("Output: " + output)
        Print("Success, job completed without error.")
        exit(0)
    elif ((result == 1) or (result == 2)):
        print("Return code: {}".format(result));
        print("Output: " + output)
        print("Warning, job completed but finished with non fatal errors. Error:" + error)
        exit(0)
    elif ((result == 126) or (result == 127)):
        print("Return code: {}".format(result));
        print("Output: " + output)
        print("Error: " + error)
        print("Aborting due to command not found or unable to execute.")
        exit(result)
    elif ((result > 2) and (counter <= attempts)):
        print("Return code: {}".format(result));
        print("Output: " + output)
        print("Error: " + error)
        print("Retrying job, attempt: " + str(counter))
    else:
        print("Return code: {}".format(result));
        print("Output: " + output)
        print("Error: " + error)
        exit(result)
