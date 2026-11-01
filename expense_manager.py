from json_handiling import JsonHandiling
from expense import Expense
import json

class ExpenseManager() : 
    def __init__(self,filepath):
        self.Jfile = JsonHandiling(filepath)

    def get_all_expenses(self):
        whole_data=self.Jfile.load()
        return whole_data
    
    def add_expense(self,expense: Expense):
        is_valid,error=expense.validate()
        if not is_valid :
            print(f"Validation failed, Error {error}")
            return False
        
        expense_dict=expense.to_dict()
        self.Jfile.add(expense_dict)
        return True

    def delete_expense(self, expense_id):
        is_deleted = self.Jfile.delete(expense_id)
        #is_deleted is a boolean
        return is_deleted

    def update_expense(self, expense_id, **changes):
        valid,is_updated = self.Jfile.update(expense_id, **changes)
        #is_deleted is a boolean
        return valid,is_updated       

    def search_expense(self, expense_id):
        whole_data=self.Jfile.load()
        for data in whole_data:
            if data['id']==expense_id:
                # Use json.dumps to print the dictionary cleanly with indentation
                return True,data#(json.dumps(data, indent=2))

        return False,None
        
    def Total_spend(self):
        whole_data=self.Jfile.load()
        tot_expense=0
        for data in whole_data:
            tot_expense+= data["amount"]
        return tot_expense
    
    def Total_spend_bycategory(self):
        whole_data=self.Jfile.load()
        tot_spend_categoty={}
        for data in whole_data:
            if data['category'] not in tot_spend_categoty.keys():
                tot_spend_categoty[data['category']:None]
        for cat in tot_spend_categoty.keys():
            sum=0
            for data in whole_data:
                if cat == data['category']:
                    sum+= data['amount']
            tot_spend_categoty[cat : sum]

        return tot_spend_categoty  
                

    def filter_expenses_cat(self, category:str):
        whole_data=self.Jfile.load()
        filtered=[]
        for data in whole_data:
            if data['category']==category:
                filtered.append(data)
        if filtered : 
            return True,filtered
        else:
            return False,filtered

    def filter_expenses_date(self , date : str):
        whole_data=self.Jfile.load()
        filtered=[]
        for data in whole_data:
            if data['date']==date:
                filtered.append(data)
        if filtered : 
                return True,filtered
        else:
                return False,filtered

