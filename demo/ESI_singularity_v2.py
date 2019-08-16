import ESI_request


def get_alliances_alliance_id(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about an alliance
    ---
    Alternate route: `/legacy/alliances/{alliance_id}/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/alliances/{alliance_id}/)
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/alliances/{alliance_id}/contacts/`
    Alternate route: `/latest/alliances/{alliance_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/alliances/{alliance_id}/contacts/')


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
    Alternate route: `/legacy/characters/{character_id}/assets/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/characters/{character_id}/assets/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/assets/')


def post_characters_character_id_assets_locations(*, character_id, item_ids,
                                                  token):
    """
    :param character_id: An EVE character ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    Alternate route: `/dev/characters/{character_id}/assets/locations/`
    Alternate route: `/latest/characters/{character_id}/assets/locations/`
    
    """
    ESI_request.request(character_id=character_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/assets/locations/')


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
    Alternate route: `/dev/characters/{character_id}/blueprints/`
    Alternate route: `/latest/characters/{character_id}/blueprints/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/characters/{character_id}/bookmarks/`
    Alternate route: `/latest/characters/{character_id}/bookmarks/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/characters/{character_id}/bookmarks/folders/`
    Alternate route: `/latest/characters/{character_id}/bookmarks/folders/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/bookmarks/folders/')


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
    Alternate route: `/legacy/characters/{character_id}/calendar/{event_id}/`
    ---
    This route is cached for up to 5 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/characters/{character_id}/calendar/{event_id}/)
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='v2',
        path=f'/characters/{character_id}/calendar/{event_id}/')


def put_characters_character_id_calendar_event_id(*, character_id, event_id,
                                                  response, token):
    """
    :param character_id: An EVE character ID
    :param event_id: The ID of the event requested
    :param response: ['accepted', 'declined', 'tentative'] The response value to set, overriding current value
    :param token: Access token to use if unable to set a header
    Set your response status to an event
    ---
    Alternate route: `/legacy/characters/{character_id}/calendar/{event_id}/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#PUT-/characters/{character_id}/calendar/{event_id}/)
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        response=response,
        token=token,
        data_source='singularity',
        version='v2',
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
    Alternate route: `/legacy/characters/{character_id}/clones/`
    ---
    This route is cached for up to 120 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/characters/{character_id}/clones/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/clones/')


def delete_characters_character_id_contacts(*, character_id, contact_ids,
                                            token):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts to delete
    :param token: Access token to use if unable to set a header
    Bulk delete contacts
    ---
    Alternate route: `/dev/characters/{character_id}/contacts/`
    Alternate route: `/latest/characters/{character_id}/contacts/`
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/characters/{character_id}/contacts/`
    Alternate route: `/latest/characters/{character_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/characters/{character_id}/contacts/`
    Alternate route: `/latest/characters/{character_id}/contacts/`
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_ids=label_ids,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/characters/{character_id}/contacts/`
    Alternate route: `/latest/characters/{character_id}/contacts/`
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_ids=label_ids,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/contacts/')


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
    Alternate route: `/dev/characters/{character_id}/fittings/`
    Alternate route: `/latest/characters/{character_id}/fittings/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/fittings/')


def post_characters_character_id_fittings(*, character_id, fitting, token):
    """
    :param character_id: An EVE character ID
    :param fitting: Details about the new fitting
    :param token: Access token to use if unable to set a header
    Save a new fitting for a character
    ---
    Alternate route: `/dev/characters/{character_id}/fittings/`
    Alternate route: `/latest/characters/{character_id}/fittings/`
    
    """
    ESI_request.request(character_id=character_id,
                        fitting=fitting,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/fittings/')


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
    Alternate route: `/dev/characters/{character_id}/fleet/`
    ---
    This route is cached for up to 60 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/fleet/')


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
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/location/')


def get_characters_character_id_mail_labels(*,
                                            character_id,
                                            token,
                                            if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return a list of the users mail labels
    ---
    Alternate route: `/legacy/characters/{character_id}/mail/labels/`
    ---
    This route is cached for up to 30 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/characters/{character_id}/mail/labels/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/mail/labels/')


def post_characters_character_id_mail_labels(*, character_id, label, token):
    """
    :param character_id: An EVE character ID
    :param label: Label to create
    :param token: Access token to use if unable to set a header
    Create a mail label
    ---
    Alternate route: `/dev/characters/{character_id}/mail/labels/`
    Alternate route: `/latest/characters/{character_id}/mail/labels/`
    Alternate route: `/legacy/characters/{character_id}/mail/labels/`
    
    """
    ESI_request.request(character_id=character_id,
                        label=label,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/latest/characters/{character_id}/online/`
    ---
    This route is cached for up to 60 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/online/')


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
    Alternate route: `/dev/characters/{character_id}/orders/`
    Alternate route: `/latest/characters/{character_id}/orders/`
    ---
    This route is cached for up to 1200 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/orders/')


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
    Alternate route: `/legacy/characters/{character_id}/planets/{planet_id}/`
    ---
    This route is cached for up to 600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/characters/{character_id}/planets/{planet_id}/)
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        planet_id=planet_id,
        token=token,
        data_source='singularity',
        version='v2',
        path=f'/characters/{character_id}/planets/{planet_id}/')


def get_characters_character_id_portrait(*, character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get portrait urls for a character
    ---
    Alternate route: `/dev/characters/{character_id}/portrait/`
    Alternate route: `/latest/characters/{character_id}/portrait/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/characters/{character_id}/roles/`
    Alternate route: `/latest/characters/{character_id}/roles/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    ---
    This route is cached for up to 5 seconds
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/characters/{character_id}/ship/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/characters/{character_id}/skillqueue/`
    Alternate route: `/latest/characters/{character_id}/skillqueue/`
    Alternate route: `/legacy/characters/{character_id}/skillqueue/`
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/skillqueue/')


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
    Alternate route: `/dev/characters/{character_id}/stats/`
    Alternate route: `/latest/characters/{character_id}/stats/`
    ---
    This route is cached for up to 86400 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/characters/{character_id}/stats/')


def get_corporations_corporation_id_alliancehistory(*,
                                                    corporation_id,
                                                    if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of all the alliances a corporation has been a member of
    ---
    Alternate route: `/dev/corporations/{corporation_id}/alliancehistory/`
    Alternate route: `/latest/corporations/{corporation_id}/alliancehistory/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        data_source='singularity',
        version='v2',
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
    Alternate route: `/legacy/corporations/{corporation_id}/assets/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/corporations/{corporation_id}/assets/)
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/corporations/{corporation_id}/assets/')


def post_corporations_corporation_id_assets_locations(*, corporation_id,
                                                      item_ids, token):
    """
    :param corporation_id: An EVE corporation ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    Alternate route: `/dev/corporations/{corporation_id}/assets/locations/`
    Alternate route: `/latest/corporations/{corporation_id}/assets/locations/`
    
    ---
    Requires one of the following EVE corporation role(s): Director
    
    """
    ESI_request.request(
        corporation_id=corporation_id,
        item_ids=item_ids,
        token=token,
        data_source='singularity',
        version='v2',
        path=f'/corporations/{corporation_id}/assets/locations/')


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
    Alternate route: `/dev/corporations/{corporation_id}/blueprints/`
    Alternate route: `/latest/corporations/{corporation_id}/blueprints/`
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
                        version='v2',
                        path=f'/corporations/{corporation_id}/blueprints/')


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
    Alternate route: `/dev/corporations/{corporation_id}/contacts/`
    Alternate route: `/latest/corporations/{corporation_id}/contacts/`
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/corporations/{corporation_id}/contacts/')


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
    Alternate route: `/dev/corporations/{corporation_id}/containers/logs/`
    Alternate route: `/latest/corporations/{corporation_id}/containers/logs/`
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
        version='v2',
        path=f'/corporations/{corporation_id}/containers/logs/')


