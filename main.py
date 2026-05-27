import flet as ft
from flet import Page, Icons, TextField, Checkbox, FloatingActionButton
import os
from dotenv import load_dotenv


def main(page: Page):
    # Sets up page
    page.title = 'Meal Planner'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 300
    page.expand=True


    # @add_meal = adds a Text element with value from texInput
    counter = 0
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday', 7: 'Press reset to start again'}

    class Meal():
        def add_meal(e):
            nonlocal counter
            # page.add(ft.Text(meal_input.value))
            meal_list.controls.append(ft.Text(meal_input.value))
            meal_input.value=''
            counter = counter + 1
            meal_input.hint_text = f'Enter meal for {days[counter]}'
            if counter > 6:
                meal_input.hint_text = 'Press reset to enter a new meal for the week'
                meal_input.disabled=True 
                add_meal_btn.disabled=True
                add_meal_btn.bgcolor='grey200'
                reset_btn.disabled=False
                reset_btn.bgcolor='green200'
                # page.add(ft.FloatingActionButton(icon=Icons.RESET_TV))
                counter = 0  
            print(counter)
            page.update()

        def reset_meal(e):
            nonlocal counter
            counter = 0
            meal_input.hint_text = 'Enter meal name for Monday'
            meal_input.disabled=False
            add_meal_btn.disabled=False
            add_meal_btn.bgcolor='green200'
            reset_btn.disabled=True
            reset_btn.bgcolor='grey200'
            # deletes the contents of the meal_list Column
            meal_list.controls.clear()
            page.update()
        
    

    # define label elements
    app_title = ft.Text('Meal Planner', size=24, weight=ft.FontWeight.BOLD )
    app_header = ft.Text('Enter meal name for each of the days')
    meal_list = ft.Column()


    # define input elements
    try:
        add_meal_btn = ft.FloatingActionButton(icon=Icons.ADD, on_click=Meal.add_meal)
        meal_input = ft.TextField(hint_text=f'Enter the meal for {days[counter]}')
        reset_btn = ft.FloatingActionButton(icon=Icons.RESET_TV, disabled=True, bgcolor='grey200', on_click=Meal.reset_meal)
    except:
        print('Something went wrong')


    page.add(app_title, app_header, meal_input, add_meal_btn,  reset_btn, meal_list )
 


ft.run(main)
