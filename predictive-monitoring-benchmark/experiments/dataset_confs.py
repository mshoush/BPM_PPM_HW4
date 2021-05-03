import os

case_id_col = {}
activity_col = {}
resource_col = {}
timestamp_col = {}
label_col = {}
pos_label = {}
neg_label = {}
dynamic_cat_cols = {}
static_cat_cols = {}
dynamic_num_cols = {}
static_num_cols = {}
filename = {}



logs_dir = "logs"
#### Production log settings ####
dataset = "turnaround_anon_sla"

filename[dataset] = os.path.join(logs_dir, "turnaround_anon_sla.csv")

case_id_col[dataset] = "Case ID"
activity_col[dataset] = "Activity"
#resource_col[dataset] = "Resource"
timestamp_col[dataset] = "time:timestamp"
label_col[dataset] = "label"
neg_label[dataset] = "regular"
pos_label[dataset] = "deviant"

# features for classifier
static_cat_cols[dataset] = []

static_num_cols[dataset] = ['SLA MIN', 'dur_min']
dynamic_cat_cols[dataset] = ["Activity",]
dynamic_num_cols[dataset] = ["wip"]

