import argparse
import os

from task_gen.dag_gen import Task, DAGGen
from sched.classic import ClassicBound
from sched.cpc_based import CPCBound

BATCH_SIZE = 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    for i in range(BATCH_SIZE):
        # Generate Graph for one DAG
        dag_param_1 = {
            "task_num" : [20, 0],
            "depth" : [5.0, 1.0],
            "exec_t" : [50.0, 30.0],
            "start_node" : [1, 0],
            "extra_arc_ratio" : 0.2
        }

        Task.idx = 0
        DAG = DAGGen(**dag_param_1)

        # TODO : Implement class bound algorithm
        classic = ClassicBound(DAG.task_set)
        classic_bound = classic.calculate_bound()        

        print(DAG)
        print(classic_bound)

        # Generate Graph for CPC Model
        dag_param_cpc = {
            "node_num": [10, 0],
            "depth": [5.0, 0],
            "exec_t": [50.0, 30.0],
            "start_node": [1, 0],
            "end_node": [1, 0],
            "extra_arc_ratio": 0.2
        }
        CPC_DAG = DAGGen(**dag_param_cpc)
        cpc_model = CPCBound(CPC_DAG, 2)
        print(cpc_model.task_set)
