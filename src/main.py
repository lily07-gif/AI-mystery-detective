from models import Case, Person, StolenItem, TimelineEvent


# Create the stolen item
item = StolenItem(
    name="Diamond Necklace",
    value=500000
)

# Create a person
arun = Person(
    name="Arun",
    contact="9876543210"
)

# Create a timeline event
event = TimelineEvent(
    time="22:15",
    description="Arun entered the building"
)

# Create the investigation case
case = Case(
    case_id="CASE-001",
    stolen_item=item,
    people=[arun],
    timeline=[event]
)

# Display the case
print(case)