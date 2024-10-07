[![Build Status](https://travis-ci.org/moira-alert/python-moira-client.svg?branch=master)](https://travis-ci.org/moira-alert/python-moira-client)

# Moira Client

If you're new here, better check out our main [README](https://github.com/moira-alert/moira/blob/master/README.md).

Python client for Moira.

# Installation

```
pip install moira-python-client
```

# Getting started

Initialize Moira client:
```
from moira_client import Moira

moira = Moira('http://localhost:8888/api/')
```

## Triggers

### Create new trigger
```
from moira_client.models.trigger import STATE_ERROR

trigger = moira.trigger.create(
    id='service_trigger_name',
    name='Trigger name',
    tags=['service'],
    targets=['prefix.service.*.postfix'],
    warn_value=300,
    error_value=600,
    desc='my trigger',
    ttl_state=STATE_ERROR
)

trigger.disable_day('Tue')
trigger.save()
print(trigger.id)
```

> **Note:** id parameter is not required but highly recommended for large production solutions <br>
> (e.q. fetch_by_id will work faster than is_exist).
> If parameter is not specified, random trigger guid will be generated.

### Update triggers
Turn off all triggers for Monday.
```
triggers = moira.trigger.fetch_all()
for trigger in triggers:
    trigger.disable_day('Mon')
    trigger.update()
```

### Delete trigger
```
trigger = moira.trigger.fetch_by_id('bb1a8514-128b-406e-bec3-25e94153ab30')
moira.trigger.delete(trigger.id)
```

### Check whether trigger exists or not (manually)
```
trigger = moira.trigger.create(
    name='service',
    targets=['service.rps'],
    tags=['ops']
)

if not moira.trigger.is_exist(trigger):
    trigger.save()
```

### Get non existent triggers
```
trigger1 = moira.trigger.create(
    name='service',
    targets=['service.rps'],
    tags=['ops']
)

trigger2 = moira.trigger.create(
    name='site',
    targets=['site.rps'],
    tags=['ops']
)

triggers = [trigger1, trigger2]

non_existent_triggers = moira.trigger.get_non_existent(triggers)
```

## Subscription

### Create subscription
```
subscription = moira.subscription.create(
    contacts=['79ac9de2-a3b3-4f94-b3ea-74f6f4094fd2'],
    tags=['tag']
)
subscription.save()
```

### Delete subscription
Delete all subscriptions
```
subscriptions = moira.subscription.fetch_all()
for subscription in subscriptions:
    moira.subscription.delete(subscription.id)
```

## Contact

### Get all contacts
```
contacts = moira.contact.fetch_all()
for contact in contacts:
    print(contact.id)
```

### Get contact id by type and value
```
contact_id = moira.contact.get_id(type='slack', value='#err')
print(contact_id)
```

## Team

### Get all teams
```python
teams = moira.team.get_all()
```

### Create a new team
```python
from moira_client.models.team import TeamModel

team = TeamModel(
    description="Team that holds all members of infrastructure division",
    name="Infrastructure Team",
)

saved_team = moira.team.create(team)
```

### Delete a team
```python
team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"

deleted_team = moira.team.delete(team_id)
```

### Get a team by ID
```python
team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"

team = moira.team.get(team_id)
```

### Update existing team
```python
from moira_client.models.team import TeamModel

team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"
team = TeamModel(
    description="Team that holds all members of infrastructure division",
    name="Infrastructure Team",
)

updated_team = moira.team.update(team_id, team)
```

### Team Settings

#### Get team settings
```python
team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"

settings = moira.team.settings.get(team_id)
```

### Team User

#### Get users of a team

```python
team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"

users = moira.team.user.get(team_id)
```

#### Add users to a team

```python
from moira_client.models.team.user import TeamMembers

team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"
users_to_add = TeamMembers(usernames=["anonymous", ])

users = moira.team.user.add(team_id, users_to_add)
```

#### Set users of a team

```python
from moira_client.models.team.user import TeamMembers

team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"
users_to_set = TeamMembers(usernames=["anonymous", ])

users = moira.team.user.set(team_id, users_to_set)
```

#### Delete a user from a team

```python
team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"
team_user_id = "anonymous"

users = moira.team.user.delete(team_id, team_user_id)
```

### Team Subscription

#### Create a new team subscription

```python
from moira_client.models.subscription import SubscriptionModel

team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"
subscription_to_create = SubscriptionModel(
    any_tags=False,
    contacts=[
        "acd2db98-1659-4a2f-b227-52d71f6e3ba1"
    ],
    enabled=True,
    ignore_recoverings=False,
    ignore_warnings=False,
    plotting={
        "enabled": True,
        "theme": "dark"
    },
    sched={
        "days": [
            {
                "enabled": True,
                "name": "Mon"
            }
        ],
        "endOffset": 1439,
        "startOffset": 0,
        "tzOffset": -60
    },
    tags=[
        "server",
        "cpu"
    ],
    throttling=False,
    user="",
)

subscription = moira.team.subscription.create(team_id, subscription_to_create)
```

### Team Contact

#### Create a new team contact

```python
from moira_client.models.contact import Contact

team_id = "d5d98eb3-ee18-4f75-9364-244f67e23b54"
contact_to_create = Contact(
    name="Mail Alerts",
    team_id=team_id,
    type="mail",
    user="",
    value="devops@example.com",
)

contact = moira.team.contact.create(team_id, contact_to_create)
```
