import numpy as np

# randomly assign people to table, while minimizing overlaps
"""
keep track of :
num of overlaps per meal
num iteration
"""

"""
1. randomly fill the arrays
2. calculate overlaps between meals
3  see if the count is minimal, if so, save it
"""

person_per_table = 8  # person per table
num_meals = 8 # number of meals to serve
num_total_people = 174 # number of people total
num_tables = num_total_people//person_per_table +1

zero_matrix = np.zeros((person_per_table*num_tables,person_per_table*num_tables))

min_array = None
min_overlap_count = num_meals *num_total_people * person_per_table

done = False
MAX_ITER = 1000

def create_array(num_tables, num_total_people):
    table_array = np.arange(1,num_total_people+1)
    np.random.shuffle(table_array)
    table_array = list(table_array)
    leftover = person_per_table*num_tables - num_total_people
    if leftover>0:
        for i in range(leftover):
            table_array.append(num_total_people+i)
    table_array= np.asarray(table_array).reshape(num_tables,-1)
    return table_array


def create_adjacency_matrix(table_array,zero_adjacency_matrix):
    for i in range(num_tables):
        for people in table_array[i]:
            for j in range(person_per_table):
                zero_adjacency_matrix[people,table_array[i][j]] += 1
    return zero_adjacency_matrix


def calc_overlaps(adjacency_matrix):

    overlap_count = 0
    dim= adjacency_matrix.shape[0]
    for i in range(dim):
        for j in range(dim):
            if adjacency_matrix[i][j]<num_tables*num_meals:
                if adjacency_matrix[i][j]>1:
                    overlap_count+= adjacency_matrix[i][j] -1
    return overlap_count

leftover = person_per_table*num_tables - num_total_people
loop_count = 0

while not done:
    print("lc",loop_count)
    loop_count+=1
    table_list = []
    adj_mat_list = []
    adj_mat = zero_matrix

    for i in range(num_meals):
        #print('num meals',i)
        # create array
        table_array = create_array(num_tables,num_total_people)
        # create adjacency matrix
        adj_mat += create_adjacency_matrix(table_array,zero_matrix)

        table_list.append(table_array)

        adj_mat_list.append(adj_mat_list)

    adj_mat = zero_matrix
    # calculate overlap
    overlap_count = calc_overlaps(adj_mat)

    print("overlap count: {}, min count:{}".format(overlap_count,min_overlap_count))
    #
    if overlap_count<min_overlap_count:
        min_array_list = table_list
        min_overlap_count = overlap_count
    if loop_count>MAX_ITER:
        done = True
    if overlap_count <= 1:
        done = True
#print
print("\nOverlap count: ",overlap_count)
for i, tables in enumerate(min_array_list):
    print("\nMeal {}\n".format(i+1))
    for table in tables:
        print(table)

