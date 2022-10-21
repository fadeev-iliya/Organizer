# Чтение файла с действиями
file = open("Actions2.txt", encoding="utf-8")
beginActions = file.read().splitlines()
actions = []
for elem in beginActions:
    action_A = elem.split(",")
    actions.append([action_A[0],action_A[1:]])
file.close()

# Временные настройки
hour_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
hour_word = ["часов ", "часа ", "час "]
minute_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
               '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
               '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
               '51', '52', '53', '54', '55', '56', '57', '58', '59']
minute_word = ["минута", "минут", "минуты"]

evening = ["вечера", "дня", "вечерком", "вечером","днем"]
morning = ["ночи", "утра"]


def action(text):
    for act_all in actions:
        for act in act_all[1]:
            if act in text:
                return act_all[0]


def time_function(text):
    for hour in hour_list:
        for minute in minute_list:
            for elem in morning:
                if f" {hour}:{minute} {elem}" in text:
                    return f" {hour}:{minute}"
            for elem in evening:
                if f" {hour}:{minute} {elem}" in text and hour < 12:
                    return f" {hour + 12}:{minute}"
                elif f" {hour} {elem}" in text and hour >= 12:
                    return f" {hour}:{minute}"
            if f" {hour}:{minute} " in text:
                return f" {hour}:{minute}"
        for elem in morning:
            if f" {hour} {elem}" in text:
                return f" {hour}:00"
        for elem in evening:
            if f" {hour} " in text and f" {elem}" in text and hour < 12:
                return f" {hour + 12}:00"
            elif f" {hour} " in text and f" {elem}" in text and hour >= 12:
                return f" {hour}:00"
        if f" {hour} " in text:
            return f" {hour}:00"

def find_event(text):
    words = text.split(" ")
    actA, time = [""], [""]

    for i in range(1, len(words)):
        reduce = f" {words[i - 1]} {words[i]} "
        if action(reduce) is not None:
            actA.append(action(reduce))
        if time_function(reduce) is not None:
            reduce = f" {words[i - 1]} {words[i]} {words[i + 1]}"
            if time_function(reduce) != time[-1]:
                time.append(time_function(reduce))

    for i in range(1, min(len(actA), len(time))):
        print(f"Action: {actA[i]} | Time: {time[i]}")