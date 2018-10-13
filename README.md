[![Build Status](https://travis-ci.org/moira-alert/python-moira-client.svg?branch=master)](https://travis-ci.org/moira-alert/python-moira-client)

# Moira Client

If you're new here, better check out our main [README](https://github.com/moira-alert/moira/blob/master/README.md).

Python client for Moira.

# Installation

```
pip install moira-client
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
