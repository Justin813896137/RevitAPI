# -*- coding: utf-8 -*-


# Imports

from Autodesk.Revit.DB import *

import clr
clr.AddReference('System')
from System.Collections.Generic import List

from Autodesk.Revit.DB import *

# pyRevit
from pyrevit import revit, forms                                        # import pyRevit modules. (Lots of useful features)


# Variables
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document

#Reusable Snippets


def  get_selected_elements(filter_types = None):

    '''e.g.
    sel_walls = get_selected_elements([wall])
    '''

    selected_element_ids = uidoc.Selection.GetElementIds()
    selected_elements    = [doc.GetElement(e_id) for e_id in selected_element_ids]

    # Filter Selection (Optionally)
    if filter_types:
        return [el for el in selected_elements if type(el) in filter_types]
    return selected_elements