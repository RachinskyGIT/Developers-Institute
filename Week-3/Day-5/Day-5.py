# Daily Challenge

def how_many_time_to_load(website):
    from requests import get
    a = get(website).elapsed.total_seconds()
    return(a)

print(how_many_time_to_load("https://google.com/"), "seconds")