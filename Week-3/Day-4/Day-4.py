
# ex1
def get_words_from_file(file="sowpods.txt"):
    with open(file, "r") as f:
        secret = (f.readlines())
        secret = [s.strip() for s in secret]
        return secret

def get_random_sentence(length):
    from random import sample
    random_words_str = " ".join(sample(get_words_from_file(), length)).lower()
    print(random_words_str)


if __name__ == '__main__':

    print("The programm prints sentence with 'length' number of random words.")
    inp = input("How long you want the sentence to be? Acceptable values are: an integer between 2 and 20.\n")
    try: 
        if (int(inp)>=2 and int(inp)<=20):
            get_random_sentence(inp)
        else:
            raise Exception("Wrong number")
    except ValueError:
        raise ValueError("Not an integer")



# ex2

if __name__ == '__main__':
    import json
    sampleJson = """{ 
    "company":{ 
        "employee":{ 
            "name":"emma",
            "payable":{ 
                "salary":7000,
                "bonus":800
            }
        }
    }
    }"""

    data = json.loads(sampleJson)
    salary = data['company']['employee']['payable']['salary']
    data['company']['employee']["birth_date"]=None
    # print(data)

    with open("sampleJson.json", "w") as f:
        json.dump(data, f)