from collections import namedtuple

Resolver = namedtuple("Resolve", "path name kwargs")


valid_resolvers = [
    Resolver(
        path="/",
        name="cv",
        kwargs={},
    ),
    Resolver(
        path="/pdf/",
        name="pdf",
        kwargs={},
    ),
]
