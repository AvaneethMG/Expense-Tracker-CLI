import json
from expense import Expense
class JsonHandiling:
    def __init__(self,filepath):
        self.path=filepath

    def load(self):
        with open(self.path) as f:
            data = json.load(f)
        return data

    def add(self, new_expense):
        data = self.load()          # existing list of dicts
        data.append(new_expense)    # add the new one
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def delete(self, expense_id):
        full_data = self.load()
        updated_data = []
        found = False

        for data in full_data:
            if data["id"] != expense_id:
                updated_data.append(data)
            else:
                found = True

        if found:
            with open(self.path, "w") as f:
                json.dump(updated_data, f, indent=2)

        return found

    def update(self, expense_id, **changes):
        full_data = self.load()
        found = False
        valid = False
        error = None

        for data in full_data:
            if data["id"] == expense_id:

                initial_data = data.copy()
                initial_data.update(changes)

                expense = Expense.from_dict(initial_data)
                valid, error = expense.validate()

                if valid:
                    data.update(changes)
                    found = True

                break

        if not found:
            return False, False

        if not valid:
            print(f"ERROR: {error}")
            return False, False

        with open(self.path, "w") as f:
            json.dump(full_data, f, indent=2)

        return True, True