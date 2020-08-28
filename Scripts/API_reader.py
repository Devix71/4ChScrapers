from random import random

import basc_py4chan
import urllib.request
import os
import glob
import time
import json

'''
Using the 4chan python api the script downloads both text (nicely formatted in .json) and images on a specified board.
My main goal is eventually replacing it with a custom(and faster) scraper, but until then I won't sacrifice the features
for performance
'''


# downloads images across a single board from every thread
def picture_download(path, brd):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        files = glob.glob(path + '*')
        for g in files:
            os.remove(g)
        os.rmdir(path)
        os.mkdir(path)

    board = basc_py4chan.Board(brd)
    t = time.thread_time()
    all_thread_ids = board.get_all_thread_ids()

    for z in all_thread_ids:
        if t <= 7:
            thread = board.get_thread(z)

            # print thread information
            print(thread)
            print('Sticky?', thread.sticky)
            print('Closed?', thread.closed)
            print('Replies:', len(thread.replies))

            # print topic post information
            topic = thread.topic
            print('Topic Repr', topic)
            print('Postnumber', topic.post_number)
            print('Timestamp', topic.timestamp)
            print('Datetime', repr(topic.datetime))
            print('Subject', topic.subject)
            print('Comment', topic.text_comment)

            smth = topic.text_comment[:65].translate({ord('?'): " question "})
            smth = smth.translate({ord('<'): " less than "})
            smth = smth.translate({ord('>'): "Implying "})
            smth = smth.translate({ord(':'): ";"})
            smth = smth.translate({ord('"'): "'"})
            smth = smth.translate({ord('/'): " slash "})
            smth = smth.translate({ord('\n'): " newLine "})
            smth = smth.translate({ord('\\'): " backslash "})

            info = "folder" + smth + str(random())

            pather = path + info + "\\"
            os.mkdir(pather)
            for x, y in zip(thread.replies, thread.file_objects()):
                print(t)
                print('Filename', y.filename_original)
                print('Fileurl', y.file_url)
                urllib.request.urlretrieve(y.file_url, pather + y.filename_original)
                print()
                print(x.post_id)
                print(x.text_comment)
        else:
            break


# downloads all replies across a board and stores it in .json format
def text_download(path, brd):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        files = glob.glob(path + '*')
        for g in files:
            os.remove(g)
        os.rmdir(path)
        os.mkdir(path)

    board = basc_py4chan.Board(brd)
    t = time.thread_time()
    all_thread_ids = board.get_all_thread_ids()

    for z in all_thread_ids:
        if t <= 7:
            thread = board.get_thread(z)

            # print thread information
            print(thread)
            print('Sticky?', thread.sticky)
            print('Closed?', thread.closed)
            print('Replies:', len(thread.replies))

            # print topic post information
            topic = thread.topic
            print('Topic Repr', topic)
            print('Postnumber', topic.post_number)
            print('Timestamp', topic.timestamp)
            print('Datetime', repr(topic.datetime))
            print('Subject', topic.subject)
            print('Comment', topic.text_comment)

            smth = topic.text_comment[:65].translate({ord('?'): " question "})
            smth = smth.translate({ord('<'): " less than "})
            smth = smth.translate({ord('>'): "Implying "})
            smth = smth.translate({ord(':'): ";"})
            smth = smth.translate({ord('"'): "'"})
            smth = smth.translate({ord('/'): " slash "})
            smth = smth.translate({ord('\n'): " newLine "})
            smth = smth.translate({ord('\\'): " backslash "})
            smth = smth.translate({ord('*'): " asterisk "})

            info = "folder" + smth + str(random())

            data = {}
            data[info] = []
            REP = {}
            REP["Replies"] = []

            pather = path + info + "\\"
            os.mkdir(pather)

            for x, y in zip(thread.replies, thread.file_objects()):
                print(t)
                print()

                REP["Replies"].append({'Post ID:': x.post_id,
                                       'Reply :': x.text_comment,
                                       'Filename :': y.filename_original,
                                       'File URL :': y.file_url + "\n"})

            data[info].append({'Sticky :': thread.sticky,
                               'Closed :': thread.closed,
                               'OP Postnumber :': topic.post_number,
                               'DateTime :': repr(topic.datetime),
                               'Subject :': topic.subject,
                               'Comment :': topic.text_comment,
                               'Replies': REP["Replies"]})

            with open(pather + smth + '.json', 'w') as outfile:
                json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            break


