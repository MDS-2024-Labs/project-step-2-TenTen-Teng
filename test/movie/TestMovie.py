import unittest
import os
from unittest import mock
import unittest.mock

from movie.movie import Movie

@unittest.mock.patch.dict(os.environ, {"TMDB_API_KEY": "abc"})
class TestMovie(unittest.TestCase):   

    def test_init_true(self):
        with unittest.mock.patch.object(
            Movie, "test_api_connection", return_value=True):
            movie = Movie()

        self.assertEqual(os.environ["TMDB_API_KEY"], "abc")
        self.assertEqual(movie.get_TMDB_key, "abc")

        self.assertIsNotNone(movie.config)
        self.assertEqual(movie.url, "https://api.themoviedb.org/3")
        self.assertDictEqual(
            movie.header, 
            {
                "accept": "application/json",
                "Authorization": "Bearer " + "abc"
                }
            )
        
    def test_init_false(self):
        with unittest.mock.patch.object(
            Movie, "test_api_connection", return_value=False):
            with self.assertRaises(ConnectionError):
                Movie()

    @unittest.mock.patch.object(Movie, "fetch_movie", return_value = {})
    @unittest.mock.patch.object(
        Movie, "movie_parse_response", return_value = ["a", "b"]
        )
    def test_movie_search(
        self, 
        mock_fetch_movie, mock_movie_parse_response
        ):

        with unittest.mock.patch.object(
            Movie, "test_api_connection", return_value=True):
            self.movie = Movie()

        # Check invaild input.
        with self.assertRaises(AssertionError):
            self.movie.movie_search(None, {})

        self.assertEqual(self.movie.movie_search("abc", {}), ["a", "b"])


    # def test_fetch_movie(self):
    #     pass

    # def test_fetch_collection(self):
    #     pass

    # def test_movie_parse_response(self):
    #     pass

    # def test_movie_recom(self):
    #     pass

    # def test_fetch_recom(self):
    #     pass

    # def test_test_api_connection(self):
    #     pass


if __name__ == "__main__":
    unittest.main()