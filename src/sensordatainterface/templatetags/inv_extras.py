from django import template
from django.template.defaultfilters import stringfilter

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
