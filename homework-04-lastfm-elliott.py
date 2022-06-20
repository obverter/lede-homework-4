# %% [markdown]
# # Last FM API (Music)
#
# Spotify's API is dead to us, so we're using Last.fm's - it's still music, just not as nice of an API.
#
# 1. Create an account at https://www.last.fm/api/
# 2. Create an "application" to get a key: https://www.last.fm/api/account/create
#     - It isn't a real application, it's just your project
#     - Name/description doesn't matter, ignore callback key and callback url
# 3. And save the API key that shows up on the next screen
#
# You can find documentation at https://www.last.fm/api/
#
# The domain for the API is `http://ws.audioscrobbler.com`, so all of your endpoints will be connected to that. To test your API key, check the following URL in your browser: `http://ws.audioscrobbler.com/2.0/?method=artist.search&artist=cher&api_key=XXXXXXXXXXXXXXXXXXXX&format=json` (change the `XXXXXX` to be your API key, of course!).
#
# > Last.fm used to be called **AudioScrobbler**, which is why its URLs don't have "last.fm" in them.
# > While we're asking about URLs, notice that the API endpoints have a lot of `?` and `&` in them - these are key/value pairs, kind of like dictionaries, but for URLs instead of Python.

# %% [markdown]
# # FIRST: SETUP

# %% [markdown]
# ## 1) Import the libraries/packages you might need
#
# We need a library to read in the data for us! We don't like `urllib2`, so it must be something cooler and better.

# %%
%%time
# Import what you need here
import requests
import random
import time
LFM_key = 'dceeeb420753458b13ba2cc8af00e91b'
LFM_master_ep = 'http://ws.audioscrobbler.com/2.0/?method='

# %% [markdown]
# ## 2) Save your API key
#
# Write your API key here so you don't forget it - it's the "api key" one, not the "shared secret" one

# %% [markdown]
# ## 3) The death of an API
#
# I used to have some code here that allowed you to display images, but _the images don't work any more._ Let this be an important lesson: when you depend on external services, they can die at any time.

# %% [markdown]
# # NOW: YOUR ASSIGNMENT

# %% [markdown]
# ## 1) Search for and print a list of 50 musicians with `lil` in their name, along with the number of listeners they have
#
# There are a lot of musicians with "Lil" in their name - it used to be all Lil Wayne and Lil Kim, but we live in a new world now!
#
# - *Tip: Remember, the domain for the API is `http://ws.audioscrobbler.com`*
# - *Tip: Make sure you ask the API for 50 musicians! This involves adding another parameter to the URL - notice they all have a `&` before them. [Read the documentation](http://www.last.fm/api/show/artist.search) to find the parameter's name.*
# - *Tip: When you are looking at any piece of data - is it a dictionary? Look at the keys! Is it a list? Look at the first element!*
# - *Tip: LOOK AT THE KEYS. and then the other keys and the other keys and the other keys. It's an ugly series of dictionaries!*

# %% [markdown]
# Let's jsonify our artist pile:

# %%
artist = 'lil'
result_count = 51
artist_query = f'{LFM_master_ep}artist.search&artist={artist}&api_key={LFM_key}&limit={result_count}&format=json'
artist_query
artist_result = requests.get(artist_query)
artist_result = artist_result.json()


# %% [markdown]
# Let's watch me root around in the pile for a minute just to get my bearings:

# %%
# print(artist_result.keys())
# print(artist_result['results'].keys())
# print(artist_result['results']['artistmatches'])
# print(artist_result['results']['artistmatches']['artist'][1])

# %% [markdown]
# Let's use a loop pull out our artists and listeners to a working lists, throw those into dictionaries, append those dictionaries to a list called clown car, and then reset everything for the next Lil:

# %%
listeners = []
lil_clown_car = []  # master list of dicts
lil_dic = {}  # each lil dict
lil_location = artist_result["results"]["artistmatches"]["artist"]
lil_counter = 0
lils = [lil_location[lil_counter]["name"]]
for _ in range(len(lil_location)):
    lils.append(lil_location[int(lil_counter)]["name"])
    listeners.append(
        int(lil_location[int(lil_counter)]["listeners"])
    )  # I'll need this later.

    lil_dic["artist"] = lils[int(lil_counter)]
    lil_dic["listeners"] = listeners[int(lil_counter)]

    lil_clown_car.append(lil_dic)
    lil_dic = {}
    lil_counter += 1
