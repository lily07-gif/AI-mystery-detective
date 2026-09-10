from models import Case, Person, StolenItem, TimelineEvent, Evidence
from evidence import analyze_evidence


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

# Create an evidence object
evidence = Evidence(
    evidence_id="E001",
    description="Security camera shows Arun entering the building",
    source="Security Camera"
)

# Create the investigation case
case = Case(
    case_id="CASE-001",
    stolen_item=item,
    people=[arun],
    timeline=[event],
    evidence=[evidence]
)

# Display the case
print(case)

# Analyze the evidence
analyze_evidence(evidence)
