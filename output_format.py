def get_output(anime_num):

    num_index = 0
    title_index = 1
    score_index = 2
    link_index = 3


    file = open('anime_list.txt', 'r', encoding='utf-8')

    all_data = file.readlines()
    splitted_data = all_data[anime_num - 1].split(' | ')

    file.close()

    return f'# {splitted_data[num_index]}\nTitle: {splitted_data[title_index]}\nScore: {splitted_data[score_index]}\nLink: {splitted_data[link_index]}'