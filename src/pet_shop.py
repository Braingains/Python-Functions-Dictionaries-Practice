# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(shop):
    return shop ["name"]

def get_total_cash(cash):
    return cash ["admin"]["total_cash"]

def add_or_remove_cash(current_cash, cash_added_or_removed):
    current_cash["admin"]["total_cash"] += cash_added_or_removed
#this works for both q3 and 4, because adding a negative is the same as taking away

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(current_pets_sold, additional_pets_sold):
    current_pets_sold["admin"]["pets_sold"] += additional_pets_sold

def get_stock_count(current_stock):
    return len(["pets":x])
    # stock_of_pets = 0
    # for pet in ["pets"]:
    #     stock_of_pets = stock_of_pets + 
    # stock_of_pets = current_stock
    # return current_stock