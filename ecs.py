import boto3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
ecs_client = boto3.client('ecs')

def create_cluster(cluster_name):
    logging.info("Creating cluster: " + cluster_name)
    # Create ECS client
    try:
        if not get_clusters(cluster_name):
            response = ecs_client.create_cluster(
                clusterName=cluster_name
            )
            logging.debug(response)
            logging.info("Created cluster: " + response['cluster']['clusterName'])
        else:
            logging.warning("Cluster \"" + cluster_name + "\" already exists.")

    except BaseException as exe:
        logging.error(exe)


def get_clusters(cluster_name):
    try:
        response = ecs_client.list_clusters()
        cluster_arns = response['clusterArns']
        logging.debug(cluster_arns)

        for arn_cluster in cluster_arns:
            logging.debug(arn_cluster)
            if cluster_name in str(arn_cluster):
                return True
            else:
                return False

    except BaseException as exe:
        logging.error(exe)


