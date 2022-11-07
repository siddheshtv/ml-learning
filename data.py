data = [
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

    for row_tuple in data:
        for key in row_tuple:
            if key != 'id':
                bins[key].add(row_tuple[key])
    print(bins)

scan_data()