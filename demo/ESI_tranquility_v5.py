import ESI_request


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
    Alternate route: `/dev/characters/{character_id}/notifications/`
    Alternate route: `/latest/characters/{character_id}/notifications/`
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='tranquility',
                        version='v5',
                        path=f'/characters/{character_id}/notifications/')


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
    Alternate route: `/legacy/characters/{character_id}/wallet/journal/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v5/dev/#GET-/characters/{character_id}/wallet/journal/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='tranquility',
                        version='v5',
                        path=f'/characters/{character_id}/wallet/journal/')
