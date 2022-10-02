import data_input


def to_do(action):
    if action == 1:
        data_input.new_student()
    if action == 2:
        data_input.new_teacher()
    if action == 3:
        data_input.find_student()
    if action == 4:
        data_input.find_teacher()
    if action == 5:
        data_input.get_timetable()
