from enum import Enum

class UserRole(Enum):
    ROLE_USER = 1
    ROLE_ADMIN = 2


class AccessKeyStatus(Enum):
    ACTIVATED = 'ACTIVATED'
    PENDING = 'PENDING'
    EXPIRED = 'EXPIRED'
    INVALIDATED = 'INVALIDATED'