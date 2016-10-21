#usr/bin/env python

'''
Syntax errors: eg like the extra . in my_list..append(foo)
Logical Errors: divide by 0,
systemic errors can also be checked for. Perhaps the program always crashes when the user inputs a number greater than 100, or hangs if the web site it's retrieving is not available
'''

import pytest
import film_search

def test_film_search():
    ''' Tests that TODO '''
    response = film_search.search_words_return_titles("Jaws")
    print response
    assert "Revenge" in response.read()
