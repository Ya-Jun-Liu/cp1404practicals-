def date_to_str(date):
    return date.strftime("%d/%m/%Y")


class Project:
    """Store project information."""

    def __init__(self, name, start_date, priority,
                 cost_estimate, complete_percentage):
        """Project initial information."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.complete_percentage = complete_percentage

    def __str__(self):
        """Return string format."""
        return f"{self.name}, " + \
            f"start: {date_to_str(self.start_date)}, " + \
            f"priority {self.priority}, " + \
            f"estimate: ${self.cost_estimate}, " + \
            f"completion {self.complete_percentage}%"

    def __lt__(self, other):
        """Compare priority."""
        return self.priority < other.priority
