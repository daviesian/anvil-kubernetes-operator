import anvil.server

from kubernetes import client, config, watch


@anvil.server.callable
def list_pods():
  config.load_config()
  return client.CoreV1Api().list_pod_for_all_namespaces().to_dict()

@anvil.server.callable
def deploy_anvil():
  config.load_config()
  api_instance = client.AppsV1Api()
  api_instance.create_namespaced_deployment(
    namespace="default",
    body=client.V1Deployment(
      metadata=client.V1ObjectMeta(
        name="platform-server"
      ),
      spec=client.V1DeploymentSpec(
        selector=client.V1LabelSelector(
          match_labels={"anvil":"platform-server"}
        ), 
        template=client.V1PodTemplateSpec(
          metadata=client.V1ObjectMeta(
            name="busybox",
            labels={"anvil": "platform-server"},
          ),
          spec=client.V1PodSpec(
            image_pull_secrets=[client.V1LocalObjectReference(name="anvil-registry")],
            containers=[
              client.V1Container(
                name="platform-server",
                image="anvil.works:4455/on-site/anvil-platform-server"
              ),
            ]
          )
        )
      )
    )
  )