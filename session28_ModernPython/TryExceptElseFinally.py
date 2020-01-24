try:
    # The Code you care about
    print('I really want to print this line!')
    pass
except OSError as e:
    # The things to do if stuff goes wrong one way
    print('Oh no a OSError occurred:', e)
except KeyError as e:
    # The things to do if stuff goes wrong another way
    print('Where are my Keys?:', e)
else:
    # this will be executed if no exceptions are raised
    print('Luckily nothing bad happend!')
finally:
    # This will be executed regardless whether exceptions are raised
    print('This will be printed in any case.')
