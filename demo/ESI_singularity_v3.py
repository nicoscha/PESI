import ESI_request


def get_alliances_alliance_id(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about an alliance
    ---
    Alternate route: `/dev/alliances/{alliance_id}/`
    Alternate route: `/latest/alliances/{alliance_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v3',
                        path=f'/alliances/{alliance_id}/')


def get_characters_character_id(*, character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a character
    ---
    Alternate route: `/legacy/characters/{character_id}/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v3/dev/#GET-/characters/{character_id}/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v3',
                        path=f'/characters/{character_id}/')


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
    Alternate route: `/dev/characters/{character_id}/assets/`
    Alternate route: `/latest/characters/{character_id}/assets/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v3',
                        path=f'/characters/{character_id}/assets/')


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
    Alternate route: `/dev/characters/{character_id}/calendar/{event_id}/`
    Alternate route: `/latest/characters/{character_id}/calendar/{event_id}/`
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='v3',
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
    Alternate route: `/dev/characters/{character_id}/calendar/{event_id}/`
    Alternate route: `/latest/characters/{character_id}/calendar/{event_id}/`
    
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        response=response,
        token=token,
        data_source='singularity',
        version='v3',
        path=f'/characters/{character_id}/calendar/{event_id}/')


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
    Alternate route: `/dev/characters/{character_id}/clones/`
    Alternate route: `/latest/characters/{character_id}/clones/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v3',
                        path=f'/characters/{character_id}/clones/')


def post_characters_character_id_cspa(*, character_id, characters, token):
    """
    :param character_id: An EVE character ID
    :param characters: The target characters to calculate the charge for
    :param token: Access token to use if unable to set a header
    Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost
    ---
    Alternate route: `/legacy/characters/{character_id}/cspa/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v3/dev/#POST-/characters/{character_id}/cspa/)
    """
    ESI_request.request(character_id=character_id,
                        characters=characters,
                        token=token,
                        data_source='singularity',
                        version='v3',
                        path=f'/characters/{character_id}/cspa/')


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
    Alternate route: `/dev/characters/{character_id}/mail/labels/`
    Alternate route: `/latest/characters/{character_id}/mail/labels/`
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v3',
                        path=f'/characters/{character_id}/mail/labels/')


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
    Alternate route: `/dev/characters/{character_id}/online/`
    ---
    This route is cached for up to 60 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v3',
                        path=f'/characters/{character_id}/online/')


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
    Alternate route: `/dev/characters/{character_id}/planets/{planet_id}/`
    Alternate route: `/latest/characters/{character_id}/planets/{planet_id}/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        planet_id=planet_id,
        token=token,
        data_source='singularity',
        version='v3',
        path=f'/characters/{character_id}/planets/{planet_id}/')


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
    Alternate route: `/dev/characters/{character_id}/search/`
    Alternate route: `/latest/characters/{character_id}/search/`
    Alternate route: `/legacy/characters/{character_id}/search/`
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
                        version='v3',
                        path=f'/characters/{character_id}/search/')


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
    Alternate route: `/legacy/characters/{character_id}/skills/`
    ---
    This route is cached for up to 120 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v3/dev/#GET-/characters/{character_id}/skills/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v3',
                        path=f'/characters/{character_id}/skills/')


def get_corporations_corporation_id(*, corporation_id, if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a corporation
    ---
    Alternate route: `/legacy/corporations/{corporation_id}/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v3/dev/#GET-/corporations/{corporation_id}/)
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v3',
                        path=f'/corporations/{corporation_id}/')


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
    Alternate route: `/dev/corporations/{corporation_id}/assets/`
    Alternate route: `/latest/corporations/{corporation_id}/assets/`
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
                        version='v3',
                        path=f'/corporations/{corporation_id}/assets/')


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
    Alternate route: `/dev/corporations/{corporation_id}/members/`
    Alternate route: `/latest/corporations/{corporation_id}/members/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v3',
                        path=f'/corporations/{corporation_id}/members/')


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
    Alternate route: `/dev/corporations/{corporation_id}/orders/`
    Alternate route: `/latest/corporations/{corporation_id}/orders/`
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
                        version='v3',
                        path=f'/corporations/{corporation_id}/orders/')


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
    Alternate route: `/dev/corporations/{corporation_id}/structures/`
    Alternate route: `/latest/corporations/{corporation_id}/structures/`
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
                        version='v3',
                        path=f'/corporations/{corporation_id}/structures/')


def get_corporations_corporation_id_wallets_division_journal(
        *, corporation_id, division, token, if_none_match=None, page='1'):
    """
    :param corporation_id: An EVE corporation ID
    :param division: Wallet key of the division to fetch journals from
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Retrieve the given corporation's wallet journal for the given division going 30 days back. Note: any journal records having to do with the new navigation structures from the release of Onslaught will not show up in this version. To see those, use the v4 version of this route.
    ---
    Alternate route: `/legacy/corporations/{corporation_id}/wallets/{division}/journal/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v3/dev/#GET-/corporations/{corporation_id}/wallets/{division}/journal/)
    """
    ESI_request.request(
        corporation_id=corporation_id,
        division=division,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='v3',
        path=f'/corporations/{corporation_id}/wallets/{division}/journal/')


def post_universe_names(*, ids):
    """
    :param ids: The ids to resolve
    Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions
    ---
    Alternate route: `/dev/universe/names/`
    Alternate route: `/latest/universe/names/`
    
    """
    ESI_request.request(ids=ids,
                        data_source='singularity',
                        version='v3',
                        path=f'/universe/names/')


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
    Get information on a solar system. NOTE: This route does not work with abyssal systems.
    ---
    Alternate route: `/legacy/universe/systems/{system_id}/`
    ---
    This route expires daily at 11:05
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v3/dev/#GET-/universe/systems/{system_id}/)
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        system_id=system_id,
                        data_source='singularity',
                        version='v3',
                        path=f'/universe/systems/{system_id}/')


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
    Alternate route: `/dev/universe/types/{type_id}/`
    Alternate route: `/latest/universe/types/{type_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        type_id=type_id,
                        data_source='singularity',
                        version='v3',
                        path=f'/universe/types/{type_id}/')
