#given a string representing the list of M photos, returns the string representing the list of new names of all photos (the order of photos should stay the same).

def solution(S):
    # write your code in Python 3.6
  photos = S.split('\n')
  photos = [photo.split(' ') for photo in photos]
  photos_dict = {}
  for photo in photos:
    photos_dict[photo.split(' ')[0]] = photo.split(' ')[1:]
  
  photos_dict_sorted = sorted(photos_dict.items(), key=lambda x: x[0])

  photos_dict_sorted_list = []
  for photo in photos_dict_sorted:
    photos_dict_sorted_list.append(photo[1])
  
  return '\n'.join(photos_dict_sorted_list)



