"""
file: main.py
author: Afnan Enayet

This module is the entry point for the data processing pipeline, which takes
the raw HTML data scraped from the course assessment portal.
"""

import os
from typing import List
from pathlib import Path
from bs4 import BeautifulSoup
import argparse

# The set of classes that need to be present for a valid "review"
REVIEW_CLASSES: set = {"mPTDC", "TTHC", "mPTLC", "PTLC", "OOLT"}


def load_html(path: str) -> str:
    """ Load the contents of an HTML file given some path

    This function will raise an exception if the path is not a valid,
    accessible file.

    Args:
        - path: The path to a file
    Returns: The contents of the file as a string
    """
    # Check the validity of the path
    path_obj = Path(path)

    if not path_obj.is_file():
        raise ValueError("Given path is not a valid file")

    # The string holding the contents of the file
    file_str: str = ""

    # Read the contents of a file to string
    with open(path, "r") as f:
        file_str = f.read()
    return file_str


def parse_html(html_contents: str) -> List[str]:
    """ Given a file containing reviews for a class, a faculty member, or a
    cross section, this function parses the actual text content of reviews and
    dumps them into a list.

    Args:
        - html_contents: A string containing the contents of the HTML file to parse
    Returns: A list of strings, containing all of the reviews that were parsed
    """
    soup = BeautifulSoup(html_contents, "lxml")

    # try to look for the table elements with the review text
    review_candidates = soup.findAll("td")
    reviews = list()

    # Look for elements that have the proper set of classes, so we
    # can determine that they are valid reviews
    for rev in review_candidates:
        if rev.has_attr("class"):
            classes: set = set(rev.get("class", []))

            if classes == REVIEW_CLASSES:
                reviews.append(rev.text)
    return reviews


def main():
    """ Entry point for the main function
    """
    parser = argparse.ArgumentParser(
        description="Process HTML files with class review data")
    parser.add_argument("file_loc", type=str,
                        help="The location of the HTML file to parse")
    args = parser.parse_args()

    # load file into a string
    f = load_html(args.file_loc)
    l = parse_html(f)

    for review in l:
        print(review)


if __name__ == "__main__":
    main()
