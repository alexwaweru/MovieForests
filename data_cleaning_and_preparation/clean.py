import csv
import logging

def remove_unwanted_rows(inputfilename):
    """
    Args:
        filename (str): The csv file containing the movie metadata to be remove unwanted columns
    Returns:
        filename (str): The filename of the new csv file containing features used for the training model.
    Raises:
        IOError: Unable to read file
    """

    outputfile =open('clean_movie_data.csv', 'w')

    try:
        inputfile = open(inputfilename, 'r')
        title_row = (inputfile.readline())
        length = len(title_row.split(','))
        outputfile.write(title_row)

        for row in (inputfile.readlines()):
            row = row.split(',')
            if ("" not in row) and (len(row)==length) :
                row = str(row)
                row = row[1:]
                row = row[:-4]+"'"
                outputfile.write(row+'\n')

        inputfile.close()
        outputfile.close()
    except IOError:
        logging.exception('')

    return 'clean_movie_data.csv'


def remove_unwanted_columns(inputfilename):
    """
    Args:
        filename (str): The csv file containing the movie metadata to be remove unwanted columns
    Returns:
        filename (str): The filename of the new csv file containing features used for the training model."facenumber_in_poster", "title_year", "aspect_ratio"
    Raises:
        IOError: Unable to read file
    """

    #outputfileX = open('features.csv', 'w')
    outputfileY1 = open('gross.csv', 'w')
    outputfileY1.write('gross'+'\n')
    outputfileY2 = open('imdb_ratings.csv', 'w')
    outputfileY2.write('imdb_ratings'+'\n')

    try:
        with open(inputfilename) as file:
            reader = csv.DictReader(file, delimiter=',')
            fieldnames = reader.fieldnames

            for fieldname in fieldnames:
                deleted_cols = ["movie_title",
                                "movie_imdb_link","gross","imdb_score", "num_critic_for_reviews",
                                "num_voted_users","num_user_for_reviews"]
                for col in deleted_cols:
                    if col == fieldname:
                        idx = fieldnames.index(fieldname)
                        fieldnames =  fieldnames[:idx] + fieldnames[idx+1:]
                        break

            writer = csv.DictWriter(open('features.csv','w'), fieldnames=fieldnames)
            stopper = 0
            for row in reader:
                del row["num_critic_for_reviews"]
                #del row["director_name"]
                #del row["actor_2_name"]
                #del row["actor_1_name"]
                del row["movie_title"]
                #del row["actor_3_name"]
                del row["num_voted_users"]
                del row["num_user_for_reviews"]
                del row["movie_imdb_link"]
                outputfileY1.write(row['gross'].replace(u"'", "")+'\n')
                outputfileY2.write(row['imdb_score'].replace(u"'", "")+'\n')
                del row["gross"]
                del row["imdb_score"]
                if stopper == 0:
                    writer.writeheader()
                    stopper = 1
                writer.writerow(row)
            outputfileY1.close()
            outputfileY2.close()
    except IOError:
        logging.exception('')
