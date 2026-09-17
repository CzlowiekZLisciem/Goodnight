class Routine:
    def __init__(self):
        self.items = {}

    # Adding a task to the list
    def add_item(self, item_id, name):
        self.items[item_id] = {
            'name': name,
            'completed': False
        }

    # Compleating an item from the list
    def complete_item(self, item_id):
        if item_id not in self.items:
            raise ValueError(f'Unknown item in the routine; {item_id}')
        
        self.items[item_id]['completed'] = True

    # Calculationg total things done on the daily list
    def get_progress(self):
        if not self.items:
            return 0
        completed_items = sum(
            item['completed'] for item in self.items.values()
        )

        return (completed_items / len(self.items)) * 100

    def is_complete(self):
        return bool(self.items) and all(
        item["completed"] for item in self.items.values()
    )
    
