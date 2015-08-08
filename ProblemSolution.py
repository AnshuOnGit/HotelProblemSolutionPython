__author__ = 'anshu'

#assumption hotel_id are always integere
#value meal will always be cheaper compared to the scenario where in items are bought seperately
#in input  list of items also one item occurs only once

import itertools,ParseInputCSV

class PriceList:
    def __init__(self):
        self.price=0.0
        self.list_of_items=[]

class MenuItem:
    def __init__(self):
        self.hotel_id=0
        self.menu_item_price_list = PriceList()

input_list=['i2','i3','i4']

def getListOfMenuItems():
    menuItems=[]
    for line in ParseInputCSV.parseInputCSV():
        line1= line.strip('\n')
        values= line1.split(',')
        menuItem = MenuItem()
        menuItem.hotel_id=values[0]
        menuItem.menu_item_price_list.price=values[1]
        menuItem.menu_item_price_list.list_of_items=values[2:]
        menuItems.append(menuItem)
    return menuItems

menuItems = getListOfMenuItems()
listOfHotels =[]

def getListOfHotels():
    global menuItems, listOfHotels
    for i in menuItems:
        if(not listOfHotels.__contains__(int(i.hotel_id))):
            listOfHotels.append(int(i.hotel_id))
    return listOfHotels

def checkIfDemandedlistCanBeFullfilledFromHotel(input_list,hotel):
    listOfAllItems = []
    global menuItems
    for j in menuItems:
        if(j.hotel_id == str(hotel)):
            listOfAllItems = listOfAllItems + j.menu_item_price_list.list_of_items
    if(set(listOfAllItems).issuperset(set(input_list))):
        return True
    else:
        return False

def getSimplePriceForItemListFromaHotel(input_list,hotel):
    global menuItems
    price = 0.0
    listOfMenuItemsForaParticularHotel =[]
    for j in menuItems:
        if(j.hotel_id == str(hotel)):
            listOfMenuItemsForaParticularHotel.append(j)
    for i in input_list:
        for k in listOfMenuItemsForaParticularHotel:
            if(len(k.menu_item_price_list.list_of_items) == 1):
                if(i == k.menu_item_price_list.list_of_items[0]):
                    price = price + float(k.menu_item_price_list.price)
    return price



def getMinimumPriceForItemListFromaHotel(input_list,hotel):
    global menuItems
    minimalPrice = getSimplePriceForItemListFromaHotel(input_list,hotel)
    listOfMenuItemsForaParticularHotel =[]
    for j in menuItems:
        if(j.hotel_id == str(hotel)):
            listOfMenuItemsForaParticularHotel.append(j)
    directorList= list(range(0,len(listOfMenuItemsForaParticularHotel)))

    for L in range(1,len(directorList) + 1):
        for subset in itertools.combinations(directorList, L):
            compareList = []
            price = 0.0
            for i in list(subset):
                compareList = compareList + listOfMenuItemsForaParticularHotel[i].menu_item_price_list.list_of_items
                price = price + float(listOfMenuItemsForaParticularHotel[i].menu_item_price_list.price)
            if(set(compareList).issuperset(set(input_list)) and price < minimalPrice):
                minimalPrice = price
    return minimalPrice

if(__name__ == '__main__'):
    inputPrompt = raw_input("Enter the list of food items you want to order seperated by space: \n")
    input_list1 = list(inputPrompt.split(' '))
    #print input_list1
    output_list=[1,float("inf")]
    for hotel in getListOfHotels():
        if(checkIfDemandedlistCanBeFullfilledFromHotel(input_list1,hotel)):
            minimal_price =getMinimumPriceForItemListFromaHotel(input_list1,hotel)
            if(minimal_price < output_list[1]):
                output_list[0] = hotel
                output_list[1] = minimal_price

    print output_list










