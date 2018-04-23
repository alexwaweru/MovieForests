import csv
import logging


def get_encoding_columns_titles(inputfile):
    """
    Args:
        filename (str): The csv file containing the movie metadata from which to obtain the categorical column titles
    Returns:
        column_titles (dict): A dictionary with keys as title of a categorical features and values as the possible categories under the feature
    Raises:
        IOError: Unable to read file
    """
    #categorical_features = ["color", "genres", "plot_keywords", "language", "country", "content_rating", "facenumber_in_poster", "title_year", "aspect_ratio"]
    categorical_features = ["director_name", "actor_2_name", "actor_1_name", "actor_3_name", "color", "genres", "plot_keywords", "language", "country", "content_rating", "facenumber_in_poster", "title_year", "aspect_ratio"]
    feature_and_categories = {}
    for item in categorical_features:
        feature_and_categories[item] = []
        
    try:
        with open(inputfile) as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                for feature in categorical_features:
                    temp = row[feature].strip()
                    temp = temp.replace(u"'" , '')
                    temp = temp.lower()
                    categories = temp.split('|')
                    for category in categories:
                        if category not in feature_and_categories[feature]:
                            feature_and_categories[feature].append(category)
    except IOError:
        logging.exception('')

    return feature_and_categories


def encode_categorical_features(inputfile):
    """
    Args:
        inputfilename (str): The csv file containing the movie metadata
    Returns:
        encoded_features (str): A csv file in which all categorical features are encoded
    Raises:
        IOError: Unable to read file
    """

    feature_and_categories = get_encoding_columns_titles(inputfile)
    outputfile = open('encoded_features.csv', 'w')
    try:
        with open(inputfile) as file:
            reader = csv.DictReader(file, delimiter=',')
            fieldnames = reader.fieldnames

            title_line = ''
            for fieldname in fieldnames:
                if fieldname.strip().lower() in feature_and_categories.keys():
                    for category in feature_and_categories[fieldname.strip().lower()]:
                        title_line = title_line + ',' + category.strip()
                else:
                    title_line = title_line + ',' + fieldname
            if title_line[0] == ",":
                title_line = title_line[1:]

            outputfile.write(title_line + '\n')

            for row in reader:
                line = ''
                for fieldname in fieldnames:
                    if fieldname.strip().lower() in feature_and_categories.keys():
                        temp = row[fieldname].strip()
                        temp = temp.replace(u"'" , '')
                        temp = temp.lower()
                        data = temp.split('|')
                        for category in feature_and_categories[fieldname.strip().lower()]:
                            if category in data:
                                line = line + ',' + '1'
                            else:
                                line = line + ',' + '0'
                    else:
                        temp = row[fieldname].strip()
                        temp = temp.replace(u"'" , '')
                        temp = temp.lower()
                        line = line + ',' + temp
                if line[0] == ",":
                    line = line[1:]
                outputfile.write(line + '\n')
            outputfile.close()
    except IOError:
        logging.exception('')
