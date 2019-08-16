import ESI_request


def get_alliances(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all active player alliances
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/alliances/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/alliances/{alliance_id}/contacts/labels/')


def get_alliances_alliance_id_corporations(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all current member corporations of an alliance
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/alliances/{alliance_id}/corporations/')


def get_alliances_alliance_id_icons(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the icon urls for a alliance
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/alliances/{alliance_id}/icons/')


def post_characters_affiliation(*, characters):
    """
    :param characters: The character IDs to fetch affiliations for. All characters must exist, or none will be returned
    Bulk lookup of character IDs to corporation, alliance and faction
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(characters=characters,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/affiliation/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/agents_research/')


def post_characters_character_id_assets_names(*, character_id, item_ids,
                                              token):
    """
    :param character_id: An EVE character ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        item_ids=item_ids,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/assets/names/')


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
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/attributes/')


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
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        from_event=from_event,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/calendar/')


def get_characters_character_id_calendar_event_id_attendees(
        *, character_id, event_id, token, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param event_id: The id of the event requested
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Get all invited attendees for a given event
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/calendar/{event_id}/attendees/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/contacts/labels/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/contracts/')


def get_characters_character_id_contracts_contract_id_bids(
        *, character_id, contract_id, token, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param contract_id: ID of a contract
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Lists bids on a particular auction contract
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(
        character_id=character_id,
        contract_id=contract_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/contracts/{contract_id}/bids/')


def get_characters_character_id_contracts_contract_id_items(
        *, character_id, contract_id, token, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param contract_id: ID of a contract
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Lists items of a particular contract
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        contract_id=contract_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/contracts/{contract_id}/items/')


def get_characters_character_id_corporationhistory(*,
                                                   character_id,
                                                   if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of all the corporations a character has been a member of
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/corporationhistory/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/fatigue/')


def delete_characters_character_id_fittings_fitting_id(*, character_id,
                                                       fitting_id, token):
    """
    :param character_id: An EVE character ID
    :param fitting_id: ID for a fitting of this character
    :param token: Access token to use if unable to set a header
    Delete a fitting from a character
    ---
    
    """
    ESI_request.request(
        character_id=character_id,
        fitting_id=fitting_id,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/fittings/{fitting_id}/')


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
    This route is cached for up to 60 seconds
    ---
    Warning: This route has an upgrade available
    ---
    [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/fleet/)
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/fleet/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/fw/stats/')


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
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/implants/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        include_completed=include_completed,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/industry/jobs/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/killmails/recent/')


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
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/location/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/loyalty/points/')


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
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        labels=labels,
                        last_mail_id=last_mail_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/mail/')


def post_characters_character_id_mail(*, character_id, mail, token):
    """
    :param character_id: An EVE character ID
    :param mail: The mail to send
    :param token: Access token to use if unable to set a header
    Create and send a new mail
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        mail=mail,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/mail/')


def delete_characters_character_id_mail_labels_label_id(
        *, character_id, label_id, token):
    """
    :param character_id: An EVE character ID
    :param label_id: An EVE label id
    :param token: Access token to use if unable to set a header
    Delete a mail label
    ---
    
    """
    ESI_request.request(
        character_id=character_id,
        label_id=label_id,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/mail/labels/{label_id}/')


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
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/mail/lists/')


def delete_characters_character_id_mail_mail_id(*, character_id, mail_id,
                                                token):
    """
    :param character_id: An EVE character ID
    :param mail_id: An EVE mail ID
    :param token: Access token to use if unable to set a header
    Delete a mail
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        mail_id=mail_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/mail/{mail_id}/')


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
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        mail_id=mail_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/mail/{mail_id}/')


def put_characters_character_id_mail_mail_id(*, character_id, contents,
                                             mail_id, token):
    """
    :param character_id: An EVE character ID
    :param contents: Data used to update the mail
    :param mail_id: An EVE mail ID
    :param token: Access token to use if unable to set a header
    Update metadata about a mail
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        contents=contents,
                        mail_id=mail_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/mail/{mail_id}/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/medals/')


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
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/mining/')


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
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/notifications/contacts/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/opportunities/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/orders/history/')


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
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/planets/')


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
    This route is cached for up to 5 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/ship/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/standings/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/titles/')


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
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/characters/{character_id}/wallet/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        from_id=from_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/characters/{character_id}/wallet/transactions/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(contract_id=contract_id,
                        if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/contracts/public/bids/{contract_id}/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(contract_id=contract_id,
                        if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/contracts/public/items/{contract_id}/')


def get_contracts_public_region_id(*, region_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param region_id: An EVE region id
    Returns a paginated list of all public contracts in the given region
    ---
    This route is cached for up to 1800 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        region_id=region_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/contracts/public/{region_id}/')


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
        version='_latest',
        path=f'/v1/corporation/{corporation_id}/mining/extractions/')


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
        version='_latest',
        path=f'/v1/corporation/{corporation_id}/mining/observers/')


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
        version='_latest',
        path=f'/v1/corporation/{corporation_id}/mining/observers/{observer_id}/'
    )


def get_corporations_npccorps(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of npc corporations
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/npccorps/')


def post_corporations_corporation_id_assets_names(*, corporation_id, item_ids,
                                                  token):
    """
    :param corporation_id: An EVE corporation ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(
        corporation_id=corporation_id,
        item_ids=item_ids,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/assets/names/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/bookmarks/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/bookmarks/folders/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/contacts/labels/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/contracts/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        contract_id=contract_id,
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/contracts/{contract_id}/bids/'
    )


def get_corporations_corporation_id_contracts_contract_id_items(
        *, contract_id, corporation_id, token, if_none_match=None):
    """
    :param contract_id: ID of a contract
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Lists items of a particular contract
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        contract_id=contract_id,
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/contracts/{contract_id}/items/'
    )


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
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/customs_offices/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/divisions/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Factory_Manager
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/facilities/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/fw/stats/')


def get_corporations_corporation_id_icons(*,
                                          corporation_id,
                                          if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the icon urls for a corporation
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/icons/')


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
    This route is cached for up to 300 seconds
    ---
    Requires one of the following EVE corporation role(s): Factory_Manager
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        include_completed=include_completed,
        page=page,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/industry/jobs/')


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
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/killmails/recent/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/medals/')


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
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/medals/issued/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/members/limit/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/members/titles/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/membertracking/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/roles/')


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
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/roles/history/')


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
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/shareholders/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/standings/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/starbases/')


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
        version='_latest',
        path=f'/v1/corporations/{corporation_id}/starbases/{starbase_id}/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/titles/')


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
    This route is cached for up to 300 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/corporations/{corporation_id}/wallets/')


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
        version='_latest',
        path=
        f'/v1/corporations/{corporation_id}/wallets/{division}/transactions/')


def get_dogma_attributes(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of dogma attribute ids
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/dogma/attributes/')


def get_dogma_attributes_attribute_id(*, attribute_id, if_none_match=None):
    """
    :param attribute_id: A dogma attribute ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a dogma attribute
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(attribute_id=attribute_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/dogma/attributes/{attribute_id}/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        item_id=item_id,
                        type_id=type_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/dogma/dynamic/items/{type_id}/{item_id}/')


def get_dogma_effects(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of dogma effect ids
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/dogma/effects/')


def get_fleets_fleet_id(*, fleet_id, token, if_none_match=None):
    """
    :param fleet_id: ID for a fleet
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param token: Access token to use if unable to set a header
    Return details about a fleet
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/')


def put_fleets_fleet_id(*, fleet_id, new_settings, token):
    """
    :param fleet_id: ID for a fleet
    :param new_settings: What to update for this fleet
    :param token: Access token to use if unable to set a header
    Update settings about a fleet
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        new_settings=new_settings,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/')


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
    This route is cached for up to 5 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        language=language,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/members/')


def post_fleets_fleet_id_members(*, fleet_id, invitation, token):
    """
    :param fleet_id: ID for a fleet
    :param invitation: Details of the invitation
    :param token: Access token to use if unable to set a header
    Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        invitation=invitation,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/members/')


def delete_fleets_fleet_id_members_member_id(*, fleet_id, member_id, token):
    """
    :param fleet_id: ID for a fleet
    :param member_id: The character ID of a member in this fleet
    :param token: Access token to use if unable to set a header
    Kick a fleet member
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        member_id=member_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/members/{member_id}/')


def put_fleets_fleet_id_members_member_id(*, fleet_id, member_id, movement,
                                          token):
    """
    :param fleet_id: ID for a fleet
    :param member_id: The character ID of a member in this fleet
    :param movement: Details of the invitation
    :param token: Access token to use if unable to set a header
    Move a fleet member around
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        member_id=member_id,
                        movement=movement,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/members/{member_id}/')


def delete_fleets_fleet_id_squads_squad_id(*, fleet_id, squad_id, token):
    """
    :param fleet_id: ID for a fleet
    :param squad_id: The squad to delete
    :param token: Access token to use if unable to set a header
    Delete a fleet squad, only empty squads can be deleted
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        squad_id=squad_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/squads/{squad_id}/')


def put_fleets_fleet_id_squads_squad_id(*, fleet_id, naming, squad_id, token):
    """
    :param fleet_id: ID for a fleet
    :param naming: New name of the squad
    :param squad_id: The squad to rename
    :param token: Access token to use if unable to set a header
    Rename a fleet squad
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        naming=naming,
                        squad_id=squad_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/squads/{squad_id}/')


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
    This route is cached for up to 5 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        fleet_id=fleet_id,
                        if_none_match=if_none_match,
                        language=language,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/wings/')


def post_fleets_fleet_id_wings(*, fleet_id, token):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    Create a new wing in a fleet
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/wings/')


def delete_fleets_fleet_id_wings_wing_id(*, fleet_id, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing to delete
    Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        wing_id=wing_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/wings/{wing_id}/')


def put_fleets_fleet_id_wings_wing_id(*, fleet_id, naming, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param naming: New name of the wing
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing to rename
    Rename a fleet wing
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        naming=naming,
                        token=token,
                        wing_id=wing_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/wings/{wing_id}/')


def post_fleets_fleet_id_wings_wing_id_squads(*, fleet_id, token, wing_id):
    """
    :param fleet_id: ID for a fleet
    :param token: Access token to use if unable to set a header
    :param wing_id: The wing_id to create squad in
    Create a new squad in a fleet
    ---
    
    """
    ESI_request.request(fleet_id=fleet_id,
                        token=token,
                        wing_id=wing_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fleets/{fleet_id}/wings/{wing_id}/squads/')


def get_fw_leaderboards(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fw/leaderboards/')


def get_fw_leaderboards_characters(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fw/leaderboards/characters/')


def get_fw_leaderboards_corporations(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fw/leaderboards/corporations/')


def get_fw_stats(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Statistical overviews of factions involved in faction warfare
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fw/stats/')


def get_fw_wars(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Data about which NPC factions are at war
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/fw/wars/')


def get_incursions(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of current incursions
    ---
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/incursions/')


def get_industry_facilities(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of industry facilities
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/industry/facilities/')


def get_industry_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return cost indices for solar systems
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/industry/systems/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/insurance/prices/')


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
    This route is cached for up to 1209600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        killmail_hash=killmail_hash,
                        killmail_id=killmail_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/killmails/{killmail_id}/{killmail_hash}/')


def get_loyalty_stores_corporation_id_offers(*,
                                             corporation_id,
                                             if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of offers from a specific corporation's loyalty store
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/loyalty/stores/{corporation_id}/offers/')


def get_markets_groups(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of item groups
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/markets/groups/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        market_group_id=market_group_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/markets/groups/{market_group_id}/')


def get_markets_prices(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of prices
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/markets/prices/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        structure_id=structure_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/markets/structures/{structure_id}/')


def get_markets_region_id_history(*, region_id, type_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param region_id: Return statistics in this region
    :param type_id: Return statistics for this type
    Return a list of historical market statistics for the specified type in a region
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        region_id=region_id,
                        type_id=type_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/markets/{region_id}/history/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        order_type=order_type,
                        page=page,
                        region_id=region_id,
                        type_id=type_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/markets/{region_id}/orders/')


def get_markets_region_id_types(*, region_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param region_id: Return statistics in this region
    Return a list of type IDs that have active orders in the region, for efficient market indexing.
    ---
    This route is cached for up to 600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        region_id=region_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/markets/{region_id}/types/')


def get_opportunities_groups(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of opportunities groups
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/opportunities/groups/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        group_id=group_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/opportunities/groups/{group_id}/')


def get_opportunities_tasks(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Return a list of opportunities tasks
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/opportunities/tasks/')


def get_opportunities_tasks_task_id(*, task_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param task_id: ID of an opportunities task
    Return information of an opportunities task
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        task_id=task_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/opportunities/tasks/{task_id}/')


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
    This route is cached for up to 86400 seconds
    """
    ESI_request.request(avoid=avoid,
                        connections=connections,
                        destination=destination,
                        flag=flag,
                        if_none_match=if_none_match,
                        origin=origin,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/route/{origin}/{destination}/')


def get_sovereignty_campaigns(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty data for campaigns.
    ---
    This route is cached for up to 5 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/sovereignty/campaigns/')


def get_sovereignty_map(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty information for solar systems
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/sovereignty/map/')


def get_sovereignty_structures(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Shows sovereignty data for structures.
    ---
    This route is cached for up to 120 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/sovereignty/structures/')


def get_status(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    EVE Server status
    ---
    This route is cached for up to 30 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/status/')


def post_ui_openwindow_contract(*, contract_id, token):
    """
    :param contract_id: The contract to open
    :param token: Access token to use if unable to set a header
    Open the contract window inside the client
    ---
    
    """
    ESI_request.request(contract_id=contract_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/ui/openwindow/contract/')


def post_ui_openwindow_information(*, target_id, token):
    """
    :param target_id: The target to open
    :param token: Access token to use if unable to set a header
    Open the information window for a character, corporation or alliance inside the client
    ---
    
    """
    ESI_request.request(target_id=target_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/ui/openwindow/information/')


def post_ui_openwindow_marketdetails(*, token, type_id):
    """
    :param token: Access token to use if unable to set a header
    :param type_id: The item type to open in market window
    Open the market details window for a specific typeID inside the client
    ---
    
    """
    ESI_request.request(token=token,
                        type_id=type_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/ui/openwindow/marketdetails/')


def post_ui_openwindow_newmail(*, new_mail, token):
    """
    :param new_mail: The details of mail to create
    :param token: Access token to use if unable to set a header
    Open the New Mail window, according to settings from the request if applicable
    ---
    
    """
    ESI_request.request(new_mail=new_mail,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/ui/openwindow/newmail/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/ancestries/')


def get_universe_asteroid_belts_asteroid_belt_id(*,
                                                 asteroid_belt_id,
                                                 if_none_match=None):
    """
    :param asteroid_belt_id: asteroid_belt_id integer
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on an asteroid belt
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(
        asteroid_belt_id=asteroid_belt_id,
        if_none_match=if_none_match,
        data_source='singularity',
        version='_latest',
        path=f'/v1/universe/asteroid_belts/{asteroid_belt_id}/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/bloodlines/')


def get_universe_categories(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of item categories
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/categories/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        category_id=category_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/categories/{category_id}/')


def get_universe_constellations(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of constellations
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/constellations/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(
        accept_language=accept_language,
        constellation_id=constellation_id,
        if_none_match=if_none_match,
        language=language,
        data_source='singularity',
        version='_latest',
        path=f'/v1/universe/constellations/{constellation_id}/')


def get_universe_graphics(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of graphics
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/graphics/')


def get_universe_graphics_graphic_id(*, graphic_id, if_none_match=None):
    """
    :param graphic_id: graphic_id integer
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a graphic
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(graphic_id=graphic_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/graphics/{graphic_id}/')


def get_universe_groups(*, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Get a list of item groups
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/groups/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        group_id=group_id,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/groups/{group_id}/')


def post_universe_ids(*, language, names, accept_language='en-us'):
    """
    :param accept_language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response
    :param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param names: The names to resolve
    Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours
    ---
    
    """
    ESI_request.request(accept_language=accept_language,
                        language=language,
                        names=names,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/ids/')


def get_universe_moons_moon_id(*, moon_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param moon_id: moon_id integer
    Get information on a moon
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        moon_id=moon_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/moons/{moon_id}/')


def get_universe_planets_planet_id(*, planet_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param planet_id: planet_id integer
    Get information on a planet
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        planet_id=planet_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/planets/{planet_id}/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/races/')


def get_universe_regions(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of regions
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/regions/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        region_id=region_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/regions/{region_id}/')


def get_universe_schematics_schematic_id(*, schematic_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param schematic_id: A PI schematic ID
    Get information on a planetary factory schematic
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        schematic_id=schematic_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/schematics/{schematic_id}/')


def get_universe_stargates_stargate_id(*, stargate_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param stargate_id: stargate_id integer
    Get information on a stargate
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        stargate_id=stargate_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/stargates/{stargate_id}/')


def get_universe_stars_star_id(*, star_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param star_id: star_id integer
    Get information on a star
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        star_id=star_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/stars/{star_id}/')


def get_universe_structures(*, filter, if_none_match=None):
    """
    :param filter: ['market', 'manufacturing_basic'] Only list public structures that have this service online
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    List all public structures
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(filter=filter,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/structures/')


def get_universe_system_jumps(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/system_jumps/')


def get_universe_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of solar systems
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/systems/')


def get_universe_types(*, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    Get a list of type ids
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/universe/types/')


def get_wars(*, max_war_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param max_war_id: Only return wars with ID smaller than this
    Return a list of wars
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        max_war_id=max_war_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/wars/')


def get_wars_war_id(*, war_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param war_id: ID for a war
    Return details about a war
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        war_id=war_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/wars/{war_id}/')


def get_wars_war_id_killmails(*, war_id, if_none_match=None, page='1'):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param war_id: A valid war ID
    Return a list of kills related to a war
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        page=page,
                        war_id=war_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v1/wars/{war_id}/killmails/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/alliances/{alliance_id}/contacts/')


def post_characters_character_id_assets_locations(*, character_id, item_ids,
                                                  token):
    """
    :param character_id: An EVE character ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    
    """
    ESI_request.request(
        character_id=character_id,
        item_ids=item_ids,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v2/characters/{character_id}/assets/locations/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/blueprints/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/bookmarks/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v2/characters/{character_id}/bookmarks/folders/')


def delete_characters_character_id_contacts(*, character_id, contact_ids,
                                            token):
    """
    :param character_id: An EVE character ID
    :param contact_ids: A list of contacts to delete
    :param token: Access token to use if unable to set a header
    Bulk delete contacts
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/contacts/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/contacts/')


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
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_ids=label_ids,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/contacts/')


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
    
    """
    ESI_request.request(character_id=character_id,
                        contact_ids=contact_ids,
                        label_ids=label_ids,
                        standing=standing,
                        token=token,
                        watched=watched,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/contacts/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/fittings/')


def post_characters_character_id_fittings(*, character_id, fitting, token):
    """
    :param character_id: An EVE character ID
    :param fitting: Details about the new fitting
    :param token: Access token to use if unable to set a header
    Save a new fitting for a character
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        fitting=fitting,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/fittings/')


def post_characters_character_id_mail_labels(*, character_id, label, token):
    """
    :param character_id: An EVE character ID
    :param label: Label to create
    :param token: Access token to use if unable to set a header
    Create a mail label
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        label=label,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/mail/labels/')


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
    This route is cached for up to 60 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/online/')


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
    This route is cached for up to 1200 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/orders/')


def get_characters_character_id_portrait(*, character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get portrait urls for a character
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/portrait/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/roles/')


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
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/skillqueue/')


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
    This route is cached for up to 86400 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/characters/{character_id}/stats/')


def get_corporations_corporation_id_alliancehistory(*,
                                                    corporation_id,
                                                    if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get a list of all the alliances a corporation has been a member of
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        data_source='singularity',
        version='_latest',
        path=f'/v2/corporations/{corporation_id}/alliancehistory/')


def post_corporations_corporation_id_assets_locations(*, corporation_id,
                                                      item_ids, token):
    """
    :param corporation_id: An EVE corporation ID
    :param item_ids: A list of item ids
    :param token: Access token to use if unable to set a header
    Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(
        corporation_id=corporation_id,
        item_ids=item_ids,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v2/corporations/{corporation_id}/assets/locations/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/corporations/{corporation_id}/blueprints/')


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
    This route is cached for up to 300 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/corporations/{corporation_id}/contacts/')


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
        version='_latest',
        path=f'/v2/corporations/{corporation_id}/containers/logs/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Trader
    """
    ESI_request.request(
        corporation_id=corporation_id,
        if_none_match=if_none_match,
        page=page,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v2/corporations/{corporation_id}/orders/history/')


def get_dogma_effects_effect_id(*, effect_id, if_none_match=None):
    """
    :param effect_id: A dogma effect ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get information on a dogma effect
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(effect_id=effect_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/dogma/effects/{effect_id}/')


def get_fw_systems(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    An overview of the current ownership of faction warfare solar systems
    ---
    This route is cached for up to 1800 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/fw/systems/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(accept_language=accept_language,
                        categories=categories,
                        if_none_match=if_none_match,
                        language=language,
                        search=search,
                        strict=strict,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/search/')


def post_ui_autopilot_waypoint(*, add_to_beginning, clear_other_waypoints,
                               destination_id, token):
    """
    :param add_to_beginning: Whether this solar system should be added to the beginning of all waypoints
    :param clear_other_waypoints: Whether clean other waypoints beforing adding this one
    :param destination_id: The destination to travel to, can be solar system, station or structure's id
    :param token: Access token to use if unable to set a header
    Set a solar system as autopilot waypoint
    ---
    
    """
    ESI_request.request(add_to_beginning=add_to_beginning,
                        clear_other_waypoints=clear_other_waypoints,
                        destination_id=destination_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/ui/autopilot/waypoint/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/universe/factions/')


def get_universe_stations_station_id(*, station_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param station_id: station_id integer
    Get information on a station
    ---
    This route expires daily at 11:05
    """
    ESI_request.request(if_none_match=if_none_match,
                        station_id=station_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/universe/stations/{station_id}/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        structure_id=structure_id,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/universe/structures/{structure_id}/')


def get_universe_system_kills(*, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v2/universe/system_kills/')


def get_alliances_alliance_id(*, alliance_id, if_none_match=None):
    """
    :param alliance_id: An EVE alliance ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about an alliance
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(alliance_id=alliance_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/alliances/{alliance_id}/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/characters/{character_id}/assets/')


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
    This route is cached for up to 5 seconds
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        if_none_match=if_none_match,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v3/characters/{character_id}/calendar/{event_id}/')


def put_characters_character_id_calendar_event_id(*, character_id, event_id,
                                                  response, token):
    """
    :param character_id: An EVE character ID
    :param event_id: The ID of the event requested
    :param response: The response value to set, overriding current value
    :param token: Access token to use if unable to set a header
    Set your response status to an event
    ---
    
    """
    ESI_request.request(
        character_id=character_id,
        event_id=event_id,
        response=response,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v3/characters/{character_id}/calendar/{event_id}/')


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
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/characters/{character_id}/clones/')


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
    This route is cached for up to 30 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/characters/{character_id}/mail/labels/')


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
    This route is cached for up to 600 seconds
    """
    ESI_request.request(
        character_id=character_id,
        if_none_match=if_none_match,
        planet_id=planet_id,
        token=token,
        data_source='singularity',
        version='_latest',
        path=f'/v3/characters/{character_id}/planets/{planet_id}/')


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
                        version='_latest',
                        path=f'/v3/characters/{character_id}/search/')


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
    This route is cached for up to 3600 seconds
    ---
    Requires one of the following EVE corporation role(s): Director
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/corporations/{corporation_id}/assets/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/corporations/{corporation_id}/members/')


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
    This route is cached for up to 1200 seconds
    ---
    Requires one of the following EVE corporation role(s): Accountant, Trader
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/corporations/{corporation_id}/orders/')


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
                        version='_latest',
                        path=f'/v3/corporations/{corporation_id}/structures/')


def post_universe_names(*, ids):
    """
    :param ids: The ids to resolve
    Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions
    ---
    
    """
    ESI_request.request(ids=ids,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/universe/names/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        type_id=type_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v3/universe/types/{type_id}/')


def get_characters_character_id(*, character_id, if_none_match=None):
    """
    :param character_id: An EVE character ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a character
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v4/characters/{character_id}/')


def post_characters_character_id_cspa(*, character_id, characters, token):
    """
    :param character_id: An EVE character ID
    :param characters: The target characters to calculate the charge for
    :param token: Access token to use if unable to set a header
    Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost
    ---
    
    """
    ESI_request.request(character_id=character_id,
                        characters=characters,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v4/characters/{character_id}/cspa/')


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
    This route is cached for up to 120 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v4/characters/{character_id}/skills/')


def get_corporations_corporation_id(*, corporation_id, if_none_match=None):
    """
    :param corporation_id: An EVE corporation ID
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    Public information about a corporation
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(corporation_id=corporation_id,
                        if_none_match=if_none_match,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v4/corporations/{corporation_id}/')


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
        version='_latest',
        path=f'/v4/corporations/{corporation_id}/wallets/{division}/journal/')


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
    This route expires daily at 11:05
    """
    ESI_request.request(accept_language=accept_language,
                        if_none_match=if_none_match,
                        language=language,
                        system_id=system_id,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v4/universe/systems/{system_id}/')


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
    This route is cached for up to 600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v5/characters/{character_id}/notifications/')


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
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(character_id=character_id,
                        if_none_match=if_none_match,
                        page=page,
                        token=token,
                        data_source='singularity',
                        version='_latest',
                        path=f'/v6/characters/{character_id}/wallet/journal/')
