# Python EVE Swagger Interface
# https://github.com/nicoscha/PESI
# ESI version 0.8.9
import ESI_request


def get_alliances(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all active player alliances
    ---
    Alternate route: `/dev/alliances/`
    Alternate route: `/latest/alliances/`
    Alternate route: `/legacy/alliances/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/alliances/')


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
    Alternate route: `/legacy/alliances/{alliance_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/alliances/{alliance_id}/contacts/)
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/alliances/{alliance_id}/contacts/labels/`
    Alternate route: `/latest/alliances/{alliance_id}/contacts/labels/`
    Alternate route: `/legacy/alliances/{alliance_id}/contacts/labels/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/alliances/{alliance_id}/contacts/labels/')


def get_alliances_alliance_id_corporations(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all current member corporations of an alliance
    ---
    Alternate route: `/dev/alliances/{alliance_id}/corporations/`
    Alternate route: `/latest/alliances/{alliance_id}/corporations/`
    Alternate route: `/legacy/alliances/{alliance_id}/corporations/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/alliances/{alliance_id}/corporations/')


def get_alliances_alliance_id_icons(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the icon urls for a alliance
    ---
    Alternate route: `/dev/alliances/{alliance_id}/icons/`
    Alternate route: `/latest/alliances/{alliance_id}/icons/`
    Alternate route: `/legacy/alliances/{alliance_id}/icons/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/alliances/{alliance_id}/icons/')


def post_characters_affiliation(*, characters):
    """
    :param characters: The character IDs to fetch affiliations for. All characters must exist, or none will be returned
    Bulk lookup of character IDs to corporation, alliance and faction
    ---
    Alternate route: `/dev/characters/affiliation/`
    Alternate route: `/latest/characters/affiliation/`
    Alternate route: `/legacy/characters/affiliation/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(characters=characters,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/affiliation/')


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
    Alternate route: `/dev/characters/{character_id}/agents_research/`
    Alternate route: `/latest/characters/{character_id}/agents_research/`
    Alternate route: `/legacy/characters/{character_id}/agents_research/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/agents_research/')


def post_characters_character_id_assets_locations(*, character_id, item_ids,
                                                  token):
    """
    :param character_id: An EVE character ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    Alternate route: `/legacy/characters/{character_id}/assets/locations/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#POST-/characters/{character_id}/assets/locations/)
    """
    ESI_request.request(character_id=character_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/assets/locations/')


def post_characters_character_id_assets_names(*, character_id, item_ids,
                                              token):
    """
    :param character_id: An EVE character ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.
    ---
    Alternate route: `/dev/characters/{character_id}/assets/names/`
    Alternate route: `/latest/characters/{character_id}/assets/names/`
    Alternate route: `/legacy/characters/{character_id}/assets/names/`
    
    """
    ESI_request.request(character_id=character_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/attributes/`
    Alternate route: `/latest/characters/{character_id}/attributes/`
    Alternate route: `/legacy/characters/{character_id}/attributes/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/attributes/')


def get_characters_character_id_blueprints(*,
                                           character_id,
                                           token,
                                           if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a list of blueprints the character has
    ---
    Alternate route: `/legacy/characters/{character_id}/blueprints/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/blueprints/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/blueprints/')


def get_characters_character_id_bookmarks(*,
                                          character_id,
                                          token,
                                          if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    List your character's personal bookmarks
    ---
    Alternate route: `/legacy/characters/{character_id}/bookmarks/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/bookmarks/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/bookmarks/')


def get_characters_character_id_bookmarks_folders(*,
                                                  character_id,
                                                  token,
                                                  if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    List your character's personal bookmark folders
    ---
    Alternate route: `/legacy/characters/{character_id}/bookmarks/folders/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/bookmarks/folders/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/calendar/`
    Alternate route: `/latest/characters/{character_id}/calendar/`
    Alternate route: `/legacy/characters/{character_id}/calendar/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        from_event=from_event,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/calendar/')


def get_characters_character_id_calendar_event_id_attendees(
        *, character_id, event_id, token, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param event_id: The id of the event requested
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get all invited attendees for a given event
    ---
    Alternate route: `/dev/characters/{character_id}/calendar/{event_id}/attendees/`
    Alternate route: `/latest/characters/{character_id}/calendar/{event_id}/attendees/`
    Alternate route: `/legacy/characters/{character_id}/calendar/{event_id}/attendees/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        if_none_match=if_none_match,
        token=token,
        data_source='tranquility',
        version='v1',
        path=f'/characters/{character_id}/calendar/{event_id}/attendees/')


def delete_characters_character_id_contacts(*, character_id, contact_ids,
                                            token):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts to delete
    :param token: Access token to use if unable to set a header
    Bulk delete contacts
    ---
    Alternate route: `/legacy/characters/{character_id}/contacts/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#DELETE-/characters/{character_id}/contacts/)
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/legacy/characters/{character_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/contacts/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/contacts/')


def post_characters_character_id_contacts(*, character_id, contact_ids,
                                          label_id, standing, token, watched):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts
    :param label_id: Add a custom label to the new contact
    :param standing: Standing for the contact
    :param token: Access token to use if unable to set a header
    :param watched: Whether the contact should be watched, note this is only effective on characters
    Bulk add contacts with same settings
    ---
    Alternate route: `/legacy/characters/{character_id}/contacts/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#POST-/characters/{character_id}/contacts/)
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_id=label_id,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/contacts/')


def put_characters_character_id_contacts(*, character_id, contact_ids,
                                         label_id, standing, token, watched):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts
    :param label_id: Add a custom label to the contact, use 0 for clearing label
    :param standing: Standing for the contact
    :param token: Access token to use if unable to set a header
    :param watched: Whether the contact should be watched, note this is only effective on characters
    Bulk edit contacts with same settings
    ---
    Alternate route: `/legacy/characters/{character_id}/contacts/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#PUT-/characters/{character_id}/contacts/)
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_id=label_id,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/contacts/labels/`
    Alternate route: `/latest/characters/{character_id}/contacts/labels/`
    Alternate route: `/legacy/characters/{character_id}/contacts/labels/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/contracts/`
    Alternate route: `/latest/characters/{character_id}/contracts/`
    Alternate route: `/legacy/characters/{character_id}/contracts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/contracts/{contract_id}/bids/`
    Alternate route: `/latest/characters/{character_id}/contracts/{contract_id}/bids/`
    Alternate route: `/legacy/characters/{character_id}/contracts/{contract_id}/bids/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(
        character_id=character_id,
        contract_id=contract_id,
        if_none_match=if_none_match,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/contracts/{contract_id}/items/`
    Alternate route: `/latest/characters/{character_id}/contracts/{contract_id}/items/`
    Alternate route: `/legacy/characters/{character_id}/contracts/{contract_id}/items/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        contract_id=contract_id,
        if_none_match=if_none_match,
        token=token,
        data_source='tranquility',
        version='v1',
        path=f'/characters/{character_id}/contracts/{contract_id}/items/')


def get_characters_character_id_corporationhistory(*,
                                                   character_id,
                                                   if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of all the corporations a character has been a member of
    ---
    Alternate route: `/dev/characters/{character_id}/corporationhistory/`
    Alternate route: `/latest/characters/{character_id}/corporationhistory/`
    Alternate route: `/legacy/characters/{character_id}/corporationhistory/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/corporationhistory/')


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
    Alternate route: `/dev/characters/{character_id}/fatigue/`
    Alternate route: `/latest/characters/{character_id}/fatigue/`
    Alternate route: `/legacy/characters/{character_id}/fatigue/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/legacy/characters/{character_id}/fittings/`
    ---
    This route is cached for up to 300 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/fittings/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/fittings/')


def post_characters_character_id_fittings(*, character_id, fitting, token):
    """
    :param character_id: An EVE character ID
    :param fitting: Details about the new fitting
    :param token: Access token to use if unable to set a header
    Save a new fitting for a character
    ---
    Alternate route: `/legacy/characters/{character_id}/fittings/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#POST-/characters/{character_id}/fittings/)
    """
    ESI_request.request(character_id=character_id,
                        fitting=fitting,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/fittings/')


def delete_characters_character_id_fittings_fitting_id(*, character_id,
                                                       fitting_id, token):
    """
    :param character_id: An EVE character ID
    :param fitting_id: ID for a fitting of this character
    :param token: Access token to use if unable to set a header
    Delete a fitting from a character
    ---
    Alternate route: `/dev/characters/{character_id}/fittings/{fitting_id}/`
    Alternate route: `/latest/characters/{character_id}/fittings/{fitting_id}/`
    Alternate route: `/legacy/characters/{character_id}/fittings/{fitting_id}/`
    
    """
    ESI_request.request(
        character_id=character_id,
        fitting_id=fitting_id,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/latest/characters/{character_id}/fleet/`
    Alternate route: `/legacy/characters/{character_id}/fleet/`
    ---
    This route is cached for up to 60 seconds
    ---
    Warning: This route has an upgrade available
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/fleet/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/fw/stats/`
    Alternate route: `/latest/characters/{character_id}/fw/stats/`
    Alternate route: `/legacy/characters/{character_id}/fw/stats/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/implants/`
    Alternate route: `/latest/characters/{character_id}/implants/`
    Alternate route: `/legacy/characters/{character_id}/implants/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/industry/jobs/`
    Alternate route: `/latest/characters/{character_id}/industry/jobs/`
    Alternate route: `/legacy/characters/{character_id}/industry/jobs/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        include_completed=include_completed,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/killmails/recent/`
    Alternate route: `/latest/characters/{character_id}/killmails/recent/`
    Alternate route: `/legacy/characters/{character_id}/killmails/recent/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/location/`
    Alternate route: `/latest/characters/{character_id}/location/`
    Alternate route: `/legacy/characters/{character_id}/location/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/loyalty/points/`
    Alternate route: `/latest/characters/{character_id}/loyalty/points/`
    Alternate route: `/legacy/characters/{character_id}/loyalty/points/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/mail/`
    Alternate route: `/latest/characters/{character_id}/mail/`
    Alternate route: `/legacy/characters/{character_id}/mail/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        labels=labels,
                        last_mail_id=last_mail_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/mail/')


def post_characters_character_id_mail(*, character_id, mail, token):
    """
    :param character_id: An EVE character ID
    :param mail: The mail to send
    :param token: Access token to use if unable to set a header
    Create and send a new mail
    ---
    Alternate route: `/dev/characters/{character_id}/mail/`
    Alternate route: `/latest/characters/{character_id}/mail/`
    Alternate route: `/legacy/characters/{character_id}/mail/`
    
    """
    ESI_request.request(character_id=character_id,
                        mail=mail,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/mail/')


def delete_characters_character_id_mail_labels_label_id(
        *, character_id, label_id, token):
    """
    :param character_id: An EVE character ID
    :param label_id: An EVE label id
    :param token: Access token to use if unable to set a header
    Delete a mail label
    ---
    Alternate route: `/dev/characters/{character_id}/mail/labels/{label_id}/`
    Alternate route: `/latest/characters/{character_id}/mail/labels/{label_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/labels/{label_id}/`
    
    """
    ESI_request.request(
        character_id=character_id,
        label_id=label_id,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/mail/lists/`
    Alternate route: `/latest/characters/{character_id}/mail/lists/`
    Alternate route: `/legacy/characters/{character_id}/mail/lists/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/mail/lists/')


def get_characters_character_id_mail_unread(*,
                                            character_id,
                                            token,
                                            if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return the number of unread mails for the character
    ---
    Alternate route: `/legacy/characters/{character_id}/mail/unread/`
    ---
    This route is cached for up to 5 seconds
    ---
    Warning: This route is deprecated as of 2016-10-10
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/mail/unread/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/mail/unread/')


def delete_characters_character_id_mail_mail_id(*, character_id, mail_id,
                                                token):
    """
    :param character_id: An EVE character ID
    :param mail_id: An EVE mail ID
    :param token: Access token to use if unable to set a header
    Delete a mail
    ---
    Alternate route: `/dev/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/latest/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`
    
    """
    ESI_request.request(character_id=character_id,
                        mail_id=mail_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/latest/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        mail_id=mail_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/latest/characters/{character_id}/mail/{mail_id}/`
    Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`
    
    """
    ESI_request.request(character_id=character_id,
                        contents=contents,
                        mail_id=mail_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/medals/`
    Alternate route: `/latest/characters/{character_id}/medals/`
    Alternate route: `/legacy/characters/{character_id}/medals/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/mining/`
    Alternate route: `/latest/characters/{character_id}/mining/`
    Alternate route: `/legacy/characters/{character_id}/mining/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/mining/')


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
    Alternate route: `/dev/characters/{character_id}/notifications/contacts/`
    Alternate route: `/latest/characters/{character_id}/notifications/contacts/`
    Alternate route: `/legacy/characters/{character_id}/notifications/contacts/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/legacy/characters/{character_id}/online/`
    ---
    This route is cached for up to 60 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/online/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/opportunities/`
    Alternate route: `/latest/characters/{character_id}/opportunities/`
    Alternate route: `/legacy/characters/{character_id}/opportunities/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/opportunities/')


def get_characters_character_id_orders(*,
                                       character_id,
                                       token,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    List market orders placed by a character
    ---
    Alternate route: `/legacy/characters/{character_id}/orders/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/orders/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/orders/history/`
    Alternate route: `/latest/characters/{character_id}/orders/history/`
    Alternate route: `/legacy/characters/{character_id}/orders/history/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/planets/`
    Alternate route: `/latest/characters/{character_id}/planets/`
    Alternate route: `/legacy/characters/{character_id}/planets/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/planets/')


def get_characters_character_id_portrait(*, character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get portrait urls for a character
    ---
    Alternate route: `/legacy/characters/{character_id}/portrait/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated as of 2016-10-01
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/portrait/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/legacy/characters/{character_id}/roles/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/roles/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/roles/')


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
    Alternate route: `/dev/characters/{character_id}/ship/`
    Alternate route: `/latest/characters/{character_id}/ship/`
    Alternate route: `/legacy/characters/{character_id}/ship/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/ship/')


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
    Alternate route: `/dev/characters/{character_id}/standings/`
    Alternate route: `/latest/characters/{character_id}/standings/`
    Alternate route: `/legacy/characters/{character_id}/standings/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/legacy/characters/{character_id}/stats/`
    ---
    This route is cached for up to 86400 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/characters/{character_id}/stats/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/titles/`
    Alternate route: `/latest/characters/{character_id}/titles/`
    Alternate route: `/legacy/characters/{character_id}/titles/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/characters/{character_id}/wallet/`
    Alternate route: `/latest/characters/{character_id}/wallet/`
    Alternate route: `/legacy/characters/{character_id}/wallet/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/characters/{character_id}/wallet/')


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
    Alternate route: `/dev/characters/{character_id}/wallet/transactions/`
    Alternate route: `/latest/characters/{character_id}/wallet/transactions/`
    Alternate route: `/legacy/characters/{character_id}/wallet/transactions/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        from_id=from_id,
        if_none_match=if_none_match,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/contracts/public/bids/{contract_id}/`
    Alternate route: `/latest/contracts/public/bids/{contract_id}/`
    Alternate route: `/legacy/contracts/public/bids/{contract_id}/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(contract_id=contract_id,
                        if_none_match=if_none_match,
                        page=page,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/contracts/public/items/{contract_id}/`
    Alternate route: `/latest/contracts/public/items/{contract_id}/`
    Alternate route: `/legacy/contracts/public/items/{contract_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(contract_id=contract_id,
                        if_none_match=if_none_match,
                        page=page,
                        data_source='tranquility',
                        version='v1',
                        path=f'/contracts/public/items/{contract_id}/')


def get_contracts_public_region_id(*, region_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param region_id: An EVE region id
    Returns a paginated list of all public contracts in the given region
    ---
    Alternate route: `/dev/contracts/public/{region_id}/`
    Alternate route: `/latest/contracts/public/{region_id}/`
    Alternate route: `/legacy/contracts/public/{region_id}/`
    ---
    This route is cached for up to 1800 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        region_id=region_id,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporation/{corporation_id}/mining/extractions/`
    Alternate route: `/latest/corporation/{corporation_id}/mining/extractions/`
    Alternate route: `/legacy/corporation/{corporation_id}/mining/extractions/`
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
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/corporation/{corporation_id}/mining/observers/`
    Alternate route: `/latest/corporation/{corporation_id}/mining/observers/`
    Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/`
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
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/corporation/{corporation_id}/mining/observers/{observer_id}/`
    Alternate route: `/latest/corporation/{corporation_id}/mining/observers/{observer_id}/`
    Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/{observer_id}/`
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
        data_source='tranquility',
        version='v1',
        path=f'/corporation/{corporation_id}/mining/observers/{observer_id}/')


def get_corporations_npccorps(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of npc corporations
    ---
    Alternate route: `/dev/corporations/npccorps/`
    Alternate route: `/latest/corporations/npccorps/`
    Alternate route: `/legacy/corporations/npccorps/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/corporations/npccorps/')


def get_corporations_corporation_id_alliancehistory(*,
                                                    corporation_id,
                                                    if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of all the alliances a corporation has been a member of
    ---
    Alternate route: `/legacy/corporations/{corporation_id}/alliancehistory/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/corporations/{corporation_id}/alliancehistory/)
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        data_source='tranquility',
        version='v1',
        path=f'/corporations/{corporation_id}/alliancehistory/')


def post_corporations_corporation_id_assets_locations(*, corporation_id,
                                                      item_ids, token):
    """
    :param corporation_id: An EVE corporation ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    Alternate route: `/legacy/corporations/{corporation_id}/assets/locations/`
    
    ---
    Requires one of the following EVE corporation role(s): Director
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#POST-/corporations/{corporation_id}/assets/locations/)
    """
    ESI_request.request(
        corporation_id=corporation_id,
        item_ids=item_ids,
        token=token,
        data_source='tranquility',
        version='v1',
        path=f'/corporations/{corporation_id}/assets/locations/')


def post_corporations_corporation_id_assets_names(*, corporation_id, item_ids,
                                                  token):
    """
    :param corporation_id: An EVE corporation ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships
    ---
    Alternate route: `/dev/corporations/{corporation_id}/assets/names/`
    Alternate route: `/latest/corporations/{corporation_id}/assets/names/`
    Alternate route: `/legacy/corporations/{corporation_id}/assets/names/`
    
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/legacy/corporations/{corporation_id}/blueprints/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/corporations/{corporation_id}/blueprints/)
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/bookmarks/`
    Alternate route: `/latest/corporations/{corporation_id}/bookmarks/`
    Alternate route: `/legacy/corporations/{corporation_id}/bookmarks/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/bookmarks/folders/`
    Alternate route: `/latest/corporations/{corporation_id}/bookmarks/folders/`
    Alternate route: `/legacy/corporations/{corporation_id}/bookmarks/folders/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/legacy/corporations/{corporation_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/corporations/{corporation_id}/contacts/)
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/contacts/labels/`
    Alternate route: `/latest/corporations/{corporation_id}/contacts/labels/`
    Alternate route: `/legacy/corporations/{corporation_id}/contacts/labels/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/legacy/corporations/{corporation_id}/containers/logs/`
    ---
    This route is cached for up to 600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/corporations/{corporation_id}/containers/logs/)
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/contracts/`
    Alternate route: `/latest/corporations/{corporation_id}/contracts/`
    Alternate route: `/legacy/corporations/{corporation_id}/contracts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/contracts/{contract_id}/bids/`
    Alternate route: `/latest/corporations/{corporation_id}/contracts/{contract_id}/bids/`
    Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/bids/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        contract_id=contract_id,
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/contracts/{contract_id}/items/`
    Alternate route: `/latest/corporations/{corporation_id}/contracts/{contract_id}/items/`
    Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/items/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        contract_id=contract_id,
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/customs_offices/`
    Alternate route: `/latest/corporations/{corporation_id}/customs_offices/`
    Alternate route: `/legacy/corporations/{corporation_id}/customs_offices/`
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
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/divisions/`
    Alternate route: `/latest/corporations/{corporation_id}/divisions/`
    Alternate route: `/legacy/corporations/{corporation_id}/divisions/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/facilities/`
    Alternate route: `/latest/corporations/{corporation_id}/facilities/`
    Alternate route: `/legacy/corporations/{corporation_id}/facilities/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Factory_Manager
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/fw/stats/`
    Alternate route: `/latest/corporations/{corporation_id}/fw/stats/`
    Alternate route: `/legacy/corporations/{corporation_id}/fw/stats/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/corporations/{corporation_id}/fw/stats/')


def get_corporations_corporation_id_icons(*,
                                          corporation_id,
                                          if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the icon urls for a corporation
    ---
    Alternate route: `/dev/corporations/{corporation_id}/icons/`
    Alternate route: `/latest/corporations/{corporation_id}/icons/`
    Alternate route: `/legacy/corporations/{corporation_id}/icons/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/industry/jobs/`
    Alternate route: `/latest/corporations/{corporation_id}/industry/jobs/`
    Alternate route: `/legacy/corporations/{corporation_id}/industry/jobs/`
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
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/killmails/recent/`
    Alternate route: `/latest/corporations/{corporation_id}/killmails/recent/`
    Alternate route: `/legacy/corporations/{corporation_id}/killmails/recent/`
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
        data_source='tranquility',
        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/medals/`
    Alternate route: `/latest/corporations/{corporation_id}/medals/`
    Alternate route: `/legacy/corporations/{corporation_id}/medals/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/medals/issued/`
    Alternate route: `/latest/corporations/{corporation_id}/medals/issued/`
    Alternate route: `/legacy/corporations/{corporation_id}/medals/issued/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/corporations/{corporation_id}/medals/issued/')


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
    Alternate route: `/dev/corporations/{corporation_id}/members/limit/`
    Alternate route: `/latest/corporations/{corporation_id}/members/limit/`
    Alternate route: `/legacy/corporations/{corporation_id}/members/limit/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/members/titles/`
    Alternate route: `/latest/corporations/{corporation_id}/members/titles/`
    Alternate route: `/legacy/corporations/{corporation_id}/members/titles/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/membertracking/`
    Alternate route: `/latest/corporations/{corporation_id}/membertracking/`
    Alternate route: `/legacy/corporations/{corporation_id}/membertracking/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/corporations/{corporation_id}/membertracking/')


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
    Alternate route: `/legacy/corporations/{corporation_id}/orders/history/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Trader
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/corporations/{corporation_id}/orders/history/)
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/roles/`
    Alternate route: `/latest/corporations/{corporation_id}/roles/`
    Alternate route: `/legacy/corporations/{corporation_id}/roles/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/roles/history/`
    Alternate route: `/latest/corporations/{corporation_id}/roles/history/`
    Alternate route: `/legacy/corporations/{corporation_id}/roles/history/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/shareholders/`
    Alternate route: `/latest/corporations/{corporation_id}/shareholders/`
    Alternate route: `/legacy/corporations/{corporation_id}/shareholders/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/standings/`
    Alternate route: `/latest/corporations/{corporation_id}/standings/`
    Alternate route: `/legacy/corporations/{corporation_id}/standings/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/starbases/`
    Alternate route: `/latest/corporations/{corporation_id}/starbases/`
    Alternate route: `/legacy/corporations/{corporation_id}/starbases/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/starbases/{starbase_id}/`
    Alternate route: `/latest/corporations/{corporation_id}/starbases/{starbase_id}/`
    Alternate route: `/legacy/corporations/{corporation_id}/starbases/{starbase_id}/`
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
        data_source='tranquility',
        version='v1',
        path=f'/corporations/{corporation_id}/starbases/{starbase_id}/')


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
    Alternate route: `/dev/corporations/{corporation_id}/titles/`
    Alternate route: `/latest/corporations/{corporation_id}/titles/`
    Alternate route: `/legacy/corporations/{corporation_id}/titles/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/corporations/{corporation_id}/wallets/`
    Alternate route: `/latest/corporations/{corporation_id}/wallets/`
    Alternate route: `/legacy/corporations/{corporation_id}/wallets/`
    ---
    This route is cached for up to 300 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
    
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/corporations/{corporation_id}/wallets/')


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
    Alternate route: `/dev/corporations/{corporation_id}/wallets/{division}/transactions/`
    Alternate route: `/latest/corporations/{corporation_id}/wallets/{division}/transactions/`
    Alternate route: `/legacy/corporations/{corporation_id}/wallets/{division}/transactions/`
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
        data_source='tranquility',
        version='v1',
        path=f'/corporations/{corporation_id}/wallets/{division}/transactions/'
    )


def get_dogma_attributes(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of dogma attribute ids
    ---
    Alternate route: `/dev/dogma/attributes/`
    Alternate route: `/latest/dogma/attributes/`
    Alternate route: `/legacy/dogma/attributes/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/dogma/attributes/')


def get_dogma_attributes_attribute_id(*, attribute_id, if_none_match=None):
    """
    :param attribute_id: A dogma attribute ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a dogma attribute
    ---
    Alternate route: `/dev/dogma/attributes/{attribute_id}/`
    Alternate route: `/latest/dogma/attributes/{attribute_id}/`
    Alternate route: `/legacy/dogma/attributes/{attribute_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(attribute_id=attribute_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/dogma/dynamic/items/{type_id}/{item_id}/`
    Alternate route: `/latest/dogma/dynamic/items/{type_id}/{item_id}/`
    Alternate route: `/legacy/dogma/dynamic/items/{type_id}/{item_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        item_id=item_id,
                        type_id=type_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/dogma/dynamic/items/{type_id}/{item_id}/')


def get_dogma_effects(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of dogma effect ids
    ---
    Alternate route: `/dev/dogma/effects/`
    Alternate route: `/latest/dogma/effects/`
    Alternate route: `/legacy/dogma/effects/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/dogma/effects/')


def get_dogma_effects_effect_id(*, effect_id, if_none_match=None):
    """
    :param effect_id: A dogma effect ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a dogma effect
    ---
    Alternate route: `/legacy/dogma/effects/{effect_id}/`
    ---
    This route expires daily at 11:05
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/dogma/effects/{effect_id}/)
    """
    ESI_request.request(effect_id=effect_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/dogma/effects/{effect_id}/')


def get_fleets_fleet_id(*, fleet_id, token, if_none_match=None):
    """
    :param fleet_id: ID for a fleet
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return details about a fleet
    ---
    Alternate route: `/dev/fleets/{fleet_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/')


def put_fleets_fleet_id(*, fleet_id, new_settings, token):
    """
    :param fleet_id: ID for a fleet
    :param new_settings: What to update for this fleet
    :param token: Access token to use if unable to set a header
    Update settings about a fleet
    ---
    Alternate route: `/dev/fleets/{fleet_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        new_settings=new_settings,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/fleets/{fleet_id}/members/`
    Alternate route: `/latest/fleets/{fleet_id}/members/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        language=language,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/members/')


def post_fleets_fleet_id_members(*, fleet_id, invitation, token):
    """
    :param fleet_id: ID for a fleet
    :param invitation: Details of the invitation
    :param token: Access token to use if unable to set a header
    Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI
    ---
    Alternate route: `/dev/fleets/{fleet_id}/members/`
    Alternate route: `/latest/fleets/{fleet_id}/members/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        invitation=invitation,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/members/')


def delete_fleets_fleet_id_members_member_id(*, fleet_id, member_id, token):
    """
    :param fleet_id: ID for a fleet
    :param member_id: The character ID of a member in this fleet
    :param token: Access token to use if unable to set a header
    Kick a fleet member
    ---
    Alternate route: `/dev/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        member_id=member_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/members/{member_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        member_id=member_id,
                        movement=movement,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/members/{member_id}/')


def delete_fleets_fleet_id_squads_squad_id(*, fleet_id, squad_id, token):
    """
    :param fleet_id: ID for a fleet
    :param squad_id: The squad to delete
    :param token: Access token to use if unable to set a header
    Delete a fleet squad, only empty squads can be deleted
    ---
    Alternate route: `/dev/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        squad_id=squad_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/squads/{squad_id}/')


def put_fleets_fleet_id_squads_squad_id(*, fleet_id, naming, squad_id, token):
    """
    :param fleet_id: ID for a fleet
    :param naming: New name of the squad
    :param squad_id: The squad to rename
    :param token: Access token to use if unable to set a header
    Rename a fleet squad
    ---
    Alternate route: `/dev/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/squads/{squad_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        naming=naming,
                        squad_id=squad_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/fleets/{fleet_id}/wings/`
    Alternate route: `/latest/fleets/{fleet_id}/wings/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        language=language,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/wings/')


def post_fleets_fleet_id_wings(*, fleet_id, token):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    Create a new wing in a fleet
    ---
    Alternate route: `/dev/fleets/{fleet_id}/wings/`
    Alternate route: `/latest/fleets/{fleet_id}/wings/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/wings/')


def delete_fleets_fleet_id_wings_wing_id(*, fleet_id, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing to delete
    Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty
    ---
    Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        wing_id=wing_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/wings/{wing_id}/')


def put_fleets_fleet_id_wings_wing_id(*, fleet_id, naming, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param naming: New name of the wing
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing to rename
    Rename a fleet wing
    ---
    Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/latest/fleets/{fleet_id}/wings/{wing_id}/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        naming=naming,
                        token=token,
                        wing_id=wing_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/wings/{wing_id}/')


def post_fleets_fleet_id_wings_wing_id_squads(*, fleet_id, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing_id to create squad in
    Create a new squad in a fleet
    ---
    Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/squads/`
    Alternate route: `/latest/fleets/{fleet_id}/wings/{wing_id}/squads/`
    Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/squads/`
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        wing_id=wing_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fleets/{fleet_id}/wings/{wing_id}/squads/')


def get_fw_leaderboards(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday
    ---
    Alternate route: `/dev/fw/leaderboards/`
    Alternate route: `/latest/fw/leaderboards/`
    Alternate route: `/legacy/fw/leaderboards/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fw/leaderboards/')


def get_fw_leaderboards_characters(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday
    ---
    Alternate route: `/dev/fw/leaderboards/characters/`
    Alternate route: `/latest/fw/leaderboards/characters/`
    Alternate route: `/legacy/fw/leaderboards/characters/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fw/leaderboards/characters/')


def get_fw_leaderboards_corporations(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday
    ---
    Alternate route: `/dev/fw/leaderboards/corporations/`
    Alternate route: `/latest/fw/leaderboards/corporations/`
    Alternate route: `/legacy/fw/leaderboards/corporations/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fw/leaderboards/corporations/')


def get_fw_stats(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Statistical overviews of factions involved in faction warfare
    ---
    Alternate route: `/dev/fw/stats/`
    Alternate route: `/latest/fw/stats/`
    Alternate route: `/legacy/fw/stats/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fw/stats/')


def get_fw_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    An overview of the current ownership of faction warfare solar systems
    ---
    Alternate route: `/legacy/fw/systems/`
    ---
    This route is cached for up to 1800 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/fw/systems/)
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fw/systems/')


def get_fw_wars(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Data about which NPC factions are at war
    ---
    Alternate route: `/dev/fw/wars/`
    Alternate route: `/latest/fw/wars/`
    Alternate route: `/legacy/fw/wars/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/fw/wars/')


def get_incursions(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of current incursions
    ---
    Alternate route: `/dev/incursions/`
    Alternate route: `/latest/incursions/`
    Alternate route: `/legacy/incursions/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/incursions/')


def get_industry_facilities(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of industry facilities
    ---
    Alternate route: `/dev/industry/facilities/`
    Alternate route: `/latest/industry/facilities/`
    Alternate route: `/legacy/industry/facilities/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/industry/facilities/')


def get_industry_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return cost indices for solar systems
    ---
    Alternate route: `/dev/industry/systems/`
    Alternate route: `/latest/industry/systems/`
    Alternate route: `/legacy/industry/systems/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/insurance/prices/`
    Alternate route: `/latest/insurance/prices/`
    Alternate route: `/legacy/insurance/prices/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/killmails/{killmail_id}/{killmail_hash}/`
    Alternate route: `/latest/killmails/{killmail_id}/{killmail_hash}/`
    Alternate route: `/legacy/killmails/{killmail_id}/{killmail_hash}/`
    ---
    This route is cached for up to 1209600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        killmail_hash=killmail_hash,
                        killmail_id=killmail_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/killmails/{killmail_id}/{killmail_hash}/')


def get_loyalty_stores_corporation_id_offers(*,
                                             corporation_id,
                                             if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of offers from a specific corporation's loyalty store
    ---
    Alternate route: `/dev/loyalty/stores/{corporation_id}/offers/`
    Alternate route: `/latest/loyalty/stores/{corporation_id}/offers/`
    Alternate route: `/legacy/loyalty/stores/{corporation_id}/offers/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/loyalty/stores/{corporation_id}/offers/')


def get_markets_groups(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of item groups
    ---
    Alternate route: `/dev/markets/groups/`
    Alternate route: `/latest/markets/groups/`
    Alternate route: `/legacy/markets/groups/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/markets/groups/{market_group_id}/`
    Alternate route: `/latest/markets/groups/{market_group_id}/`
    Alternate route: `/legacy/markets/groups/{market_group_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        market_group_id=market_group_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/markets/groups/{market_group_id}/')


def get_markets_prices(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of prices
    ---
    Alternate route: `/dev/markets/prices/`
    Alternate route: `/latest/markets/prices/`
    Alternate route: `/legacy/markets/prices/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/markets/structures/{structure_id}/`
    Alternate route: `/latest/markets/structures/{structure_id}/`
    Alternate route: `/legacy/markets/structures/{structure_id}/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        structure_id=structure_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/markets/structures/{structure_id}/')


def get_markets_region_id_history(*, region_id, type_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param region_id: Return statistics in this region
    :param type_id: Return statistics for this type
    Return a list of historical market statistics for the specified type in a region
    ---
    Alternate route: `/dev/markets/{region_id}/history/`
    Alternate route: `/latest/markets/{region_id}/history/`
    Alternate route: `/legacy/markets/{region_id}/history/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        region_id=region_id,
                        type_id=type_id,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/markets/{region_id}/orders/`
    Alternate route: `/latest/markets/{region_id}/orders/`
    Alternate route: `/legacy/markets/{region_id}/orders/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        order_type=order_type,
                        page=page,
                        region_id=region_id,
                        type_id=type_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/markets/{region_id}/orders/')


def get_markets_region_id_types(*, region_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param region_id: Return statistics in this region
    Return a list of type IDs that have active orders in the region, for efficient market indexing.
    ---
    Alternate route: `/dev/markets/{region_id}/types/`
    Alternate route: `/latest/markets/{region_id}/types/`
    Alternate route: `/legacy/markets/{region_id}/types/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        region_id=region_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/markets/{region_id}/types/')


def get_opportunities_groups(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of opportunities groups
    ---
    Alternate route: `/dev/opportunities/groups/`
    Alternate route: `/latest/opportunities/groups/`
    Alternate route: `/legacy/opportunities/groups/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/opportunities/groups/{group_id}/`
    Alternate route: `/latest/opportunities/groups/{group_id}/`
    Alternate route: `/legacy/opportunities/groups/{group_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        group_id=group_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
                        path=f'/opportunities/groups/{group_id}/')


def get_opportunities_tasks(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of opportunities tasks
    ---
    Alternate route: `/dev/opportunities/tasks/`
    Alternate route: `/latest/opportunities/tasks/`
    Alternate route: `/legacy/opportunities/tasks/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/opportunities/tasks/')


def get_opportunities_tasks_task_id(*, task_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param task_id: ID of an opportunities task
    Return information of an opportunities task
    ---
    Alternate route: `/dev/opportunities/tasks/{task_id}/`
    Alternate route: `/latest/opportunities/tasks/{task_id}/`
    Alternate route: `/legacy/opportunities/tasks/{task_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        task_id=task_id,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/route/{origin}/{destination}/`
    Alternate route: `/latest/route/{origin}/{destination}/`
    Alternate route: `/legacy/route/{origin}/{destination}/`
    ---
    This route is cached for up to 86400 seconds
    """
    ESI_request.request(avoid=avoid,
                        connections=connections,
                        destination=destination,
                        flag=flag,
                        if_none_match=if_none_match,
                        origin=origin,
                        data_source='tranquility',
                        version='v1',
                        path=f'/route/{origin}/{destination}/')


def get_sovereignty_campaigns(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty data for campaigns.
    ---
    Alternate route: `/dev/sovereignty/campaigns/`
    Alternate route: `/latest/sovereignty/campaigns/`
    Alternate route: `/legacy/sovereignty/campaigns/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/sovereignty/campaigns/')


def get_sovereignty_map(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty information for solar systems
    ---
    Alternate route: `/dev/sovereignty/map/`
    Alternate route: `/latest/sovereignty/map/`
    Alternate route: `/legacy/sovereignty/map/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/sovereignty/map/')


def get_sovereignty_structures(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty data for structures.
    ---
    Alternate route: `/dev/sovereignty/structures/`
    Alternate route: `/latest/sovereignty/structures/`
    Alternate route: `/legacy/sovereignty/structures/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/sovereignty/structures/')


def get_status(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    EVE Server status
    ---
    Alternate route: `/dev/status/`
    Alternate route: `/latest/status/`
    Alternate route: `/legacy/status/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/status/')


def post_ui_openwindow_contract(*, contract_id, token):
    """
    :param contract_id: The contract to open
    :param token: Access token to use if unable to set a header
    Open the contract window inside the client
    ---
    Alternate route: `/dev/ui/openwindow/contract/`
    Alternate route: `/latest/ui/openwindow/contract/`
    Alternate route: `/legacy/ui/openwindow/contract/`
    
    """
    ESI_request.request(contract_id=contract_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/ui/openwindow/contract/')


def post_ui_openwindow_information(*, target_id, token):
    """
    :param target_id: The target to open
    :param token: Access token to use if unable to set a header
    Open the information window for a character, corporation or alliance inside the client
    ---
    Alternate route: `/dev/ui/openwindow/information/`
    Alternate route: `/latest/ui/openwindow/information/`
    Alternate route: `/legacy/ui/openwindow/information/`
    
    """
    ESI_request.request(target_id=target_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/ui/openwindow/information/')


def post_ui_openwindow_marketdetails(*, token, type_id):
    """
    :param token: Access token to use if unable to set a header
    :param type_id: The item type to open in market window
    Open the market details window for a specific typeID inside the client
    ---
    Alternate route: `/dev/ui/openwindow/marketdetails/`
    Alternate route: `/latest/ui/openwindow/marketdetails/`
    Alternate route: `/legacy/ui/openwindow/marketdetails/`
    
    """
    ESI_request.request(token=token,
                        type_id=type_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/ui/openwindow/marketdetails/')


def post_ui_openwindow_newmail(*, new_mail, token):
    """
    :param new_mail: The details of mail to create
    :param token: Access token to use if unable to set a header
    Open the New Mail window, according to settings from the request if applicable
    ---
    Alternate route: `/dev/ui/openwindow/newmail/`
    Alternate route: `/latest/ui/openwindow/newmail/`
    Alternate route: `/legacy/ui/openwindow/newmail/`
    
    """
    ESI_request.request(new_mail=new_mail,
                        token=token,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/universe/ancestries/`
    Alternate route: `/latest/universe/ancestries/`
    Alternate route: `/legacy/universe/ancestries/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/ancestries/')


def get_universe_asteroid_belts_asteroid_belt_id(*,
                                                 asteroid_belt_id,
                                                 if_none_match=None):
    """
    :param asteroid_belt_id: asteroid_belt_id integer
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on an asteroid belt
    ---
    Alternate route: `/dev/universe/asteroid_belts/{asteroid_belt_id}/`
    Alternate route: `/latest/universe/asteroid_belts/{asteroid_belt_id}/`
    Alternate route: `/legacy/universe/asteroid_belts/{asteroid_belt_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(asteroid_belt_id=asteroid_belt_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/universe/bloodlines/`
    Alternate route: `/latest/universe/bloodlines/`
    Alternate route: `/legacy/universe/bloodlines/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/bloodlines/')


def get_universe_categories(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of item categories
    ---
    Alternate route: `/dev/universe/categories/`
    Alternate route: `/latest/universe/categories/`
    Alternate route: `/legacy/universe/categories/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/universe/categories/{category_id}/`
    Alternate route: `/latest/universe/categories/{category_id}/`
    Alternate route: `/legacy/universe/categories/{category_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        category_id=category_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/categories/{category_id}/')


def get_universe_constellations(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of constellations
    ---
    Alternate route: `/dev/universe/constellations/`
    Alternate route: `/latest/universe/constellations/`
    Alternate route: `/legacy/universe/constellations/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/universe/constellations/{constellation_id}/`
    Alternate route: `/latest/universe/constellations/{constellation_id}/`
    Alternate route: `/legacy/universe/constellations/{constellation_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        constellation_id=constellation_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/legacy/universe/factions/`
    ---
    This route expires daily at 11:05
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/universe/factions/)
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/factions/')


def get_universe_graphics(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of graphics
    ---
    Alternate route: `/dev/universe/graphics/`
    Alternate route: `/latest/universe/graphics/`
    Alternate route: `/legacy/universe/graphics/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/graphics/')


def get_universe_graphics_graphic_id(*, graphic_id, if_none_match=None):
    """
    :param graphic_id: graphic_id integer
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a graphic
    ---
    Alternate route: `/dev/universe/graphics/{graphic_id}/`
    Alternate route: `/latest/universe/graphics/{graphic_id}/`
    Alternate route: `/legacy/universe/graphics/{graphic_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(graphic_id=graphic_id,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/graphics/{graphic_id}/')


def get_universe_groups(*, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Get a list of item groups
    ---
    Alternate route: `/dev/universe/groups/`
    Alternate route: `/latest/universe/groups/`
    Alternate route: `/legacy/universe/groups/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/universe/groups/{group_id}/`
    Alternate route: `/latest/universe/groups/{group_id}/`
    Alternate route: `/legacy/universe/groups/{group_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        group_id=group_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/groups/{group_id}/')


def post_universe_ids(*, language, names, accept_language='en-us'):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param names: The names to resolve
    Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours
    ---
    Alternate route: `/dev/universe/ids/`
    Alternate route: `/latest/universe/ids/`
    Alternate route: `/legacy/universe/ids/`
    
    """
    ESI_request.request(accept_language=accept_language,
                        language=language,
                        names=names,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/ids/')


def get_universe_moons_moon_id(*, moon_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param moon_id: moon_id integer
    Get information on a moon
    ---
    Alternate route: `/dev/universe/moons/{moon_id}/`
    Alternate route: `/latest/universe/moons/{moon_id}/`
    Alternate route: `/legacy/universe/moons/{moon_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        moon_id=moon_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/moons/{moon_id}/')


def get_universe_planets_planet_id(*, planet_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param planet_id: planet_id integer
    Get information on a planet
    ---
    Alternate route: `/dev/universe/planets/{planet_id}/`
    Alternate route: `/latest/universe/planets/{planet_id}/`
    Alternate route: `/legacy/universe/planets/{planet_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        planet_id=planet_id,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/universe/races/`
    Alternate route: `/latest/universe/races/`
    Alternate route: `/legacy/universe/races/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/races/')


def get_universe_regions(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of regions
    ---
    Alternate route: `/dev/universe/regions/`
    Alternate route: `/latest/universe/regions/`
    Alternate route: `/legacy/universe/regions/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
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
    Alternate route: `/dev/universe/regions/{region_id}/`
    Alternate route: `/latest/universe/regions/{region_id}/`
    Alternate route: `/legacy/universe/regions/{region_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        region_id=region_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/regions/{region_id}/')


def get_universe_schematics_schematic_id(*, schematic_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param schematic_id: A PI schematic ID
    Get information on a planetary factory schematic
    ---
    Alternate route: `/dev/universe/schematics/{schematic_id}/`
    Alternate route: `/latest/universe/schematics/{schematic_id}/`
    Alternate route: `/legacy/universe/schematics/{schematic_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        schematic_id=schematic_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/schematics/{schematic_id}/')


def get_universe_stargates_stargate_id(*, stargate_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param stargate_id: stargate_id integer
    Get information on a stargate
    ---
    Alternate route: `/dev/universe/stargates/{stargate_id}/`
    Alternate route: `/latest/universe/stargates/{stargate_id}/`
    Alternate route: `/legacy/universe/stargates/{stargate_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        stargate_id=stargate_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/stargates/{stargate_id}/')


def get_universe_stars_star_id(*, star_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param star_id: star_id integer
    Get information on a star
    ---
    Alternate route: `/dev/universe/stars/{star_id}/`
    Alternate route: `/latest/universe/stars/{star_id}/`
    Alternate route: `/legacy/universe/stars/{star_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        star_id=star_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/stars/{star_id}/')


def get_universe_stations_station_id(*, station_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param station_id: An Eve station ID
    Public information on stations
    ---
    Alternate route: `/legacy/universe/stations/{station_id}/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/universe/stations/{station_id}/)
    """
    ESI_request.request(if_none_match=if_none_match,
                        station_id=station_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/stations/{station_id}/')


def get_universe_structures(*, filter, if_none_match=None):
    """
    :param filter: ['market', 'manufacturing_basic'] Only list public structures that have this service online
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all public structures
    ---
    Alternate route: `/dev/universe/structures/`
    Alternate route: `/latest/universe/structures/`
    Alternate route: `/legacy/universe/structures/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(filter=filter,
                        if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/structures/')


def get_universe_structures_structure_id(*,
                                         structure_id,
                                         token,
                                         if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param structure_id: An Eve structure ID
    :param token: Access token to use if unable to set a header
    Returns information on requested structure, if you are on the ACL. Otherwise, returns "Forbidden" for all inputs.
    ---
    Alternate route: `/legacy/universe/structures/{structure_id}/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/universe/structures/{structure_id}/)
    """
    ESI_request.request(if_none_match=if_none_match,
                        structure_id=structure_id,
                        token=token,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/structures/{structure_id}/')


def get_universe_system_jumps(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed
    ---
    Alternate route: `/dev/universe/system_jumps/`
    Alternate route: `/latest/universe/system_jumps/`
    Alternate route: `/legacy/universe/system_jumps/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/system_jumps/')


def get_universe_system_kills(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed
    ---
    Alternate route: `/legacy/universe/system_kills/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v1/dev/#GET-/universe/system_kills/)
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/system_kills/')


def get_universe_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of solar systems
    ---
    Alternate route: `/dev/universe/systems/`
    Alternate route: `/latest/universe/systems/`
    Alternate route: `/legacy/universe/systems/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/systems/')


def get_universe_types(*, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Get a list of type ids
    ---
    Alternate route: `/dev/universe/types/`
    Alternate route: `/latest/universe/types/`
    Alternate route: `/legacy/universe/types/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        data_source='tranquility',
                        version='v1',
                        path=f'/universe/types/')


def get_wars(*, max_war_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param max_war_id: Only return wars with ID smaller than this
    Return a list of wars
    ---
    Alternate route: `/dev/wars/`
    Alternate route: `/latest/wars/`
    Alternate route: `/legacy/wars/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        max_war_id=max_war_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/wars/')


def get_wars_war_id(*, war_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param war_id: ID for a war
    Return details about a war
    ---
    Alternate route: `/dev/wars/{war_id}/`
    Alternate route: `/latest/wars/{war_id}/`
    Alternate route: `/legacy/wars/{war_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        war_id=war_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/wars/{war_id}/')


def get_wars_war_id_killmails(*, war_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param war_id: A valid war ID
    Return a list of kills related to a war
    ---
    Alternate route: `/dev/wars/{war_id}/killmails/`
    Alternate route: `/latest/wars/{war_id}/killmails/`
    Alternate route: `/legacy/wars/{war_id}/killmails/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        war_id=war_id,
                        data_source='tranquility',
                        version='v1',
                        path=f'/wars/{war_id}/killmails/')
