from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from ..CreateCluster import CreateCluster
from ..CreateDeployment import CreateDeployment

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.clusters = []
    self.deployments = []
    self.init_components(**properties)

    self.cluster_panel.add_event_handler("x-delete-cluster", self.on_delete_cluster)
    self.deployments_panel.add_event_handler("x-drain-deployment", self.on_drain_deployment)
    self.deployments_panel.add_event_handler("x-delete-deployment", self.on_delete_deployment)
    
    self.update()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_cluster = {}
    if alert(CreateCluster(item=new_cluster), title="Create Cluster", buttons=[("Create", True), ("Cancel", False)]):
      anvil.server.call("create_cluster", new_cluster)

  def on_delete_cluster(self, item, **event_args):
    item = item['metadata']
    if alert(f"Are you sure you want to delete cluster '{item['name']}'?", title="Delete cluster?", buttons=[("Delete", True), ("Cancel", False)]):
      anvil.server.call('delete_cluster', item['name'], item['namespace'])
      
  def on_delete_deployment(self, item, **event_args):
    item = item['metadata']
    if alert(f"Are you sure you want to delete deployment '{item['name']}'?", title="Delete deployment?", buttons=[("Delete", True), ("Cancel", False)]):
      anvil.server.call('delete_deployment', item['name'], item['namespace'])

  def on_drain_deployment(self, item, **event_args):
    if alert(f"Are you sure you want to drain deployment '{item['metadata']['name']}'?", title="Drain deployment?", buttons=[("Drain", True), ("Cancel", False)]):
      anvil.server.call('drain_deployment', item['metadata']['name'], item['metadata']['namespace'])
    

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.update()

  def update(self):
    with anvil.server.no_loading_indicator:
      objs = anvil.server.call('list_objects')
      self.clusters = [p for p in objs['clusters']]
      self.deployments = [p for p in objs['deployments']]
    self.refresh_data_bindings()

  def create_deployment_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_deployment = {}
    if alert(CreateDeployment(item=new_deployment), title="Create Deployment", buttons=[("Create", True), ("Cancel", False)]):
      anvil.server.call("create_deployment", new_deployment)
    


