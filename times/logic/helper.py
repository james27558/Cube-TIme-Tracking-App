import re
from datetime import datetime
from times.models import Attempt, Session, Tag, Cube, EventType


def parseAttempt(AttemptJSON, SessionInstance):
    # Extract basic information about the attempt
    timeBeforeModifier = AttemptJSON[0][1]
    modifier = AttemptJSON[0][0]
    scramble = AttemptJSON[1]
    note = AttemptJSON[2]
    epochDateTime = AttemptJSON[3]

    return Attempt.objects.create(
        session=SessionInstance,
        time=timeBeforeModifier,
        DNF=True if modifier == -1 else False,
        plusTwo=True if modifier == 2000 else False,
        scramble=scramble,
        note=note,
        datetime=datetime.fromtimestamp(epochDateTime)
    )


def parseSession(sessionJSON):
    # TODO: Expand the docstring when the functionality of this method is complete

    """
    Parses a session
    :param sessionJSON:
    :return: Tuple of (Attempts : List[Attempt], Session : Session)
    """
    # -1 is DNF
    # anything else is time added on so 2000 would be a +2 seconds

    parsedAttempts = []
    sessionInstance = Session.objects.create()

    globalSessionTag = None

    # Go through the attemptJSON's and parse it, adding it to the list of parsed attempts
    for attemptIndex, attemptJSON in enumerate(sessionJSON):
        currentAttempt = parseAttempt(attemptJSON, sessionInstance)

        # Parse the session tag, if there is one
        # The first global session tag found in the attempts is the one that will be used
        if globalSessionTag is None:
            globalSessionTag = getSessionTagFromNotes(currentAttempt.note)

        parsedAttempts.append(currentAttempt)

    # If we've found a tag then get/create it and add that tag to the attempt
    if globalSessionTag is not None:
        for attempt in parsedAttempts:
            attempt.tags.add(Tag.objects.get_or_create(name=globalSessionTag)[0])

    # Now that we have the attempts in a friendly format we can complete the information for the session
    sessionInstance.startDateTime = min(parsedAttempts, key=lambda x: x.datetime).datetime
    sessionInstance.endDateTime = max(parsedAttempts, key=lambda x: x.datetime).datetime

    return sessionInstance, parsedAttempts

def getCommandStringParameter(commandName, notes):
    """
    Searches a string and gets text, enclosed in speech marks, that comes after a command name, if there is one. If
    there is no instance of this or there are multiple command names with speech mark enclosed strings after then
    return None
    :param commandName: String that should appear before the speech mark enclosed string
    :param notes: String to be searched
    :return: Text inside speech marks if this exists, None if it doesn't exist or if there are multiple instances of it
    """
    match = re.findall(commandName + '\s"[^"]+"', notes)

    if len(match) == 0 or len(match) > 1:
        return None
    else:
        matchString = match[0]
        tagName = matchString.split('"')[1]
        return tagName


def getSessionTagFromNotes(notes):
    """
    Extracts a string that appears in the format '#st "STRING"' from text. This is used for parsing the session tag
    command
    :param notes:
    :return:
    """
    return getCommandStringParameter("#st", notes)


def getAttemptIDAndTagDict():
    dic = {}

    for attempt in Attempt.objects.all():
        dic[attempt.id] = [tag.name for tag in attempt.tags.all()]

    return dic

def deleteAllRecords():
    Session.objects.all().delete()