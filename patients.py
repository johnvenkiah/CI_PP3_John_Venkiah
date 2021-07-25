def suggest_appointment():
    """
    Function to let patient continue with booking or go back,
    for example if a staff  member entered the wrong input.
    """

    print("\nLet's find you an appointment.\n")
    print('Your data will be saved to our database upon confirmation.\n')
    book_or_back = input(
        'Press "1" to continue or any other key to go back.\n\n'
        )

    if book_or_back == '1':
        get_month(year)

    else:
        welcome_screen()