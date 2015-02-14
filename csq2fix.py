#!/usr/bin/env python

import json
import sys
import argparse

# Use this date string instead of making real ones:
DATE = "1999-12-31T23:59:00.000Z"


def csq2fix(textin, username):
    """
    Convert Colon-Separated Questions to Django fixture (as JSON text).
    Implemented as batch rather than streaming, so some limit on size.
    A username is required because it isn't part of CSQ but is needed
    by the database.

    Parameters:
    textin : a string containing Colon-Separated Questions
    username : a string ("zero-security") identity to use
    """
    text_by_question = textin.split("\n:\n")[1:]
    q_a_blocks = [q_block.split("\n::\n") for q_block in text_by_question]
    data = []
    q, a = 0, 0 # counters for pks
    for q_block in q_a_blocks:
        q += 1
        question = q_block.pop(0)
        data.append({"pk": q,
                     "model": "shufflesort.question",
                     "fields": {"text": question,
                                "user": username,
                                "date": DATE,}})
        for answer in q_block:
            a += 1
            data.append({"pk": a,
                         "model": "shufflesort.answer",
                         "fields": {"text": answer,
                                    "user": username,
                                    "date": DATE,
                                    "question": q,}})
    result = json.dumps(data, indent=2)
    return result


if __name__ == '__main__':
    description = 'Convert Colon-Separated Questions to Django fixture'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('username', help="zero-security identity to assign")
    args = parser.parse_args()

    textin = sys.stdin.read()

    textout = csq2fix(textin, args.username)

    print(textout)
