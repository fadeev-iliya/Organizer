file = open("Actions.txt", encoding="utf-8")
actions = file.read().splitlines()
file.close()

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
    for act in actions:
        if act in text:
            return "Пойти " + act


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
