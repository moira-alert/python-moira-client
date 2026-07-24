from typing import Any, Type

from httptoolkit import AsyncService, Header
from httptoolkit.transport import AsyncHttpxTransport, BaseAsyncTransport
from pydantic import BaseModel

from moira._error_handler import ErrorHandler
from moira.exceptions import MoiraApiError
from moira.models.requests import (
    AddTeamUsersPathParams,
    CreateNewTeamContactPathParams,
    CreateNewTeamSubscriptionPathParams,
    CreateTriggerQueryParams,
    DeleteNotificationQueryParams,
    DeleteNotificationsFilteredQueryParams,
    DeletePagerQueryParams,
    DeletePatternPathParams,
    DeleteTeamPathParams,
    DeleteTeamUserPathParams,
    DeleteTriggerMetricPathParams,
    DeleteTriggerMetricQueryParams,
    DeleteTriggerNodataMetricsPathParams,
    DeleteTriggerThrottlingPathParams,
    GetAllHeavyTriggersQueryParams,
    GetAllTeamsQueryParams,
    GetContactByIdPathParams,
    GetContactEventsByIdPathParams,
    GetContactEventsByIdQueryParams,
    GetContactsNoisinessQueryParams,
    GetEventsListPathParams,
    GetEventsListQueryParams,
    GetNotificationsQueryParams,
    GetSubscriptionPathParams,
    GetTeamPathParams,
    GetTeamSettingsPathParams,
    GetTeamUsersPathParams,
    GetTriggerDumpPathParams,
    GetTriggerMetricsPathParams,
    GetTriggerMetricsQueryParams,
    GetTriggerPathParams,
    GetTriggerQueryParams,
    GetTriggersNoisinessQueryParams,
    GetTriggerStatePathParams,
    GetTriggerThrottlingPathParams,
    RemoveContactPathParams,
    RemoveSubscriptionPathParams,
    RemoveTagPathParams,
    RemoveTriggerPathParams,
    RenderTriggerMetricsPathParams,
    RenderTriggerMetricsQueryParams,
    SearchTriggersQueryParams,
    SendTestContactNotificationPathParams,
    SendTestNotificationPathParams,
    SetTeamUsersPathParams,
    SetTriggerMaintenancePathParams,
    UpdateContactPathParams,
    UpdateSubscriptionPathParams,
    UpdateTeamPathParams,
    UpdateTriggerPathParams,
    UpdateTriggerQueryParams,
)
from moira.models.responses import (
    ApiWebConfig,
    DtoContact,
    DtoContactEventItemList,
    DtoContactList,
    DtoContactNoisinessList,
    DtoEventsList,
    DtoMessageResponse,
    DtoNotificationDeleteResponse,
    DtoNotificationsList,
    DtoNotifierState,
    DtoNotifierStatesForSources,
    DtoPatternList,
    DtoSaveTeamResponse,
    DtoSaveTriggerResponse,
    DtoSubscription,
    DtoSubscriptionList,
    DtoTagsData,
    DtoTagsStatistics,
    DtoTeamMembers,
    DtoTeamModel,
    DtoTeamSettings,
    DtoTeamsList,
    DtoThrottlingResponse,
    DtoTrigger,
    DtoTriggerCheck,
    DtoTriggerCheckResponse,
    DtoTriggerDump,
    DtoTriggerMaintenance,
    DtoTriggerNoisinessList,
    DtoTriggersList,
    DtoTriggersSearchResultDeleteResponse,
    DtoUser,
    DtoUserSettings,
    DtoUserTeams,
)


