#!/usr/bin/env python
# coding: utf-8

import re
import urllib2
from xml.dom.minidom import parseString as xml_parse
import requests


def dbpedia_query(resource, desired, what='property'):
    original_query = u'''select ?{} where {{
    <{}>
    <http://dbpedia.org/{}/{}> ?{} . }}'''
    query = original_query.format(desired, resource.replace(' ', '_'), what,
                                  desired, desired)
    response = requests.get('http://dbpedia.org/sparql',
                            params={'query': query})
    xml = xml_parse(response.content)
    results = xml.getElementsByTagName('binding')
    return [result.childNodes[0].childNodes[0].toxml() for result in results]

def get_country_of_birth(name):
    uri = 'http://dbpedia.org/resource/'
    birth_places = dbpedia_query(uri + name, 'birthPlace')
    country = []
    for place in birth_places:
        if place.startswith(uri):
            place = place.replace(uri, '')
        if ',' in place:
            place = place.split(',')[-1].strip()
        country.append(get_country(place))
    return country

def get_country(place):
    uri = 'http://dbpedia.org/page/'
    place = uri + place
    response = requests.get(place)
    if 'http://schema.org/Country' in response.content:
        result = place.replace(uri, '')
    elif ':country' not in response.content:
        result = ''
    else:
        result = response.content.split(':country')[1].split('\n')[0]\
                         .split('">')[0].split('/')[-1]
    result = urllib2.unquote(result).replace('_', ' ')
    return result

def get_short_description(name):
    uri = 'http://dbpedia.org/resource/'
    result = dbpedia_query(uri + name, 'wordnet_type')[0]
    return result.replace('http://www.w3.org/2006/03/wn/wn20/instances/synset-', '')\
                 .replace('-noun-1', '')
