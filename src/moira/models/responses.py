from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field
from pydantic.experimental.missing_sentinel import MISSING

__all__ = [
    "MoiraTriggerData",
    "MoiraScheduleDataDay",
    "MoiraScheduleData",
    "MoiraCheckData",
    "MoiraTriggerCheck",
    "MoiraTrigger",
    "MoiraPlottingData",
    "MoiraSubscriptionData",
    "MoiraEventInfo",
    "MoiraNotificationEvent",
    "MoiraContactData",
    "MoiraScheduledNotification",
    "MoiraMetricValue",
    "MoiraMaintenanceInfo",
    "MoiraMetricState",
    "DtoTeamModel",
    "DtoUserTeams",
    "DtoSubscription",
    "DtoContactWithScore",
    "DtoUserSettings",
    "DtoUser",
    "DtoTriggersSearchResultDeleteResponse",
    "DtoTriggersList",
    "DtoTriggerNoisiness",
    "DtoTriggerNoisinessList",
    "DtoTriggerModel",
    "DtoTriggerMaintenance",
    "DtoPatternMetrics",
    "DtoTriggerDump",
    "DtoProblemOfTarget",
    "DtoTreeOfProblems",
    "DtoTriggerCheckResponse",
    "DtoTriggerCheck",
    "DtoTrigger",
    "DtoThrottlingResponse",
    "DtoTeamsList",
    "DtoContactScore",
    "DtoTeamContactWithScore",
    "DtoTeamSettings",
    "DtoTeamMembers",
    "DtoTeamContact",
    "DtoTagStatistics",
    "DtoTagsStatistics",
    "DtoTagsData",
    "DtoSubscriptionList",
    "DtoSaveTriggerResponse",
    "DtoSaveTeamResponse",
    "DtoPatternData",
    "DtoPatternList",
    "DtoNotifierStateForSource",
    "DtoNotifierStatesForSources",
    "DtoNotifierState",
    "DtoNotificationsList",
    "DtoNotificationDeleteResponse",
    "DtoMessageResponse",
    "DtoEventsList",
    "DtoContactNoisiness",
    "DtoContactNoisinessList",
    "DtoContactList",
    "DtoContactEventItem",
    "DtoContactEventItemList",
    "DtoContact",
    "ApiWebContact",
    "ApiSentry",
    "ApiMetricSourceCluster",
    "ApiFeatureFlags",
    "ApiWebConfig",
    "ApiErrorResponse",
]


class BaseConfig:
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
    )


class SetTriggerMaintenanceResponse200(BaseModel, BaseConfig): ...


class DeleteTriggerNodataMetricsResponse200(BaseModel, BaseConfig): ...


class DeleteTriggerMetricResponse200(BaseModel, BaseConfig): ...


class SendTestNotificationResponse200(BaseModel, BaseConfig): ...


class RemoveSubscriptionResponse200(BaseModel, BaseConfig): ...


class DeletePatternResponse200(BaseModel, BaseConfig): ...


class DeleteAllEventsResponse200(BaseModel, BaseConfig): ...


class SendTestContactNotificationRequestBody(BaseModel, BaseConfig): ...


class SendTestContactNotificationResponse200(BaseModel, BaseConfig): ...


class RemoveContactRequestBody(BaseModel, BaseConfig): ...


class RemoveContactResponse200(BaseModel, BaseConfig): ...


class MoiraTriggerData(BaseModel, BaseConfig):
    notifier_trigger_tags: list[str] = Field(..., alias="__notifier_trigger_tags")
    desc: str
    error_value: float
    id: str
    is_remote: bool
    name: str
    targets: list[str]
    warn_value: float
    cluster_id: str | MISSING = Field(MISSING)
    trigger_source: str | MISSING = Field(MISSING)


