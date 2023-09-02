from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.pods = [p['metadata'] for p in anvil.server.call('list_pods')['items']]
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # for p in pods['items']:
    #   print(f"{p['metadata']['namespace']}: {p['metadata']['name']}")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("deploy_anvil")


