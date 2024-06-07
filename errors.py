# -*- coding: utf-8 -*-

class runsAmountError(Exception):
    def __str__(self):
        return "\42Runs per participant\42 needs to be 1 or multiple of 2"
class sameParticipantsError(Exception):
    def __str__(self):
        return "There can't be 2 or more same participants"
class tooManyNobodysError(Exception):
    def __str__(self):
        return "Program has generated too many Nobodys (>5). Try to change the number of karts or the minimum number of karts"
class noResultsError(Exception):
    def __str__(self):
        return "No results were found"