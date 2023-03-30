def compare(expected: {}, actual: {}):
    result_arr = []
    compare_util(expected, actual, '', result_arr, '-')
    compare_util(actual, expected, '', result_arr, '+')
    return result_arr


def compare_util(expected: {}, actual: {}, key_starting: str, result_arr: [], sign: str):
    for key in expected.keys():
        expected_value = expected[key]
        if key in actual:
            actual_value = actual[key]
        else:
            actual_value = None

        if expected_value == actual_value:
            continue
        else:
            if isinstance(expected_value, (str, int, list)):
                if key_starting == '':
                    final_key = str(key)
                else:
                    final_key = key_starting + "." + str(key)
                result_arr.append([sign, final_key, expected_value])
            else:
                if key_starting == '':
                    append_key = str(key)
                else:
                    append_key = key_starting + "." + key
                compare_util(expected_value, actual_value, append_key, result_arr, sign)

    return result_arr


if __name__ == '__main__':
    expected_dict = {
        "_id": "63ac59923b949df3169aac1b",
        "forum": "https://www.moosejawtoday.com/rss",
        "forum_title": "MooseJawToday.com: moosejawtoday",
        "discussion_title": "France's defense minister goes to Ukraine to boost support",
        "language": "english",
        "gmt_offset": -6,
        "topic_url": "https://www.moosejawtoday.com/politics/frances-defense-minister-goes-to-ukraine-to-boost-support-6302206",
        "post_title": "\n\n",
        "persons": [
            "Lecornu",
            "Volodymyr Zelenskyy",
            "Oleksiy Reznikov",
            "Sebastien Lecornu"
        ],
        "locations": [
            "Britain",
            "United States",
            "France",
            "Kyiv",
            "Poland",
            "Ukraine",
            "Russia"
        ],
        "details": {
            "source_type": "alpha",
            "source": "table",
            "source_arg": {
                "value_tag": "asx",
                "currency": "$",
                "timestamps": [20110324, 20110415, 20121204]
            }
        }
    }

    actual_dict = {
        "_id": "63ac59923b949df3169aac1b",
        "type": "mainstream",
        "forum": "https://www.moosejawtoday.com/rss",
        "forum_title": "MooseJawToday.com: moosejawtoday",
        "discussion_title": "France's defense minister goes to Ukraine to boost support",
        "gmt_offset": -8,
        "topic_url": "https://www.moosejawtoday.com/politics/frances-defense-minister-goes-to-ukraine-to-boost-support-6302206",
        "post_title": "\n",
        "persons": [
            "Lecornu",
            "Volodymyr Zelenskyy",
            "Oleksiy Reznikov"
        ],
        "locations": [
            "Britain",
            "France",
            "Kyiv",
            "Poland",
            "Ukraine",
            "Russia"
        ],
        "details": {
            "source_type": "alpha",
            "source": "HTML",
            "source_arg": {
                "value_tag": "asx",
                "currency": "$",
                "timestamps": [20110324, 20121204]
            }
        }
    }

    result = compare(expected_dict, actual_dict)
    for obj in result:
        print(obj)
        print()
    print()

