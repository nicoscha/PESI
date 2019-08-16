import ESI_request


def get_characters_character_id(character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a character
    ---
    Alternate route: `/dev/characters/{character_id}/`
    Alternate route: `/latest/characters/{character_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v4',
                        path=f'/characters/{character_id}/')


def post_characters_character_id_cspa(token, characters, character_id):
    """
    :param character_id: An EVE character ID
    :param characters: The target characters to calculate the charge for
    :param token: Access token to use if unable to set a header
    Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost
    ---
    Alternate route: `/dev/characters/{character_id}/cspa/`
    Alternate route: `/latest/characters/{character_id}/cspa/`
    
    """
    ESI_request.request(character_id=character_id,
                        characters=characters,
                        token=token,
                        data_source='singularity',
                        version='v4',
                        path=f'/characters/{character_id}/cspa/')


def get_characters_character_id_notifications(token,
                                              character_id,
                                              if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return character notifications
    ---
    Alternate route: `/legacy/characters/{character_id}/notifications/`
    ---
    This route is cached for up to 600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v4/dev/#GET-/characters/{character_id}/notifications/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v4',
                        path=f'/characters/{character_id}/notifications/')


def get_characters_character_id_skills(token, character_id,
                                       if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    List all trained skills for the given character
    ---
    Alternate route: `/dev/characters/{character_id}/skills/`
    Alternate route: `/latest/characters/{character_id}/skills/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v4',
                        path=f'/characters/{character_id}/skills/')


def get_corporations_corporation_id(corporation_id, if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a corporation
    ---
    Alternate route: `/dev/corporations/{corporation_id}/`
    Alternate route: `/latest/corporations/{corporation_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v4',
                        path=f'/corporations/{corporation_id}/')


def get_corporations_corporation_id_wallets_division_journal(
        token, page, division, corporation_id, if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param division: Wallet key of the division to fetch journals from
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param token: Access token to use if unable to set a header
    Retrieve the given corporation's wallet journal for the given division going 30 days back
    ---
    Alternate route: `/dev/corporations/{corporation_id}/wallets/{division}/journal/`
    Alternate route: `/latest/corporations/{corporation_id}/wallets/{division}/journal/`
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
        version='v4',
        path=f'/corporations/{corporation_id}/wallets/{division}/journal/')


def get_universe_systems_system_id(system_id,
                                   language,
                                   accept_language='en-US',
                                   if_none_match=None):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param system_id: system_id integer
    Get information on a solar system.
    ---
    Alternate route: `/dev/universe/systems/{system_id}/`
    Alternate route: `/latest/universe/systems/{system_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        system_id=system_id,
                        data_source='singularity',
                        version='v4',
                        path=f'/universe/systems/{system_id}/')