# print(lils)
# print("-----")
# print(lils)
# print("-----")
# print(listeners)
# print("-----")
# print(f"len(lils): {len(lils)}")
# print("-----")
# print(f"len(listeners): {len(listeners)}")
# print("-----")
# print(f"len(lil_clown_car): {len(listeners)}")
# print("-----")
# print(lil_clown_car[:3])
lil_clown_car.pop(0)
# print("-----")
print(lil_clown_car[:3])

# %% [markdown]
# Now let's print our answer list:

# %%
print(
    f"Here's a list of {len(lil_clown_car)} LastFM artists with {artist} in their name:\n\n"
)

for clown_count, lil in enumerate(lil_clown_car):
    if int(lil_clown_car[clown_count]["listeners"]) > 1000000:
        print(
            f'{(lil_clown_car[clown_count]["artist"].title())} has about {round(float(lil_clown_car[clown_count]["listeners"]) / 1_000_000, 2)} million LastFM listeners.'
        )
    else:
        print(
            f'{(lil_clown_car[clown_count]["artist"].title())} has about {round(float(lil_clown_car[clown_count]["listeners"]) / 1_000)},000 LastFM listeners.'
        )
print(
    f"\n{lil_clown_car[random.randint(0, 49)]['artist']} is my absolute favorite."
)

# %% [markdown]
# Your results should begin something like this:
#
# ```
# Lil' Wayne has 3086628 listeners
# Lily Allen has 2074266 listeners
# Lil B has 194116 listeners
# Lilly Wood & The Prick has 359886 listeners
# Lil Ugly Mane has 31955 listeners
# LIL UZI VERT has 88517 listeners
# ```

# %% [markdown]
# ## 2) How many listeners does your list have in total?
#
# The answer should be roughly **15,000,000**. If it's lower, make sure you have 50 artists instead of 30 artists.
#
# - *Tip: What's the data type of the `listeners` count? It's going to cause a problem!*
# - *Tip: If you were crazy you could use sum and a list comprehension. But you really don't have to!*

# %% [markdown]
# Let's give ourselves a big pat on the back for doing some extra work in the previous question so that we can use a one-liner here.

# %%
print(
    f"My Lil list comprises about {round(float(sum(listeners) / 1_000_000), 2)} million Lil listeners."
)

# %% [markdown]
# ## 4) Find Lil Jon's `mbid` (or anyone else's!).
#
# Oftentimes in an API, you can do a few things: you can **search** for items, and you can **see more information** about items. To find more information about the item, you need to use their **unique id**. In this dataset, it's called an `mbid` (MusicBrainz, I think - another company associated with last.fm!).
#
# Go through the artists and print their **name and mbid**. Find Lil Jon's `mbid`. I *wanted* Lil Uzi Vert's, but for some reason it isn't there. Then I wanted us to look at Lily Allen's, but I just couldn't bring myself to do that. If you'd rather do someone else, go for it.

# %% [markdown]
# Let's mess around with Lil Dicky's mbid:

# %%
lil_dicky = lil_clown_car[19]['artist']
mbid_query_endpoint = "https://musicbrainz.org/ws/2/artist/?query=artist:"
dicky_mbid_finder = (
    mbid_query_endpoint
    + ((lil_dicky).replace(" ","%")).lower()
    + "&fmt=json"
)
# print(str(artist_mbid_finder))
dicky_mbid_finder = requests.get(dicky_mbid_finder)
dicky_mbid_finder = dicky_mbid_finder.json()

# %% [markdown]
# Let's watch me root around blindly for a few lines until I find what I'm looking for:

# %%
# print(dicky_mbid_finder.keys())  # where's that mbid?
# print(dicky_mbid_finder['artists'])
# print(dicky_mbid_finder['artists'][0])
# print(dicky_mbid_finder['artists'][0]['id'])  # here it is


lil_dicky_mbid = dicky_mbid_finder['artists'][0]['id']
print(lil_dicky_mbid)

# %% [markdown]
# Let's print out Lil Dicky's mbid.

# %%
print(
    f"{lil_dicky}'s mbid is {lil_dicky_mbid}."
)

# %%
lil_clown_car[0]

# %% [markdown]
# # NOTE FOR SOMA:
# From here on, the API threw all sorts of errors at me. Lots of 'error 6'. Lots of 'list out of index' bullshit that I just could not figure out. E.g., either my list of artists or my list of dictionaries of artists were len(50), had all of my lil's in there just fine, but when I fed those indexes into the API query, the run would crash at index 30. Every time. No matter what.
#
# Below, you'll see a bunch of flailing. I've got the entire saga broken out in commits on the big huge Lede repo that I'm working in most of the time.
#
# I'll keep working on it, but it's possible that I just painted myself in a corner somehow. Sad emoji.

