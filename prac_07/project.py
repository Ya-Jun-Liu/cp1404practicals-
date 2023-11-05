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

    def get_priority(self):
        """Get priority."""
        return self.priority

    def get_start_date(self):
        """Get start date."""
        return self.start_date

    def is_complete(self):
        """Set complete percentage."""
        return self.complete_percentage == 100

    def is_not_complete(self):
        """Set complete."""
        return not self.is_complete()
