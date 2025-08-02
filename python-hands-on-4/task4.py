"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}
guest = {"Guest": "Daisy"}
participants.update(guest)
print("Guest participant Daisy was added to dictionary", participants)

participants.pop("Student")
print("Student participant was removed from dictionary", participants)

record = []
record.append(participants)
print("New participant was added to dictionary", record)
participants.pop("Student", None)
print("Recent added student was removed from the system", participants)

# print(participants_snapshot)
# print(participants)
