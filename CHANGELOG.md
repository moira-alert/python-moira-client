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