# %%
clown_count = 0
for clown in range(50):
    mbid_bio_search = (
        LFM_master_ep
        + "artist.getinfo&artist="
        + str(lil_clown_car[clown_count]['artist']).lower().replace(" ", "%")
        + "&api_key="
        + LFM_key
        + "&format=json"
    )
    mbid_bio_search = requests.get(mbid_bio_search)
    mbid_bio_search = mbid_bio_search.json()
    print(mbid_bio_search)
    clown_count += 1

    # lil_mbid = lil_clown_car[clown_count]["artist"]
    # lil_mbid_finder = (
    #     mbid_query_endpoint + (str(lil_mbid).replace(" ", "%")).lower() + "&fmt=json"
    # )
    # lil_mbid_finder = requests.get(lil_mbid_finder)
    # lil_mbid_finder = lil_mbid_finder.json()

    # lil_clown_car[clown_count]["xl-image"] = mbid_bio_search["artist"]["image"][-3][
    #     "#text"
    # ]
    # lil_clown_car[clown_count]["bio-summary"] = mbid_bio_search["artist"]["bio"][
    #     "summary"
    # ]
    # lil_clown_car[clown_count]["bio-content"] = mbid_bio_search["artist"]["bio"][
    #     "content"
    # ]
    # lil_clown_car[clown_count]["tags"] = mbid_bio_search["artist"]["tags"]["tag"]
    # lil_clown_car[clown_count]["mbid"] = lil_mbid_finder["artist"][0]["id"]
    # clown_count += 1
    # time.sleep(0.5)

# %%
mbid_query_endpoint = "https://musicbrainz.org/ws/2/artist/?query=artist:"
for lil_mbid_counter, _ in enumerate(range(50), start=0):
    lil_mbid = lil_clown_car[lil_mbid_counter]['artist']
    lil_mbid_finder = (
        mbid_query_endpoint
        + ((lil_mbid).replace(" ","%")).lower()
        + "&fmt=json"
    )
    lil_mbid_finder = requests.get(lil_mbid_finder)
    lil_mbid_finder = lil_mbid_finder.json()
    if "mbid"  "id" in lil_mbid_finder['artists'][0].keys() or "mbid" | "id" in lil_mbid_finder['artists'].keys():
        if lil_mbid_finder['artists']['id'] != None:
            lil_clown_car[lil_mbid_counter][0]['mbid'] = lil_mbid_finder['artists'][0]['id']
            print(f" {lil_mbid_counter}: {lil_clown_car[lil_mbid_counter]['artist']} — OK")
        elif lil_mbid_finder['artists'][0]['mbid'] != None:
            lil_clown_car[lil_mbid_counter]['mbid'] = lil_mbid_finder['artists'][0]['mbid']
            print(f" {lil_mbid_counter}: {lil_clown_car[lil_mbid_counter]['artist']} — OK")
        elif lil_mbid_finder['artists']['id'] != None:
            lil_clown_car[lil_mbid_counter]['mbid'] = lil_mbid_finder['artists']['mbid']
            print(f" {lil_mbid_counter}: {lil_clown_car[lil_mbid_counter]['artist']} — OK")
        elif lil_mbid_finder['artists']['mbid'] != None:
            lil_clown_car[lil_mbid_counter]['mbid'] = lil_mbid_finder['artists']['mbid']
            print(f" {lil_mbid_counter}: {lil_clown_car[lil_mbid_counter]['artist']} — OK")
        else:
            print('Sadness')
    else:
        print('Sadness')
    time.sleep(1)

# %% [markdown]
# Let's watch me root around blindly for a few lines until I find what I'm looking for:

# %% [markdown]
# Let's make a loop that adds every artist's mbid to their dictionary:

# %%
# mbid_query = mbid_query_endpoint + str(lil_clown_car[0]["artist"]).replace(" ", "%").lower() + "&fmt=json"
# mbid_query = requests.get(mbid_query)
# mbid_query = mbid_query.json()
# mbid_query['artists'][0].keys()

# %%
# lil_mbid = (
#         mbid_query_endpoint
#         + str(lil_clown_car[0]["artist"]).replace(" ", "%").lower()
#         + ("&limit={result_count}")
#         + "&fmt=json"
#     )
# lil_mbid = requests.get(lil_mbid)
# lil_mbid = lil_mbid.json()
# lil_mbid

