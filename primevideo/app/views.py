from django.db.utils import OperationalError
from django.shortcuts import render
from django.http import JsonResponse

from .models import Movie


def _sample_movies():
    return [
        {
            "id": 1,
            "title": "Dangal",
            "category": "Biographical Sports Drama (Indian)",
            "release_year": 2016,
            "rating": "8.3/10",
            "duration": "2h 41m",
            "director": "Nitesh Tiwari",
            "cast": "Aamir Khan, Fatima Sana Shaikh, Sanya Malhotra",
            "synopsis": "Former wrestler Mahavir Singh Phogat trains his daughters to become world champions.",
            "poster_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQMCj20Dhxm40PDsgiS1lMZaNj8lepMfMv9zn3LsbwLWu2ovzUk",
            "trailer": "https://www.youtube.com/embed/x_7YlGv9u1g",
        },
        {
            "id": 2,
            "title": "Baahubali 2",
            "category": "Epic Action (Indian)",
            "release_year": 2017,
            "rating": "8.2/10",
            "duration": "2h 47m",
            "director": "S.S. Rajamouli",
            "cast": "Prabhas, Rana Daggubati, Anushka Shetty",
            "synopsis": "Amarendra Baahubali, the heir apparent to the throne of Mahishmati, finds his life and relationships endangered as his adoptive brother Bhallaladeva conspires to claim the throne.",
            "poster_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTnMA16Y55ki6WxoLTdTmxNnKwYCZiNwi0DvCakttCRBQgZyJpJ",
            "trailer": "https://www.youtube.com/embed/G62HrubdD6o",
        },
        {
            "id": 3,
            "title": "RRR",
            "category": "Action Drama (Indian)",
            "release_year": 2022,
            "rating": "7.8/10",
            "duration": "3h 2m",
            "director": "S.S. Rajamouli",
            "cast": "N.T. Rama Rao Jr., Ram Charan, Alia Bhatt",
            "synopsis": "A fictitious story about two legendary revolutionaries and their journey away from home before they started fighting for their country in the 1920s.",
            "poster_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRx0wTDoneV8OuMM6hNfD7vfibB_jt6FcCL-u8H2DljlRXgGCoG",
            "trailer": "https://www.youtube.com/embed/NgBoKQy3RGU",
        },
        {
            "id": 4,
            "title": "K.G.F.: Chapter 2",
            "category": "Action Thriller (Indian)",
            "release_year": 2022,
            "rating": "8.3/10",
            "duration": "2h 48m",
            "director": "Prashanth Neel",
            "cast": "Yash, Sanjay Dutt, Raveena Tandon",
            "synopsis": "In the blood-soaked Kolar Gold Fields, Rocky's name strikes fear into his foes. While his allies look up to him, the government sees him as a threat to law and order.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BZmQzZjVkZTUtYjI4ZC00ZDJmLWI0ZDUtZTFmMGM1Mzc5ZjIyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            "trailer": "https://www.youtube.com/embed/Qah9sSIXJqk",
        },
        {
            "id": 5,
            "title": "Jawan",
            "category": "Action Thriller (Indian)",
            "release_year": 2023,
            "rating": "7.0/10",
            "duration": "2h 49m",
            "director": "Atlee",
            "cast": "Shah Rukh Khan, Nayanthara, Vijay Sethupathi",
            "synopsis": "A high-octane action thriller which outlines the emotional journey of a man who is set to rectify the wrongs in the society.",
            "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA8fxJgOk6Q4UGjmsa1q3CQ1Q05Lt0Dn1leAl6_KexCEjqJAe6",
            "trailer": "https://www.youtube.com/embed/MWOtxug9vTg",
        },
        {
            "id": 6,
            "title": "Pathaan",
            "category": "Action Thriller (Indian)",
            "release_year": 2023,
            "rating": "5.9/10",
            "duration": "2h 26m",
            "director": "Siddharth Anand",
            "cast": "Shah Rukh Khan, Deepika Padukone, John Abraham",
            "synopsis": "An Indian spy takes on the leader of a group of mercenaries who have nefarious plans to target his homeland.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNDdkNTY1MDQtY2I5MC00OTFlLTg5OWQtZWE2YzE5NWFiMDgzXkEyXkFqcGc@._V1_.jpg",
            "trailer": "https://www.youtube.com/embed/vqu4z34wENw",
        },
        {
            "id": 7,
            "title": "Bajrangi Bhaijaan",
            "category": "Drama (Indian)",
            "release_year": 2015,
            "rating": "8.1/10",
            "duration": "2h 43m",
            "director": "Kabir Khan",
            "cast": "Salman Khan, Harshaali Malhotra, Nawazuddin Siddiqui",
            "synopsis": "An Indian man with a magnanimous heart takes a young mute Pakistani girl back to her homeland to reunite her with her family.",
            "poster_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQRGNMHX7ZlA7yp_XDkjD1iBMeFJnSkBM3PKju8auM_SpKFP4Dm",
            "trailer": "https://www.youtube.com/embed/vyX4toD395U",
        },
        {
            "id": 8,
            "title": "3 Idiots",
            "category": "Comedy Drama (Indian)",
            "release_year": 2009,
            "rating": "8.4/10",
            "duration": "2h 50m",
            "director": "Rajkumar Hirani",
            "cast": "Aamir Khan, Madhavan, Sharman Joshi",
            "synopsis": "Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently.",
            "poster_url": "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/250px-3_idiots_poster.jpg",
            "trailer": "https://www.youtube.com/embed/K0eDlFX9GZ8",
        },
        {
            "id": 9,
            "title": "PK",
            "category": "Satirical Comedy (Indian)",
            "release_year": 2014,
            "rating": "8.1/10",
            "duration": "2h 33m",
            "director": "Rajkumar Hirani",
            "cast": "Aamir Khan, Anushka Sharma, Sanjay Dutt",
            "synopsis": "An alien on Earth loses the only device he can use to communicate with his spaceship. His innocent nature and child-like questions force the country to evaluate the impact of religion on its people.",
            "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2FV_zTaMbFBBdsf_-RfdWTf7ES38QXjIiGLbzpYNjS5GRk2Sf",
            "trailer": "https://www.youtube.com/embed/SOXWc32k4zA",
        },
        {
            "id": 10,
            "title": "Sholay",
            "category": "Action Adventure (Indian)",
            "release_year": 1975,
            "rating": "8.1/10",
            "duration": "3h 24m",
            "director": "Ramesh Sippy",
            "cast": "Dharmendra, Amitabh Bachchan, Sanjeev Kumar",
            "synopsis": "After his family is murdered by a notorious and ruthless bandit, a former police officer enlists the services of two outlaws to capture him.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BOGQ2NjU0MjktMTUyYi00NjQwLTg0ZTAtNzg5NTk0YTRlMWNhXkEyXkFqcGc@._V1_.jpg",
            "trailer": "https://www.youtube.com/embed/hB835H_rK0g",
        },
        {
            "id": 11,
            "title": "Dilwale Dulhania",
            "category": "Romance (Indian)",
            "release_year": 1995,
            "rating": "8.0/10",
            "duration": "3h 9m",
            "director": "Aditya Chopra",
            "cast": "Shah Rukh Khan, Kajol, Amrish Puri",
            "synopsis": "When Raj meets Simran in Europe, it isn't love at first sight, but when Simran moves to India for an arranged marriage, love makes its presence felt.",
            "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFsQa8EcnB4W2gdO0bEh5HQnu1Y4knPPWvaUdI5zUrik_R-vD5",
            "trailer": "https://www.youtube.com/embed/c25GKl5VNeY",
        },
        {
            "id": 12,
            "title": "Mughal-e-Azam",
            "category": "Historical Drama (Indian)",
            "release_year": 1960,
            "rating": "8.1/10",
            "duration": "3h 17m",
            "director": "K. Asif",
            "cast": "Prithviraj Kapoor, Dilip Kumar, Madhubala",
            "synopsis": "A 16th century prince falls in love with a court dancer and battles with his emperor father.",
            "poster_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRJHmocnRnc8gZ_2k9aonNFC46NaITPpQ_TfL4MWQpxO-c1CZX9",
            "trailer": "https://www.youtube.com/embed/6_rXlJgXh28",
        },
        {
            "id": 13,
            "title": "Gangs of Wasseypur",
            "category": "Crime Drama (Indian)",
            "release_year": 2012,
            "rating": "8.2/10",
            "duration": "5h 21m",
            "director": "Anurag Kashyap",
            "cast": "Manoj Bajpayee, Nawazuddin Siddiqui, Tigmanshu Dhulia",
            "synopsis": "A clash between Sultan and Shahid Khan leads to the expulsion of Khan from Wasseypur, and ignites a deadly blood feud spanning three generations.",
            "poster_url": "https://m.media-amazon.com/images/I/71mntzZ3s1L._UF1000,1000_QL80_.jpg",
            "trailer": "https://www.youtube.com/embed/j-AkWDkXcMY",
        },
        {
            "id": 14,
            "title": "Swades",
            "category": "Drama (Indian)",
            "release_year": 2004,
            "rating": "8.2/10",
            "duration": "3h 9m",
            "director": "Ashutosh Gowariker",
            "cast": "Shah Rukh Khan, Gayatri Joshi, Kishori Ballal",
            "synopsis": "A successful Indian scientist returns to an Indian village to take his nanny to America with him and in the process rediscovers his roots.",
            "poster_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQQ7HywlOG2ct0iavUfvb0TSkvqg_pMJVcz3ZOjp68ZUMRilK-Xtx4Uwb1QRMNwEaXM5elFyDE_DQ6kE_DPo9To27ctdmCaAl4XXAt_pGA",
            "trailer": "https://www.youtube.com/embed/NC7HuJsRjs0",
        },
        {
            "id": 15,
            "title": "War",
            "category": "Action Thriller (Indian)",
            "release_year": 2019,
            "rating": "6.5/10",
            "duration": "2h 34m",
            "director": "Siddharth Anand",
            "cast": "Hrithik Roshan, Tiger Shroff, Vaani Kapoor",
            "synopsis": "An Indian soldier is assigned to eliminate his former mentor and he must keep his wits about him if he is to be successful in his mission.",
            "poster_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT2cuKvIaH5HRrPQ5nIx8lbHO7wSUf1GiXKE6mvY72J53GCRht6",
            "trailer": "https://www.youtube.com/embed/tQ0mzXRk-oM",
        },
        {
            "id": 16,
            "title": "Animal",
            "category": "Action Crime (Indian)",
            "release_year": 2023,
            "rating": "6.5/10",
            "duration": "3h 21m",
            "director": "Sandeep Reddy Vanga",
            "cast": "Ranbir Kapoor, Anil Kapoor, Bobby Deol",
            "synopsis": "The hardened son of a powerful industrialist returns home after years abroad and vows to take bloody revenge on those threatening his father's life.",
            "poster_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT9zRNezyoKFad1erjGfV9ejYPQZiqpAX3e6DJyCoRc0cxoYP_8",
            "trailer": "https://www.youtube.com/embed/Dydmpfo68DA",
        },
        {
            "id": 17,
            "title": "Sanju",
            "category": "Biographical Drama (Indian)",
            "release_year": 2018,
            "rating": "7.7/10",
            "duration": "2h 41m",
            "director": "Rajkumar Hirani",
            "cast": "Ranbir Kapoor, Paresh Rawal, Manisha Koirala",
            "synopsis": "A biopic of the controversial life of actor Sanjay Dutt: his film career, jail sentence and personal life.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI3NTM1NzMyNF5BMl5BanBnXkFtZTgwOTE4NTgzNTM@._V1_.jpg",
            "trailer": "https://www.youtube.com/embed/1J76wN0TPI4",
        },
        {
            "id": 18,
            "title": "Chhichhore",
            "category": "Comedy Drama (Indian)",
            "release_year": 2019,
            "rating": "8.3/10",
            "duration": "2h 23m",
            "director": "Nitesh Tiwari",
            "cast": "Sushant Singh Rajput, Shraddha Kapoor, Varun Sharma",
            "synopsis": "A tragic incident forces Anirudh, a middle-aged man, to take a trip down memory lane and reminisce his college days along with his friends.",
            "poster_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTR7lN6yKpdOvxKUBIdGX_HpkBFW5FDup4gzgMnumJzer8KEt9i",
            "trailer": "https://www.youtube.com/embed/tsxemFX0a7k",
        },
        {
            "id": 19,
            "title": "Padmaavat",
            "category": "Historical Drama (Indian)",
            "release_year": 2018,
            "rating": "7.0/10",
            "duration": "2h 44m",
            "director": "Sanjay Leela Bhansali",
            "cast": "Deepika Padukone, Ranveer Singh, Shahid Kapoor",
            "synopsis": "Set in medieval Rajasthan, Queen Padmavati is married to a noble king and they live in a prosperous fortress with their subjects until an ambitious Sultan hears of Padmavati's beauty and forms an obsessive love for the Queen of Mewar.",
            "poster_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ855ggdR5SEAk6ccnU09DB97EN1APWzD7P-zETOFF7BMlJUPs3",
            "trailer": "https://www.youtube.com/embed/8YaF2m7hCx0",
        },
        {
            "id": 20,
            "title": "Avatar",
            "category": "Science Fiction (Hollywood)",
            "release_year": 2009,
            "rating": "7.9/10",
            "duration": "2h 42m",
            "director": "James Cameron",
            "cast": "Sam Worthington, Zoe Saldana, Sigourney Weaver",
            "synopsis": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
            "poster_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSYWVMx6h59vKIGkku5l3hPkBbqsErDsCB7-QZ9zaKuhTN8edvL",
            "trailer": "https://www.youtube.com/embed/5PSNL1qE6VY",
        },
        {
            "id": 21,
            "title": "Avengers: Endgame",
            "category": "Superhero Action (Hollywood)",
            "release_year": 2019,
            "rating": "8.4/10",
            "duration": "3h 1m",
            "director": "Anthony Russo, Joe Russo",
            "cast": "Robert Downey Jr., Chris Evans, Mark Ruffalo",
            "synopsis": "After the devastating events of Infinity War, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
            "poster_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRXef9DJnZiq5az0UnjkmvkQufOQ5MFnF7HATYRUXN913swRuH1",
            "trailer": "https://www.youtube.com/embed/TcMBFSGVi1c",
        },
        {
            "id": 22,
            "title": "Titanic",
            "category": "Romance Drama (Hollywood)",
            "release_year": 1997,
            "rating": "7.9/10",
            "duration": "3h 14m",
            "director": "James Cameron",
            "cast": "Leonardo DiCaprio, Kate Winslet, Billy Zane",
            "synopsis": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
            "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwQlOeIost26Qv6cAAT73c9LLi0oRcXOJ6QQ5h3J1fUogSX_sD",
            "trailer": "https://www.youtube.com/embed/CHekzSiZcw4",
        },
        {
            "id": 23,
            "title": "Star Wars",
            "category": "Science Fiction (Hollywood)",
            "release_year": 2015,
            "rating": "7.8/10",
            "duration": "2h 18m",
            "director": "J.J. Abrams",
            "cast": "Daisy Ridley, John Boyega, Oscar Isaac",
            "synopsis": "As a new threat to the galaxy rises, Rey, a desert scavenger, and Finn, an ex-stormtrooper, must join Han Solo and Chewbacca to search for the one hope of restoring peace.",
            "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTITEc_k9echyKt6RJbPKiY-lS4RqCh2NWkAsrvI37wKFjG1po5",
            "trailer": "https://www.youtube.com/embed/sGbxmsDFVnE",
        },
        {
            "id": 24,
            "title": "Inception",
            "category": "Science Fiction Thriller (Hollywood)",
            "release_year": 2010,
            "rating": "8.8/10",
            "duration": "2h 28m",
            "director": "Christopher Nolan",
            "cast": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
            "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "poster_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQovCe0H45fWwAtV31ajOdXRPTxSsMQgPIQ3lcZX_mAW0jXV3kH",
            "trailer": "https://www.youtube.com/embed/YoHD9XEInc0",
        },
        {
            "id": 25,
            "title": "The Dark Knight",
            "category": "Superhero Action (Hollywood)",
            "release_year": 2008,
            "rating": "9.0/10",
            "duration": "2h 32m",
            "director": "Christopher Nolan",
            "cast": "Christian Bale, Heath Ledger, Aaron Eckhart",
            "synopsis": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
            "poster_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQkUywIUXDjHSQJIaNHYVs08osgBpF5Ot-xmB_omyEZeeRP9Xug",
            "trailer": "https://www.youtube.com/embed/EXeTwQWrcwY",
        },
        {
            "id": 26,
            "title": "Pulp Fiction",
            "category": "Crime Drama (Hollywood)",
            "release_year": 1994,
            "rating": "8.9/10",
            "duration": "2h 34m",
            "director": "Quentin Tarantino",
            "cast": "John Travolta, Uma Thurman, Samuel L. Jackson",
            "synopsis": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
            "poster_url": "https://m.media-amazon.com/images/I/914mMOJHWVL._UF894,1000_QL80_.jpg",
            "trailer": "https://www.youtube.com/embed/s7EdQ4FqbhY",
        },
        {
            "id": 27,
            "title": "Shawshank Redemption",
            "category": "Drama (Hollywood)",
            "release_year": 1994,
            "rating": "9.3/10",
            "duration": "2h 22m",
            "director": "Frank Darabont",
            "cast": "Tim Robbins, Morgan Freeman, Bob Gunton",
            "synopsis": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "poster_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRipfEoI8fb4qxidki3e_kp3fr_Kopvoi2yCKcpJGf2ngnKweMR",
            "trailer": "https://www.youtube.com/embed/6hB3S9bIaco",
        },
        {
            "id": 28,
            "title": "The Godfather",
            "category": "Crime Drama (Hollywood)",
            "release_year": 1972,
            "rating": "9.2/10",
            "duration": "2h 55m",
            "director": "Francis Ford Coppola",
            "cast": "Marlson Brando, Al Pacino, James Caan",
            "synopsis": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
            "poster_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTWmKJlXjXTiE9hkekFBy9WCRMf0eKZx2mrsgenlO-qzr9H7v0A",
            "trailer": "https://www.youtube.com/embed/sY1S34973zA",
        },
        {
            "id": 29,
            "title": "Spider-Man",
            "category": "Superhero Action (Hollywood)",
            "release_year": 2021,
            "rating": "8.2/10",
            "duration": "2h 28m",
            "director": "Jon Watts",
            "cast": "Tom Holland, Zendaya, Benedict Cumberbatch",
            "synopsis": "With Spider-Man's identity now revealed, Peter asks Doctor Strange for help. When a spell goes wrong, dangerous foes from other worlds start to appear.",
            "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtauzk4w5HwCXrx3nAm5VTFcywz62gV18C3A7KFT03SgB2k8c0",
            "trailer": "https://www.youtube.com/embed/JfVOs4VSpmA",
        },
        {
            "id": 30,
            "title": "Dune: Part Two",
            "category": "Science Fiction (Hollywood)",
            "release_year": 2024,
            "rating": "8.6/10",
            "duration": "2h 46m",
            "director": "Denis Villeneuve",
            "cast": "Timothée Chalamet, Zendaya, Rebecca Ferguson",
            "synopsis": "Paul Atreides unites with Chani and the Fremen while on a warpath of revenge against the conspirators who destroyed his family.",
            "poster_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRBu8Gzdygf5OOqBJUIJ3-ZxiPbLh62OhvLmtOvuR7x2gF3DucU",
            "trailer": "https://www.youtube.com/embed/Way9Dexny3w",
        },
    ]


