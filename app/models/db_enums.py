from enum import Enum


class SubscriptionType(str, Enum):
    STANDART: str = "standart"
    PREMIUM: str = "premium"
