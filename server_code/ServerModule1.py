import anvil.server

from kubernetes import client, config, watch

@anvil.server.callable
def list_pods():
  config.load_config()
  return client.CoreV1Api().list_pod_for_all_namespaces().to_dict()