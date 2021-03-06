from data_cleaning_and_preparation.clean import remove_unwanted_rows, remove_unwanted_columns
from data_cleaning_and_preparation.pre_process import encode_categorical_features, get_encoding_columns_titles, encode_categorical_features
from data_cleaning_and_preparation.feature_selection import continuous_features_selection, discrete_features_selection
from training_and_testing_gross.training_and_testing import training_and_testing as g_training_and_testing
from training_and_testing_gross.oob_error import oob_error as g_oob_error
from training_and_testing_imdb_ratings.training_and_testing import training_and_testing as i_training_and_testing
from training_and_testing_imdb_ratings.oob_error import oob_error as i_oob_error

remove_unwanted_rows("movie_metadata.csv")
remove_unwanted_columns("clean_movie_data.csv")
encode_categorical_features("features.csv")
encode_categorical_features("features.csv")
g_oob_error("encoded_features.csv", "imdb_ratings.csv")
i_oob_error("encoded_features.csv", "imdb_ratings.csv")
print(g_training_and_testing("encoded_features.csv", "gross.csv"))
print(i_training_and_testing("encoded_features.csv", "imdb_ratings.csv"))
g_oob_error("encoded_features.csv", "imdb_ratings.csv")
i_oob_error("encoded_features.csv", "imdb_ratings.csv")
