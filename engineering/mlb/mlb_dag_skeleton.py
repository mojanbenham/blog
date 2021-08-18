# import necessary libraries
import airflow 

from airflow import DAG
from airflow.operators.python import PythonOperator

# define DAG
mlb_dag=DAG(
    dag_id="baseball_info",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)

# define tasks
def _get_team():
    print("_get_team task is running.")

def _get_players():
    print("_get_players task is running.")

def _get_games():
    print("_get_games task is running.")

def _write_file():
    print("_write_file task is running.")

# write operators
get_team = PythonOperator(
    task_id = "get_team",
    python_callable=_get_team,
    dag=mlb_dag,
)

get_players = PythonOperator(
    task_id = "get_players",
    python_callable=_get_players,
    dag=mlb_dag,
)

get_games = PythonOperator(
    task_id = "get_games",
    python_callable=_get_games,
    dag=mlb_dag,
)

write_file = PythonOperator(
    task_id = "write_file",
    python_callable=_write_file,
    dag=mlb_dag,
)

# structure dag
get_team >> [get_players, get_games] >> write_file