# %% [markdown]
# ## 6) Print every tag of that artist

# %% [markdown]
# Let's make sure we know where these tags are:

# %%
# lil_clown_car[19].keys()
# lil_clown_car[19]['tags']
# lil_clown_car[19]['tags'][0]['name']  # Yahtzee.


# %%
artist_index = 19
artist_tags = [lil_clown_car[artist_index]['tags'][tag]['name'] for tag in range(len(lil_clown_car[artist_index]['tags'][0]))]

print(
    f"Here's a list of all of {lil_clown_car[artist_index]['artist']}'s tags:\n{artist_tags}\n"
)

# %% [markdown]
# # GETTING A LITTLE CRAZY
#
# So you know your original list of musicians? I want to get tag data for ALL OF THEM. How are we going to do that?
#
# ## 7) Find the mbids (again)
#
# If we have a musician with an mbid of `AAA-AAA-AAA`, we get their info from a url like `http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=AAA-AAA-AAA`.
#
# |artist|url|
# |---|---|
# |`AAA-AAA-AAA`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=AAA-AAA-AAA`|
# |`BBB-BBB-BBB`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=BBB-BBB-BBB`|
# |`CCC-CCC-CCC`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=CCC-CCC-CCC`|
#
# I guess we should start trying to get a list of all of the mbids.
#
# **Loop through your artists, and print out the `mbid` for each artist**
#
# - *Tip: You probably need to request your artist search result data again, because you probably saved over `data` with your other API request. Maybe call it `artist_data` this time?*
# - *Tip: If the artist does NOT have an `mbid`, don't print it.*

# %% [markdown]
# Let's give myself an even larger pat on the back for doing some heavy lifting earlier, meaning that I can can answer this question with a one-liner.

# %%
lil_clown_car[34]['mbid']

# %%
clown_count = 0
for clown_count in range(len(lil_clown_car)):
    if lil_clown_car[clown_count]['mbid'] != None:
        print(lil_clown_car[clown_count]['mbid'])
    clown_count += 1

# %%


# %% [markdown]
# Your results should look something like
#
# ```
# 6e0c7c0e-cba5-4c2c-a652-38f71ef5785d
# 1550f952-c91b-40d7-9b4d-d26a259ee932
# 1b72331b-3a97-4981-a81c-eeee9c275d28
# 5f1adfe1-4d07-4141-b181-79e5d379d539
# a95384b1-6aec-468c-ae0d-8c6daf87c4c2
# bc1b5c95-e6d6-46b5-957a-5e8908b02c1e
# 243c6f61-d83b-4459-bebd-5899df0da111
# ```

# %% [markdown]
# ## 8) Saving those mbids
#
# For those `mbid` values, instead of printing them out, save them to a new list of just mbid values. Call this list `mbids`.
#
# - *Tip: Use `.append` to add a single element onto a list*

# %%


# %% [markdown]
# Your results should look something like
#
# ```['6e0c7c0e-cba5-4c2c-a652-38f71ef5785d',
#  '1550f952-c91b-40d7-9b4d-d26a259ee932',
#  '1b72331b-3a97-4981-a81c-eeee9c275d28',
#  '5f1adfe1-4d07-4141-b181-79e5d379d539',
#  'a95384b1-6aec-468c-ae0d-8c6daf87c4c2',
#  'bc1b5c95-e6d6-46b5-957a-5e8908b02c1e',
#  '243c6f61-d83b-4459-bebd-5899df0da111',
#  '8ba17cf6-bec2-4ae4-9820-b1cda47adc08',
#  'ad29ae1c-2eda-4071-9dc8-31910e7e546c',
#  '3268f062-6e76-480a-a384-e1dd2a276afb',
#  '3ad4f6ec-253f-4050-8849-ca26266edfb8',
#  '9b5ce0c1-1bc0-4ea2-a8d3-f5ee7af9eda8',
#  '981d39fc-bd00-4cc6-ac67-6410f8b89098',
#  'b89f4c50-72f5-48ce-b08c-a643b191b24f',
#  'bc21df5c-3d79-479b-b638-8ddb5ecea403',
#  'c9cd225b-4883-428e-82c2-73e0b6282fb6',
#  '9acaf734-b380-4c48-954c-a2cf1d7990a9',
#  'd4d5ae85-700c-4a55-8a39-7f923da07ef2',
#  '77fafce8-a32f-4d42-bdce-266bbf913cee',
#  '50ad1cde-1536-4268-a55f-e47a7b8280ab',
#  '9803d120-716d-45ba-9eb7-9a120813f908',
#  'b27560ea-2783-4a91-be45-9e8711917562',
#  '194e87c9-b3fe-4fbd-82a7-8c54b4dd4c76',
#  'fd90af91-ed07-4e85-8816-26c954fe5286',
#  '5652bb3e-f225-49de-9637-5aa1539b4a7c']```

