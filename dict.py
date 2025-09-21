r = "aab"
m = "baa"
def ransom_note(ransomNote, magazine):
    hmap1= {}
    hmap2= {}
    for i in magazine:
        hmap1[i] = hmap1.get(i, 0) + 1
    for i in ransomNote:
        hmap2[i] = hmap2.get(i, 0) + 1
    for k,v in hmap2.items():
        if k in hmap1.keys() and v in hmap1.values():
            continue
        else:
            return False
    return True
print(ransom_note(r, m))
