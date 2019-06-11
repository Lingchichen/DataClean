"""
------------------------------------------------------------------------
[program description]
function clean : clean those unnecessary data from original file.ex:breaking lines(-------------)
                 Whitespace at the start of string.
function parse : create common pattern and match pattern within cleaned contents.
                 Also deal with some special sentences.
                 ex:"Will you keep working on it?" asked Man. (take care of this as one sentence)
function sort :  take care of sentences started with non-word characters
                 ex:"And don't say we'll switch to another sun."
                 remove " first then compare it with other sentences.
                 Also takeing care of upper cases and lower cases.
------------------------------------------------------------------------
Author: Jack Chen
Email:  jackchen4work@gmail.com
Cell:   519-616-7521
github: https://github.com/waterloostar
__updated__ = "2019-03-16"
------------------------------------------------------------------------
"""
import re
def clean(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        contents=f.read()
        clean_contents=re.sub(r'(\-{5,})|^\s*$','',contents)
        print(clean_contents)
        print(len(clean_contents))
        clean_contents=re.sub(r'^\n','',clean_contents)
    f.close()
    return clean_contents

def parse(clean_contents):
    temp=[]
    n=0
    pattern=re.compile(r'[\.\?!]\'?"?\)?')
    matches=pattern.finditer(clean_contents)
    for match in matches:
        print(match.group(0))
    var=re.sub(r'([\.\?!]\'?"?\)?)',r'\1|',clean_contents)
    print(var)
    parse_content=re.split(re.compile(r'\|'),var)
    for i in range(len(parse_content)):
        parse_content[i]=re.sub(r'(^\s)','',parse_content[i])
    print(parse_content)
    for i in range(len(parse_content)):
        if parse_content[i][0].islower():
            temp.append(i)
            print(parse_content[i-1:i+1])
            parse_content[i-1]=''.join(parse_content[i-1:i+1])
            print(parse_content[i])
            print(parse_content[i-1])
    for i in temp:
        print(parse_content[i])
        parse_content.remove(parse_content[i-n])
        print(parse_content[i-n])
        n=n+1
    for i in range(len(parse_content)):
        if parse_content[i][0].islower():
            print(parse_content[i])
    return parse_content

def sort(parse_content,output_file):
    print(parse_content)
    parse_content.sort(key=rep)
    print(parse_content)
    with open(output_file,'w') as of:
        for i in range(len(parse_content)):
            of.write((parse_content)[i]+'\n')
def rep(str):
    return re.sub(r'^[\W]+','',str.lower())
