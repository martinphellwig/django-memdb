"""
Mixins
"""

# pylint: disable=too-few-public-methods
class InMemoryDB:
    "We will use this more like a tag."
    pass

class PeristentInMemoryDB(InMemoryDB):
    "This journals the insert/update/delete operations."
    pass