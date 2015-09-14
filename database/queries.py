#!/usr/bin/python
# -*- coding: utf-8 -*-

#from flask import g
#from config import *
#import sys, sqlite3

#con = app.app_context()

def get_all_survey_responses(project):
    with con:

        cur = con.cursor()
        cur.execute(
            "SELECT * FROM surveys WHERE project = %s", [project])
        response = cur.fetchall()
        return response


def get_survey_response(username, project):
    with con:

        cur = con.cursor()
        cur.execute(
            "SELECT * FROM surveys WHERE username = %s AND project = %s", [username, project])
        try:
            response = cur.fetchone()
            return response[0]
        except:
            return "There was a problem grabbing the info from the database"


def get_individual_survey_response(username, project, column):
    with con:

        cur = con.cursor()
        cur.execute("SELECT %s FROM surveys WHERE username = %s AND project = %s", [
                    column, username, project])
        try:
            response = cur.fetchone()
            return response[0]
        except:
            return "There was a problem grabbing the info from the database"


def insert_survey_entry(first_name, last_name, phone_number, phone_carrier, email, age, gender, platforms, genres, buy_frequency, play_frequency, spending, games_played, is_industry_employed, appointment_time, notifications):
    with con:

        cur = con.cursor()
        cur.execute("""INSERT INTO surveys (first_name, last_name, phone_number, phone_carrier, email, age, gender, platforms, genres, buy_frequency, play_frequency, spending, games_played, is_industry_employed, appointment_time, notifications) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    [first_name, last_name, phone_number, phone_carrier, email, age, gender, platforms, genres, buy_frequency, play_frequency, spending, games_played, is_industry_employed, appointment_time, notifications])


