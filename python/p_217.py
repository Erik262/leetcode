def groupAnagrams(strs: list[str]) -> list[list[str]]:

    h_map = {}

    for idx, word in enumerate(strs):
        s_word = "".join(sorted(word))

        if s_word in h_map:
            h_map[s_word].append(word)
        else:
            h_map[s_word] = [word]
            
    return h_map.values()



    



strs = ["act","pots","tops","cat","stop","hat"]
out = groupAnagrams(strs)
print(out)