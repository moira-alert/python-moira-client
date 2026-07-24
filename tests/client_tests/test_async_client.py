from typing import Any
from urllib.parse import urlencode

import pytest
from httptoolkit.response import Response
from polyfactory.factories.pydantic_factory import ModelFactory
from pydantic import RootModel
from pydantic_core import to_jsonable_python
from pytest_httpx import HTTPXMock

from moira.clients import MoiraClientAsync
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


class CustomError(MoiraApiError):
    def __init__(self, response: Response):
        reason = response.reason + " My own error"
        super(MoiraApiError, self).__init__(reason)


@pytest.fixture
def async_client() -> MoiraClientAsync:
    return MoiraClientAsync(base_url="https://moira-api.example.com")


@pytest.fixture
def async_client_with_custom_error() -> MoiraClientAsync:
    return MoiraClientAsync(base_url="https://moira-api.example.com", error_class=CustomError)


@pytest.mark.asyncio
async def test_async_get_web_config(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = ApiWebConfig
    api_web_config_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = api_web_config_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/config")
    result = await async_client.get_web_config()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_contacts(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoContactList
    dto_contact_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_contact_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/contact")
    result = await async_client.get_all_contacts()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_contact_by_id(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetContactByIdPathParams
    get_contact_by_id_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_contact_by_id_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoContact
    dto_contact_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_contact_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/contact/{contactID}".format(**path_params_json),
    )
    result = await async_client.get_contact_by_id(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_contact_events_by_id(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetContactEventsByIdPathParams
    get_contact_events_by_id_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = get_contact_events_by_id_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    query_params_model = GetContactEventsByIdQueryParams
    get_contact_events_by_id_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = get_contact_events_by_id_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoContactEventItemList
    dto_contact_event_item_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_contact_event_item_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/contact/{contactID}/events?{query_params}".format(
            **path_params_json, query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_contact_events_by_id(
        path_params=path_params_obj,
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_contacts_noisiness(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = GetContactsNoisinessQueryParams
    get_contacts_noisiness_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = get_contacts_noisiness_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoContactNoisinessList
    dto_contact_noisiness_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_contact_noisiness_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/contact/noisiness?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_contacts_noisiness(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_events_list(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetEventsListPathParams
    get_events_list_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_events_list_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    query_params_model = GetEventsListQueryParams
    get_events_list_query_params_factory = ModelFactory.create_factory(model=query_params_model, __use_defaults__=True)
    query_params_obj = get_events_list_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoEventsList
    dto_events_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_events_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/event/{triggerID}?{query_params}".format(
            **path_params_json, query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_events_list(
        path_params=path_params_obj,
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_notifier_state_for_sources(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoNotifierStatesForSources
    dto_notifier_states_for_sources_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_notifier_states_for_sources_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/health/notifier")
    result = await async_client.get_notifier_state_for_sources()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_system_subscription(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoSubscriptionList
    dto_subscription_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_subscription_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get", json=result_json, url="https://moira-api.example.com/health/system-subscriptions"
    )
    result = await async_client.get_system_subscription()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_notifications(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = GetNotificationsQueryParams
    get_notifications_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = get_notifications_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoNotificationsList
    dto_notifications_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_notifications_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/notification?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_notifications(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_patterns(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoPatternList
    dto_pattern_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_pattern_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/pattern")
    result = await async_client.get_all_patterns()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_user_subscriptions(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoSubscriptionList
    dto_subscription_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_subscription_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/subscription")
    result = await async_client.get_user_subscriptions()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_subscription(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetSubscriptionPathParams
    get_subscription_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_subscription_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoSubscription
    dto_subscription_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_subscription_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/subscription/{subscriptionID}".format(**path_params_json),
    )
    result = await async_client.get_subscription(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_system_tags(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoTagsData
    dto_tags_data_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_tags_data_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/system-tag")
    result = await async_client.get_all_system_tags()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_tags(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoTagsData
    dto_tags_data_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_tags_data_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/tag")
    result = await async_client.get_all_tags()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_tags_and_subscriptions(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoTagsStatistics
    dto_tags_statistics_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_tags_statistics_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/tag/stats")
    result = await async_client.get_all_tags_and_subscriptions()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_teams_for_user(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoUserTeams
    dto_user_teams_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_user_teams_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/teams")
    result = await async_client.get_all_teams_for_user()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_team(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTeamPathParams
    get_team_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_team_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTeamModel
    dto_team_model_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_team_model_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/teams/{teamID}".format(**path_params_json),
    )
    result = await async_client.get_team(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_team_settings(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTeamSettingsPathParams
    get_team_settings_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_team_settings_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTeamSettings
    dto_team_settings_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_team_settings_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/teams/{teamID}/settings".format(**path_params_json),
    )
    result = await async_client.get_team_settings(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_team_users(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTeamUsersPathParams
    get_team_users_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_team_users_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTeamMembers
    dto_team_members_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_team_members_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/teams/{teamID}/users".format(**path_params_json),
    )
    result = await async_client.get_team_users(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_teams(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = GetAllTeamsQueryParams
    get_all_teams_query_params_factory = ModelFactory.create_factory(model=query_params_model, __use_defaults__=True)
    query_params_obj = get_all_teams_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoTeamsList
    dto_teams_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_teams_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/teams/all?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_all_teams(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_triggers(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoTriggersList
    dto_triggers_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_triggers_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/trigger")
    result = await async_client.get_all_triggers()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_trigger(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTriggerPathParams
    get_trigger_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_trigger_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    query_params_model = GetTriggerQueryParams
    get_trigger_query_params_factory = ModelFactory.create_factory(model=query_params_model, __use_defaults__=True)
    query_params_obj = get_trigger_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoTrigger
    dto_trigger_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_trigger_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/{triggerID}?{query_params}".format(
            **path_params_json, query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_trigger(
        path_params=path_params_obj,
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_trigger_dump(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTriggerDumpPathParams
    get_trigger_dump_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_trigger_dump_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTriggerDump
    dto_trigger_dump_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_trigger_dump_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/{triggerID}/dump".format(**path_params_json),
    )
    result = await async_client.get_trigger_dump(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_trigger_metrics(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTriggerMetricsPathParams
    get_trigger_metrics_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = get_trigger_metrics_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    query_params_model = GetTriggerMetricsQueryParams
    get_trigger_metrics_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = get_trigger_metrics_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/{triggerID}/metrics?{query_params}".format(
            **path_params_json, query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_trigger_metrics(
        path_params=path_params_obj,
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_render_trigger_metrics(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = RenderTriggerMetricsPathParams
    render_trigger_metrics_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = render_trigger_metrics_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    query_params_model = RenderTriggerMetricsQueryParams
    render_trigger_metrics_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = render_trigger_metrics_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)

    class RespBytes(RootModel[bytes]): ...

    resp_bytes_factory = ModelFactory.create_factory(model=RespBytes, __use_defaults__=True)
    result_obj = resp_bytes_factory.build().root
    httpx_mock.add_response(
        method="get",
        content=result_obj,
        url="https://moira-api.example.com/trigger/{triggerID}/render?{query_params}".format(
            **path_params_json, query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.render_trigger_metrics(
        path_params=path_params_obj,
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_trigger_state(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTriggerStatePathParams
    get_trigger_state_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = get_trigger_state_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTriggerCheck
    dto_trigger_check_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_trigger_check_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/{triggerID}/state".format(**path_params_json),
    )
    result = await async_client.get_trigger_state(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_trigger_throttling(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = GetTriggerThrottlingPathParams
    get_trigger_throttling_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = get_trigger_throttling_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoThrottlingResponse
    dto_throttling_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_throttling_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/{triggerID}/throttling".format(**path_params_json),
    )
    result = await async_client.get_trigger_throttling(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_all_heavy_triggers(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = GetAllHeavyTriggersQueryParams
    get_all_heavy_triggers_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = get_all_heavy_triggers_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoTriggersList
    dto_triggers_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_triggers_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/heavy?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_all_heavy_triggers(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_triggers_noisiness(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = GetTriggersNoisinessQueryParams
    get_triggers_noisiness_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = get_triggers_noisiness_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoTriggerNoisinessList
    dto_trigger_noisiness_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_trigger_noisiness_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/noisiness?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.get_triggers_noisiness(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_search_triggers(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = SearchTriggersQueryParams
    search_triggers_query_params_factory = ModelFactory.create_factory(model=query_params_model, __use_defaults__=True)
    query_params_obj = search_triggers_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoTriggersList
    dto_triggers_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_triggers_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get",
        json=result_json,
        url="https://moira-api.example.com/trigger/search?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.search_triggers(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_unused_triggers(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoTriggersList
    dto_triggers_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_triggers_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/trigger/unused")
    result = await async_client.get_unused_triggers()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_user_name(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoUser
    dto_user_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_user_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/user")
    result = await async_client.get_user_name()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_user_settings(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoUserSettings
    dto_user_settings_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_user_settings_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="get", json=result_json, url="https://moira-api.example.com/user/settings")
    result = await async_client.get_user_settings()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_send_test_contact_notification(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_obj: dict[Any, Any] = {}
    body_json = to_jsonable_python(body_obj)
    path_params_model = SendTestContactNotificationPathParams
    send_test_contact_notification_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = send_test_contact_notification_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="post",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/contact/{contactID}/test".format(**path_params_json),
    )
    result = await async_client.send_test_contact_notification(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_create_tags(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTagsData
    dto_tags_data_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_tags_data_factory.build()
    body_json = to_jsonable_python(body_obj)

    class RespStr(RootModel[str]): ...

    resp_str_factory = ModelFactory.create_factory(model=RespStr, __use_defaults__=True)
    result_obj = resp_str_factory.build().root
    httpx_mock.add_response(
        method="post", text=str(result_obj), match_json=body_json, url="https://moira-api.example.com/tag"
    )
    result = await async_client.create_tags(
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_create_team(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTeamModel
    dto_team_model_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_team_model_factory.build()
    body_json = to_jsonable_python(body_obj)
    response_model = DtoSaveTeamResponse
    dto_save_team_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_save_team_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="post", json=result_json, match_json=body_json, url="https://moira-api.example.com/teams"
    )
    result = await async_client.create_team(
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_create_new_team_contact(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoContact
    dto_contact_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_contact_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = CreateNewTeamContactPathParams
    create_new_team_contact_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = create_new_team_contact_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoContact
    dto_contact_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_contact_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="post",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/teams/{teamID}/contacts".format(**path_params_json),
    )
    result = await async_client.create_new_team_contact(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_create_new_team_subscription(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoSubscription
    dto_subscription_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_subscription_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = CreateNewTeamSubscriptionPathParams
    create_new_team_subscription_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = create_new_team_subscription_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoSubscription
    dto_subscription_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_subscription_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="post",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/teams/{teamID}/subscriptions".format(**path_params_json),
    )
    result = await async_client.create_new_team_subscription(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_add_team_users(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTeamMembers
    dto_team_members_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_team_members_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = AddTeamUsersPathParams
    add_team_users_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = add_team_users_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTeamMembers
    dto_team_members_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_team_members_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="post",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/teams/{teamID}/users".format(**path_params_json),
    )
    result = await async_client.add_team_users(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_update_team(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTeamModel
    dto_team_model_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_team_model_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = UpdateTeamPathParams
    update_team_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = update_team_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoSaveTeamResponse
    dto_save_team_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_save_team_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="patch",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/teams/{teamID}".format(**path_params_json),
    )
    result = await async_client.update_team(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_create_new_contact(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoContact
    dto_contact_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_contact_factory.build()
    body_json = to_jsonable_python(body_obj)
    response_model = DtoContact
    dto_contact_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_contact_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put", json=result_json, match_json=body_json, url="https://moira-api.example.com/contact"
    )
    result = await async_client.create_new_contact(
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_update_contact(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoContact
    dto_contact_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_contact_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = UpdateContactPathParams
    update_contact_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = update_contact_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoContact
    dto_contact_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_contact_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/contact/{contactID}".format(**path_params_json),
    )
    result = await async_client.update_contact(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_set_notifier_state(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoNotifierState
    dto_notifier_state_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_notifier_state_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="put", json=result_json, url="https://moira-api.example.com/health/notifier")
    result = await async_client.set_notifier_state()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_create_subscription(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoSubscription
    dto_subscription_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_subscription_factory.build()
    body_json = to_jsonable_python(body_obj)
    response_model = DtoSubscription
    dto_subscription_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_subscription_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put", json=result_json, match_json=body_json, url="https://moira-api.example.com/subscription"
    )
    result = await async_client.create_subscription(
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_update_subscription(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoSubscription
    dto_subscription_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_subscription_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = UpdateSubscriptionPathParams
    update_subscription_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = update_subscription_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoSubscription
    dto_subscription_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_subscription_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/subscription/{subscriptionID}".format(**path_params_json),
    )
    result = await async_client.update_subscription(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_send_test_notification(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = SendTestNotificationPathParams
    send_test_notification_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = send_test_notification_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put",
        json=result_json,
        url="https://moira-api.example.com/subscription/{subscriptionID}/test".format(**path_params_json),
    )
    result = await async_client.send_test_notification(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_set_team_users(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTeamMembers
    dto_team_members_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_team_members_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = SetTeamUsersPathParams
    set_team_users_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = set_team_users_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTeamMembers
    dto_team_members_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_team_members_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/teams/{teamID}/users".format(**path_params_json),
    )
    result = await async_client.set_team_users(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_create_trigger(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTrigger
    dto_trigger_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_trigger_factory.build()
    body_json = to_jsonable_python(body_obj)
    query_params_model = CreateTriggerQueryParams
    create_trigger_query_params_factory = ModelFactory.create_factory(model=query_params_model, __use_defaults__=True)
    query_params_obj = create_trigger_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoSaveTriggerResponse
    dto_save_trigger_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_save_trigger_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/trigger?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.create_trigger(
        query_params=query_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_update_trigger(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTrigger
    dto_trigger_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_trigger_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = UpdateTriggerPathParams
    update_trigger_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = update_trigger_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    query_params_model = UpdateTriggerQueryParams
    update_trigger_query_params_factory = ModelFactory.create_factory(model=query_params_model, __use_defaults__=True)
    query_params_obj = update_trigger_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoSaveTriggerResponse
    dto_save_trigger_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_save_trigger_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/trigger/{triggerID}?{query_params}".format(
            **path_params_json, query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.update_trigger(
        path_params=path_params_obj,
        query_params=query_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_set_trigger_maintenance(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTriggerMaintenance
    dto_trigger_maintenance_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_trigger_maintenance_factory.build()
    body_json = to_jsonable_python(body_obj)
    path_params_model = SetTriggerMaintenancePathParams
    set_trigger_maintenance_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = set_trigger_maintenance_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/trigger/{triggerID}/setMaintenance".format(**path_params_json),
    )
    result = await async_client.set_trigger_maintenance(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_trigger_check(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_model = DtoTrigger
    dto_trigger_factory = ModelFactory.create_factory(model=body_model, __use_defaults__=True)
    body_obj = dto_trigger_factory.build()
    body_json = to_jsonable_python(body_obj)
    response_model = DtoTriggerCheckResponse
    dto_trigger_check_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_trigger_check_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="put", json=result_json, match_json=body_json, url="https://moira-api.example.com/trigger/check"
    )
    result = await async_client.trigger_check(
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_remove_contact(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    body_obj: dict[Any, Any] = {}
    body_json = to_jsonable_python(body_obj)
    path_params_model = RemoveContactPathParams
    remove_contact_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = remove_contact_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        match_json=body_json,
        url="https://moira-api.example.com/contact/{contactID}".format(**path_params_json),
    )
    result = await async_client.remove_contact(
        path_params=path_params_obj,
        body=body_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_all_events(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="delete", json=result_json, url="https://moira-api.example.com/event/all")
    result = await async_client.delete_all_events()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_notification(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = DeleteNotificationQueryParams
    delete_notification_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = delete_notification_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoNotificationDeleteResponse
    dto_notification_delete_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_notification_delete_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/notification?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.delete_notification(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_all_notifications(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    response_model = DtoNotificationsList
    dto_notifications_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_notifications_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(method="delete", json=result_json, url="https://moira-api.example.com/notification/all")
    result = await async_client.delete_all_notifications()
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_notifications_filtered(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = DeleteNotificationsFilteredQueryParams
    delete_notifications_filtered_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = delete_notifications_filtered_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoNotificationsList
    dto_notifications_list_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_notifications_list_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/notification/filtered?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.delete_notifications_filtered(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_pattern(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = DeletePatternPathParams
    delete_pattern_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = delete_pattern_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/pattern/{pattern}".format(**path_params_json),
    )
    result = await async_client.delete_pattern(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_remove_subscription(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = RemoveSubscriptionPathParams
    remove_subscription_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = remove_subscription_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/subscription/{subscriptionID}".format(**path_params_json),
    )
    result = await async_client.remove_subscription(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_remove_tag(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = RemoveTagPathParams
    remove_tag_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = remove_tag_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoMessageResponse
    dto_message_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_message_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/tag/{tag}".format(**path_params_json),
    )
    result = await async_client.remove_tag(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_team(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = DeleteTeamPathParams
    delete_team_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = delete_team_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoSaveTeamResponse
    dto_save_team_response_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_save_team_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/teams/{teamID}".format(**path_params_json),
    )
    result = await async_client.delete_team(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_team_user(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = DeleteTeamUserPathParams
    delete_team_user_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = delete_team_user_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    response_model = DtoTeamMembers
    dto_team_members_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = dto_team_members_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/teams/{teamID}/users/{teamUserID}".format(**path_params_json),
    )
    result = await async_client.delete_team_user(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_remove_trigger(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = RemoveTriggerPathParams
    remove_trigger_path_params_factory = ModelFactory.create_factory(model=path_params_model, __use_defaults__=True)
    path_params_obj = remove_trigger_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj = None
    httpx_mock.add_response(
        method="delete",
        content=b"",
        url="https://moira-api.example.com/trigger/{triggerID}".format(**path_params_json),
    )
    result = await async_client.remove_trigger(
        path_params=path_params_obj,
    )  # type: ignore[func-returns-value]
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_trigger_metric(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = DeleteTriggerMetricPathParams
    delete_trigger_metric_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = delete_trigger_metric_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    query_params_model = DeleteTriggerMetricQueryParams
    delete_trigger_metric_query_params_factory = ModelFactory.create_factory(
        model=query_params_model, __use_defaults__=True
    )
    query_params_obj = delete_trigger_metric_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/trigger/{triggerID}/metrics?{query_params}".format(
            **path_params_json, query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.delete_trigger_metric(
        path_params=path_params_obj,
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_trigger_nodata_metrics(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = DeleteTriggerNodataMetricsPathParams
    delete_trigger_nodata_metrics_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = delete_trigger_nodata_metrics_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj: dict[Any, Any] = {}
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/trigger/{triggerID}/metrics/nodata".format(**path_params_json),
    )
    result = await async_client.delete_trigger_nodata_metrics(
        path_params=path_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_trigger_throttling(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    path_params_model = DeleteTriggerThrottlingPathParams
    delete_trigger_throttling_path_params_factory = ModelFactory.create_factory(
        model=path_params_model, __use_defaults__=True
    )
    path_params_obj = delete_trigger_throttling_path_params_factory.build()
    path_params_json = to_jsonable_python(path_params_obj)
    result_obj = None
    httpx_mock.add_response(
        method="delete",
        content=b"",
        url="https://moira-api.example.com/trigger/{triggerID}/throttling".format(**path_params_json),
    )
    result = await async_client.delete_trigger_throttling(
        path_params=path_params_obj,
    )  # type: ignore[func-returns-value]
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_delete_pager(async_client: MoiraClientAsync, httpx_mock: HTTPXMock) -> None:
    query_params_model = DeletePagerQueryParams
    delete_pager_query_params_factory = ModelFactory.create_factory(model=query_params_model, __use_defaults__=True)
    query_params_obj = delete_pager_query_params_factory.build()
    query_params_json = to_jsonable_python(query_params_obj)
    response_model = DtoTriggersSearchResultDeleteResponse
    dto_triggers_search_result_delete_response_factory = ModelFactory.create_factory(
        model=response_model, __use_defaults__=True
    )
    result_obj = dto_triggers_search_result_delete_response_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="delete",
        json=result_json,
        url="https://moira-api.example.com/trigger/search/pager?{query_params}".format(
            query_params=urlencode(query_params_json, doseq=False)
        ),
    )
    result = await async_client.delete_pager(
        query_params=query_params_obj,
    )
    assert result == result_obj


@pytest.mark.asyncio
async def test_async_get_web_config_custom_error(
    async_client_with_custom_error: MoiraClientAsync, httpx_mock: HTTPXMock
) -> None:
    response_model = ApiWebConfig
    api_web_config_factory = ModelFactory.create_factory(model=response_model, __use_defaults__=True)
    result_obj = api_web_config_factory.build()
    result_json = to_jsonable_python(result_obj)
    httpx_mock.add_response(
        method="get", json=result_json, status_code=404, url="https://moira-api.example.com/config"
    )
    with pytest.raises(CustomError) as error:
        await async_client_with_custom_error.get_web_config()
    assert "My own error" in str(error.value)
