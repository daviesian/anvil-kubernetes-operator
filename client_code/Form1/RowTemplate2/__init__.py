from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.parent.raise_event("x-drain-deployment", item=self.item)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.parent.raise_event("x-delete-deployment", item=self.item)


