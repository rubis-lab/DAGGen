# class Node(object):
#     def __init__(self, **kwargs):
#         # make a node with a task information
#         self.vid = kwargs.get('vid', 0)  # v_j
#         self.exec_t = kwargs.get('exec_t', 30.0)
#
#         # Node information
#         self.pred = []
#         self.succ = []
#         self.alpha = 0
#         self.beta = 0
#         self.isLeaf = False
#         self.deadline = -1
#         self.level = 0
#
#     def __str__(self):
#         return ''


class CPCBound:
    def __init__(self, task_set, core_num):
        self.task_set = task_set # G = (V,E)
        self.core_num = core_num # m
        self.critical_workload = [] # Theta_i
        self.total_workload = [] # W_i
        self.consumer_group = [] # F(theta_i)
        self.consumer_next_provider_group = [] # G(theta_i)
        self.finish_time_bound_arr = []
        self.alpha_arr = [] # alpha_i = alpha_arr[i]
        self.beta_arr = [] # beta_i = beta_arr[i]

    def __str__(self):
        return ''

    def get_critical_path(self):

        for i in range(len(self.task_set)):
            if self.task_set[i].level == 0:
                self.critical_workload.append(self.task_set[i])


    def construct_cpc_model(self, graph):
        providers = []

    def generate_finish_time_bound(self):
        self.finish_time_bound_arr = []

    def assign_priority(self, graph):

    def calculate_cpc_based_response_time_bound(self):
        self.calculate_critical_path()
        return self.critical_workload + (self.total_workload - self.critical_workload) / self.core_num