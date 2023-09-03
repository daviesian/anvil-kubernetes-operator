import anvil.server

from kubernetes import client, config, watch


@anvil.server.callable
def list_pods():
  config.load_config()
  return client.CoreV1Api().list_pod_for_all_namespaces().to_dict()

@anvil.server.callable
def create_cluster():
  config.load_config()

  client.CustomObjectsApi().create_namespaced_custom_object(
      group="anvil.works",
      version="v1",
      namespace="default",
      plural="anvilclusters",
      body={
      "apiVersion": "anvil.works/v1",
      "kind": "AnvilCluster",
      "metadata": { "name": "cluster-1" },
      "spec": {},
  })