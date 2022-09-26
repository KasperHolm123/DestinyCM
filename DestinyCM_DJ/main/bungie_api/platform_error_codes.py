from enum import Enum, auto

class PlatformErrorCodes(Enum):
    Unauthorized = 401
    ForumBodyCannotBeEmpty = 500
    TokenInvalid = 2000

print(PlatformErrorCodes.TokenInvalid.value)