def _get_movies():
    try:
        return list(Movie.objects.all().order_by('-is_featured', '-release_year')[:10])
    except OperationalError:
        return []


def _get_movie_values():
    try:
        return list(
            Movie.objects.all().values(
                "id", "title", "release_year", "category", "rating", "poster_url"
            )
        )
    except OperationalError:
        return []


def _get_trailer_embed_url(trailer_url):
    if not trailer_url:
        return None

    import re

    match = re.search(r"youtube\.com/embed/([A-Za-z0-9_-]+)", trailer_url)
    if not match:
        match = re.search(r"youtube\.com/watch\?v=([A-Za-z0-9_-]+)", trailer_url)
    if not match:
        match = re.search(r"youtu\.be/([A-Za-z0-9_-]+)", trailer_url)
    if not match:
        return trailer_url

    video_id = match.group(1)
    return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0"


def index(request):
    """Render the homepage with featured and recommended movies."""
    movies = _get_movies()
    if not movies:
        movies = _sample_movies()

    return render(request, "Home.html", {"title": "PrimeVideo - Home", "movies": movies})


def movie_list(request):
    """Return a JSON list of available movies."""
    movies = _get_movie_values()
    if not movies:
        movies = _sample_movies()
    return JsonResponse({"movies": movies})


def movie_detail(request, movie_id):
    """Render a movie detail page or return JSON when requested."""
    movie_data = None

    try:
        movie = Movie.objects.get(pk=movie_id)
    except (Movie.DoesNotExist, OperationalError):
        movie_data = next((item for item in _sample_movies() if item["id"] == movie_id), None)
        if movie_data is None:
            return JsonResponse({"error": "Movie not found"}, status=404)
        movie_data = dict(movie_data)
        movie_data["trailer_embed_url"] = _get_trailer_embed_url(movie_data.get("trailer"))
    else:
        movie_data = {
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "category": movie.category,
            "rating": movie.rating,
            "synopsis": movie.synopsis,
            "poster_url": movie.poster_url,
            "duration": None,
            "director": None,
            "cast": None,
            "trailer": None,
            "trailer_embed_url": None,
        }

    if request.headers.get("Accept") == "application/json" or request.GET.get("format") == "json":
        return JsonResponse(movie_data)

    return render(request, "movie_detail.html", {"movie": movie_data})
