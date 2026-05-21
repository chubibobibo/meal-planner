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
    counter = 1
    
    def add_meal(e):
        nonlocal counter
        days = {1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        page.add(ft.Text(meal_input.value))
        meal_input.value=''
        meal_input.hint_text = f'Enter meal for {days[counter]}'
        counter = counter + 1
        print(counter)
        page.update()
        
    

    # define label elements
    app_title = ft.Text('Meal Planner', size=24, weight=ft.FontWeight.BOLD )
    app_header = ft.Text('Enter meal name for each of the days')
    page.update()


    
    # define input elements
    add_meal_btn = ft.FloatingActionButton(icon=Icons.ADD, on_click=add_meal)
    meal_input = ft.TextField(hint_text=f'Enter the meal for Monday')


  

    # add elements to page
    page.add(app_title, app_header, meal_input, add_meal_btn, )


ft.run(main)
