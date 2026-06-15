import requests

# Apni OMDb API key yahan paste karo
API_KEY = "YOUR_API_KEY"

print("🎬 Movie Search Application")
print("-" * 30)

movie_name = input("Enter Movie Name: ").strip()

url = f"https://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}"

try:
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":

        print("\n🎥 Movie Details")
        print("=" * 40)

        print(f"Title       : {data.get('Title')}")
        print(f"Year        : {data.get('Year')}")
        print(f"Rated       : {data.get('Rated')}")
        print(f"Released    : {data.get('Released')}")
        print(f"Runtime     : {data.get('Runtime')}")
        print(f"Genre       : {data.get('Genre')}")
        print(f"Director    : {data.get('Director')}")
        print(f"Writer      : {data.get('Writer')}")
        print(f"Actors      : {data.get('Actors')}")
        print(f"Language    : {data.get('Language')}")
        print(f"Country     : {data.get('Country')}")
        print(f"IMDb Rating : {data.get('imdbRating')}")
        print(f"Awards      : {data.get('Awards')}")
        print(f"Plot        : {data.get('Plot')}")
        print(f"Poster URL  : {data.get('Poster')}")

    else:
        print("\n❌ Error:", data.get("Error"))

except requests.exceptions.RequestException as e:
    print("❌ Network Error:", e)

except Exception as e:
    print("❌ Unexpected Error:", e)