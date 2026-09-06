from dataclasses import dataclass


@dataclass
class Person:
    name: str
    contact: str


@dataclass
class TimelineEvent:
    time: str
    description: str


@dataclass
class StolenItem:
    name: str
    value: float


@dataclass
class Case:
    case_id: str
    stolen_item: StolenItem
    people: list[Person]
    timeline: list[TimelineEvent]