class Expense:
    #expense = {id,amount,category,date,description}
    def __init__(self,id,amount,category,date,description):
        self.id = id  # Instance attribute
        self.amount = amount
        self.category=category
        self.date=date
        self.description=description


    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
            }

    @classmethod
    def from_dict(cls, dic):
        return cls(
            dic["id"],
            dic["amount"],
            dic["category"],
            dic["date"],
            dic["description"]
        )

    def __repr__(self):
        # Returns a clean, readable string showing the object's data
        return f"Expense(id={self.id}, amount={self.amount}, category='{self.category}',date='{self.date}',description='{self.description}')"

    def validate(self):
        if self.id < 1:
            return False, "id_error"

        if self.amount <= 0:
            return False, "amount_error"

        if not self.category.strip():
            return False, "category_error"

        return True, None