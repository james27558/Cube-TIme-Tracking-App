from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import AttemptModelForm, TagModelForm, SessionJSONModelForm
from django.urls import reverse
import json

from .logic.helper import parseSession, getAttemptIDAndTagDict, deleteAllRecords
from .models import Attempt, Session
from .logic.DataExporter import DataExporter


def deleteAllRecordsPage(request, confirm):
    if confirm == 1:
        deleteAllRecords()
        return HttpResponseRedirect(reverse('home'))

    else:
        return render(request, 'deleteAllRecordsPage.html')


def base(request):
    """
    Renders the base page
    :param request:
    :return:
    """

    return render(request, "base.html")


def home(request):
    """
    Renders the index page
    :param request:
    :return:
    """
    con = {"sessions": Session.objects.all(),
           "attempts": Paginator(Attempt.objects.all().order_by("id"), 20),
           "attemptsList": Attempt.objects.all().order_by("id"),
           "attemptTagsDict": getAttemptIDAndTagDict()}
    return render(request, "home.html", con)


def addTimesPage(request):
    con = {"attemptForm": AttemptModelForm,
           "sessionForm": SessionJSONModelForm,
           "tagForm": TagModelForm}

    return render(request, 'AddTimes.html', con)


def statsPage(request):
    con = {'chart': DataExporter.exportTimes()}

    return render(request, 'stats.html', con)


def addAttempt(request):
    """
    Renders a page that adds a single time to the database and then redirects to the index page
    :param request:
    :return:
    """
    if request.GET is not None:
        filledForm = AttemptModelForm(request.GET)
        if filledForm.is_valid():
            filledForm.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("Not valid")


def addTag(request):
    """
    Renders a page that adds a single time to the database and then redirects to the index page
    :param request:
    :return:
    """
    if request.GET is not None:
        filledForm = TagModelForm(request.GET)
        if filledForm.is_valid():
            filledForm.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("Not valid")


def addFileOfTimes(request):
    """
    Renders a page that takes a JSON file from CS Timer through POST and it displays the times to be added,
    when the user confirms, the page will be loaded again with the file passed through POST and also a variable
    'confirmed' set to 1. When 'confirmed' is 1, the view will add the times to the database and redirect the user
    back to the index page
    :param request:
    :return:
    """

    if request.method == 'POST':
        form = SessionJSONModelForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()

        # Allows multiple files to be passed through for extensibility
        for key, fileName in enumerate(request.FILES):
            sessionJSON = json.loads(request.FILES[fileName].read())

            # Iterate through all keys that are of the form session[NUMBER], e.g. session1, session2 etc
            for topElement in sessionJSON:

                # Also skip if the session is empty
                if "session" in topElement and len(sessionJSON[topElement]) != 0:
                    session, attempts = parseSession(sessionJSON[topElement])

                    # Save session
                    session.save()
                    # Save Attempts
                    for a in attempts:
                        a.save()

            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("No data POSTED")