# downloads both text and images from every thread from a specified board
def all_download(path, brd):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        files = glob.glob(path + '*')
        for g in files:
            os.remove(g)
        os.rmdir(path)
        os.mkdir(path)

    board = basc_py4chan.Board(brd)
    t = time.thread_time()
    all_thread_ids = board.get_all_thread_ids()

    for z in all_thread_ids:
        if t <= 7:
            thread = board.get_thread(z)

            # print thread information
            print(thread)
            print('Sticky?', thread.sticky)
            print('Closed?', thread.closed)
            print('Replies:', len(thread.replies))

            # print topic post information
            topic = thread.topic
            print('Topic Repr', topic)
            print('Postnumber', topic.post_number)
            print('Timestamp', topic.timestamp)
            print('Datetime', repr(topic.datetime))
            print('Subject', topic.subject)
            print('Comment', topic.text_comment)

            smth = topic.text_comment[:65].translate({ord('?'): " question "})
            smth = smth.translate({ord('<'): " less than "})
            smth = smth.translate({ord('>'): "Implying "})
            smth = smth.translate({ord(':'): ";"})
            smth = smth.translate({ord('"'): "'"})
            smth = smth.translate({ord('/'): " slash "})
            smth = smth.translate({ord('\n'): " newLine "})
            smth = smth.translate({ord('\\'): " backslash "})
            smth = smth.translate({ord('*'): " asterisk "})

            info = "folder" + smth + str(random())

            data = {}
            data[info] = []
            REP = {}
            REP["Replies"] = []

            pather = path + info + "\\"
            os.mkdir(pather)

            for x, y in zip(thread.replies, thread.file_objects()):
                print(t)
                print()

                REP["Replies"].append({'Post ID:': x.post_id,
                                       'Reply :': x.text_comment,
                                       'Filename :': y.filename_original,
                                       'File URL :': y.file_url})
                urllib.request.urlretrieve(y.file_url, pather + y.filename_original)
            data[info].append({'Sticky :': thread.sticky,
                               'Closed :': thread.closed,
                               'OP Postnumber :': topic.post_number,
                               'DateTime :': repr(topic.datetime),
                               'Subject :': topic.subject,
                               'Comment :': topic.text_comment,
                               'Replies': REP["Replies"]})

            with open(pather + smth + '.json', 'w') as outfile:
                json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            break


# downloads images from a specified thread
def picture_download_single(path, brd, id):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        files = glob.glob(path + '*')
        for g in files:
            os.remove(g)
        os.rmdir(path)
        os.mkdir(path)

    board = basc_py4chan.Board(brd)
    thread = board.get_thread(id)

    # print thread information
    print(thread)
    print('Sticky?', thread.sticky)
    print('Closed?', thread.closed)
    print('Replies:', len(thread.replies))

    # print topic post information
    topic = thread.topic
    print('Topic Repr', topic)
    print('Postnumber', topic.post_number)
    print('Timestamp', topic.timestamp)
    print('Datetime', repr(topic.datetime))
    print('Subject', topic.subject)
    print('Comment', topic.text_comment)

    smth = topic.text_comment[:65].translate({ord('?'): " question "})
    smth = smth.translate({ord('<'): " less than "})
    smth = smth.translate({ord('>'): "Implying "})
    smth = smth.translate({ord(':'): ";"})
    smth = smth.translate({ord('"'): "'"})
    smth = smth.translate({ord('/'): " slash "})
    smth = smth.translate({ord('\n'): " newLine "})
    smth = smth.translate({ord('\\'): " backslash "})

    info = "folder" + smth + str(random())

    pather = path + info + "\\"
    os.mkdir(pather)
    for x, y in zip(thread.replies, thread.file_objects()):
        print('Filename', y.filename_original)
        print('Fileurl', y.file_url)
        urllib.request.urlretrieve(y.file_url, pather + y.filename_original)
        print()
        print(x.post_id)
        print(x.text_comment)
