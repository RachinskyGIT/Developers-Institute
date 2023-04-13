
# # ex1
# def get_words_from_file(file="sowpods.txt"):
#     with open(file, "r") as f:
#         secret = (f.readlines())
#         secret = [s.strip() for s in secret]
#         return secret

# def get_random_sentence(length):
#     from random import sample
#     random_words_str = " ".join(sample(get_words_from_file(), length)).lower()
#     print(random_words_str)


# if __name__ == '__main__':

#     print("The programm prints sentence with 'length' number of random words.")
#     inp = input("How long you want the sentence to be? Acceptable values are: an integer between 2 and 20.\n")
#     try: 
#         if (int(inp)>=2 and int(inp)<=20):
#             get_random_sentence(inp)
#         else:
#             raise Exception("Wrong number")
#     except ValueError:
#         raise ValueError("Not an integer")



# # ex2

# if __name__ == '__main__':
#     import json
#     sampleJson = """{ 
#     "company":{ 
#         "employee":{ 
#             "name":"emma",
#             "payable":{ 
#                 "salary":7000,
#                 "bonus":800
#             }
#         }
#     }
#     }"""

#     data = json.loads(sampleJson)
#     salary = data['company']['employee']['payable']['salary']
#     data['company']['employee']["birth_date"]=None
#     # print(data)

#     with open("sampleJson.json", "w") as f:
#         json.dump(data, f)





# ex2 & 3 - GOLD

if __name__ == '__main__':
    import requests

    # Ask user for search term or phrase
    search_query = input("Enter a term or phrase to search for: ")

    rating = "g"
    api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"

    url = f"https://api.giphy.com/v1/gifs/search?q={search_query}&rating={rating}&api_key={api_key}"
    
    # Send GET request to Giphy API
    response = requests.get(url)

    # If the status code is 200, proceed with parsing the JSON object
    if response.status_code == 200:
        # Check that response content is not empty
        if response.content:
            # Parse the JSON object
            data = response.json()
        else:
            # If response content is empty, set data to an empty dictionary
            data = {}
        
        # If the JSON object has data, proceed with extracting relevant gifs
        if data.get("data"):
            # Initialize a list to hold the relevant gifs
            relevant_gifs = []

            # Loop through the gifs in the JSON object
            for gif in data["data"]:
                # Check if the gif has a height bigger than 100
                if int(gif["images"]["original"]["height"]) > 100:
                    # Append the relevant gif to the list
                    relevant_gifs.append(gif)

                    # Check if we've found 10 relevant gifs already
                    if len(relevant_gifs) == 10:
                        # If we have, break out of the loop
                        break

            # Print the length of the list of relevant gifs
            print(f'The length of the list of relevant gifs is: {len(relevant_gifs)}')

            # Print the URLs of the relevant gifs
            for gif in relevant_gifs:
                print(gif["images"]["original"]["url"])
        else:
            # If the JSON object doesn't have data, print a message saying the search term couldn't be found
            print(f"Sorry, we couldn't find any gifs for the search term '{search_query}'. Here are the trending gifs for today instead:")

            # Construct URL for trending gifs
            url = f"https://api.giphy.com/v1/gifs/trending?api_key={api_key}"

            # Send GET request to Giphy API for trending gifs
            response = requests.get(url)

            # If the status code is 200, proceed with parsing the JSON object
            if response.status_code == 200:
                # Check that response content is not empty
                if response.content:
                    # Parse the JSON object
                    data = response.json()
                else:
                    # If response content is empty, set data to an empty dictionary
                    data = {}

                # Initialize a list to hold the trending gifs
                trending_gifs = []

                # Loop through the gifs in the JSON object
                for gif in data["data"]:
                    # Check if the gif has a height bigger than 100
                    if int(gif["images"]["original"]["height"]) > 100:
                        # Append the trending gif to the list
                        trending_gifs.append(gif)

                        # Check if we've found 10 trending gifs already
                        if len(trending_gifs) == 10:
                            # If we have, break out of the loop
                            break

                # Print the length of the list of trending gifs
                print(f'The length of the list of trending gifs is: {len(trending_gifs)}')

                # Print the URLs of the trending gifs
                for gif in trending_gifs:
                    print(gif["images"]["original"]["url"])
    else:
        # If the status code is not 200, print an error message
        print("Error:", response.status_code)
    


