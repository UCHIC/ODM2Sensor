from django import template
from django.template.defaultfilters import stringfilter

from sensordatainterface.models import Action

register = template.Library()

@register.filter
@stringfilter
def separatewordsbycaps(word):
    """This custom template tag will add space to fields when it finds a capital letter.
    Ex. InstrumentDeployment --> Instrument Deployment"""

    wordList = list(word)
    offset = 0
    space = " "
    spaceIndexes = [index for index, char in enumerate(wordList) if char.isupper() and index!=0]

    for val in spaceIndexes:
        if wordList[val+offset-1] != space:
            wordList.insert(val+offset, space)
            offset += 1

    return ''.join(wordList)

@register.filter
@stringfilter
def get_media_file_name(file_path):
    """ This filter takes a path to a media files (as stored in the database) and
    gets the file name to display"""

    file_start = file_path.rfind('/')
    return file_path[file_start+1:]


@register.filter
def get_deployment_retrieval(deployment):
    if not isinstance(deployment, Action):
        return
    if deployment.actiontypecv_id not in ['Equipment deployment', 'Instrument deployment']:
        return

    retrieval = None
    for related_action in deployment.parent_relatedaction.all():
        if related_action.relationshiptypecv_id == 'Is retrieval for':
            retrieval = related_action

    return retrieval
