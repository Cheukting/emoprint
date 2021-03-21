refined_dataset = {}

with open("emojis.json") as json_file:
    emojipedia = json.load(json_file)

for emoji_entry in emojipedia:
    if emoji_entry['category'] != 'Miscellaneous Symbols And Pictographs -> Emoji modifiers':
        info_dict= {}
        emoji = chr(int(emoji_entry['unicode'].split()[0][2:], base=16))
        info_dict['keywords'] = emoji_entry['keywords']
        info_dict['senses'] = emoji_entry['senses']
        if emoji in emoji_map.values():
            refined_dataset[emoji] = info_dict

pickle.dump(refined_dataset, open("pickled/refined_dataset.p", "wb"))
