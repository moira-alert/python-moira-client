[![Build Status](https://travis-ci.org/moira-alert/python-moira-client.svg?branch=master)](https://travis-ci.org/moira-alert/python-moira-client)

# Moira Client

Python client for Moira.

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
    name='trigger_name', 
    targets=['metric.rps', 'another_metric.rps'],
    desc='my trigger',
    warn_value=300,
    error_value=600,
    tags=['service'],
    ttl_state=STATE_ERROR
)

trigger.disable_day('Tue')
trigger.save()
print(trigger.id)
```

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
trigger = moira.trigger.get_by_id('bb1a8514-128b-406e-bec3-25e94153ab30')
moira.trigger.delete(trigger.id)
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