# %% [markdown]
# ## 9) Printing our API urls
#
# To get tag data for each artist, you need to use those `mbid` values to access their artist page on the API. Loop through the mbids, displying the URL you'll need to access.
#
# - *Tip: You don't want to use a comma when printing, because commas add spaces into your text and URLs can't have that*
# - *Tip: Make sure your URL has `artist.getinfo` in it - if not, you're using the wrong endpoint.*

# %%


# %% [markdown]
# Your results should look something like
#
# ```http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&api_key=XXXXX&format=json&mbid=6e0c7c0e-cba5-4c2c-a652-38f71ef5785d
# http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&api_key=XXXXX&format=json&mbid=1550f952-c91b-40d7-9b4d-d26a259ee932
# http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&api_key=XXXXX&format=json&mbid=1b72331b-3a97-4981-a81c-eeee9c275d28
# http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&api_key=XXXXX&format=json&mbid=5f1adfe1-4d07-4141-b181-79e5d379d539
# http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&api_key=XXXXX&format=json&mbid=a95384b1-6aec-468c-ae0d-8c6daf87c4c2
# http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&api_key=XXXXX&format=json&mbid=bc1b5c95-e6d6-46b5-957a-5e8908b02c1e```

# %% [markdown]
# ## OKAY HERE IS A LITTLE INFORMATION: Using our API urls
#
# This time instead of just *displaying* the URL, we're going to *request and process it*. **But first I'm going to teach you something.**
#
# When you're dealing with an API, you don't want to make a million requests, have bad code, and then need to do those million requests again. It's usually best to test your code with a few of the results first.
#
# So, if we have a list of numbers like this:

# %%
numbers = [4, 5, 6, 7]
numbers

# %% [markdown]
# You can actually say to Python, **give me the first two**, and it will only give you the first two.

# %%
numbers[:2]

# %% [markdown]
# The is **very convenient** with loopng with APIs, because instead of trying to use all FIFTY artists, you can just say "hey, please try this out with 2 of them" and you don't waste time.

# %% [markdown]
# ## 10) Using the first three `mbids`, request the API urls and print the artist's name.
#
# You built the URLs in the last question, now it's time to use them! Use `requests` etc to grab the URL and get out the artist's name.
#
# - *Tip: The code is the same as last time you got an artist's name from their info page, it's just going to be inside of a loop*
# - *Tip: USE `PRINT` TO SEE WHAT YOU ARE LOOKING AT!!!!!*

# %%


# %% [markdown]
# ## 11) Using the first three `mbids`, request the API urls and print the artist's name and their tags
#
# - *Tip: The code is the same as last time you got an artist's name from their info page, it's just going to be inside of a loop*
# - *Tip: It's a for loop in a for loop!*

# %%


# %% [markdown]
# ## 12) Using the first ten mbids, print the artist's name and whether they're a rapper
#
# Only print their name ONCE and only print whether they are hip hop or not ONCE.
#
# - *Tip: Rap tags include hip hop, swag, crunk, rap, dirty south, and probably a bunch of other stuff! You can include as many categories as you'd like.*
# - *Tip: You can use `2 in [1, 2, 3]` to find out if `2` is in the list of `[1, 2, 3]`.*
# - *Tip: Every time you look at a new artist, you can say they are NOT a rapper. And once you find out one of their tags is hip hop or rap, then you can note that they're a rapper. Then once you're done looking at their tags, then you can say HEY this is a rapper, or HEY this is not a rapper.*

# %%


# %% [markdown]
# Your results might look something like
#
# ```ARTIST: Lily Allen
# NO hip hop
# ARTIST: Lil B
# YES hip hop
# ARTIST: Lilly Wood & The Prick
# NO hip hop
# ARTIST: Lil Ugly Mane
# YES hip hop
# ARTIST: Lil Jon
# YES hip hop
# ARTIST: Lil' Kim
# YES hip hop
# ARTIST: Lil Jon & The East Side Boyz
# YES hip hop
# ```

# %% [markdown]
# ## 13) What percent of "lil" results are rappers?

# %%


# %% [markdown]
# ## 14) Seriously you are all-powerful now.

# %%