def get_corporations_corporation_id_members(*,
                                            corporation_id,
                                            token,
                                            if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Read the current list of members if the calling character is a member.
    ---
    Alternate route: `/legacy/corporations/{corporation_id}/members/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/corporations/{corporation_id}/members/)
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/legacy/corporations/{corporation_id}/orders/`
    ---
    This route is cached for up to 1200 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Trader
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/corporations/{corporation_id}/orders/)
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
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
    Alternate route: `/dev/corporations/{corporation_id}/orders/history/`
    Alternate route: `/latest/corporations/{corporation_id}/orders/history/`
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
                        version='v2',
                        path=f'/corporations/{corporation_id}/orders/history/')


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
    Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th Note: this route will not return any flex structures owned by a corporation, use the v3 route to have those included in the response. A list of FLEX structures can be found here: https://support.eveonline.com/hc/en-us/articles/213021829-Upwell-Structures
    ---
    Alternate route: `/legacy/corporations/{corporation_id}/structures/`
    ---
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Station_Manager
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/corporations/{corporation_id}/structures/)
    """
    ESI_request.request(accept_language=accept_language,
                        corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        language=language,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/corporations/{corporation_id}/structures/')


def get_dogma_effects_effect_id(*, effect_id, if_none_match=None):
    """
    :param effect_id: A dogma effect ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a dogma effect
    ---
    Alternate route: `/dev/dogma/effects/{effect_id}/`
    Alternate route: `/latest/dogma/effects/{effect_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(effect_id=effect_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='v2',
                        path=f'/dogma/effects/{effect_id}/')


def get_fw_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    An overview of the current ownership of faction warfare solar systems
    ---
    Alternate route: `/dev/fw/systems/`
    Alternate route: `/latest/fw/systems/`
    ---
    This route is cached for up to 1800 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='v2',
                        path=f'/fw/systems/')


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
    Alternate route: `/dev/search/`
    Alternate route: `/latest/search/`
    Alternate route: `/legacy/search/`
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
                        version='v2',
                        path=f'/search/')


def post_ui_autopilot_waypoint(*, add_to_beginning, clear_other_waypoints,
                               destination_id, token):
    """
    :param add_to_beginning: Whether this solar system should be added to the beginning of all waypoints
    :param clear_other_waypoints: Whether clean other waypoints beforing adding this one
    :param destination_id: The destination to travel to, can be solar system, station or structure's id
    :param token: Access token to use if unable to set a header
    Set a solar system as autopilot waypoint
    ---
    Alternate route: `/dev/ui/autopilot/waypoint/`
    Alternate route: `/latest/ui/autopilot/waypoint/`
    Alternate route: `/legacy/ui/autopilot/waypoint/`
    
    """
    ESI_request.request(add_to_beginning=add_to_beginning,
                        clear_other_waypoints=clear_other_waypoints,
                        destination_id=destination_id,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/ui/autopilot/waypoint/')


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
    Alternate route: `/dev/universe/factions/`
    Alternate route: `/latest/universe/factions/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='v2',
                        path=f'/universe/factions/')


