class todo:
    id: int
    title: str
    description: str
    color: str
    checked: bool

    def __init__(self, id: int, title: str, description: str, color: str):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
        self.checked = False # Every new item begins as unchecked
