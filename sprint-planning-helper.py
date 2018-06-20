#! python 3
# planning_helper.py - finding the most efficient set of tasks to be taken from the file

import csv
from sys import argv, stdout


def collecting_data_from_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        data_from_csv = csv.DictReader(csvfile)

        task_id = []
        story_points = {}
        KSP = {}

        for row in data_from_csv:
            task_id.append(int(row['task_id']))
            story_points.update({int(row['task_id']): int(row['story_points'])})
            KSP.update({int(row['task_id']): int(row['KSP'])})

    return task_id, story_points, KSP


def initialize_result_array(task_id, velocity):
    result = []
    for i in range(len(task_id) + 1):
        result.append([0 for j in range(velocity + 1)])

    return result


def knapsack(array,data_from_csv, velocity):
    story_points = data_from_csv[1]
    KSP = data_from_csv[2]
    left_id = len(story_points)
    output_tasks = []

    for ids in range(left_id + 1):
        for v in range(velocity + 1):
            if ids == 0 or v == 0:
                array[ids][v] = 0
            elif story_points[ids - 1] <= v:
                array[ids][v] = max(KSP[ids - 1] + array[ids - 1][v - story_points[ids - 1]], array[ids - 1][v])
            else:
                array[ids][v] = array[ids-1][v]

    result = array[left_id][velocity]

    v = velocity
    for ids in range(left_id, 0, -1):
        if result <= 0:
            break
        if result == array[ids - 1][v]:
            continue
        else:
            output_tasks.append(ids-1)
            result -= KSP[ids-1]
            v -= story_points[ids-1]

    return output_tasks


def conv_list_to_string(output_tasks_list):
    output_tasks_list = sorted(output_tasks_list)
    output_tasks = ', '.join(map(str, output_tasks_list))

    return output_tasks



if __name__ == '__main__':
    arguments = argv
    file_name = arguments[1]
    velocity = int(arguments[2])

    data_from_csv = collecting_data_from_csv(file_name)
    task_id = data_from_csv[0]

    array = initialize_result_array(task_id, velocity)
    output_tasks_list = knapsack(array, data_from_csv, velocity)
    output_tasks = conv_list_to_string(output_tasks_list)
    stdout.write(output_tasks)