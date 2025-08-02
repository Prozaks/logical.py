"""
Task 1: Music Concert Ticketing System
During the Jos Summer Music Concert, ticket sales were recorded as follows:

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

Later in the day:
- A new "Backstage" experience with 10 tickets was introduced.
- The "Student" category sold out completely.
- The team wanted to keep a record of the day’s sales before preparing for next week’s concert.
"""

tickets = {}
tickets = {"VIP": 50, "Regular": 150, "Student": 75}
backstage = {"Backstage": 10}
tickets.update(backstage)
print("Backstage discovered 10 tickets and was added to the tickets", tickets)
tickets.pop("Student")
print("Students ticket was sold completely and was removed from the dictionary", tickets)
print(tickets)