def post_universe_names(*, ids):
    """
    :param ids: The ids to resolve
    Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types
    ---
    Alternate route: `/legacy/universe/names/`
    
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#POST-/universe/names/)
    """
    ESI_request.request(ids=ids,
                        data_source='singularity',
                        version='v2',
                        path=f'/universe/names/')


def get_universe_stations_station_id(*, station_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param station_id: station_id integer
    Get information on a station
    ---
    Alternate route: `/dev/universe/stations/{station_id}/`
    Alternate route: `/latest/universe/stations/{station_id}/`
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        station_id=station_id,
                        data_source='singularity',
                        version='v2',
                        path=f'/universe/stations/{station_id}/')


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
    Alternate route: `/dev/universe/structures/{structure_id}/`
    Alternate route: `/latest/universe/structures/{structure_id}/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        structure_id=structure_id,
                        token=token,
                        data_source='singularity',
                        version='v2',
                        path=f'/universe/structures/{structure_id}/')


def get_universe_system_kills(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed
    ---
    Alternate route: `/dev/universe/system_kills/`
    Alternate route: `/latest/universe/system_kills/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='v2',
                        path=f'/universe/system_kills/')


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
    Alternate route: `/legacy/universe/types/{type_id}/`
    ---
    This route expires daily at 11:05
    ---
    Warning: This route is deprecated
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/v2/dev/#GET-/universe/types/{type_id}/)
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        type_id=type_id,
                        data_source='singularity',
                        version='v2',
                        path=f'/universe/types/{type_id}/')
