from pyscript import display, document

def get_nickname(e):
    nickname = document.getElementById("nordic_countries") #gets the users inputted country
    nickname_result = nickname.value #gets the value of the users inputted country

    display(f'Nickname of this Nordic Country is "{nickname_result}"', target='display_nickname', append=False)

