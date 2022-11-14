from random import choice

def generate_rek():
    """ fungsi generate rekening """
    list_rek = []
    random_rek = ["1","2","3","4","5","6","7","8","9","0"]
    for x in range(10):
        rekening = choice(random_rek)
        list_rek.append(rekening)

    return (""+"".join(list_rek))
