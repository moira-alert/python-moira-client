# 4.3.1

Fix package issues

# 4.3.0

Add support for Team APIs

# 4.2.1

Add support for name field in contacts

# 4.2.0

Add support for multiple clusters in trigger creation

Now you can use `cluster_id` field in api to set non-default cluster for remote triggers. List of available clusters can be seen in api at `https://your-moira-url/api/config`

# 4.1.0

Add support for prometheus trigger creation.

Now you can use `trigger_source` field in api that overrides `is_remote` field

# 4.0.2

Fix typo

# 4.0.1

Small refactor to satisfy users that use Python < 3.6

# 4.0.0

Make validation for Python-client like validation in Web Moira. It is need to make valiation right and unified for all Moira client sides.

[Use new validation for creating/updating triggers](https://github.com/moira-alert/python-moira-client/commit/3edb4c720d4b80ae8a4bd6117cb2b9cf0c5bec16)

[Return response object instead of string ID](https://github.com/moira-alert/python-moira-client/commit/5f2bccdd11d6ef6a2a548b9c7072037ebf0445c0)

# 3.0.0

‼️ Remove underscore-prefixed fields that contained scheduling time settings:

- `_start_hour`
- `_start_minute`
- `_end_hour`
- `_end_minute`
- `_timezone_offset`
- `disabled_days`

Because they were duplicates of data from sched field.

Please use sched field for scheduling settings instead.

# 2.6.1

- Fix missed disabled_days
- Push only tags create

# 2.6.0
- Add "/setMaintenance" methods #8
- Set login equal to auth_user by default if last one is specified #9
- Add "/config" methods #10
- Add support for changing moira notification state #16

# 2.5.1
- Added ability to subscribe for all triggers without specifying tags (moira-alert/moira#236).

# 2.4

- Python Moira client is now MIT licensed
- Changed default timezone offset to UTC
- Added dictionary attribute with plotting settings to subscription and<br/>
  corresponding methods enable_plotting(theme) and disable_plotting()
- Added boolean attribute mute_new_metrics to trigger
- Optimized tag stats methods (stats, fetch_assigned_triggers, fetch_assigned_triggers_by_tags)<br/>
to return trigger id's instead of triggers to speed up method execution time

# 2.3.5
- Fixed url to update existing subscription

# 2.3.4

- Added health methods (get_notifier_state, disable_notifications, enable_notifications) to potect<br/>
  end user from false NODATA notifications. <br/>
  See more details: https://moira.readthedocs.io/en/latest/user_guide/selfstate.html
- Added event.delete_all() and notification.delete_all() to remove unexpectedly generated<br/>
  trigger events and notifications in cases when Moira Notifier is managed to stop sending notifications.
- Added subscription.test(subscription_id) to trigger test notification
- Added boolean attributes to subscription (ignore_warnings, ignore_recoverings).<br/>
  Corresponding tags "ERROR", "DEGRADATION" and "HIGH DEGRADATION" are deprecated
- Added boolean "is_remote" attribute to trigger to provide ability to use external Graphite storage<br/>
  instead of Redis
- Added string "trigger_type" attribute to trigger. Options are: rising, falling, expression<br/>
  Single thresholds (only warn_value or only error_value) may be used if "trigger_type" value<br/>
  is defined.

# 2.1.1
- Allow passing warn_value and error_value for trigger as None when expression is used
- Fixed case with subscription's schedule with no days selected

# 2.0
- Added custom headers support
- Added trigger creation by custom id
- Removed tags extra data addition feature
- Changed ttl type from string to int
- Optimized fetch_by_id for large production solutions

# 0.4
- Added fetch_assigned_triggers_by_tags method for Tag entity
- Fixed trigger existence check. Check equals by casting to sets
- Fixed trigger delete logic

# 0.3.3
- Fixed contact creation. Explore only current user's contacts

# 0.3.2
- Added basic authorization

# 0.3.1
- Trigger update on save
- Subscription is_exist method added
- Contact idempotent creation

# 0.3
- Store id in Trigger after save of existent trigger
- Add get_id Contact method

# 0.2
- TriggerManager is_exist function added
- TriggerManager get_non_existent function added

# 0.1.1
- Trigger exist check added

# 0.1
- base functionality (support for models: contact, event, notification, pattern, subscription, tag, trigger)
