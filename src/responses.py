from random import choice
from zebu_dict import zebu


def handle_response(message) -> str:
    r = 1
    all = ""
    indexes = [i for i in range(1, 53)]
    p_message = message.lower()[1:]

    if p_message == "zebu":
        key = choice(list(zebu.keys()))
        print(key)
        return key + "\n" + zebu[key]

    if p_message == "all":
        for i, x in zebu.items():
            all += f"{r}. " + i + "\n"
            r += 1
        return all
    if p_message == "help":
        commands = "\nZEBU COMMANDS:\n" + "-" * 80 + ("\n/zebu = random hypnotic language pattern\n/all = "
                                                      "all the patterns\n/number = specific language pattern (i.e: /32) note: "
                                                      "there are 52 total patterns\n") + "-" * 80
        return commands
    try:
        if int(p_message) in indexes:
            dict_items = list(zebu.items())

            return dict_items[int(p_message) - 1][0] + '\n' + dict_items[int(p_message) - 1][1]
    except ValueError:
        pass
