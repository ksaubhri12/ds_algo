import json
from itertools import islice


def lambda_handler(event, context):
    # TODO implement
    return {
        'headers': {
            "Content-Type": "application/json",

        },
        'statusCode': 200,
        'body': json.dumps(str(type(event['body'])))
    }


def get_word_count(word: str):
    try:
        small_case = word.lower()
        final_dict = {}
        for char in small_case:
            if char in final_dict:
                final_dict[char] = final_dict[char] + 1
            else:
                final_dict[char] = 1
        raise KeyError("Missing  ke")
        return final_dict
    except Exception as e:
        print("Nothing issue : {}".format(e))
        return {}


def chunk_map_keys(data, batch_size):
    it = iter(data)
    for i in range(0, len(data), batch_size):
        yield {k: data[k] for k in islice(it, batch_size)}


def first_time_update():
    for i in chunk_map_keys(list(range(0, 256)), 100):
        range_list = list(i.keys())
        print(range_list[0], range_list[len(range_list) - 1])


if __name__ == '__main__':
    first_time_update()
