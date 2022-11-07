data_json = [
    {
        'id': 1,
        'age': 'youth',
        'income': 'high',
        'student': 'no',
        'credit_rating': 'fair',
        'buys_computer': 'no',
    },
    {
        'id': 2,
        'age': 'youth',
        'income': 'high',
        'student': 'no',
        'credit_rating': 'excellent',
        'buys_computer': 'no',
    },
    {
        'id': 3,
        'age': 'middle_aged',
        'income': 'high',
        'student': 'no',
        'credit_rating': 'fair',
        'buys_computer': 'yes',
    },
    {
        'id': 4,
        'age': 'senior',
        'income': 'medium',
        'student': 'no',
        'credit_rating': 'fair',
        'buys_computer': 'yes',
    },
    {
        'id': 5,
        'age': 'senior',
        'income': 'high',
        'student': 'yes',
        'credit_rating': 'fair',
        'buys_computer': 'yes',
    },
    {
        'id': 6,
        'age': 'senior',
        'income': 'high',
        'student': 'yes',
        'credit_rating': 'excellent',
        'buys_computer': 'no',
    },
    {
        'id': 7,
        'age': 'middle_aged',
        'income': 'high',
        'student': 'yes',
        'credit_rating': 'excellent',
        'buys_computer': 'yes',
    },
    {
        'id': 8,
        'age': 'youth',
        'income': 'medium',
        'student': 'no',
        'credit_rating': 'fair',
        'buys_computer': 'no',
    },
    {
        'id': 9,
        'age': 'youth',
        'income': 'high',
        'student': 'yes',
        'credit_rating': 'fair',
        'buys_computer': 'yes',
    },
    {
        'id': 10,
        'age': 'senior',
        'income': 'medium',
        'student': 'yes',
        'credit_rating': 'fair',
        'buys_computer': 'yes',
    },
    {
        'id': 11,
        'age': 'youth',
        'income': 'medium',
        'student': 'yes',
        'credit_rating': 'excellent',
        'buys_computer': 'yes',
    },
    {
        'id': 12,
        'age': 'middle_aged',
        'income': 'medium',
        'student': 'no',
        'credit_rating': 'excellent',
        'buys_computer': 'yes',
    },
    {
        'id': 13,
        'age': 'middle_aged',
        'income': 'high',
        'student': 'yes',
        'credit_rating': 'fair',
        'buys_computer': 'yes',
    },
    {
        'id': 14,
        'age': 'senior',
        'income': 'medium',
        'student': 'no',
        'credit_rating': 'excellent',
        'buys_computer': 'no',
    },
]

def scan_data():
    bins = {
        'age': set(),
        'income': set(),
        'student': set(),
        'credit_rating': set(),
        'buys_computer': set(),
    }

    for row_tuple in data_json:
        for key in row_tuple:
            if key != 'id':
                bins[key].add(row_tuple[key])
    print(bins)

scan_data()

def create_tree():
    bins = scan_data()

    decision_tree_start_node = Node()
    decision_tree_start_node.data = data_json
    attribute_list = []

    for i in bins:
        attribute_list.append(custom_bin)
    
    create_nodes(decision_tree_start_node, bins, attribute_list, 0)
    print_decision_tree_bfs(decision_tree_start_node)
    print(decision_tree_start_node)


class Node:
    data = list(),
    attribute = " ",
    neighbors = list(),
    tuple_ids = list()

    def __init__(self) -> None:
        self.data = []
        self.attribute = []
        self.neighbors = []
        self.tuple_ids = []

def print_decision_tree_bfs():
    
