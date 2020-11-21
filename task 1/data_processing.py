class DataAggregation:
    @staticmethod
    def aggregate(students_list: list, rooms_list: list):
        dict_for_aggregate = {}
        for room in rooms_list:
            dict_for_aggregate[room['id']] = ['Room #' + str(room['id'])]
        for student in students_list:
            dict_for_aggregate[student['room']].append(student['name'])
        result = {}
        for value in dict_for_aggregate.values():
            result[value[0]] = value[1:]
        return result
