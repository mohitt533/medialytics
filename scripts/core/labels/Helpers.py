import json


class Helper(object):
    @classmethod
    def get_desc(cls, label):
        result = {}
        with open('scripts/meta/tags.json') as fh:
            data = json.load(fh)

        for tags in data:
            for tag in data[tags]:
                for props in label:
                    if tag == props.description:
                        result[tag] = round((props.score*100), 2)
        return result
