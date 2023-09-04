from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def delete_cluster_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.parent.raise_event("x-delete-cluster", item=self.item)

