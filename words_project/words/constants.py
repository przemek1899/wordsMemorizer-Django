# -*- coding: utf-8 -*-

EN = 'EN'
IT = 'IT'
SP = 'SP'
FR = 'FR'

ENGLISH = 'ENGLISH'
SPANISH = 'SPANISH'
FRENCH = 'FRENCH'
ITALIAN = 'ITALIAN'

LANGUAGES = (
    (EN, ENGLISH),
    (IT, ITALIAN),
    (SP, SPANISH),
    (FR, FRENCH),
)

LANGUAGES_DICT = dict(LANGUAGES)

URLS_NOT_AUTHENTICATED = ('login', 'logout', 'register', 'restapi', 'api-auth', 'o', 'admin')
