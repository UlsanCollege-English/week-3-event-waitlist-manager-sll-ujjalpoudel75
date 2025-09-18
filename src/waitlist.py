
### `/src/waitlist.py` (starter)

class _Node:
    __slots__ = ("name", "next")
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

class Waitlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Return number of people on the waitlist."""
        ...

    def to_list(self):
        """Return names from head to tail as a Python list."""
        ...

    def join(self, name):
        """Append name at the tail (O(1))."""
        ...

    def find(self, name):
        """Return True if name exists, else False."""
        ...

    def cancel(self, name):
        """Remove first occurrence; return True if removed."""
        ...

    def bump(self, name):
        """Move first occurrence to the head; return True if moved."""

