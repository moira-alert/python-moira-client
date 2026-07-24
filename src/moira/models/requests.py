from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from pydantic.experimental.missing_sentinel import MISSING

__all__ = [
    "GetContactByIdPathParams",
    "GetContactEventsByIdPathParams",
    "GetContactEventsByIdQueryParams",
    "GetContactsNoisinessQueryParams",
    "GetEventsListPathParams",
    "GetEventsListQueryParams",
    "GetNotificationsQueryParams",
    "GetSubscriptionPathParams",
    "GetTeamPathParams",
    "GetTeamSettingsPathParams",
    "GetTeamUsersPathParams",
    "GetAllTeamsQueryParams",
    "GetTriggerPathParams",
    "GetTriggerQueryParams",
    "GetTriggerDumpPathParams",
    "GetTriggerMetricsPathParams",
    "GetTriggerMetricsQueryParams",
    "RenderTriggerMetricsPathParams",
    "RenderTriggerMetricsQueryParams",
    "GetTriggerStatePathParams",
    "GetTriggerThrottlingPathParams",
    "GetAllHeavyTriggersQueryParams",
    "GetTriggersNoisinessQueryParams",
    "SearchTriggersQueryParams",
    "SendTestContactNotificationPathParams",
    "CreateNewTeamContactPathParams",
    "CreateNewTeamSubscriptionPathParams",
    "AddTeamUsersPathParams",
    "UpdateContactPathParams",
    "UpdateSubscriptionPathParams",
    "SendTestNotificationPathParams",
    "SetTeamUsersPathParams",
    "CreateTriggerQueryParams",
    "UpdateTriggerPathParams",
    "UpdateTriggerQueryParams",
    "SetTriggerMaintenancePathParams",
    "UpdateTeamPathParams",
    "RemoveContactPathParams",
    "DeleteNotificationQueryParams",
    "DeleteNotificationsFilteredQueryParams",
    "DeletePatternPathParams",
    "RemoveSubscriptionPathParams",
    "RemoveTagPathParams",
    "DeleteTeamPathParams",
    "DeleteTeamUserPathParams",
    "RemoveTriggerPathParams",
    "DeleteTriggerMetricPathParams",
    "DeleteTriggerMetricQueryParams",
    "DeleteTriggerNodataMetricsPathParams",
    "DeleteTriggerThrottlingPathParams",
    "DeletePagerQueryParams",
]


class BaseConfig:
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
    )


class GetContactByIdPathParams(BaseModel, BaseConfig):
    contact_id: str = Field(alias="contactID")


class GetContactEventsByIdPathParams(BaseModel, BaseConfig):
    contact_id: str = Field(alias="contactID")


class GetContactEventsByIdQueryParams(BaseModel, BaseConfig):
    from_: str | MISSING = Field(MISSING, alias="from")
    to: str | MISSING = Field(MISSING, alias="to")
    size: int | MISSING = Field(MISSING, alias="size")
    p: int | MISSING = Field(MISSING, alias="p")


class GetContactsNoisinessQueryParams(BaseModel, BaseConfig):
    size: int | MISSING = Field(MISSING, alias="size")
    p: int | MISSING = Field(MISSING, alias="p")
    from_: str | MISSING = Field(MISSING, alias="from")
    to: str | MISSING = Field(MISSING, alias="to")
    sort: str | MISSING = Field(MISSING, alias="sort")


class GetEventsListPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class GetEventsListQueryParams(BaseModel, BaseConfig):
    size: int | MISSING = Field(MISSING, alias="size")
    p: int | MISSING = Field(MISSING, alias="p")
    from_: str | MISSING = Field(MISSING, alias="from")
    to: str | MISSING = Field(MISSING, alias="to")
    metric: str | MISSING = Field(MISSING, alias="metric")
    states: list[str] | MISSING = Field(MISSING, alias="states")


class GetNotificationsQueryParams(BaseModel, BaseConfig):
    start: int | MISSING = Field(MISSING, alias="start")
    end: int | MISSING = Field(MISSING, alias="end")


class GetSubscriptionPathParams(BaseModel, BaseConfig):
    subscription_id: str = Field(alias="subscriptionID")


class GetTeamPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class GetTeamSettingsPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class GetTeamUsersPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class GetAllTeamsQueryParams(BaseModel, BaseConfig):
    size: int | MISSING = Field(MISSING, alias="size")
    p: int | MISSING = Field(MISSING, alias="p")
    search_text: str | MISSING = Field(MISSING, alias="searchText")
    sort: str | MISSING = Field(MISSING, alias="sort")


class GetTriggerPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class GetTriggerQueryParams(BaseModel, BaseConfig):
    populated: bool | MISSING = Field(MISSING, alias="populated")


class GetTriggerDumpPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class GetTriggerMetricsPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class GetTriggerMetricsQueryParams(BaseModel, BaseConfig):
    from_: str | MISSING = Field(MISSING, alias="from")
    to: str | MISSING = Field(MISSING, alias="to")


class RenderTriggerMetricsPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class RenderTriggerMetricsQueryParams(BaseModel, BaseConfig):
    target: str | MISSING = Field(MISSING, alias="target")
    from_: str | MISSING = Field(MISSING, alias="from")
    to: str | MISSING = Field(MISSING, alias="to")
    timezone: str | MISSING = Field(MISSING, alias="timezone")
    theme: str | MISSING = Field(MISSING, alias="theme")
    realtime: bool | MISSING = Field(MISSING, alias="realtime")


class GetTriggerStatePathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class GetTriggerThrottlingPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class GetAllHeavyTriggersQueryParams(BaseModel, BaseConfig):
    from_: int | MISSING = Field(MISSING, alias="from")


class GetTriggersNoisinessQueryParams(BaseModel, BaseConfig):
    size: int | MISSING = Field(MISSING, alias="size")
    p: int | MISSING = Field(MISSING, alias="p")
    from_: str | MISSING = Field(MISSING, alias="from")
    to: str | MISSING = Field(MISSING, alias="to")
    sort: str | MISSING = Field(MISSING, alias="sort")


class SearchTriggersQueryParams(BaseModel, BaseConfig):
    only_problems: bool | MISSING = Field(MISSING, alias="onlyProblems")
    text: str | MISSING = Field(MISSING, alias="text")
    p: int | MISSING = Field(MISSING, alias="p")
    size: int | MISSING = Field(MISSING, alias="size")
    tags: list[str] | MISSING = Field(MISSING, alias="tags")
    create_pager: bool | MISSING = Field(MISSING, alias="createPager")
    pager_id: str | MISSING = Field(MISSING, alias="pagerID")
    created_by: str | MISSING = Field(MISSING, alias="createdBy")
    team_id: str | MISSING = Field(MISSING, alias="teamID")


class SendTestContactNotificationPathParams(BaseModel, BaseConfig):
    contact_id: str = Field(alias="contactID")


class CreateNewTeamContactPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class CreateNewTeamSubscriptionPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class AddTeamUsersPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class UpdateContactPathParams(BaseModel, BaseConfig):
    contact_id: str = Field(alias="contactID")


class UpdateSubscriptionPathParams(BaseModel, BaseConfig):
    subscription_id: str = Field(alias="subscriptionID")


class SendTestNotificationPathParams(BaseModel, BaseConfig):
    subscription_id: str = Field(alias="subscriptionID")


class SetTeamUsersPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class CreateTriggerQueryParams(BaseModel, BaseConfig):
    validate: bool | MISSING = Field(MISSING, alias="validate")


class UpdateTriggerPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class UpdateTriggerQueryParams(BaseModel, BaseConfig):
    validate: bool | MISSING = Field(MISSING, alias="validate")


class SetTriggerMaintenancePathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class UpdateTeamPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class RemoveContactPathParams(BaseModel, BaseConfig):
    contact_id: str = Field(alias="contactID")


class DeleteNotificationQueryParams(BaseModel, BaseConfig):
    id: str = Field(alias="id")


class DeleteNotificationsFilteredQueryParams(BaseModel, BaseConfig):
    start: int = Field(alias="start")
    end: int = Field(alias="end")
    ignored_tags: list[str] | MISSING = Field(MISSING, alias="ignoredTags")
    cluster_keys: list[str] | MISSING = Field(MISSING, alias="clusterKeys")


class DeletePatternPathParams(BaseModel, BaseConfig):
    pattern: str = Field(alias="pattern")


class RemoveSubscriptionPathParams(BaseModel, BaseConfig):
    subscription_id: str = Field(alias="subscriptionID")


class RemoveTagPathParams(BaseModel, BaseConfig):
    tag: str = Field(alias="tag")


class DeleteTeamPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")


class DeleteTeamUserPathParams(BaseModel, BaseConfig):
    team_id: str = Field(alias="teamID")
    team_user_id: str = Field(alias="teamUserID")


class RemoveTriggerPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class DeleteTriggerMetricPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class DeleteTriggerMetricQueryParams(BaseModel, BaseConfig):
    name: str | MISSING = Field(MISSING, alias="name")


class DeleteTriggerNodataMetricsPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class DeleteTriggerThrottlingPathParams(BaseModel, BaseConfig):
    trigger_id: str = Field(alias="triggerID")


class DeletePagerQueryParams(BaseModel, BaseConfig):
    pager_id: str | MISSING = Field(MISSING, alias="pagerID")