class MoiraClientAsync(AsyncService):
    def __init__(
        self,
        headers: tuple[Header, ...] = (),
        error_class: Type[MoiraApiError] = MoiraApiError,
        transport: BaseAsyncTransport = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(transport=transport or AsyncHttpxTransport(*args, **kwargs), headers=headers)
        self._error_handler = ErrorHandler(error_class)

    @staticmethod
    def convert_headers(headers: BaseModel | None = None) -> tuple[Header, ...]:
        if headers is None:
            return ()

        return tuple(
            Header(name=name, value=value, is_sensitive=False) for name, value in headers.model_dump().items()
        )

    async def get_web_config(
        self,
    ) -> ApiWebConfig:
        path = "/config"
        with self._error_handler.handle():
            response = await self.get(path)
        return ApiWebConfig.model_validate(response.json())

    async def get_all_contacts(
        self,
    ) -> DtoContactList:
        path = "/contact"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoContactList.model_validate(response.json())

    async def get_contact_by_id(
        self,
        path_params: GetContactByIdPathParams,
    ) -> DtoContact:
        path = "/contact/{contactID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoContact.model_validate(response.json())

    async def get_contact_events_by_id(
        self,
        path_params: GetContactEventsByIdPathParams,
        query_params: GetContactEventsByIdQueryParams,
    ) -> DtoContactEventItemList:
        path = "/contact/{contactID}/events".format(**path_params.model_dump(by_alias=True, mode="json"))
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoContactEventItemList.model_validate(response.json())

    async def get_contacts_noisiness(
        self,
        query_params: GetContactsNoisinessQueryParams,
    ) -> DtoContactNoisinessList:
        path = "/contact/noisiness"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoContactNoisinessList.model_validate(response.json())

    async def get_events_list(
        self,
        path_params: GetEventsListPathParams,
        query_params: GetEventsListQueryParams,
    ) -> DtoEventsList:
        path = "/event/{triggerID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoEventsList.model_validate(response.json())

    async def get_notifier_state_for_sources(
        self,
    ) -> DtoNotifierStatesForSources:
        path = "/health/notifier"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoNotifierStatesForSources.model_validate(response.json())

    async def get_system_subscription(
        self,
    ) -> DtoSubscriptionList:
        path = "/health/system-subscriptions"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoSubscriptionList.model_validate(response.json())

    async def get_notifications(
        self,
        query_params: GetNotificationsQueryParams,
    ) -> DtoNotificationsList:
        path = "/notification"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoNotificationsList.model_validate(response.json())

    async def get_all_patterns(
        self,
    ) -> DtoPatternList:
        path = "/pattern"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoPatternList.model_validate(response.json())

    async def get_user_subscriptions(
        self,
    ) -> DtoSubscriptionList:
        path = "/subscription"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoSubscriptionList.model_validate(response.json())

    async def get_subscription(
        self,
        path_params: GetSubscriptionPathParams,
    ) -> DtoSubscription:
        path = "/subscription/{subscriptionID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoSubscription.model_validate(response.json())

    async def get_all_system_tags(
        self,
    ) -> DtoTagsData:
        path = "/system-tag"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTagsData.model_validate(response.json())

    async def get_all_tags(
        self,
    ) -> DtoTagsData:
        path = "/tag"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTagsData.model_validate(response.json())

    async def get_all_tags_and_subscriptions(
        self,
    ) -> DtoTagsStatistics:
        path = "/tag/stats"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTagsStatistics.model_validate(response.json())

    async def get_all_teams_for_user(
        self,
    ) -> DtoUserTeams:
        path = "/teams"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoUserTeams.model_validate(response.json())

    async def get_team(
        self,
        path_params: GetTeamPathParams,
    ) -> DtoTeamModel:
        path = "/teams/{teamID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTeamModel.model_validate(response.json())

    async def get_team_settings(
        self,
        path_params: GetTeamSettingsPathParams,
    ) -> DtoTeamSettings:
        path = "/teams/{teamID}/settings".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTeamSettings.model_validate(response.json())

    async def get_team_users(
        self,
        path_params: GetTeamUsersPathParams,
    ) -> DtoTeamMembers:
        path = "/teams/{teamID}/users".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTeamMembers.model_validate(response.json())

    async def get_all_teams(
        self,
        query_params: GetAllTeamsQueryParams,
    ) -> DtoTeamsList:
        path = "/teams/all"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoTeamsList.model_validate(response.json())

    async def get_all_triggers(
        self,
    ) -> DtoTriggersList:
        path = "/trigger"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTriggersList.model_validate(response.json())

    async def get_trigger(
        self,
        path_params: GetTriggerPathParams,
        query_params: GetTriggerQueryParams,
    ) -> DtoTrigger:
        path = "/trigger/{triggerID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoTrigger.model_validate(response.json())

    async def get_trigger_dump(
        self,
        path_params: GetTriggerDumpPathParams,
    ) -> DtoTriggerDump:
        path = "/trigger/{triggerID}/dump".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTriggerDump.model_validate(response.json())

    async def get_trigger_metrics(
        self,
        path_params: GetTriggerMetricsPathParams,
        query_params: GetTriggerMetricsQueryParams,
    ) -> dict[Any, Any]:
        path = "/trigger/{triggerID}/metrics".format(**path_params.model_dump(by_alias=True, mode="json"))
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return response.json()

    async def render_trigger_metrics(
        self,
        path_params: RenderTriggerMetricsPathParams,
        query_params: RenderTriggerMetricsQueryParams,
    ) -> bytes:
        path = "/trigger/{triggerID}/render".format(**path_params.model_dump(by_alias=True, mode="json"))
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return response.content

    async def get_trigger_state(
        self,
        path_params: GetTriggerStatePathParams,
    ) -> DtoTriggerCheck:
        path = "/trigger/{triggerID}/state".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTriggerCheck.model_validate(response.json())

    async def get_trigger_throttling(
        self,
        path_params: GetTriggerThrottlingPathParams,
    ) -> DtoThrottlingResponse:
        path = "/trigger/{triggerID}/throttling".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoThrottlingResponse.model_validate(response.json())

    async def get_all_heavy_triggers(
        self,
        query_params: GetAllHeavyTriggersQueryParams,
    ) -> DtoTriggersList:
        path = "/trigger/heavy"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoTriggersList.model_validate(response.json())

    async def get_triggers_noisiness(
        self,
        query_params: GetTriggersNoisinessQueryParams,
    ) -> DtoTriggerNoisinessList:
        path = "/trigger/noisiness"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoTriggerNoisinessList.model_validate(response.json())

    async def search_triggers(
        self,
        query_params: SearchTriggersQueryParams,
    ) -> DtoTriggersList:
        path = "/trigger/search"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.get(path, params=params)
        return DtoTriggersList.model_validate(response.json())

    async def get_unused_triggers(
        self,
    ) -> DtoTriggersList:
        path = "/trigger/unused"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoTriggersList.model_validate(response.json())

    async def get_user_name(
        self,
    ) -> DtoUser:
        path = "/user"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoUser.model_validate(response.json())

    async def get_user_settings(
        self,
    ) -> DtoUserSettings:
        path = "/user/settings"
        with self._error_handler.handle():
            response = await self.get(path)
        return DtoUserSettings.model_validate(response.json())

    async def send_test_contact_notification(
        self,
        path_params: SendTestContactNotificationPathParams,
        body: dict[Any, Any],
    ) -> dict[Any, Any]:
        path = "/contact/{contactID}/test".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body
        with self._error_handler.handle():
            response = await self.post(path, json=json)
        return response.json()

    async def create_tags(
        self,
        body: DtoTagsData,
    ) -> str:
        path = "/tag"
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.post(path, json=json)
        return response.text

    async def create_team(
        self,
        body: DtoTeamModel,
    ) -> DtoSaveTeamResponse:
        path = "/teams"
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.post(path, json=json)
        return DtoSaveTeamResponse.model_validate(response.json())

    async def create_new_team_contact(
        self,
        path_params: CreateNewTeamContactPathParams,
        body: DtoContact,
    ) -> DtoContact:
        path = "/teams/{teamID}/contacts".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.post(path, json=json)
        return DtoContact.model_validate(response.json())

    async def create_new_team_subscription(
        self,
        path_params: CreateNewTeamSubscriptionPathParams,
        body: DtoSubscription,
    ) -> DtoSubscription:
        path = "/teams/{teamID}/subscriptions".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.post(path, json=json)
        return DtoSubscription.model_validate(response.json())

    async def add_team_users(
        self,
        path_params: AddTeamUsersPathParams,
        body: DtoTeamMembers,
    ) -> DtoTeamMembers:
        path = "/teams/{teamID}/users".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.post(path, json=json)
        return DtoTeamMembers.model_validate(response.json())

    async def update_team(
        self,
        path_params: UpdateTeamPathParams,
        body: DtoTeamModel,
    ) -> DtoSaveTeamResponse:
        path = "/teams/{teamID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.patch(path, json=json)
        return DtoSaveTeamResponse.model_validate(response.json())

    async def create_new_contact(
        self,
        body: DtoContact,
    ) -> DtoContact:
        path = "/contact"
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json)
        return DtoContact.model_validate(response.json())

    async def update_contact(
        self,
        path_params: UpdateContactPathParams,
        body: DtoContact,
    ) -> DtoContact:
        path = "/contact/{contactID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json)
        return DtoContact.model_validate(response.json())

    async def set_notifier_state(
        self,
    ) -> DtoNotifierState:
        path = "/health/notifier"
        with self._error_handler.handle():
            response = await self.put(path)
        return DtoNotifierState.model_validate(response.json())

    async def create_subscription(
        self,
        body: DtoSubscription,
    ) -> DtoSubscription:
        path = "/subscription"
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json)
        return DtoSubscription.model_validate(response.json())

    async def update_subscription(
        self,
        path_params: UpdateSubscriptionPathParams,
        body: DtoSubscription,
    ) -> DtoSubscription:
        path = "/subscription/{subscriptionID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json)
        return DtoSubscription.model_validate(response.json())

    async def send_test_notification(
        self,
        path_params: SendTestNotificationPathParams,
    ) -> dict[Any, Any]:
        path = "/subscription/{subscriptionID}/test".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.put(path)
        return response.json()

    async def set_team_users(
        self,
        path_params: SetTeamUsersPathParams,
        body: DtoTeamMembers,
    ) -> DtoTeamMembers:
        path = "/teams/{teamID}/users".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json)
        return DtoTeamMembers.model_validate(response.json())

    async def create_trigger(
        self,
        query_params: CreateTriggerQueryParams,
        body: DtoTrigger,
    ) -> DtoSaveTriggerResponse:
        path = "/trigger"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json, params=params)
        return DtoSaveTriggerResponse.model_validate(response.json())

    async def update_trigger(
        self,
        path_params: UpdateTriggerPathParams,
        query_params: UpdateTriggerQueryParams,
        body: DtoTrigger,
    ) -> DtoSaveTriggerResponse:
        path = "/trigger/{triggerID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json, params=params)
        return DtoSaveTriggerResponse.model_validate(response.json())

    async def set_trigger_maintenance(
        self,
        path_params: SetTriggerMaintenancePathParams,
        body: DtoTriggerMaintenance,
    ) -> dict[Any, Any]:
        path = "/trigger/{triggerID}/setMaintenance".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json)
        return response.json()

    async def trigger_check(
        self,
        body: DtoTrigger,
    ) -> DtoTriggerCheckResponse:
        path = "/trigger/check"
        json = body.model_dump(by_alias=True, mode="json")
        with self._error_handler.handle():
            response = await self.put(path, json=json)
        return DtoTriggerCheckResponse.model_validate(response.json())

    async def remove_contact(
        self,
        path_params: RemoveContactPathParams,
        body: dict[Any, Any],
    ) -> dict[Any, Any]:
        path = "/contact/{contactID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        json = body
        with self._error_handler.handle():
            response = await self.delete(path, json=json)
        return response.json()

    async def delete_all_events(
        self,
    ) -> dict[Any, Any]:
        path = "/event/all"
        with self._error_handler.handle():
            response = await self.delete(path)
        return response.json()

    async def delete_notification(
        self,
        query_params: DeleteNotificationQueryParams,
    ) -> DtoNotificationDeleteResponse:
        path = "/notification"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.delete(path, params=params)
        return DtoNotificationDeleteResponse.model_validate(response.json())

    async def delete_all_notifications(
        self,
    ) -> DtoNotificationsList:
        path = "/notification/all"
        with self._error_handler.handle():
            response = await self.delete(path)
        return DtoNotificationsList.model_validate(response.json())

    async def delete_notifications_filtered(
        self,
        query_params: DeleteNotificationsFilteredQueryParams,
    ) -> DtoNotificationsList:
        path = "/notification/filtered"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.delete(path, params=params)
        return DtoNotificationsList.model_validate(response.json())

    async def delete_pattern(
        self,
        path_params: DeletePatternPathParams,
    ) -> dict[Any, Any]:
        path = "/pattern/{pattern}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.delete(path)
        return response.json()

    async def remove_subscription(
        self,
        path_params: RemoveSubscriptionPathParams,
    ) -> dict[Any, Any]:
        path = "/subscription/{subscriptionID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.delete(path)
        return response.json()

    async def remove_tag(
        self,
        path_params: RemoveTagPathParams,
    ) -> DtoMessageResponse:
        path = "/tag/{tag}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.delete(path)
        return DtoMessageResponse.model_validate(response.json())

    async def delete_team(
        self,
        path_params: DeleteTeamPathParams,
    ) -> DtoSaveTeamResponse:
        path = "/teams/{teamID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.delete(path)
        return DtoSaveTeamResponse.model_validate(response.json())

    async def delete_team_user(
        self,
        path_params: DeleteTeamUserPathParams,
    ) -> DtoTeamMembers:
        path = "/teams/{teamID}/users/{teamUserID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.delete(path)
        return DtoTeamMembers.model_validate(response.json())

    async def remove_trigger(
        self,
        path_params: RemoveTriggerPathParams,
    ) -> None:
        path = "/trigger/{triggerID}".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            await self.delete(path)
        return None

    async def delete_trigger_metric(
        self,
        path_params: DeleteTriggerMetricPathParams,
        query_params: DeleteTriggerMetricQueryParams,
    ) -> dict[Any, Any]:
        path = "/trigger/{triggerID}/metrics".format(**path_params.model_dump(by_alias=True, mode="json"))
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.delete(path, params=params)
        return response.json()

    async def delete_trigger_nodata_metrics(
        self,
        path_params: DeleteTriggerNodataMetricsPathParams,
    ) -> dict[Any, Any]:
        path = "/trigger/{triggerID}/metrics/nodata".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            response = await self.delete(path)
        return response.json()

    async def delete_trigger_throttling(
        self,
        path_params: DeleteTriggerThrottlingPathParams,
    ) -> None:
        path = "/trigger/{triggerID}/throttling".format(**path_params.model_dump(by_alias=True, mode="json"))
        with self._error_handler.handle():
            await self.delete(path)
        return None

    async def delete_pager(
        self,
        query_params: DeletePagerQueryParams,
    ) -> DtoTriggersSearchResultDeleteResponse:
        path = "/trigger/search/pager"
        params = query_params.model_dump(by_alias=True, mode="json", exclude_none=True)
        with self._error_handler.handle():
            response = await self.delete(path, params=params)
        return DtoTriggersSearchResultDeleteResponse.model_validate(response.json())