class MoiraScheduleDataDay(BaseModel, BaseConfig):
    enabled: bool
    name: Literal["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] | MISSING = Field(MISSING)


class MoiraScheduleData(BaseModel, BaseConfig):
    """
    Determines when Moira should monitor trigger
    """

    days: list[MoiraScheduleDataDay]
    end_offset: int = Field(..., alias="endOffset")
    start_offset: int = Field(..., alias="startOffset")
    tz_offset: int = Field(..., alias="tzOffset")


class MoiraCheckData(BaseModel, BaseConfig):
    last_successful_check_timestamp: int = Field(
        ...,
        description=(
            "LastSuccessfulCheckTimestamp - time of the last check of the trigger, during which there were no errors"
        ),
    )
    maintenance_info: MoiraMaintenanceInfo
    metrics: dict
    metrics_to_target_relation: dict = Field(
        ...,
        description=(
            "MetricsToTargetRelation is a map that holds relation between metric names that was alone during last"
            ' check and targets that fetched this metric 	{"t1": "metric.name.1", "t2": "metric.name.2"}'
        ),
    )
    score: int
    state: str
    event_timestamp: int | MISSING = Field(MISSING)
    maintenance: int | MISSING = Field(MISSING)
    msg: str | MISSING = Field(MISSING)
    suppressed: bool | MISSING = Field(MISSING)
    suppressed_state: str | MISSING = Field(MISSING)
    timestamp: int | MISSING = Field(
        MISSING,
        description=(
            "Timestamp - time, which means when the checker last checked this trigger, this value stops updating if"
            " the trigger does not receive metrics"
        ),
    )


class MoiraTriggerCheck(BaseModel, BaseConfig):
    alone_metrics: dict
    created_at: int
    created_by: str
    error_value: float
    highlights: dict
    id: str
    last_check: MoiraCheckData
    mute_new_metrics: bool
    name: str
    patterns: list[str]
    tags: list[str]
    targets: list[str]
    throttling: int
    trigger_type: str
    updated_at: int
    updated_by: str
    warn_value: float
    cluster_id: str | MISSING = Field(MISSING)
    desc: str | MISSING = Field(MISSING)
    expression: str | MISSING = Field(MISSING)
    python_expression: str | MISSING = Field(MISSING)
    sched: MoiraScheduleData | MISSING = Field(MISSING, description="Determines when Moira should monitor trigger")
    team_id: str | MISSING = Field(MISSING)
    trigger_source: str | MISSING = Field(MISSING)
    ttl: int | MISSING = Field(MISSING)
    ttl_state: str | MISSING = Field(MISSING)


class MoiraTrigger(BaseModel, BaseConfig):
    alone_metrics: dict
    created_at: int
    created_by: str
    error_value: float
    id: str
    mute_new_metrics: bool
    name: str
    patterns: list[str]
    tags: list[str]
    targets: list[str]
    trigger_type: str
    updated_at: int
    updated_by: str
    warn_value: float
    cluster_id: str | MISSING = Field(MISSING)
    desc: str | MISSING = Field(MISSING)
    expression: str | MISSING = Field(MISSING)
    python_expression: str | MISSING = Field(MISSING)
    sched: MoiraScheduleData | MISSING = Field(MISSING, description="Determines when Moira should monitor trigger")
    team_id: str | MISSING = Field(MISSING)
    trigger_source: str | MISSING = Field(MISSING)
    ttl: int | MISSING = Field(MISSING)
    ttl_state: str | MISSING = Field(MISSING)


class MoiraPlottingData(BaseModel, BaseConfig):
    enabled: bool
    theme: str


class MoiraSubscriptionData(BaseModel, BaseConfig):
    any_tags: bool
    contacts: list[str]
    enabled: bool
    id: str
    plotting: MoiraPlottingData
    sched: MoiraScheduleData = Field(..., description="Determines when Moira should monitor trigger")
    tags: list[str]
    team_id: str
    throttling: bool
    user: str
    ignore_recoverings: bool | MISSING = Field(MISSING)
    ignore_warnings: bool | MISSING = Field(MISSING)


class MoiraEventInfo(BaseModel, BaseConfig):
    interval: int | MISSING = Field(MISSING)
    maintenance: MoiraMaintenanceInfo | MISSING = Field(MISSING)


class MoiraNotificationEvent(BaseModel, BaseConfig):
    event_message: MoiraEventInfo
    metric: str
    old_state: str
    state: str
    timestamp: int
    trigger_id: str
    contact_id: str | MISSING = Field(MISSING)
    msg: str | MISSING = Field(MISSING)
    sub_id: str | MISSING = Field(MISSING)
    trigger_event: bool | MISSING = Field(MISSING)
    value: float | MISSING = Field(MISSING)
    values: dict | MISSING = Field(MISSING)


class MoiraContactData(BaseModel, BaseConfig):
    id: str
    team: str
    type: str
    user: str
    value: str
    extra_message: str | MISSING = Field(MISSING)
    name: str | MISSING = Field(MISSING)


class MoiraScheduledNotification(BaseModel, BaseConfig):
    contact: MoiraContactData
    event: MoiraNotificationEvent
    plotting: MoiraPlottingData
    send_fail: int
    throttled: bool
    timestamp: int
    trigger: MoiraTriggerData
    created_at: int | MISSING = Field(MISSING)


class MoiraMetricValue(BaseModel, BaseConfig):
    ts: int
    value: float
    step: int | MISSING = Field(MISSING)


class MoiraMaintenanceInfo(BaseModel, BaseConfig):
    remove_time: int
    remove_user: str
    setup_time: int
    setup_user: str


class MoiraMetricState(BaseModel, BaseConfig):
    event_timestamp: int
    maintenance_info: MoiraMaintenanceInfo
    state: str
    suppressed: bool
    timestamp: int
    deleted_but_kept: bool | MISSING = Field(
        MISSING,
        description=(
            "DeletedButKept controls whether the metric is shown to the user if the trigger has ttlState = Del and the"
            " metric is in Maintenance. The metric remains in the database"
        ),
    )
    maintenance: int | MISSING = Field(MISSING)
    suppressed_state: str | MISSING = Field(MISSING)
    value: float | MISSING = Field(MISSING)
    values: dict | MISSING = Field(MISSING)


class DtoTeamModel(BaseModel, BaseConfig):
    id: str
    name: str
    description: str | MISSING = Field(MISSING)


class DtoUserTeams(BaseModel, BaseConfig):
    teams: list[DtoTeamModel]


class DtoSubscription(BaseModel, BaseConfig):
    any_tags: bool
    contacts: list[str]
    enabled: bool
    id: str
    plotting: MoiraPlottingData
    sched: MoiraScheduleData = Field(..., description="Determines when Moira should monitor trigger")
    tags: list[str]
    team_id: str
    throttling: bool
    user: str
    ignore_recoverings: bool | MISSING = Field(MISSING)
    ignore_warnings: bool | MISSING = Field(MISSING)


class DtoContactWithScore(BaseModel, BaseConfig):
    id: str
    type: str
    value: str
    extra_message: str | MISSING = Field(MISSING)
    name: str | MISSING = Field(MISSING)
    score: DtoContactScore | MISSING = Field(MISSING)
    team_id: str | MISSING = Field(MISSING)
    user: str | MISSING = Field(MISSING)


class DtoUserSettings(BaseModel, BaseConfig):
    contacts: list[DtoContactWithScore]
    login: str
    subscriptions: list[DtoSubscription]
    auth_enabled: bool | MISSING = Field(MISSING)
    role: str | MISSING = Field(MISSING)


class DtoUser(BaseModel, BaseConfig):
    login: str
    auth_enabled: bool | MISSING = Field(MISSING)
    role: str | MISSING = Field(MISSING)


class DtoTriggersSearchResultDeleteResponse(BaseModel, BaseConfig):
    pager_id: str


class DtoTriggersList(BaseModel, BaseConfig):
    list: list[MoiraTriggerCheck]
    page: int | MISSING = Field(MISSING)
    pager: str | MISSING = Field(MISSING)
    size: int | MISSING = Field(MISSING)
    total: int | MISSING = Field(MISSING)


class DtoTriggerNoisiness(BaseModel, BaseConfig):
    alone_metrics: dict = Field(..., description="A list of targets that have only alone metrics")
    cluster_id: str = Field(..., description="Shows the exact cluster from where the metrics are fetched")
    created_at: str = Field(..., description="Datetime when the trigger was created")
    created_by: str = Field(..., description="Username who created trigger")
    error_value: float = Field(..., description="ERROR threshold")
    events_count: int = Field(..., description="EventsCount for the trigger.")
    expression: str = Field(..., description="Used if you need more complex logic than provided by WARN/ERROR values")
    id: str = Field(..., description="Trigger unique ID")
    is_remote: bool = Field(
        ...,
        description=(
            "Shows if trigger is remote (graphite-backend) based or stored inside Moira-Redis DB  Deprecated: Use"
            " TriggerSource field instead"
        ),
    )
    mute_new_metrics: bool = Field(..., description="If true, first event NODATA → OK will be omitted")
    name: str = Field(..., description="Trigger name")
    patterns: list[str] = Field(..., description="Graphite patterns for trigger")
    tags: list[str] = Field(..., description="Set of tags to manipulate subscriptions")
    targets: list[str] = Field(..., description="Graphite-like targets: t1, t2, ...")
    throttling: int
    trigger_source: str = Field(..., description="Shows the type of source from where the metrics are fetched")
    trigger_type: str = Field(..., description="Could be: rising, falling, expression")
    updated_at: str = Field(..., description="Datetime  when the trigger was updated")
    updated_by: str = Field(..., description="Username who updated trigger")
    warn_value: float = Field(..., description="WARN threshold")
    desc: str | MISSING = Field(MISSING, description="Description string")
    sched: MoiraScheduleData | MISSING = Field(MISSING, description="Determines when Moira should monitor trigger")
    team_id: str | MISSING = Field(MISSING, description="ID of a Team that owns this trigger")
    ttl: int | MISSING = Field(
        MISSING,
        description=(
            "When there are no metrics for trigger, Moira will switch metric to TTLState state after TTL seconds"
        ),
    )
    ttl_state: str | MISSING = Field(
        MISSING,
        description=(
            "When there are no metrics for trigger, Moira will switch metric to TTLState state after TTL seconds"
        ),
    )


class DtoTriggerNoisinessList(BaseModel, BaseConfig):
    list: list[DtoTriggerNoisiness] = Field(..., description="List of entities.")
    page: int = Field(..., description="Page number.")
    size: int = Field(..., description="Size is the amount of entities per Page.")
    total: int = Field(..., description="Total amount of entities in the database.")


class DtoTriggerModel(BaseModel, BaseConfig):
    alone_metrics: dict = Field(..., description="A list of targets that have only alone metrics")
    cluster_id: str = Field(..., description="Shows the exact cluster from where the metrics are fetched")
    created_at: str = Field(..., description="Datetime when the trigger was created")
    created_by: str = Field(..., description="Username who created trigger")
    error_value: float = Field(..., description="ERROR threshold")
    expression: str = Field(..., description="Used if you need more complex logic than provided by WARN/ERROR values")
    id: str = Field(..., description="Trigger unique ID")
    is_remote: bool = Field(
        ...,
        description=(
            "Shows if trigger is remote (graphite-backend) based or stored inside Moira-Redis DB  Deprecated: Use"
            " TriggerSource field instead"
        ),
    )
    mute_new_metrics: bool = Field(..., description="If true, first event NODATA → OK will be omitted")
    name: str = Field(..., description="Trigger name")
    patterns: list[str] = Field(..., description="Graphite patterns for trigger")
    tags: list[str] = Field(..., description="Set of tags to manipulate subscriptions")
    targets: list[str] = Field(..., description="Graphite-like targets: t1, t2, ...")
    trigger_source: str = Field(..., description="Shows the type of source from where the metrics are fetched")
    trigger_type: str = Field(..., description="Could be: rising, falling, expression")
    updated_at: str = Field(..., description="Datetime  when the trigger was updated")
    updated_by: str = Field(..., description="Username who updated trigger")
    warn_value: float = Field(..., description="WARN threshold")
    desc: str | MISSING = Field(MISSING, description="Description string")
    sched: MoiraScheduleData | MISSING = Field(MISSING, description="Determines when Moira should monitor trigger")
    team_id: str | MISSING = Field(MISSING, description="ID of a Team that owns this trigger")
    ttl: int | MISSING = Field(
        MISSING,
        description=(
            "When there are no metrics for trigger, Moira will switch metric to TTLState state after TTL seconds"
        ),
    )
    ttl_state: str | MISSING = Field(
        MISSING,
        description=(
            "When there are no metrics for trigger, Moira will switch metric to TTLState state after TTL seconds"
        ),
    )


class DtoTriggerMetrics(BaseModel, BaseConfig): ...


class DtoMetricsMaintenance(BaseModel, BaseConfig): ...


class DtoTriggerMaintenance(BaseModel, BaseConfig):
    metrics: dict[Any, Any]
    trigger: int | MISSING = Field(MISSING)


class DtoPatternMetrics(BaseModel, BaseConfig):
    metrics: dict
    pattern: str
    retention: dict


class DtoTriggerDump(BaseModel, BaseConfig):
    created: str
    last_check: MoiraCheckData
    metrics: list[DtoPatternMetrics]
    trigger: MoiraTrigger


class DtoProblemOfTarget(BaseModel, BaseConfig):
    argument: str
    position: int
    description: str | MISSING = Field(MISSING)
    problems: list[DtoProblemOfTarget] | MISSING = Field(MISSING)
    type: str | MISSING = Field(MISSING)


class DtoTreeOfProblems(BaseModel, BaseConfig):
    syntax_ok: bool
    tree_of_problems: DtoProblemOfTarget | MISSING = Field(MISSING)


class DtoTriggerCheckResponse(BaseModel, BaseConfig):
    targets: list[DtoTreeOfProblems] | MISSING = Field(MISSING, description="Graphite-like targets: t1, t2, ...")


class DtoTriggerCheck(BaseModel, BaseConfig):
    last_successful_check_timestamp: int = Field(
        ...,
        description=(
            "LastSuccessfulCheckTimestamp - time of the last check of the trigger, during which there were no errors"
        ),
    )
    maintenance_info: MoiraMaintenanceInfo
    metrics: dict
    metrics_to_target_relation: dict = Field(
        ...,
        description=(
            "MetricsToTargetRelation is a map that holds relation between metric names that was alone during last"
            ' check and targets that fetched this metric 	{"t1": "metric.name.1", "t2": "metric.name.2"}'
        ),
    )
    score: int
    state: str
    trigger_id: str
    event_timestamp: int | MISSING = Field(MISSING)
    maintenance: int | MISSING = Field(MISSING)
    msg: str | MISSING = Field(MISSING)
    suppressed: bool | MISSING = Field(MISSING)
    suppressed_state: str | MISSING = Field(MISSING)
    timestamp: int | MISSING = Field(
        MISSING,
        description=(
            "Timestamp - time, which means when the checker last checked this trigger, this value stops updating if"
            " the trigger does not receive metrics"
        ),
    )


class DtoTrigger(BaseModel, BaseConfig):
    alone_metrics: dict = Field(..., description="A list of targets that have only alone metrics")
    cluster_id: str = Field(..., description="Shows the exact cluster from where the metrics are fetched")
    created_at: str = Field(..., description="Datetime when the trigger was created")
    created_by: str = Field(..., description="Username who created trigger")
    error_value: float = Field(..., description="ERROR threshold")
    expression: str = Field(..., description="Used if you need more complex logic than provided by WARN/ERROR values")
    id: str = Field(..., description="Trigger unique ID")
    is_remote: bool = Field(
        ...,
        description=(
            "Shows if trigger is remote (graphite-backend) based or stored inside Moira-Redis DB  Deprecated: Use"
            " TriggerSource field instead"
        ),
    )
    mute_new_metrics: bool = Field(..., description="If true, first event NODATA → OK will be omitted")
    name: str = Field(..., description="Trigger name")
    patterns: list[str] = Field(..., description="Graphite patterns for trigger")
    tags: list[str] = Field(..., description="Set of tags to manipulate subscriptions")
    targets: list[str] = Field(..., description="Graphite-like targets: t1, t2, ...")
    throttling: int
    trigger_source: str = Field(..., description="Shows the type of source from where the metrics are fetched")
    trigger_type: str = Field(..., description="Could be: rising, falling, expression")
    updated_at: str = Field(..., description="Datetime  when the trigger was updated")
    updated_by: str = Field(..., description="Username who updated trigger")
    warn_value: float = Field(..., description="WARN threshold")
    desc: str | MISSING = Field(MISSING, description="Description string")
    sched: MoiraScheduleData | MISSING = Field(MISSING, description="Determines when Moira should monitor trigger")
    team_id: str | MISSING = Field(MISSING, description="ID of a Team that owns this trigger")
    ttl: int | MISSING = Field(
        MISSING,
        description=(
            "When there are no metrics for trigger, Moira will switch metric to TTLState state after TTL seconds"
        ),
    )
    ttl_state: str | MISSING = Field(
        MISSING,
        description=(
            "When there are no metrics for trigger, Moira will switch metric to TTLState state after TTL seconds"
        ),
    )


class DtoThrottlingResponse(BaseModel, BaseConfig):
    throttling: int


class DtoTeamsList(BaseModel, BaseConfig):
    list: list[DtoTeamModel]
    page: int
    size: int
    total: int


class DtoContactScore(BaseModel, BaseConfig):
    last_err: str | MISSING = Field(MISSING, description="LastErrMessage is the last error message encountered.")
    last_err_timestamp: int | MISSING = Field(
        MISSING, description="LastErrTimestamp is the timestamp of the last error."
    )
    score_percent: int | MISSING = Field(
        MISSING, description="ScorePercent is the percentage score of successful transactions."
    )
    status: str | MISSING = Field(MISSING, description="Status is the current status of the contact.")


class DtoTeamContactWithScore(BaseModel, BaseConfig):
    id: str
    type: str
    value: str
    extra_message: str | MISSING = Field(MISSING)
    name: str | MISSING = Field(MISSING)
    score: DtoContactScore | MISSING = Field(MISSING)
    team: str | MISSING = Field(MISSING, description="This field is deprecated")
    team_id: str | MISSING = Field(MISSING)
    user: str | MISSING = Field(MISSING)


class DtoTeamSettings(BaseModel, BaseConfig):
    contacts: list[DtoTeamContactWithScore]
    subscriptions: list[MoiraSubscriptionData]
    team_id: str


class DtoTeamMembers(BaseModel, BaseConfig):
    usernames: list[str]


class DtoTeamContact(BaseModel, BaseConfig):
    id: str
    type: str
    value: str
    extra_message: str | MISSING = Field(MISSING)
    name: str | MISSING = Field(MISSING)
    team: str | MISSING = Field(MISSING, description="This field is deprecated")
    team_id: str | MISSING = Field(MISSING)
    user: str | MISSING = Field(MISSING)


class DtoTagStatistics(BaseModel, BaseConfig):
    name: str
    subscriptions: list[MoiraSubscriptionData]
    triggers: list[str]


class DtoTagsStatistics(BaseModel, BaseConfig):
    list: list[DtoTagStatistics]


class DtoTagsData(BaseModel, BaseConfig):
    list: list[str]


class DtoSubscriptionList(BaseModel, BaseConfig):
    list: list[MoiraSubscriptionData]


class DtoSaveTriggerResponse(BaseModel, BaseConfig):
    id: str
    message: str
    check_result: DtoTriggerCheckResponse | MISSING = Field(MISSING, alias="checkResult")


class DtoSaveTeamResponse(BaseModel, BaseConfig):
    id: str


class DtoPatternData(BaseModel, BaseConfig):
    metrics: list[str]
    pattern: str
    triggers: list[DtoTriggerModel]


class DtoPatternList(BaseModel, BaseConfig):
    list: list[DtoPatternData]


class DtoNotifierStateForSource(BaseModel, BaseConfig):
    actor: str
    cluster_id: str
    state: str
    trigger_source: str
    message: str | MISSING = Field(MISSING)


class DtoNotifierStatesForSources(BaseModel, BaseConfig):
    sources: list[DtoNotifierStateForSource]


class DtoNotifierState(BaseModel, BaseConfig):
    actor: str
    state: str
    message: str | MISSING = Field(MISSING)


class DtoNotificationsList(BaseModel, BaseConfig):
    list: list[MoiraScheduledNotification]
    total: int


class DtoNotificationDeleteResponse(BaseModel, BaseConfig):
    result: int


class DtoMessageResponse(BaseModel, BaseConfig):
    message: str


class DtoEventsList(BaseModel, BaseConfig):
    list: list[MoiraNotificationEvent]
    page: int
    size: int
    total: int


class DtoContactNoisiness(BaseModel, BaseConfig):
    events_count: int = Field(..., description="EventsCount for the contact.")
    id: str
    type: str
    value: str
    extra_message: str | MISSING = Field(MISSING)
    name: str | MISSING = Field(MISSING)
    team_id: str | MISSING = Field(MISSING)
    user: str | MISSING = Field(MISSING)


class DtoContactNoisinessList(BaseModel, BaseConfig):
    list: list[DtoContactNoisiness] = Field(..., description="List of entities.")
    page: int = Field(..., description="Page number.")
    size: int = Field(..., description="Size is the amount of entities per Page.")
    total: int = Field(..., description="Total amount of entities in the database.")


class DtoContactList(BaseModel, BaseConfig):
    list: list[DtoTeamContact]


class DtoContactEventItem(BaseModel, BaseConfig):
    metric: str
    old_state: str
    state: str
    timestamp: int
    trigger_id: str


class DtoContactEventItemList(BaseModel, BaseConfig):
    list: list[DtoContactEventItem]
    page: int
    size: int
    total: int


class DtoContact(BaseModel, BaseConfig):
    id: str
    type: str
    value: str
    extra_message: str | MISSING = Field(MISSING)
    name: str | MISSING = Field(MISSING)
    team_id: str | MISSING = Field(MISSING)
    user: str | MISSING = Field(MISSING)


class ApiWebContact(BaseModel, BaseConfig):
    label: str
    type: str
    help: str | MISSING = Field(MISSING)
    logo_uri: str | MISSING = Field(MISSING)
    placeholder: str | MISSING = Field(MISSING)
    validation: str | MISSING = Field(MISSING)


class ApiSentry(BaseModel, BaseConfig):
    dsn: str | MISSING = Field(MISSING)
    platform: str | MISSING = Field(MISSING)


class ApiMetricSourceCluster(BaseModel, BaseConfig):
    cluster_id: str
    cluster_name: str
    metrics_ttl: int
    trigger_source: str


class ApiFeatureFlags(BaseModel, BaseConfig):
    celebration_mode: str = Field(..., alias="celebrationMode")
    is_plotting_available: bool = Field(..., alias="isPlottingAvailable")
    is_plotting_default_on: bool = Field(..., alias="isPlottingDefaultOn")
    is_readonly_enabled: bool = Field(..., alias="isReadonlyEnabled")
    is_subscription_to_all_tags_available: bool = Field(..., alias="isSubscriptionToAllTagsAvailable")


class ApiWebConfig(BaseModel, BaseConfig):
    contacts: list[ApiWebContact]
    feature_flags: ApiFeatureFlags = Field(..., alias="featureFlags")
    metric_source_clusters: list[ApiMetricSourceCluster]
    remote_allowed: bool = Field(..., alias="remoteAllowed")
    sentry: ApiSentry
    support_email: str | MISSING = Field(MISSING, alias="supportEmail")


class ApiErrorResponse(BaseModel, BaseConfig):
    status: str = Field(..., description="user-level status message")
    error: str | MISSING = Field(MISSING, description="application-level error message, for debugging")
