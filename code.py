import re
import os
from pathlib import Path

if os.path.isfile('./data/IssueContentQuote/result.txt') :
    open('./data/IssueContentQuote/result.txt', "w").close()  ##Have to clear the file if it already exists before using it

def store_on_fs(data, file_name):
    ##Store data in file named `file_name`
    with open(file_name, "a") as f:
        for i in range(0,len(data)):
            f.write(str(data[i])+'\n')




def regexify(s):
    pattern = r"(?<=\`)Test_openjdk\d+.+?\/?(?=\`)"
    internal_jenkins_job_names = re.findall(pattern, s)
    new_links = [''.join(('https://internal_jenkins/job/',x)) for x in internal_jenkins_job_names]

    pattern2 = r"(https:\/\/.+\/job\/Test_openjdk\d+.+\/\d+)"
    adoptium_jenkins_links = re.findall(pattern2, s)

    pattern3 = r"(^[a-zA-Z].+(?=_FAILED))"
    content = s.split()
    test_cases_names = [a for a in content if re.findall(pattern3, a) != []]

    jenkins_links = []
    test_names = []

    jenkins_links = new_links + adoptium_jenkins_links
    test_names = "test_names"+" "+ "=" + " "+ "["+", ".join(test_cases_names)+ "]"
    print(test_names)

    return jenkins_links, test_names





directory = './data/IssueContent' ##enter directory address


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f,'r') as file:
            s=file.read()
            res=regexify(s)
            #print(res)
            store_on_fs(res, './data/IssueContentQuote/result.txt') #Enter result file and use in loop to prevent unexplained
