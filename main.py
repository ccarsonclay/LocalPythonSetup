def greet():
  print('Hello World')

greet()


def pack():
  print('Dinner', 'lunch', 'breakfast')

pack()

lunch_items = ["tacos", "chips", "cereal"]

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)
                  
eat_lunch(lunch_items)
