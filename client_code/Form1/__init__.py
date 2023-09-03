from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.pods = []
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("create_cluster")

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.update_pods()

  def update_pods(self):
    with anvil.server.no_loading_indicator:
      self.pods = [p['metadata'] for p in anvil.server.call('list_pods')['items']]
    self.refresh_data_bindings()

