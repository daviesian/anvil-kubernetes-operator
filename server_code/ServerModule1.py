import anvil.server

from kubernetes import client, config, watch


@anvil.server.callable
def list_objects(ns="default"):
  config.load_config()

  clusters = client.CustomObjectsApi().list_namespaced_custom_object("anvil.works", "v1", ns, "anvilclusters")['items']
  deployments = client.CustomObjectsApi().list_namespaced_custom_object("anvil.works", "v1", ns, "anvildeployments")['items']

  
  return {
    "clusters": clusters,
    "deployments": deployments,
  }

@anvil.server.callable
def create_cluster(new_cluster, ns="default"):
  config.load_config()

  if not new_cluster['name']:
    raise Exception("Cluster must have a name")
    
  client.CustomObjectsApi().create_namespaced_custom_object(
      group="anvil.works",
      version="v1",
      namespace=ns,
      plural="anvilclusters",
      body={
      "apiVersion": "anvil.works/v1",
      "kind": "AnvilCluster",
      "metadata": { "name": new_cluster['name'] },
      "spec": {
        "httpPort": 30000,
        "origin": new_cluster['origin'],
        "licenceKey": new_cluster['licence_key']
      },
  })

@anvil.server.callable
def create_deployment(new_deployment, ns="default"):
  config.load_config()

  if not new_deployment['name']:
    raise Exception("Deployment must have a name")

  client.CustomObjectsApi().create_namespaced_custom_object(
      group="anvil.works",
      version="v1",
      namespace=ns,
      plural="anvildeployments",
      body={
      "apiVersion": "anvil.works/v1",
      "kind": "AnvilDeployment",
      "metadata": { "name": new_deployment['name'] },
      "spec": {
        "clusterName": new_deployment['cluster_name'],
        "platformServerCount": new_deployment['platform_server_count'],
        "version": new_deployment['version'],
      },
  })


@anvil.server.callable
def delete_cluster(name, ns):
  config.load_config()

  client.CustomObjectsApi().delete_namespaced_custom_object(
      group="anvil.works",
      version="v1",
      namespace=ns,
      plural="anvilclusters",
      name=name,
  )


@anvil.server.callable
def delete_deployment(name, ns):
  config.load_config()

  client.CustomObjectsApi().delete_namespaced_custom_object(
      group="anvil.works",
      version="v1",
      namespace=ns,
      plural="anvildeployments",
      name=name,
  )


@anvil.server.callable
def drain_deployment(name, ns):
  config.load_config()

  client.CustomObjectsApi().patch_namespaced_custom_object(
      group="anvil.works",
      version="v1",
      namespace=ns,
      plural="anvildeployments",
      name=name,
      body={
      "spec": {
        "active": False
      },
  })
