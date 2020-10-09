import sys
import json
import requests
import datetime
import sqlite3

def loadMembers(membersFile):    
    try:
        members = []
        f = open(membersFile, "r")
        membersJson = json.load(f)
        count = 0
        for member in membersJson:            
            count +=1
            members.append(member['login'])
        
        return members
    except Exception as identifier:
        print("Error while loading file: {}".format(identifier))
        sys.exit(-1)

def getCommits(token):    
    i = 1
    url = "https://api.github.com" +"/repos/BendingSpoons/katana-swift/commits?sha=master&per_page=100&page={}".format(i)
    
    headers = {'Content-Type': 'application/json',
           'Authorization': 'token {}'.format(token)}
    res = requests.get(url, headers=headers)
    commits = res.json()            

    while "next" in res.headers.get('link', None):
        i += 1
        url = "https://api.github.com" +"/repos/BendingSpoons/katana-swift/commits?sha=master&per_page=100&page={}".format(i)        
        res = requests.get(url, headers=headers)
        commits.extend(res.json())

    return commits

def getCommitData(commits):
    commitInfo = []
    for commit in commits:
        try:
            aux = {}
            aux['login'] = commit['author']['login']
            aux['data'] = commit['commit']['author']['date']
            aux['sha'] = commit['sha']
            aux['message'] = commit['commit']['message']
            d1 = datetime.datetime(2018, 6, 27)
            format = '%Y-%m-%dT%H:%M:%SZ'            
            date_time_obj = datetime.datetime.strptime(aux['data'], format)
            if date_time_obj > d1 :
                commitInfo.append(aux)
                aux['is_external'] = checkIsInternal(commit)

                        
        except Exception:                            
            aux['login'] = "notfound"
            aux['data'] = commit['commit']['author']['date']
            aux['sha'] = commit['sha']
            aux['message'] = commit['commit']['message']
            d1 = datetime.datetime(2018, 6, 27)
            format = '%Y-%m-%dT%H:%M:%SZ'            
            date_time_obj = datetime.datetime.strptime(aux['data'], format)
            if date_time_obj > d1 :
                commitInfo.append(aux)
                aux['is_external'] = checkIsInternal(commit)
            
        
    
    return commitInfo

def checkIsInternal(commit):
    try:                
        is_external = 1                
        for member in membersArray:            
            if commit['author']['login'] == member:                
                is_external = 0
        return is_external    
    except Exception:
        return 1

def createSqlite(sqlfile):
    with sqlite3.connect(sqlfile) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS commits (sha TEXT, date TEXT, author TEXT, message TEXT, is_external INTEGER)')
        #data = cursor.fetchone()   

def updateSqlite(sqlfile, commits):
    try:
        for commit in commits:
            msg = commit['message'].replace("'", "''")
            sql = "insert into commits(sha, date, author, message, is_external) values('{}','{}','{}','{}',{})".format(commit['sha'],commit['data'],commit['login'],msg,commit['is_external'],)            
            with sqlite3.connect(sqlfile) as conn:
                cursor = conn.cursor()
                cursor.execute(sql)            
    except Exception as ex:
        print("Error while inserting: {} \n {}".format(sql,ex))

token = "insert your token here"
filePath = "assets/members.json"
sqlFile = "github.db"

print("loading members..")
membersArray = loadMembers(filePath)

print("getting commits..")
commits = getCommits(token)
print("got: {}".format(len(commits)))

commitsData = getCommitData(commits)

print("creating sqlite db {}".format(sqlFile))
createSqlite(sqlFile)

updateSqlite(sqlFile,commitsData)

#for commit in commitsData:
    #print(commit)
