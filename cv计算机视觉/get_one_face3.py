#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  get_one_face3.py
#
#  Copyright 2019 Dell <Dell@DESKTOP-7RQIMGT>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import face_recognition
from PIL import Image, ImageDraw
import time
from cv2 import cv2
import threading

import os


def img_process():
    #TODO:这里要遍历图片文件夹
    total_image = os.listdir('E:/person_face_get/' + 'images')
    known_face_names = []
    known_face_encodings = []

    for images in total_image:
        temp_image = face_recognition.load_image_file("./images/" + images)
        known_face_names.append(images[0:-4])
        temp_face_encoding = face_recognition.face_encodings(temp_image)[0]
        known_face_encodings.append(temp_face_encoding)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_SATURATION, 50)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)

    while True:
        ret, img_rgb_ori = cap.read()
        if ret == False:
            time.sleep(1)
            continue

        cv2.imwrite('E:/person_face_get/' + 'cap.jpg', img_rgb_ori)
        unknown_image = face_recognition.load_image_file('E:/person_face_get' +
                                                         "/cap.jpg")
        face_locations = face_recognition.face_locations(unknown_image,
                                                         model='cnn')
        face_encodings = face_recognition.face_encodings(
            unknown_image, face_locations)
        current_name_list = []
   
        for (top, right, bottom,
             left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings,
                                                     face_encoding,
                                                     tolerance=0.35)
            name = "Unknown"
           
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                matches.remove(True)
                current_name_list.append(name)

            else:
                if len(matches) > 0:
                    is_unknown = len(matches)
            cv2.rectangle(img_rgb_ori, (left, top), (right, bottom),
                          (255, 255, 255))
            cv2.putText(img_rgb_ori,
                        name, (left, top),
                        font,
                        1, (255, 255, 255),
                        thickness=2)
        cv2.imshow('out', img_rgb_ori)

        #说明有关键人物
        if not current_name_list == []:
            pass
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    thread_img = threading.Thread(target=img_process, name='img')
    print("Thread created! Please wait ")
    thread_img.start()
