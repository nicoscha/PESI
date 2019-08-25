# Python EVE Swagger Interface
# https://github.com/nicoscha/PESI
# ESI version 0.8.9
import ESI_request


def get_alliances(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all active player alliances
    ---
    Alternate route: `/latest/alliances/`
    Alternate route: `/legacy/alliances/`
    Alternate route: `/v1/alliances/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/alliances/')


def get_alliances_alliance_id(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about an alliance
    ---
    Alternate route: `/latest/alliances/{alliance_id}/`
    Alternate route: `/v3/alliances/{alliance_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/alliances/{alliance_id}/')


def get_alliances_alliance_id_contacts(*,
                                       alliance_id,
                                       token,
                                       if_none_match=None,
                                       page='1'):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return contacts of an alliance
    ---
    Alternate route: `/latest/alliances/{alliance_id}/contacts/`
    Alternate route: `/v2/alliances/{alliance_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/alliances/{alliance_id}/contacts/')


def get_alliances_alliance_id_contacts_labels(*,
                                              alliance_id,
                                              token,
                                              if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return custom labels for an alliance's contacts
    ---
    Alternate route: `/latest/alliances/{alliance_id}/contacts/labels/`
    Alternate route: `/legacy/alliances/{alliance_id}/contacts/labels/`
    Alternate route: `/v1/alliances/{alliance_id}/contacts/labels/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/alliances/{alliance_id}/contacts/labels/')


def get_alliances_alliance_id_corporations(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all current member corporations of an alliance
    ---
    Alternate route: `/latest/alliances/{alliance_id}/corporations/`
    Alternate route: `/legacy/alliances/{alliance_id}/corporations/`
    Alternate route: `/v1/alliances/{alliance_id}/corporations/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/alliances/{alliance_id}/corporations/')


def get_alliances_alliance_id_icons(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the icon urls for a alliance
    ---
    Alternate route: `/latest/alliances/{alliance_id}/icons/`
    Alternate route: `/legacy/alliances/{alliance_id}/icons/`
    Alternate route: `/v1/alliances/{alliance_id}/icons/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/alliances/{alliance_id}/icons/')


def post_characters_affiliation(*, characters):
    """
    :param characters: The character IDs to fetch affiliations for. All characters must exist, or none will be returned
    Bulk lookup of character IDs to corporation, alliance and faction
    ---
    Alternate route: `/latest/characters/affiliation/`
    Alternate route: `/legacy/characters/affiliation/`
    Alternate route: `/v1/characters/affiliation/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(characters=characters,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/affiliation/')


def get_characters_character_id(*, character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a character
    ---
    Alternate route: `/latest/characters/{character_id}/`
    Alternate route: `/v4/characters/{character_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/')


def get_characters_character_id_agents_research(*,
                                                character_id,
                                                token,
                                                if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)
    ---
    Alternate route: `/latest/characters/{character_id}/agents_research/`
    Alternate route: `/legacy/characters/{character_id}/agents_research/`
    Alternate route: `/v1/characters/{character_id}/agents_research/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/agents_research/')


def get_characters_character_id_assets(*,
                                       character_id,
                                       token,
                                       if_none_match=None,
                                       page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return a list of the characters assets
    ---
    Alternate route: `/latest/characters/{character_id}/assets/`
    Alternate route: `/v3/characters/{character_id}/assets/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/assets/')


def post_characters_character_id_assets_locations(*, character_id, item_ids,
                                                  token):
    """
    :param character_id: An EVE character ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    Alternate route: `/latest/characters/{character_id}/assets/locations/`
    Alternate route: `/v2/characters/{character_id}/assets/locations/`
    
    """
    ESI_request.request(character_id=character_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/{character_id}/assets/locations/')


def post_characters_character_id_assets_names(*, character_id, item_ids,
                                              token):
    """
    :param character_id: An EVE character ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.
    ---
    Alternate route: `/latest/characters/{character_id}/assets/names/`
    Alternate route: `/legacy/characters/{character_id}/assets/names/`
    Alternate route: `/v1/characters/{character_id}/assets/names/`
    
    """
    ESI_request.request(character_id=character_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/{character_id}/assets/names/')


def get_characters_character_id_attributes(*,
                                           character_id,
                                           token,
                                           if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return attributes of a character
    ---
    Alternate route: `/latest/characters/{character_id}/attributes/`
    Alternate route: `/legacy/characters/{character_id}/attributes/`
    Alternate route: `/v1/characters/{character_id}/attributes/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/attributes/')


def get_characters_character_id_blueprints(*,
                                           character_id,
                                           token,
                                           if_none_match=None,
                                           page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return a list of blueprints the character owns
    ---
    Alternate route: `/latest/characters/{character_id}/blueprints/`
    Alternate route: `/v2/characters/{character_id}/blueprints/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/blueprints/')


def get_characters_character_id_bookmarks(*,
                                          character_id,
                                          token,
                                          if_none_match=None,
                                          page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    A list of your character's personal bookmarks
    ---
    Alternate route: `/latest/characters/{character_id}/bookmarks/`
    Alternate route: `/v2/characters/{character_id}/bookmarks/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/bookmarks/')


def get_characters_character_id_bookmarks_folders(*,
                                                  character_id,
                                                  token,
                                                  if_none_match=None,
                                                  page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    A list of your character's personal bookmark folders
    ---
    Alternate route: `/latest/characters/{character_id}/bookmarks/folders/`
    Alternate route: `/v2/characters/{character_id}/bookmarks/folders/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/bookmarks/folders/')


def get_characters_character_id_calendar(*,
                                         character_id,
                                         from_event,
                                         token,
                                         if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param from_event: The event ID to retrieve events from
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event
    ---
    Alternate route: `/latest/characters/{character_id}/calendar/`
    Alternate route: `/legacy/characters/{character_id}/calendar/`
    Alternate route: `/v1/characters/{character_id}/calendar/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        from_event=from_event,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/calendar/')


def get_characters_character_id_calendar_event_id(*,
                                                  character_id,
                                                  event_id,
                                                  token,
                                                  if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param event_id: The id of the event requested
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get all the information for a specific event
    ---
    Alternate route: `/latest/characters/{character_id}/calendar/{event_id}/`
    Alternate route: `/v3/characters/{character_id}/calendar/{event_id}/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/characters/{character_id}/calendar/{event_id}/')


def put_characters_character_id_calendar_event_id(*, character_id, event_id,
                                                  response, token):
    """
    :param character_id: An EVE character ID
    :param event_id: The ID of the event requested
    :param response: The response value to set, overriding current value
    :param token: Access token to use if unable to set a header
    Set your response status to an event
    ---
    Alternate route: `/latest/characters/{character_id}/calendar/{event_id}/`
    Alternate route: `/v3/characters/{character_id}/calendar/{event_id}/`
    
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        response=response,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='PUT',
        path=f'/characters/{character_id}/calendar/{event_id}/')


def get_characters_character_id_calendar_event_id_attendees(
        *, character_id, event_id, token, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param event_id: The id of the event requested
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get all invited attendees for a given event
    ---
    Alternate route: `/latest/characters/{character_id}/calendar/{event_id}/attendees/`
    Alternate route: `/legacy/characters/{character_id}/calendar/{event_id}/attendees/`
    Alternate route: `/v1/characters/{character_id}/calendar/{event_id}/attendees/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/characters/{character_id}/calendar/{event_id}/attendees/')


def get_characters_character_id_clones(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    A list of the character's clones
    ---
    Alternate route: `/latest/characters/{character_id}/clones/`
    Alternate route: `/v3/characters/{character_id}/clones/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/clones/')


def delete_characters_character_id_contacts(*, character_id, contact_ids,
                                            token):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts to delete
    :param token: Access token to use if unable to set a header
    Bulk delete contacts
    ---
    Alternate route: `/latest/characters/{character_id}/contacts/`
    Alternate route: `/v2/characters/{character_id}/contacts/`
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='DELETE',
                        path=f'/characters/{character_id}/contacts/')


def get_characters_character_id_contacts(*,
                                         character_id,
                                         token,
                                         if_none_match=None,
                                         page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return contacts of a character
    ---
    Alternate route: `/latest/characters/{character_id}/contacts/`
    Alternate route: `/v2/characters/{character_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/contacts/')


def post_characters_character_id_contacts(*, character_id, contact_ids,
                                          label_ids, standing, token, watched):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts
    :param label_ids: Add custom labels to the new contact
    :param standing: Standing for the contact
    :param token: Access token to use if unable to set a header
    :param watched: Whether the contact should be watched, note this is only effective on characters
    Bulk add contacts with same settings
    ---
    Alternate route: `/latest/characters/{character_id}/contacts/`
    Alternate route: `/v2/characters/{character_id}/contacts/`
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_ids=label_ids,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/{character_id}/contacts/')


def put_characters_character_id_contacts(*, character_id, contact_ids,
                                         label_ids, standing, token, watched):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts
    :param label_ids: Add custom labels to the contact
    :param standing: Standing for the contact
    :param token: Access token to use if unable to set a header
    :param watched: Whether the contact should be watched, note this is only effective on characters
    Bulk edit contacts with same settings
    ---
    Alternate route: `/latest/characters/{character_id}/contacts/`
    Alternate route: `/v2/characters/{character_id}/contacts/`
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_ids=label_ids,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='PUT',
                        path=f'/characters/{character_id}/contacts/')


def get_characters_character_id_contacts_labels(*,
                                                character_id,
                                                token,
                                                if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return custom labels for a character's contacts
    ---
    Alternate route: `/latest/characters/{character_id}/contacts/labels/`
    Alternate route: `/legacy/characters/{character_id}/contacts/labels/`
    Alternate route: `/v1/characters/{character_id}/contacts/labels/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/contacts/labels/')


def get_characters_character_id_contracts(*,
                                          character_id,
                                          token,
                                          if_none_match=None,
                                          page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress".
    ---
    Alternate route: `/latest/characters/{character_id}/contracts/`
    Alternate route: `/legacy/characters/{character_id}/contracts/`
    Alternate route: `/v1/characters/{character_id}/contracts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/contracts/')


def get_characters_character_id_contracts_contract_id_bids(
        *, character_id, contract_id, token, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param contract_id: ID of a contract
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Lists bids on a particular auction contract
    ---
    Alternate route: `/latest/characters/{character_id}/contracts/{contract_id}/bids/`
    Alternate route: `/legacy/characters/{character_id}/contracts/{contract_id}/bids/`
    Alternate route: `/v1/characters/{character_id}/contracts/{contract_id}/bids/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(
        character_id=character_id,
        contract_id=contract_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/characters/{character_id}/contracts/{contract_id}/bids/')


def get_characters_character_id_contracts_contract_id_items(
        *, character_id, contract_id, token, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param contract_id: ID of a contract
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Lists items of a particular contract
    ---
    Alternate route: `/latest/characters/{character_id}/contracts/{contract_id}/items/`
    Alternate route: `/legacy/characters/{character_id}/contracts/{contract_id}/items/`
    Alternate route: `/v1/characters/{character_id}/contracts/{contract_id}/items/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        contract_id=contract_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/characters/{character_id}/contracts/{contract_id}/items/')


def get_characters_character_id_corporationhistory(*,
                                                   character_id,
                                                   if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of all the corporations a character has been a member of
    ---
    Alternate route: `/latest/characters/{character_id}/corporationhistory/`
    Alternate route: `/legacy/characters/{character_id}/corporationhistory/`
    Alternate route: `/v1/characters/{character_id}/corporationhistory/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/corporationhistory/')


def post_characters_character_id_cspa(*, character_id, characters, token):
    """
    :param character_id: An EVE character ID
    :param characters: The target characters to calculate the charge for
    :param token: Access token to use if unable to set a header
    Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost
    ---
    Alternate route: `/latest/characters/{character_id}/cspa/`
    Alternate route: `/v4/characters/{character_id}/cspa/`
    
    """
    ESI_request.request(character_id=character_id,
                        characters=characters,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/{character_id}/cspa/')


def get_characters_character_id_fatigue(*,
                                        character_id,
                                        token,
                                        if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a character's jump activation and fatigue information
    ---
    Alternate route: `/latest/characters/{character_id}/fatigue/`
    Alternate route: `/legacy/characters/{character_id}/fatigue/`
    Alternate route: `/v1/characters/{character_id}/fatigue/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/fatigue/')


def get_characters_character_id_fittings(*,
                                         character_id,
                                         token,
                                         if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return fittings of a character
    ---
    Alternate route: `/latest/characters/{character_id}/fittings/`
    Alternate route: `/v2/characters/{character_id}/fittings/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/fittings/')


def post_characters_character_id_fittings(*, character_id, fitting, token):
    """
    :param character_id: An EVE character ID
    :param fitting: Details about the new fitting
    :param token: Access token to use if unable to set a header
    Save a new fitting for a character
    ---
    Alternate route: `/latest/characters/{character_id}/fittings/`
    Alternate route: `/v2/characters/{character_id}/fittings/`
    
    """
    ESI_request.request(character_id=character_id,
                        fitting=fitting,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/{character_id}/fittings/')


def delete_characters_character_id_fittings_fitting_id(*, character_id,
                                                       fitting_id, token):
    """
    :param character_id: An EVE character ID
    :param fitting_id: ID for a fitting of this character
    :param token: Access token to use if unable to set a header
    Delete a fitting from a character
    ---
    Alternate route: `/latest/characters/{character_id}/fittings/{fitting_id}/`
    Alternate route: `/legacy/characters/{character_id}/fittings/{fitting_id}/`
    Alternate route: `/v1/characters/{character_id}/fittings/{fitting_id}/`
    
    """
    ESI_request.request(
        character_id=character_id,
        fitting_id=fitting_id,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='DELETE',
        path=f'/characters/{character_id}/fittings/{fitting_id}/')


def get_characters_character_id_fleet(*,
                                      character_id,
                                      token,
                                      if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return the fleet ID the character is in, if any.
    ---
    Alternate route: `/v2/characters/{character_id}/fleet/`
    ---
    This route is cached for up to 60 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/fleet/')


def get_characters_character_id_fw_stats(*,
                                         character_id,
                                         token,
                                         if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Statistical overview of a character involved in faction warfare
    ---
    Alternate route: `/latest/characters/{character_id}/fw/stats/`
    Alternate route: `/legacy/characters/{character_id}/fw/stats/`
    Alternate route: `/v1/characters/{character_id}/fw/stats/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/fw/stats/')


def get_characters_character_id_implants(*,
                                         character_id,
                                         token,
                                         if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return implants on the active clone of a character
    ---
    Alternate route: `/latest/characters/{character_id}/implants/`
    Alternate route: `/legacy/characters/{character_id}/implants/`
    Alternate route: `/v1/characters/{character_id}/implants/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/implants/')


def get_characters_character_id_industry_jobs(*,
                                              character_id,
                                              include_completed,
                                              token,
                                              if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param include_completed: Whether to retrieve completed character industry jobs. Only includes jobs from the past 90 days
    :param token: Access token to use if unable to set a header
    List industry jobs placed by a character
    ---
    Alternate route: `/latest/characters/{character_id}/industry/jobs/`
    Alternate route: `/legacy/characters/{character_id}/industry/jobs/`
    Alternate route: `/v1/characters/{character_id}/industry/jobs/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        include_completed=include_completed,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/industry/jobs/')


def get_characters_character_id_killmails_recent(*,
                                                 character_id,
                                                 token,
                                                 if_none_match=None,
                                                 page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return a list of a character's kills and losses going back 90 days
    ---
    Alternate route: `/latest/characters/{character_id}/killmails/recent/`
    Alternate route: `/legacy/characters/{character_id}/killmails/recent/`
    Alternate route: `/v1/characters/{character_id}/killmails/recent/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/killmails/recent/')


def get_characters_character_id_location(*,
                                         character_id,
                                         token,
                                         if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable
    ---
    Alternate route: `/v2/characters/{character_id}/location/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/location/')


def get_characters_character_id_loyalty_points(*,
                                               character_id,
                                               token,
                                               if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a list of loyalty points for all corporations the character has worked for
    ---
    Alternate route: `/latest/characters/{character_id}/loyalty/points/`
    Alternate route: `/legacy/characters/{character_id}/loyalty/points/`
    Alternate route: `/v1/characters/{character_id}/loyalty/points/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/loyalty/points/')


def get_characters_character_id_mail(*,
                                     character_id,
                                     labels,
                                     last_mail_id,
                                     token,
                                     if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param labels: Fetch only mails that match one or more of the given labels
    :param last_mail_id: List only mail with an ID lower than the given ID, if present
    :param token: Access token to use if unable to set a header
    Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards
    ---
    Alternate route: `/latest/characters/{character_id}/mail/`
    Alternate route: `/legacy/characters/{character_id}/mail/`
    Alternate route: `/v1/characters/{character_id}/mail/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        labels=labels,
                        last_mail_id=last_mail_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/mail/')


def post_characters_character_id_mail(*, character_id, mail, token):
    """
    :param character_id: An EVE character ID
    :param mail: The mail to send
    :param token: Access token to use if unable to set a header
    Create and send a new mail
    ---
    Alternate route: `/latest/characters/{character_id}/mail/`
    Alternate route: `/legacy/characters/{character_id}/mail/`
    Alternate route: `/v1/characters/{character_id}/mail/`
    
    """
    ESI_request.request(character_id=character_id,
                        mail=mail,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/{character_id}/mail/')


def get_characters_character_id_mail_labels(*,
                                            character_id,
                                            token,
                                            if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a list of the users mail labels, unread counts for each label and a total unread count.
    ---
    Alternate route: `/latest/characters/{character_id}/mail/labels/`
    Alternate route: `/v3/characters/{character_id}/mail/labels/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/mail/labels/')


def post_characters_character_id_mail_labels(*, character_id, label, token):
    """
    :param character_id: An EVE character ID
    :param label: Label to create
    :param token: Access token to use if unable to set a header
    Create a mail label
    ---
    Alternate route: `/latest/characters/{character_id}/mail/labels/`
    Alternate route: `/legacy/characters/{character_id}/mail/labels/`
    Alternate route: `/v2/characters/{character_id}/mail/labels/`
    
    """
    ESI_request.request(character_id=character_id,
                        label=label,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/characters/{character_id}/mail/labels/')


def delete_characters_character_id_mail_labels_label_id(
        *, character_id, label_id, token):
    """
    :param character_id: An EVE character ID
    :param label_id: An EVE label id
    :param token: Access token to use if unable to set a header
    Delete a mail label
    ---
    Alternate route: `/latest/characters/{character_id}/mail/labels/{label_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/labels/{label_id}/`
    Alternate route: `/v1/characters/{character_id}/mail/labels/{label_id}/`
    
    """
    ESI_request.request(
        character_id=character_id,
        label_id=label_id,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='DELETE',
        path=f'/characters/{character_id}/mail/labels/{label_id}/')


def get_characters_character_id_mail_lists(*,
                                           character_id,
                                           token,
                                           if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return all mailing lists that the character is subscribed to
    ---
    Alternate route: `/latest/characters/{character_id}/mail/lists/`
    Alternate route: `/legacy/characters/{character_id}/mail/lists/`
    Alternate route: `/v1/characters/{character_id}/mail/lists/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/mail/lists/')


def delete_characters_character_id_mail_mail_id(*, character_id, mail_id,
                                                token):
    """
    :param character_id: An EVE character ID
    :param mail_id: An EVE mail ID
    :param token: Access token to use if unable to set a header
    Delete a mail
    ---
    Alternate route: `/latest/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/v1/characters/{character_id}/mail/{mail_id}/`
    
    """
    ESI_request.request(character_id=character_id,
                        mail_id=mail_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='DELETE',
                        path=f'/characters/{character_id}/mail/{mail_id}/')


def get_characters_character_id_mail_mail_id(*,
                                             character_id,
                                             mail_id,
                                             token,
                                             if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param mail_id: An EVE mail ID
    :param token: Access token to use if unable to set a header
    Return the contents of an EVE mail
    ---
    Alternate route: `/latest/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/v1/characters/{character_id}/mail/{mail_id}/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        mail_id=mail_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/mail/{mail_id}/')


def put_characters_character_id_mail_mail_id(*, character_id, contents,
                                             mail_id, token):
    """
    :param character_id: An EVE character ID
    :param contents: Data used to update the mail
    :param mail_id: An EVE mail ID
    :param token: Access token to use if unable to set a header
    Update metadata about a mail
    ---
    Alternate route: `/latest/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/v1/characters/{character_id}/mail/{mail_id}/`
    
    """
    ESI_request.request(character_id=character_id,
                        contents=contents,
                        mail_id=mail_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='PUT',
                        path=f'/characters/{character_id}/mail/{mail_id}/')


def get_characters_character_id_medals(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a list of medals the character has
    ---
    Alternate route: `/latest/characters/{character_id}/medals/`
    Alternate route: `/legacy/characters/{character_id}/medals/`
    Alternate route: `/v1/characters/{character_id}/medals/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/medals/')


def get_characters_character_id_mining(*,
                                       character_id,
                                       token,
                                       if_none_match=None,
                                       page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Paginated record of all mining done by a character for the past 30 days
    
    ---
    Alternate route: `/latest/characters/{character_id}/mining/`
    Alternate route: `/legacy/characters/{character_id}/mining/`
    Alternate route: `/v1/characters/{character_id}/mining/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/mining/')


def get_characters_character_id_notifications(*,
                                              character_id,
                                              token,
                                              if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return character notifications
    ---
    Alternate route: `/latest/characters/{character_id}/notifications/`
    Alternate route: `/v5/characters/{character_id}/notifications/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/notifications/')


def get_characters_character_id_notifications_contacts(*,
                                                       character_id,
                                                       token,
                                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return notifications about having been added to someone's contact list
    ---
    Alternate route: `/latest/characters/{character_id}/notifications/contacts/`
    Alternate route: `/legacy/characters/{character_id}/notifications/contacts/`
    Alternate route: `/v1/characters/{character_id}/notifications/contacts/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/characters/{character_id}/notifications/contacts/')


def get_characters_character_id_online(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Checks if the character is currently online
    ---
    Alternate route: `/v3/characters/{character_id}/online/`
    ---
    This route is cached for up to 60 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/online/')


def get_characters_character_id_opportunities(*,
                                              character_id,
                                              token,
                                              if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a list of tasks finished by a character
    ---
    Alternate route: `/latest/characters/{character_id}/opportunities/`
    Alternate route: `/legacy/characters/{character_id}/opportunities/`
    Alternate route: `/v1/characters/{character_id}/opportunities/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/opportunities/')


def get_characters_character_id_orders(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    List open market orders placed by a character
    ---
    Alternate route: `/latest/characters/{character_id}/orders/`
    Alternate route: `/v2/characters/{character_id}/orders/`
    ---
    This route is cached for up to 1200 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/orders/')


def get_characters_character_id_orders_history(*,
                                               character_id,
                                               token,
                                               if_none_match=None,
                                               page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    List cancelled and expired market orders placed by a character up to 90 days in the past.
    ---
    Alternate route: `/latest/characters/{character_id}/orders/history/`
    Alternate route: `/legacy/characters/{character_id}/orders/history/`
    Alternate route: `/v1/characters/{character_id}/orders/history/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/orders/history/')


def get_characters_character_id_planets(*,
                                        character_id,
                                        token,
                                        if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns a list of all planetary colonies owned by a character.
    ---
    Alternate route: `/latest/characters/{character_id}/planets/`
    Alternate route: `/legacy/characters/{character_id}/planets/`
    Alternate route: `/v1/characters/{character_id}/planets/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/planets/')


def get_characters_character_id_planets_planet_id(*,
                                                  character_id,
                                                  planet_id,
                                                  token,
                                                  if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param planet_id: Planet id of the target planet
    :param token: Access token to use if unable to set a header
    Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met.
    ---
    Alternate route: `/latest/characters/{character_id}/planets/{planet_id}/`
    Alternate route: `/v3/characters/{character_id}/planets/{planet_id}/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        planet_id=planet_id,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/characters/{character_id}/planets/{planet_id}/')


def get_characters_character_id_portrait(*, character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get portrait urls for a character
    ---
    Alternate route: `/latest/characters/{character_id}/portrait/`
    Alternate route: `/v2/characters/{character_id}/portrait/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/portrait/')


def get_characters_character_id_roles(*,
                                      character_id,
                                      token,
                                      if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns a character's corporation roles
    ---
    Alternate route: `/latest/characters/{character_id}/roles/`
    Alternate route: `/v2/characters/{character_id}/roles/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/roles/')


def get_characters_character_id_search(*,
                                       categories,
                                       character_id,
                                       language,
                                       search,
                                       strict,
                                       token,
                                       accept_language='en-us',
                                       if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param categories: Type of entities to search for
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param search: The string to search on
    :param strict: Whether the search should be a strict match
    :param token: Access token to use if unable to set a header
    Search for entities that match a given sub-string.
    ---
    Alternate route: `/latest/characters/{character_id}/search/`
    Alternate route: `/legacy/characters/{character_id}/search/`
    Alternate route: `/v3/characters/{character_id}/search/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        categories=categories,
                        character_id=character_id,
                        if_none_match=if_none_match,
                        language=language,
                        search=search,
                        strict=strict,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/search/')


def get_characters_character_id_ship(*,
                                     character_id,
                                     token,
                                     if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get the current ship type, name and id
    ---
    Alternate route: `/v2/characters/{character_id}/ship/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/ship/')


def get_characters_character_id_skillqueue(*,
                                           character_id,
                                           token,
                                           if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    List the configured skill queue for the given character
    ---
    Alternate route: `/latest/characters/{character_id}/skillqueue/`
    Alternate route: `/legacy/characters/{character_id}/skillqueue/`
    Alternate route: `/v2/characters/{character_id}/skillqueue/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/skillqueue/')


def get_characters_character_id_skills(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    List all trained skills for the given character
    ---
    Alternate route: `/latest/characters/{character_id}/skills/`
    Alternate route: `/v4/characters/{character_id}/skills/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/skills/')


def get_characters_character_id_standings(*,
                                          character_id,
                                          token,
                                          if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return character standings from agents, NPC corporations, and factions
    ---
    Alternate route: `/latest/characters/{character_id}/standings/`
    Alternate route: `/legacy/characters/{character_id}/standings/`
    Alternate route: `/v1/characters/{character_id}/standings/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/standings/')


def get_characters_character_id_stats(*,
                                      character_id,
                                      token,
                                      if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns aggregate yearly stats for a character
    ---
    Alternate route: `/latest/characters/{character_id}/stats/`
    Alternate route: `/v2/characters/{character_id}/stats/`
    ---
    This route is cached for up to 86400 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/stats/')


def get_characters_character_id_titles(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns a character's titles
    ---
    Alternate route: `/latest/characters/{character_id}/titles/`
    Alternate route: `/legacy/characters/{character_id}/titles/`
    Alternate route: `/v1/characters/{character_id}/titles/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/titles/')


def get_characters_character_id_wallet(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns a character's wallet balance
    ---
    Alternate route: `/latest/characters/{character_id}/wallet/`
    Alternate route: `/legacy/characters/{character_id}/wallet/`
    Alternate route: `/v1/characters/{character_id}/wallet/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/wallet/')


def get_characters_character_id_wallet_journal(*,
                                               character_id,
                                               token,
                                               if_none_match=None,
                                               page='1'):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Retrieve the given character's wallet journal going 30 days back
    ---
    Alternate route: `/latest/characters/{character_id}/wallet/journal/`
    Alternate route: `/v6/characters/{character_id}/wallet/journal/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/characters/{character_id}/wallet/journal/')


def get_characters_character_id_wallet_transactions(*,
                                                    character_id,
                                                    from_id,
                                                    token,
                                                    if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param from_id: Only show transactions happened before the one referenced by this id
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get wallet transactions of a character
    ---
    Alternate route: `/latest/characters/{character_id}/wallet/transactions/`
    Alternate route: `/legacy/characters/{character_id}/wallet/transactions/`
    Alternate route: `/v1/characters/{character_id}/wallet/transactions/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        from_id=from_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/characters/{character_id}/wallet/transactions/')


def get_contracts_public_bids_contract_id(*,
                                          contract_id,
                                          if_none_match=None,
                                          page='1'):
    """
    :param contract_id: ID of a contract
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Lists bids on a public auction contract
    ---
    Alternate route: `/latest/contracts/public/bids/{contract_id}/`
    Alternate route: `/legacy/contracts/public/bids/{contract_id}/`
    Alternate route: `/v1/contracts/public/bids/{contract_id}/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(contract_id=contract_id,
                        if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/contracts/public/bids/{contract_id}/')


def get_contracts_public_items_contract_id(*,
                                           contract_id,
                                           if_none_match=None,
                                           page='1'):
    """
    :param contract_id: ID of a contract
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Lists items of a public contract
    ---
    Alternate route: `/latest/contracts/public/items/{contract_id}/`
    Alternate route: `/legacy/contracts/public/items/{contract_id}/`
    Alternate route: `/v1/contracts/public/items/{contract_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(contract_id=contract_id,
                        if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/contracts/public/items/{contract_id}/')


def get_contracts_public_region_id(*, region_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param region_id: An EVE region id
    Returns a paginated list of all public contracts in the given region
    ---
    Alternate route: `/latest/contracts/public/{region_id}/`
    Alternate route: `/legacy/contracts/public/{region_id}/`
    Alternate route: `/v1/contracts/public/{region_id}/`
    ---
    This route is cached for up to 1800 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        region_id=region_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/contracts/public/{region_id}/')


def get_corporation_corporation_id_mining_extractions(*,
                                                      corporation_id,
                                                      token,
                                                      if_none_match=None,
                                                      page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Extraction timers for all moon chunks being extracted by refineries belonging to a corporation.
    
    ---
    Alternate route: `/latest/corporation/{corporation_id}/mining/extractions/`
    Alternate route: `/legacy/corporation/{corporation_id}/mining/extractions/`
    Alternate route: `/v1/corporation/{corporation_id}/mining/extractions/`
    ---
    This route is cached for up to 1800 seconds
    ---
    Requires one of the following EVE corporation role(s): Station_Manager
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporation/{corporation_id}/mining/extractions/')


def get_corporation_corporation_id_mining_observers(*,
                                                    corporation_id,
                                                    token,
                                                    if_none_match=None,
                                                    page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Paginated list of all entities capable of observing and recording mining for a corporation
    
    ---
    Alternate route: `/latest/corporation/{corporation_id}/mining/observers/`
    Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/`
    Alternate route: `/v1/corporation/{corporation_id}/mining/observers/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporation/{corporation_id}/mining/observers/')


def get_corporation_corporation_id_mining_observers_observer_id(
        *, corporation_id, observer_id, token, if_none_match=None, page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param observer_id: A mining observer id
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Paginated record of all mining seen by an observer
    
    ---
    Alternate route: `/latest/corporation/{corporation_id}/mining/observers/{observer_id}/`
    Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/{observer_id}/`
    Alternate route: `/v1/corporation/{corporation_id}/mining/observers/{observer_id}/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        observer_id=observer_id,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporation/{corporation_id}/mining/observers/{observer_id}/')


def get_corporations_npccorps(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of npc corporations
    ---
    Alternate route: `/latest/corporations/npccorps/`
    Alternate route: `/legacy/corporations/npccorps/`
    Alternate route: `/v1/corporations/npccorps/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/npccorps/')


def get_corporations_corporation_id(*, corporation_id, if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/`
    Alternate route: `/v4/corporations/{corporation_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/')


def get_corporations_corporation_id_alliancehistory(*,
                                                    corporation_id,
                                                    if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of all the alliances a corporation has been a member of
    ---
    Alternate route: `/latest/corporations/{corporation_id}/alliancehistory/`
    Alternate route: `/v2/corporations/{corporation_id}/alliancehistory/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/alliancehistory/')


def get_corporations_corporation_id_assets(*,
                                           corporation_id,
                                           token,
                                           if_none_match=None,
                                           page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return a list of the corporation assets
    ---
    Alternate route: `/latest/corporations/{corporation_id}/assets/`
    Alternate route: `/v3/corporations/{corporation_id}/assets/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/assets/')


def post_corporations_corporation_id_assets_locations(*, corporation_id,
                                                      item_ids, token):
    """
    :param corporation_id: An EVE corporation ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    Alternate route: `/latest/corporations/{corporation_id}/assets/locations/`
    Alternate route: `/v2/corporations/{corporation_id}/assets/locations/`
    
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        item_ids=item_ids,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='POST',
        path=f'/corporations/{corporation_id}/assets/locations/')


def post_corporations_corporation_id_assets_names(*, corporation_id, item_ids,
                                                  token):
    """
    :param corporation_id: An EVE corporation ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships
    ---
    Alternate route: `/latest/corporations/{corporation_id}/assets/names/`
    Alternate route: `/legacy/corporations/{corporation_id}/assets/names/`
    Alternate route: `/v1/corporations/{corporation_id}/assets/names/`
    
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/corporations/{corporation_id}/assets/names/')


def get_corporations_corporation_id_blueprints(*,
                                               corporation_id,
                                               token,
                                               if_none_match=None,
                                               page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Returns a list of blueprints the corporation owns
    ---
    Alternate route: `/latest/corporations/{corporation_id}/blueprints/`
    Alternate route: `/v2/corporations/{corporation_id}/blueprints/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/blueprints/')


def get_corporations_corporation_id_bookmarks(*,
                                              corporation_id,
                                              token,
                                              if_none_match=None,
                                              page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    A list of your corporation's bookmarks
    ---
    Alternate route: `/latest/corporations/{corporation_id}/bookmarks/`
    Alternate route: `/legacy/corporations/{corporation_id}/bookmarks/`
    Alternate route: `/v1/corporations/{corporation_id}/bookmarks/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/bookmarks/')


def get_corporations_corporation_id_bookmarks_folders(*,
                                                      corporation_id,
                                                      token,
                                                      if_none_match=None,
                                                      page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    A list of your corporation's bookmark folders
    ---
    Alternate route: `/latest/corporations/{corporation_id}/bookmarks/folders/`
    Alternate route: `/legacy/corporations/{corporation_id}/bookmarks/folders/`
    Alternate route: `/v1/corporations/{corporation_id}/bookmarks/folders/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/bookmarks/folders/')


def get_corporations_corporation_id_contacts(*,
                                             corporation_id,
                                             token,
                                             if_none_match=None,
                                             page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return contacts of a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/contacts/`
    Alternate route: `/v2/corporations/{corporation_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/contacts/')


def get_corporations_corporation_id_contacts_labels(*,
                                                    corporation_id,
                                                    token,
                                                    if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return custom labels for a corporation's contacts
    ---
    Alternate route: `/latest/corporations/{corporation_id}/contacts/labels/`
    Alternate route: `/legacy/corporations/{corporation_id}/contacts/labels/`
    Alternate route: `/v1/corporations/{corporation_id}/contacts/labels/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/contacts/labels/')


def get_corporations_corporation_id_containers_logs(*,
                                                    corporation_id,
                                                    token,
                                                    if_none_match=None,
                                                    page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/containers/logs/`
    Alternate route: `/v2/corporations/{corporation_id}/containers/logs/`
    ---
    This route is cached for up to 600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/containers/logs/')


def get_corporations_corporation_id_contracts(*,
                                              corporation_id,
                                              token,
                                              if_none_match=None,
                                              page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress".
    ---
    Alternate route: `/latest/corporations/{corporation_id}/contracts/`
    Alternate route: `/legacy/corporations/{corporation_id}/contracts/`
    Alternate route: `/v1/corporations/{corporation_id}/contracts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/contracts/')


def get_corporations_corporation_id_contracts_contract_id_bids(
        *, contract_id, corporation_id, token, if_none_match=None, page='1'):
    """
    :param contract_id: ID of a contract
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Lists bids on a particular auction contract
    ---
    Alternate route: `/latest/corporations/{corporation_id}/contracts/{contract_id}/bids/`
    Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/bids/`
    Alternate route: `/v1/corporations/{corporation_id}/contracts/{contract_id}/bids/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        contract_id=contract_id,
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/contracts/{contract_id}/bids/')


def get_corporations_corporation_id_contracts_contract_id_items(
        *, contract_id, corporation_id, token, if_none_match=None):
    """
    :param contract_id: ID of a contract
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Lists items of a particular contract
    ---
    Alternate route: `/latest/corporations/{corporation_id}/contracts/{contract_id}/items/`
    Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/items/`
    Alternate route: `/v1/corporations/{corporation_id}/contracts/{contract_id}/items/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        contract_id=contract_id,
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/contracts/{contract_id}/items/')


def get_corporations_corporation_id_customs_offices(*,
                                                    corporation_id,
                                                    token,
                                                    if_none_match=None,
                                                    page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    List customs offices owned by a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/customs_offices/`
    Alternate route: `/legacy/corporations/{corporation_id}/customs_offices/`
    Alternate route: `/v1/corporations/{corporation_id}/customs_offices/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/customs_offices/')


def get_corporations_corporation_id_divisions(*,
                                              corporation_id,
                                              token,
                                              if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return corporation hangar and wallet division names, only show if a division is not using the default name
    ---
    Alternate route: `/latest/corporations/{corporation_id}/divisions/`
    Alternate route: `/legacy/corporations/{corporation_id}/divisions/`
    Alternate route: `/v1/corporations/{corporation_id}/divisions/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/divisions/')


def get_corporations_corporation_id_facilities(*,
                                               corporation_id,
                                               token,
                                               if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a corporation's facilities
    ---
    Alternate route: `/latest/corporations/{corporation_id}/facilities/`
    Alternate route: `/legacy/corporations/{corporation_id}/facilities/`
    Alternate route: `/v1/corporations/{corporation_id}/facilities/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Factory_Manager
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/facilities/')


def get_corporations_corporation_id_fw_stats(*,
                                             corporation_id,
                                             token,
                                             if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Statistics about a corporation involved in faction warfare
    ---
    Alternate route: `/latest/corporations/{corporation_id}/fw/stats/`
    Alternate route: `/legacy/corporations/{corporation_id}/fw/stats/`
    Alternate route: `/v1/corporations/{corporation_id}/fw/stats/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/fw/stats/')


def get_corporations_corporation_id_icons(*,
                                          corporation_id,
                                          if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the icon urls for a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/icons/`
    Alternate route: `/legacy/corporations/{corporation_id}/icons/`
    Alternate route: `/v1/corporations/{corporation_id}/icons/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/icons/')


def get_corporations_corporation_id_industry_jobs(*,
                                                  corporation_id,
                                                  include_completed,
                                                  token,
                                                  if_none_match=None,
                                                  page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param include_completed: Whether to retrieve completed corporation industry jobs. Only includes jobs from the past 90 days
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    List industry jobs run by a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/industry/jobs/`
    Alternate route: `/legacy/corporations/{corporation_id}/industry/jobs/`
    Alternate route: `/v1/corporations/{corporation_id}/industry/jobs/`
    ---
    This route is cached for up to 300 seconds
    ---
    Requires one of the following EVE corporation role(s): Factory_Manager
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        include_completed=include_completed,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/industry/jobs/')


def get_corporations_corporation_id_killmails_recent(*,
                                                     corporation_id,
                                                     token,
                                                     if_none_match=None,
                                                     page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Get a list of a corporation's kills and losses going back 90 days
    ---
    Alternate route: `/latest/corporations/{corporation_id}/killmails/recent/`
    Alternate route: `/legacy/corporations/{corporation_id}/killmails/recent/`
    Alternate route: `/v1/corporations/{corporation_id}/killmails/recent/`
    ---
    This route is cached for up to 300 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/killmails/recent/')


def get_corporations_corporation_id_medals(*,
                                           corporation_id,
                                           token,
                                           if_none_match=None,
                                           page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Returns a corporation's medals
    ---
    Alternate route: `/latest/corporations/{corporation_id}/medals/`
    Alternate route: `/legacy/corporations/{corporation_id}/medals/`
    Alternate route: `/v1/corporations/{corporation_id}/medals/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/medals/')


def get_corporations_corporation_id_medals_issued(*,
                                                  corporation_id,
                                                  token,
                                                  if_none_match=None,
                                                  page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Returns medals issued by a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/medals/issued/`
    Alternate route: `/legacy/corporations/{corporation_id}/medals/issued/`
    Alternate route: `/v1/corporations/{corporation_id}/medals/issued/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/medals/issued/')


def get_corporations_corporation_id_members(*,
                                            corporation_id,
                                            token,
                                            if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return the current member list of a corporation, the token's character need to be a member of the corporation.
    ---
    Alternate route: `/latest/corporations/{corporation_id}/members/`
    Alternate route: `/v3/corporations/{corporation_id}/members/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/members/')


def get_corporations_corporation_id_members_limit(*,
                                                  corporation_id,
                                                  token,
                                                  if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a corporation's member limit, not including CEO himself
    ---
    Alternate route: `/latest/corporations/{corporation_id}/members/limit/`
    Alternate route: `/legacy/corporations/{corporation_id}/members/limit/`
    Alternate route: `/v1/corporations/{corporation_id}/members/limit/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/members/limit/')


def get_corporations_corporation_id_members_titles(*,
                                                   corporation_id,
                                                   token,
                                                   if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns a corporation's members' titles
    ---
    Alternate route: `/latest/corporations/{corporation_id}/members/titles/`
    Alternate route: `/legacy/corporations/{corporation_id}/members/titles/`
    Alternate route: `/v1/corporations/{corporation_id}/members/titles/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/members/titles/')


def get_corporations_corporation_id_membertracking(*,
                                                   corporation_id,
                                                   token,
                                                   if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns additional information about a corporation's members which helps tracking their activities
    ---
    Alternate route: `/latest/corporations/{corporation_id}/membertracking/`
    Alternate route: `/legacy/corporations/{corporation_id}/membertracking/`
    Alternate route: `/v1/corporations/{corporation_id}/membertracking/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/membertracking/')


def get_corporations_corporation_id_orders(*,
                                           corporation_id,
                                           token,
                                           if_none_match=None,
                                           page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    List open market orders placed on behalf of a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/orders/`
    Alternate route: `/v3/corporations/{corporation_id}/orders/`
    ---
    This route is cached for up to 1200 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Trader
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/orders/')


def get_corporations_corporation_id_orders_history(*,
                                                   corporation_id,
                                                   token,
                                                   if_none_match=None,
                                                   page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past.
    ---
    Alternate route: `/latest/corporations/{corporation_id}/orders/history/`
    Alternate route: `/v2/corporations/{corporation_id}/orders/history/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Trader
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/orders/history/')


def get_corporations_corporation_id_roles(*,
                                          corporation_id,
                                          token,
                                          if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return the roles of all members if the character has the personnel manager role or any grantable role.
    ---
    Alternate route: `/latest/corporations/{corporation_id}/roles/`
    Alternate route: `/legacy/corporations/{corporation_id}/roles/`
    Alternate route: `/v1/corporations/{corporation_id}/roles/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/roles/')


def get_corporations_corporation_id_roles_history(*,
                                                  corporation_id,
                                                  token,
                                                  if_none_match=None,
                                                  page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return how roles have changed for a coporation's members, up to a month
    ---
    Alternate route: `/latest/corporations/{corporation_id}/roles/history/`
    Alternate route: `/legacy/corporations/{corporation_id}/roles/history/`
    Alternate route: `/v1/corporations/{corporation_id}/roles/history/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/roles/history/')


def get_corporations_corporation_id_shareholders(*,
                                                 corporation_id,
                                                 token,
                                                 if_none_match=None,
                                                 page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return the current shareholders of a corporation.
    ---
    Alternate route: `/latest/corporations/{corporation_id}/shareholders/`
    Alternate route: `/legacy/corporations/{corporation_id}/shareholders/`
    Alternate route: `/v1/corporations/{corporation_id}/shareholders/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/shareholders/')


def get_corporations_corporation_id_standings(*,
                                              corporation_id,
                                              token,
                                              if_none_match=None,
                                              page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Return corporation standings from agents, NPC corporations, and factions
    ---
    Alternate route: `/latest/corporations/{corporation_id}/standings/`
    Alternate route: `/legacy/corporations/{corporation_id}/standings/`
    Alternate route: `/v1/corporations/{corporation_id}/standings/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/standings/')


def get_corporations_corporation_id_starbases(*,
                                              corporation_id,
                                              token,
                                              if_none_match=None,
                                              page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Returns list of corporation starbases (POSes)
    ---
    Alternate route: `/latest/corporations/{corporation_id}/starbases/`
    Alternate route: `/legacy/corporations/{corporation_id}/starbases/`
    Alternate route: `/v1/corporations/{corporation_id}/starbases/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/starbases/')


def get_corporations_corporation_id_starbases_starbase_id(
        *, corporation_id, starbase_id, system_id, token, if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param starbase_id: An EVE starbase (POS) ID
    :param system_id: The solar system this starbase (POS) is located in,
    :param token: Access token to use if unable to set a header
    Returns various settings and fuels of a starbase (POS)
    ---
    Alternate route: `/latest/corporations/{corporation_id}/starbases/{starbase_id}/`
    Alternate route: `/legacy/corporations/{corporation_id}/starbases/{starbase_id}/`
    Alternate route: `/v1/corporations/{corporation_id}/starbases/{starbase_id}/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        starbase_id=starbase_id,
        system_id=system_id,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/starbases/{starbase_id}/')


def get_corporations_corporation_id_structures(*,
                                               corporation_id,
                                               language,
                                               token,
                                               accept_language='en-us',
                                               if_none_match=None,
                                               page='1'):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th
    ---
    Alternate route: `/latest/corporations/{corporation_id}/structures/`
    Alternate route: `/v3/corporations/{corporation_id}/structures/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Station_Manager
    
    """
    ESI_request.request(accept_language=accept_language,
                        corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        language=language,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/structures/')


def get_corporations_corporation_id_titles(*,
                                           corporation_id,
                                           token,
                                           if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Returns a corporation's titles
    ---
    Alternate route: `/latest/corporations/{corporation_id}/titles/`
    Alternate route: `/legacy/corporations/{corporation_id}/titles/`
    Alternate route: `/v1/corporations/{corporation_id}/titles/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/titles/')


def get_corporations_corporation_id_wallets(*,
                                            corporation_id,
                                            token,
                                            if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get a corporation's wallets
    ---
    Alternate route: `/latest/corporations/{corporation_id}/wallets/`
    Alternate route: `/legacy/corporations/{corporation_id}/wallets/`
    Alternate route: `/v1/corporations/{corporation_id}/wallets/`
    ---
    This route is cached for up to 300 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/corporations/{corporation_id}/wallets/')


def get_corporations_corporation_id_wallets_division_journal(
        *, corporation_id, division, token, if_none_match=None, page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param division: Wallet key of the division to fetch journals from
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Retrieve the given corporation's wallet journal for the given division going 30 days back
    ---
    Alternate route: `/latest/corporations/{corporation_id}/wallets/{division}/journal/`
    Alternate route: `/v4/corporations/{corporation_id}/wallets/{division}/journal/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        division=division,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/wallets/{division}/journal/')


def get_corporations_corporation_id_wallets_division_transactions(
        *, corporation_id, division, from_id, token, if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param division: Wallet key of the division to fetch journals from
    :param from_id: Only show journal entries happened before the transaction referenced by this id
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get wallet transactions of a corporation
    ---
    Alternate route: `/latest/corporations/{corporation_id}/wallets/{division}/transactions/`
    Alternate route: `/legacy/corporations/{corporation_id}/wallets/{division}/transactions/`
    Alternate route: `/v1/corporations/{corporation_id}/wallets/{division}/transactions/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        division=division,
        from_id=from_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='dev',
        HTTP_method='GET',
        path=f'/corporations/{corporation_id}/wallets/{division}/transactions/'
    )


def get_dogma_attributes(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of dogma attribute ids
    ---
    Alternate route: `/latest/dogma/attributes/`
    Alternate route: `/legacy/dogma/attributes/`
    Alternate route: `/v1/dogma/attributes/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/dogma/attributes/')


def get_dogma_attributes_attribute_id(*, attribute_id, if_none_match=None):
    """
    :param attribute_id: A dogma attribute ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a dogma attribute
    ---
    Alternate route: `/latest/dogma/attributes/{attribute_id}/`
    Alternate route: `/legacy/dogma/attributes/{attribute_id}/`
    Alternate route: `/v1/dogma/attributes/{attribute_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(attribute_id=attribute_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/dogma/attributes/{attribute_id}/')


def get_dogma_dynamic_items_type_id_item_id(*,
                                            item_id,
                                            type_id,
                                            if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param item_id: item_id integer
    :param type_id: type_id integer
    Returns info about a dynamic item resulting from mutation with a mutaplasmid.
    ---
    Alternate route: `/latest/dogma/dynamic/items/{type_id}/{item_id}/`
    Alternate route: `/legacy/dogma/dynamic/items/{type_id}/{item_id}/`
    Alternate route: `/v1/dogma/dynamic/items/{type_id}/{item_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        item_id=item_id,
                        type_id=type_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/dogma/dynamic/items/{type_id}/{item_id}/')


def get_dogma_effects(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of dogma effect ids
    ---
    Alternate route: `/latest/dogma/effects/`
    Alternate route: `/legacy/dogma/effects/`
    Alternate route: `/v1/dogma/effects/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/dogma/effects/')


def get_dogma_effects_effect_id(*, effect_id, if_none_match=None):
    """
    :param effect_id: A dogma effect ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a dogma effect
    ---
    Alternate route: `/latest/dogma/effects/{effect_id}/`
    Alternate route: `/v2/dogma/effects/{effect_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(effect_id=effect_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/dogma/effects/{effect_id}/')


def get_fleets_fleet_id(*, fleet_id, token, if_none_match=None):
    """
    :param fleet_id: ID for a fleet
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return details about a fleet
    ---
    Alternate route: `/latest/fleets/{fleet_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fleets/{fleet_id}/')


def put_fleets_fleet_id(*, fleet_id, new_settings, token):
    """
    :param fleet_id: ID for a fleet
    :param new_settings: What to update for this fleet
    :param token: Access token to use if unable to set a header
    Update settings about a fleet
    ---
    Alternate route: `/latest/fleets/{fleet_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        new_settings=new_settings,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='PUT',
                        path=f'/fleets/{fleet_id}/')


def get_fleets_fleet_id_members(*,
                                fleet_id,
                                language,
                                token,
                                accept_language='en-us',
                                if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param fleet_id: ID for a fleet
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param token: Access token to use if unable to set a header
    Return information about fleet members
    ---
    Alternate route: `/latest/fleets/{fleet_id}/members/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/`
    Alternate route: `/v1/fleets/{fleet_id}/members/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        language=language,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fleets/{fleet_id}/members/')


def post_fleets_fleet_id_members(*, fleet_id, invitation, token):
    """
    :param fleet_id: ID for a fleet
    :param invitation: Details of the invitation
    :param token: Access token to use if unable to set a header
    Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI
    ---
    Alternate route: `/latest/fleets/{fleet_id}/members/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/`
    Alternate route: `/v1/fleets/{fleet_id}/members/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        invitation=invitation,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/fleets/{fleet_id}/members/')


def delete_fleets_fleet_id_members_member_id(*, fleet_id, member_id, token):
    """
    :param fleet_id: ID for a fleet
    :param member_id: The character ID of a member in this fleet
    :param token: Access token to use if unable to set a header
    Kick a fleet member
    ---
    Alternate route: `/latest/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/members/{member_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        member_id=member_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='DELETE',
                        path=f'/fleets/{fleet_id}/members/{member_id}/')


def put_fleets_fleet_id_members_member_id(*, fleet_id, member_id, movement,
                                          token):
    """
    :param fleet_id: ID for a fleet
    :param member_id: The character ID of a member in this fleet
    :param movement: Details of the invitation
    :param token: Access token to use if unable to set a header
    Move a fleet member around
    ---
    Alternate route: `/latest/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/members/{member_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        member_id=member_id,
                        movement=movement,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='PUT',
                        path=f'/fleets/{fleet_id}/members/{member_id}/')


def delete_fleets_fleet_id_squads_squad_id(*, fleet_id, squad_id, token):
    """
    :param fleet_id: ID for a fleet
    :param squad_id: The squad to delete
    :param token: Access token to use if unable to set a header
    Delete a fleet squad, only empty squads can be deleted
    ---
    Alternate route: `/latest/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/squads/{squad_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        squad_id=squad_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='DELETE',
                        path=f'/fleets/{fleet_id}/squads/{squad_id}/')


def put_fleets_fleet_id_squads_squad_id(*, fleet_id, naming, squad_id, token):
    """
    :param fleet_id: ID for a fleet
    :param naming: New name of the squad
    :param squad_id: The squad to rename
    :param token: Access token to use if unable to set a header
    Rename a fleet squad
    ---
    Alternate route: `/latest/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/squads/{squad_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        naming=naming,
                        squad_id=squad_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='PUT',
                        path=f'/fleets/{fleet_id}/squads/{squad_id}/')


def get_fleets_fleet_id_wings(*,
                              fleet_id,
                              language,
                              token,
                              accept_language='en-us',
                              if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param fleet_id: ID for a fleet
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param token: Access token to use if unable to set a header
    Return information about wings in a fleet
    ---
    Alternate route: `/latest/fleets/{fleet_id}/wings/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/`
    Alternate route: `/v1/fleets/{fleet_id}/wings/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        language=language,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fleets/{fleet_id}/wings/')


def post_fleets_fleet_id_wings(*, fleet_id, token):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    Create a new wing in a fleet
    ---
    Alternate route: `/latest/fleets/{fleet_id}/wings/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/`
    Alternate route: `/v1/fleets/{fleet_id}/wings/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/fleets/{fleet_id}/wings/')


def delete_fleets_fleet_id_wings_wing_id(*, fleet_id, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing to delete
    Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty
    ---
    Alternate route: `/latest/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        wing_id=wing_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='DELETE',
                        path=f'/fleets/{fleet_id}/wings/{wing_id}/')


def put_fleets_fleet_id_wings_wing_id(*, fleet_id, naming, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param naming: New name of the wing
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing to rename
    Rename a fleet wing
    ---
    Alternate route: `/latest/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        naming=naming,
                        token=token,
                        wing_id=wing_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='PUT',
                        path=f'/fleets/{fleet_id}/wings/{wing_id}/')


def post_fleets_fleet_id_wings_wing_id_squads(*, fleet_id, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing_id to create squad in
    Create a new squad in a fleet
    ---
    Alternate route: `/latest/fleets/{fleet_id}/wings/{wing_id}/squads/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/squads/`
    Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/squads/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        wing_id=wing_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/fleets/{fleet_id}/wings/{wing_id}/squads/')


def get_fw_leaderboards(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday
    ---
    Alternate route: `/latest/fw/leaderboards/`
    Alternate route: `/legacy/fw/leaderboards/`
    Alternate route: `/v1/fw/leaderboards/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fw/leaderboards/')


def get_fw_leaderboards_characters(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday
    ---
    Alternate route: `/latest/fw/leaderboards/characters/`
    Alternate route: `/legacy/fw/leaderboards/characters/`
    Alternate route: `/v1/fw/leaderboards/characters/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fw/leaderboards/characters/')


def get_fw_leaderboards_corporations(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday
    ---
    Alternate route: `/latest/fw/leaderboards/corporations/`
    Alternate route: `/legacy/fw/leaderboards/corporations/`
    Alternate route: `/v1/fw/leaderboards/corporations/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fw/leaderboards/corporations/')


def get_fw_stats(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Statistical overviews of factions involved in faction warfare
    ---
    Alternate route: `/latest/fw/stats/`
    Alternate route: `/legacy/fw/stats/`
    Alternate route: `/v1/fw/stats/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fw/stats/')


def get_fw_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    An overview of the current ownership of faction warfare solar systems
    ---
    Alternate route: `/latest/fw/systems/`
    Alternate route: `/v2/fw/systems/`
    ---
    This route is cached for up to 1800 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fw/systems/')


def get_fw_wars(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Data about which NPC factions are at war
    ---
    Alternate route: `/latest/fw/wars/`
    Alternate route: `/legacy/fw/wars/`
    Alternate route: `/v1/fw/wars/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/fw/wars/')


def get_incursions(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of current incursions
    ---
    Alternate route: `/latest/incursions/`
    Alternate route: `/legacy/incursions/`
    Alternate route: `/v1/incursions/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/incursions/')


def get_industry_facilities(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of industry facilities
    ---
    Alternate route: `/latest/industry/facilities/`
    Alternate route: `/legacy/industry/facilities/`
    Alternate route: `/v1/industry/facilities/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/industry/facilities/')


def get_industry_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return cost indices for solar systems
    ---
    Alternate route: `/latest/industry/systems/`
    Alternate route: `/legacy/industry/systems/`
    Alternate route: `/v1/industry/systems/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/industry/systems/')


def get_insurance_prices(*,
                         language,
                         accept_language='en-us',
                         if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Return available insurance levels for all ship types
    ---
    Alternate route: `/latest/insurance/prices/`
    Alternate route: `/legacy/insurance/prices/`
    Alternate route: `/v1/insurance/prices/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/insurance/prices/')


def get_killmails_killmail_id_killmail_hash(*,
                                            killmail_hash,
                                            killmail_id,
                                            if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param killmail_hash: The killmail hash for verification
    :param killmail_id: The killmail ID to be queried
    Return a single killmail from its ID and hash
    ---
    Alternate route: `/latest/killmails/{killmail_id}/{killmail_hash}/`
    Alternate route: `/legacy/killmails/{killmail_id}/{killmail_hash}/`
    Alternate route: `/v1/killmails/{killmail_id}/{killmail_hash}/`
    ---
    This route is cached for up to 1209600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        killmail_hash=killmail_hash,
                        killmail_id=killmail_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/killmails/{killmail_id}/{killmail_hash}/')


def get_loyalty_stores_corporation_id_offers(*,
                                             corporation_id,
                                             if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of offers from a specific corporation's loyalty store
    ---
    Alternate route: `/latest/loyalty/stores/{corporation_id}/offers/`
    Alternate route: `/legacy/loyalty/stores/{corporation_id}/offers/`
    Alternate route: `/v1/loyalty/stores/{corporation_id}/offers/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/loyalty/stores/{corporation_id}/offers/')


def get_markets_groups(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of item groups
    ---
    Alternate route: `/latest/markets/groups/`
    Alternate route: `/legacy/markets/groups/`
    Alternate route: `/v1/markets/groups/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/markets/groups/')


def get_markets_groups_market_group_id(*,
                                       language,
                                       market_group_id,
                                       accept_language='en-us',
                                       if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param market_group_id: An Eve item group ID
    Get information on an item group
    ---
    Alternate route: `/latest/markets/groups/{market_group_id}/`
    Alternate route: `/legacy/markets/groups/{market_group_id}/`
    Alternate route: `/v1/markets/groups/{market_group_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        market_group_id=market_group_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/markets/groups/{market_group_id}/')


def get_markets_prices(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of prices
    ---
    Alternate route: `/latest/markets/prices/`
    Alternate route: `/legacy/markets/prices/`
    Alternate route: `/v1/markets/prices/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/markets/prices/')


def get_markets_structures_structure_id(*,
                                        structure_id,
                                        token,
                                        if_none_match=None,
                                        page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param structure_id: Return orders in this structure
    :param token: Access token to use if unable to set a header
    Return all orders in a structure
    ---
    Alternate route: `/latest/markets/structures/{structure_id}/`
    Alternate route: `/legacy/markets/structures/{structure_id}/`
    Alternate route: `/v1/markets/structures/{structure_id}/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        structure_id=structure_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/markets/structures/{structure_id}/')


def get_markets_region_id_history(*, region_id, type_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param region_id: Return statistics in this region
    :param type_id: Return statistics for this type
    Return a list of historical market statistics for the specified type in a region
    ---
    Alternate route: `/latest/markets/{region_id}/history/`
    Alternate route: `/legacy/markets/{region_id}/history/`
    Alternate route: `/v1/markets/{region_id}/history/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        region_id=region_id,
                        type_id=type_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/markets/{region_id}/history/')


def get_markets_region_id_orders(*,
                                 order_type,
                                 region_id,
                                 type_id,
                                 if_none_match=None,
                                 page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param order_type: ['buy', 'sell', 'all'] Filter buy/sell orders, return all orders by default. If you query without type_id, we always return both buy and sell orders
    :param page: Which page of results to return
    :param region_id: Return orders in this region
    :param type_id: Return orders only for this type
    Return a list of orders in a region
    ---
    Alternate route: `/latest/markets/{region_id}/orders/`
    Alternate route: `/legacy/markets/{region_id}/orders/`
    Alternate route: `/v1/markets/{region_id}/orders/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        order_type=order_type,
                        page=page,
                        region_id=region_id,
                        type_id=type_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/markets/{region_id}/orders/')


def get_markets_region_id_types(*, region_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param region_id: Return statistics in this region
    Return a list of type IDs that have active orders in the region, for efficient market indexing.
    ---
    Alternate route: `/latest/markets/{region_id}/types/`
    Alternate route: `/legacy/markets/{region_id}/types/`
    Alternate route: `/v1/markets/{region_id}/types/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        region_id=region_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/markets/{region_id}/types/')


def get_opportunities_groups(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of opportunities groups
    ---
    Alternate route: `/latest/opportunities/groups/`
    Alternate route: `/legacy/opportunities/groups/`
    Alternate route: `/v1/opportunities/groups/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/opportunities/groups/')


def get_opportunities_groups_group_id(*,
                                      group_id,
                                      language,
                                      accept_language='en-us',
                                      if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param group_id: ID of an opportunities group
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Return information of an opportunities group
    ---
    Alternate route: `/latest/opportunities/groups/{group_id}/`
    Alternate route: `/legacy/opportunities/groups/{group_id}/`
    Alternate route: `/v1/opportunities/groups/{group_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        group_id=group_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/opportunities/groups/{group_id}/')


def get_opportunities_tasks(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of opportunities tasks
    ---
    Alternate route: `/latest/opportunities/tasks/`
    Alternate route: `/legacy/opportunities/tasks/`
    Alternate route: `/v1/opportunities/tasks/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/opportunities/tasks/')


def get_opportunities_tasks_task_id(*, task_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param task_id: ID of an opportunities task
    Return information of an opportunities task
    ---
    Alternate route: `/latest/opportunities/tasks/{task_id}/`
    Alternate route: `/legacy/opportunities/tasks/{task_id}/`
    Alternate route: `/v1/opportunities/tasks/{task_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        task_id=task_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/opportunities/tasks/{task_id}/')


def get_route_origin_destination(*,
                                 avoid,
                                 connections,
                                 destination,
                                 flag,
                                 origin,
                                 if_none_match=None):
    """
    :param avoid: avoid solar system ID(s)
    :param connections: connected solar system pairs
    :param destination: destination solar system ID
    :param flag: ['shortest', 'secure', 'insecure'] route security preference
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param origin: origin solar system ID
    Get the systems between origin and destination
    ---
    Alternate route: `/latest/route/{origin}/{destination}/`
    Alternate route: `/legacy/route/{origin}/{destination}/`
    Alternate route: `/v1/route/{origin}/{destination}/`
    ---
    This route is cached for up to 86400 seconds
    """
    ESI_request.request(avoid=avoid,
                        connections=connections,
                        destination=destination,
                        flag=flag,
                        if_none_match=if_none_match,
                        origin=origin,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/route/{origin}/{destination}/')


def get_search(*,
               categories,
               language,
               search,
               strict,
               accept_language='en-us',
               if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param categories: Type of entities to search for
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param search: The string to search on
    :param strict: Whether the search should be a strict match
    Search for entities that match a given sub-string.
    ---
    Alternate route: `/latest/search/`
    Alternate route: `/legacy/search/`
    Alternate route: `/v2/search/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        categories=categories,
                        if_none_match=if_none_match,
                        language=language,
                        search=search,
                        strict=strict,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/search/')


def get_sovereignty_campaigns(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty data for campaigns.
    ---
    Alternate route: `/latest/sovereignty/campaigns/`
    Alternate route: `/legacy/sovereignty/campaigns/`
    Alternate route: `/v1/sovereignty/campaigns/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/sovereignty/campaigns/')


def get_sovereignty_map(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty information for solar systems
    ---
    Alternate route: `/latest/sovereignty/map/`
    Alternate route: `/legacy/sovereignty/map/`
    Alternate route: `/v1/sovereignty/map/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/sovereignty/map/')


def get_sovereignty_structures(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty data for structures.
    ---
    Alternate route: `/latest/sovereignty/structures/`
    Alternate route: `/legacy/sovereignty/structures/`
    Alternate route: `/v1/sovereignty/structures/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/sovereignty/structures/')


def get_status(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    EVE Server status
    ---
    Alternate route: `/latest/status/`
    Alternate route: `/legacy/status/`
    Alternate route: `/v1/status/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/status/')


def post_ui_autopilot_waypoint(*, add_to_beginning, clear_other_waypoints,
                               destination_id, token):
    """
    :param add_to_beginning: Whether this solar system should be added to the beginning of all waypoints
    :param clear_other_waypoints: Whether clean other waypoints beforing adding this one
    :param destination_id: The destination to travel to, can be solar system, station or structure's id
    :param token: Access token to use if unable to set a header
    Set a solar system as autopilot waypoint
    ---
    Alternate route: `/latest/ui/autopilot/waypoint/`
    Alternate route: `/legacy/ui/autopilot/waypoint/`
    Alternate route: `/v2/ui/autopilot/waypoint/`
    
    """
    ESI_request.request(add_to_beginning=add_to_beginning,
                        clear_other_waypoints=clear_other_waypoints,
                        destination_id=destination_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/ui/autopilot/waypoint/')


def post_ui_openwindow_contract(*, contract_id, token):
    """
    :param contract_id: The contract to open
    :param token: Access token to use if unable to set a header
    Open the contract window inside the client
    ---
    Alternate route: `/latest/ui/openwindow/contract/`
    Alternate route: `/legacy/ui/openwindow/contract/`
    Alternate route: `/v1/ui/openwindow/contract/`
    
    """
    ESI_request.request(contract_id=contract_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/ui/openwindow/contract/')


def post_ui_openwindow_information(*, target_id, token):
    """
    :param target_id: The target to open
    :param token: Access token to use if unable to set a header
    Open the information window for a character, corporation or alliance inside the client
    ---
    Alternate route: `/latest/ui/openwindow/information/`
    Alternate route: `/legacy/ui/openwindow/information/`
    Alternate route: `/v1/ui/openwindow/information/`
    
    """
    ESI_request.request(target_id=target_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/ui/openwindow/information/')


def post_ui_openwindow_marketdetails(*, token, type_id):
    """
    :param token: Access token to use if unable to set a header
    :param type_id: The item type to open in market window
    Open the market details window for a specific typeID inside the client
    ---
    Alternate route: `/latest/ui/openwindow/marketdetails/`
    Alternate route: `/legacy/ui/openwindow/marketdetails/`
    Alternate route: `/v1/ui/openwindow/marketdetails/`
    
    """
    ESI_request.request(token=token,
                        type_id=type_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/ui/openwindow/marketdetails/')


def post_ui_openwindow_newmail(*, new_mail, token):
    """
    :param new_mail: The details of mail to create
    :param token: Access token to use if unable to set a header
    Open the New Mail window, according to settings from the request if applicable
    ---
    Alternate route: `/latest/ui/openwindow/newmail/`
    Alternate route: `/legacy/ui/openwindow/newmail/`
    Alternate route: `/v1/ui/openwindow/newmail/`
    
    """
    ESI_request.request(new_mail=new_mail,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/ui/openwindow/newmail/')


def get_universe_ancestries(*,
                            language,
                            accept_language='en-us',
                            if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Get all character ancestries
    ---
    Alternate route: `/latest/universe/ancestries/`
    Alternate route: `/legacy/universe/ancestries/`
    Alternate route: `/v1/universe/ancestries/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/ancestries/')


def get_universe_asteroid_belts_asteroid_belt_id(*,
                                                 asteroid_belt_id,
                                                 if_none_match=None):
    """
    :param asteroid_belt_id: asteroid_belt_id integer
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on an asteroid belt
    ---
    Alternate route: `/latest/universe/asteroid_belts/{asteroid_belt_id}/`
    Alternate route: `/legacy/universe/asteroid_belts/{asteroid_belt_id}/`
    Alternate route: `/v1/universe/asteroid_belts/{asteroid_belt_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(asteroid_belt_id=asteroid_belt_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/asteroid_belts/{asteroid_belt_id}/')


def get_universe_bloodlines(*,
                            language,
                            accept_language='en-us',
                            if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Get a list of bloodlines
    ---
    Alternate route: `/latest/universe/bloodlines/`
    Alternate route: `/legacy/universe/bloodlines/`
    Alternate route: `/v1/universe/bloodlines/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/bloodlines/')


def get_universe_categories(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of item categories
    ---
    Alternate route: `/latest/universe/categories/`
    Alternate route: `/legacy/universe/categories/`
    Alternate route: `/v1/universe/categories/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/categories/')


def get_universe_categories_category_id(*,
                                        category_id,
                                        language,
                                        accept_language='en-us',
                                        if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param category_id: An Eve item category ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Get information of an item category
    ---
    Alternate route: `/latest/universe/categories/{category_id}/`
    Alternate route: `/legacy/universe/categories/{category_id}/`
    Alternate route: `/v1/universe/categories/{category_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        category_id=category_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/categories/{category_id}/')


def get_universe_constellations(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of constellations
    ---
    Alternate route: `/latest/universe/constellations/`
    Alternate route: `/legacy/universe/constellations/`
    Alternate route: `/v1/universe/constellations/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/constellations/')


def get_universe_constellations_constellation_id(*,
                                                 constellation_id,
                                                 language,
                                                 accept_language='en-us',
                                                 if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param constellation_id: constellation_id integer
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Get information on a constellation
    ---
    Alternate route: `/latest/universe/constellations/{constellation_id}/`
    Alternate route: `/legacy/universe/constellations/{constellation_id}/`
    Alternate route: `/v1/universe/constellations/{constellation_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        constellation_id=constellation_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/constellations/{constellation_id}/')


def get_universe_factions(*,
                          language,
                          accept_language='en-us',
                          if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Get a list of factions
    ---
    Alternate route: `/latest/universe/factions/`
    Alternate route: `/v2/universe/factions/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/factions/')


def get_universe_graphics(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of graphics
    ---
    Alternate route: `/latest/universe/graphics/`
    Alternate route: `/legacy/universe/graphics/`
    Alternate route: `/v1/universe/graphics/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/graphics/')


def get_universe_graphics_graphic_id(*, graphic_id, if_none_match=None):
    """
    :param graphic_id: graphic_id integer
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a graphic
    ---
    Alternate route: `/latest/universe/graphics/{graphic_id}/`
    Alternate route: `/legacy/universe/graphics/{graphic_id}/`
    Alternate route: `/v1/universe/graphics/{graphic_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(graphic_id=graphic_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/graphics/{graphic_id}/')


def get_universe_groups(*, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Get a list of item groups
    ---
    Alternate route: `/latest/universe/groups/`
    Alternate route: `/legacy/universe/groups/`
    Alternate route: `/v1/universe/groups/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/groups/')


def get_universe_groups_group_id(*,
                                 group_id,
                                 language,
                                 accept_language='en-us',
                                 if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param group_id: An Eve item group ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Get information on an item group
    ---
    Alternate route: `/latest/universe/groups/{group_id}/`
    Alternate route: `/legacy/universe/groups/{group_id}/`
    Alternate route: `/v1/universe/groups/{group_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        group_id=group_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/groups/{group_id}/')


def post_universe_ids(*, language, names, accept_language='en-us'):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param names: The names to resolve
    Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours
    ---
    Alternate route: `/latest/universe/ids/`
    Alternate route: `/legacy/universe/ids/`
    Alternate route: `/v1/universe/ids/`
    
    """
    ESI_request.request(accept_language=accept_language,
                        language=language,
                        names=names,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/universe/ids/')


def get_universe_moons_moon_id(*, moon_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param moon_id: moon_id integer
    Get information on a moon
    ---
    Alternate route: `/latest/universe/moons/{moon_id}/`
    Alternate route: `/legacy/universe/moons/{moon_id}/`
    Alternate route: `/v1/universe/moons/{moon_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        moon_id=moon_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/moons/{moon_id}/')


def post_universe_names(*, ids):
    """
    :param ids: The ids to resolve
    Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions
    ---
    Alternate route: `/latest/universe/names/`
    Alternate route: `/v3/universe/names/`
    
    """
    ESI_request.request(ids=ids,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='POST',
                        path=f'/universe/names/')


def get_universe_planets_planet_id(*, planet_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param planet_id: planet_id integer
    Get information on a planet
    ---
    Alternate route: `/latest/universe/planets/{planet_id}/`
    Alternate route: `/legacy/universe/planets/{planet_id}/`
    Alternate route: `/v1/universe/planets/{planet_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        planet_id=planet_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/planets/{planet_id}/')


def get_universe_races(*,
                       language,
                       accept_language='en-us',
                       if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    Get a list of character races
    ---
    Alternate route: `/latest/universe/races/`
    Alternate route: `/legacy/universe/races/`
    Alternate route: `/v1/universe/races/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/races/')


def get_universe_regions(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of regions
    ---
    Alternate route: `/latest/universe/regions/`
    Alternate route: `/legacy/universe/regions/`
    Alternate route: `/v1/universe/regions/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/regions/')


def get_universe_regions_region_id(*,
                                   language,
                                   region_id,
                                   accept_language='en-us',
                                   if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param region_id: region_id integer
    Get information on a region
    ---
    Alternate route: `/latest/universe/regions/{region_id}/`
    Alternate route: `/legacy/universe/regions/{region_id}/`
    Alternate route: `/v1/universe/regions/{region_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        region_id=region_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/regions/{region_id}/')


def get_universe_schematics_schematic_id(*, schematic_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param schematic_id: A PI schematic ID
    Get information on a planetary factory schematic
    ---
    Alternate route: `/latest/universe/schematics/{schematic_id}/`
    Alternate route: `/legacy/universe/schematics/{schematic_id}/`
    Alternate route: `/v1/universe/schematics/{schematic_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        schematic_id=schematic_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/schematics/{schematic_id}/')


def get_universe_stargates_stargate_id(*, stargate_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param stargate_id: stargate_id integer
    Get information on a stargate
    ---
    Alternate route: `/latest/universe/stargates/{stargate_id}/`
    Alternate route: `/legacy/universe/stargates/{stargate_id}/`
    Alternate route: `/v1/universe/stargates/{stargate_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        stargate_id=stargate_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/stargates/{stargate_id}/')


def get_universe_stars_star_id(*, star_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param star_id: star_id integer
    Get information on a star
    ---
    Alternate route: `/latest/universe/stars/{star_id}/`
    Alternate route: `/legacy/universe/stars/{star_id}/`
    Alternate route: `/v1/universe/stars/{star_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        star_id=star_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/stars/{star_id}/')


def get_universe_stations_station_id(*, station_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param station_id: station_id integer
    Get information on a station
    ---
    Alternate route: `/latest/universe/stations/{station_id}/`
    Alternate route: `/v2/universe/stations/{station_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        station_id=station_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/stations/{station_id}/')


def get_universe_structures(*, filter, if_none_match=None):
    """
    :param filter: ['market', 'manufacturing_basic'] Only list public structures that have this service online
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all public structures
    ---
    Alternate route: `/latest/universe/structures/`
    Alternate route: `/legacy/universe/structures/`
    Alternate route: `/v1/universe/structures/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(filter=filter,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/structures/')


def get_universe_structures_structure_id(*,
                                         structure_id,
                                         token,
                                         if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param structure_id: An Eve structure ID
    :param token: Access token to use if unable to set a header
    Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs.
    ---
    Alternate route: `/latest/universe/structures/{structure_id}/`
    Alternate route: `/v2/universe/structures/{structure_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        structure_id=structure_id,
                        token=token,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/structures/{structure_id}/')


def get_universe_system_jumps(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed
    ---
    Alternate route: `/latest/universe/system_jumps/`
    Alternate route: `/legacy/universe/system_jumps/`
    Alternate route: `/v1/universe/system_jumps/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/system_jumps/')


def get_universe_system_kills(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed
    ---
    Alternate route: `/latest/universe/system_kills/`
    Alternate route: `/v2/universe/system_kills/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/system_kills/')


def get_universe_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of solar systems
    ---
    Alternate route: `/latest/universe/systems/`
    Alternate route: `/legacy/universe/systems/`
    Alternate route: `/v1/universe/systems/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/systems/')


def get_universe_systems_system_id(*,
                                   language,
                                   system_id,
                                   accept_language='en-us',
                                   if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param system_id: system_id integer
    Get information on a solar system.
    ---
    Alternate route: `/latest/universe/systems/{system_id}/`
    Alternate route: `/v4/universe/systems/{system_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        system_id=system_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/systems/{system_id}/')


def get_universe_types(*, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Get a list of type ids
    ---
    Alternate route: `/latest/universe/types/`
    Alternate route: `/legacy/universe/types/`
    Alternate route: `/v1/universe/types/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/types/')


def get_universe_types_type_id(*,
                               language,
                               type_id,
                               accept_language='en-us',
                               if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param type_id: An Eve item type ID
    Get information on a type
    ---
    Alternate route: `/latest/universe/types/{type_id}/`
    Alternate route: `/v3/universe/types/{type_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        type_id=type_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/universe/types/{type_id}/')


def get_wars(*, max_war_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param max_war_id: Only return wars with ID smaller than this
    Return a list of wars
    ---
    Alternate route: `/latest/wars/`
    Alternate route: `/legacy/wars/`
    Alternate route: `/v1/wars/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        max_war_id=max_war_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/wars/')


def get_wars_war_id(*, war_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param war_id: ID for a war
    Return details about a war
    ---
    Alternate route: `/latest/wars/{war_id}/`
    Alternate route: `/legacy/wars/{war_id}/`
    Alternate route: `/v1/wars/{war_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        war_id=war_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/wars/{war_id}/')


def get_wars_war_id_killmails(*, war_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param war_id: A valid war ID
    Return a list of kills related to a war
    ---
    Alternate route: `/latest/wars/{war_id}/killmails/`
    Alternate route: `/legacy/wars/{war_id}/killmails/`
    Alternate route: `/v1/wars/{war_id}/killmails/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        war_id=war_id,
                        data_source='singularity',
                        version='dev',
                        HTTP_method='GET',
                        path=f'/wars/{war_id}/killmails/')
