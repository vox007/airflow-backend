import airflow_client

from pprint import pprint
from airflow_client.client.api import config_api
from airflow_client.client.api import dag_api

configuration = airflow_client.client.Configuration(
    host="http://localhost:8080/api/v1",
    username='airflow',
    password='airflow',
)


def get_config():
    with airflow_client.client.ApiClient(configuration) as api_client:

        api_instance = dag_api.DAGApi(api_client)
        dag_id = "first_dag"
        try:
            api_response = api_instance.get_dag(dag_id)
            print(api_response)
        except airflow_client.client.ApiException as e:
            print("Exception when calling ConfigApi->get_config: %s\n" % e)


if __name__ == "__main__":
    get_config()

