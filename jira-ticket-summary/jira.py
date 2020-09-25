#!/usr/bin/env python
from atlassian import Jira

def daily_standup():
    jira = Jira(
            url='https://asdf.atlassian.net',
            username='username@email.com',
            password='jira-api-token')

    jql_request_to_do = "project = PROJECTNAME AND assignee = currentuser() AND status IN ('To Do') ORDER BY issuekey"
    jql_request_in_progress = "project = PROJECTNAME AND assignee = currentuser() AND status IN ('In Progress') ORDER BY issuekey"

    to_do = jira.jql(jql_request_to_do)=['issues']
    in_progress = jira.jql(jql_request_in_progress)=['issues']

    to_do_list = []
    in_progress_list = []

    for i in to_do:
        to_do_list.append(i['fields']['summary'])

    for i in in_progress:
        in_progress_list.append(i['fields']['summary'])

    print("To Do")
    for i in to_do_list:
        print(" > " + i)
    print ("")
    print("In Progress")
    for i in in_progress_list:
        print(" - " + i)

daily_standup()
