#!/usr/bin/env python
from atlassian import Jira

def create_onboarding_tickets():
    jira = Jira(
            url='https://asdf.atlassian.net',
            username='username@email.com',
            password='jira-api-token')

    ticket = {
            "project": {"key": "AWD"},
            "summary": "Issue created via REST.",
            "description": "bla bla bla goes here",
            "issuetype": {"name": "Task"}
       }
    jira.issue_create(ticket)

create_onboarding_tickets()
