import random
import string


import random


class FakeDynamicData:
    _characters = 'abcdxyzpfdqrhjon'
    _domain = '@gmail.com'

    def generate_random_email(self):
        local_part = ''.join(random.choices(self._characters, k=9))
        return local_part + self._domain

