#!/usr/bin/env python3
from jeepney.integrate.blocking import DBusConnection
import secretstorage  #3.1.1
from pprint import pprint
import argparse
import json
import sys


class create_connection():
  def __enter__(self) -> DBusConnection:
    print("open sock!")
    self.connection = secretstorage.dbus_init()
    return self.connection

  def __exit__(self, exc_type, exc_value, traceback): # type: ignore
    print("close sock!")
    self.connection.sock.close()

def add(args):
  if args.app_name and args.password and args.attributes:
    attributes = json.loads(args.attributes)

    with create_connection() as conn:
      collection = secretstorage.get_default_collection(conn)
      if (collection.is_locked()):
        print("base locked:" + str(collection.is_locked()))
        collection.unlock()

      item = collection.create_item(args.app_name, attributes, args.password)
      return True

def get(args):
    attributes = json.loads(args.attributes)
    pprint(attributes)
    with create_connection() as conn:
      collection = secretstorage.get_default_collection(conn)
      if (collection.is_locked()):
        print("base locked:" + str(collection.is_locked()))
        collection.unlock()

      items = collection.search_items(attributes)
      for item in items:
        print("----------------")
        print("label: " + item.get_label())
        pprint(item.get_attributes())
        print("secret: " + item.get_secret().decode('utf-8'))
      return True

def remove(args):
    attributes = json.loads(args.attributes)
    pprint(attributes)
    with create_connection() as conn:
      collection = secretstorage.get_default_collection(conn)
      if (collection.is_locked()):
        print("base locked:" + str(collection.is_locked()))
        collection.unlock()

      items = [ item for item in collection.search_items(attributes) ]
      if len(items) == 1:
          items[0].delete()
          return True
      if len(items) > 1:
          print("ERROR: many matches found")
          return False
      if len(items) < 1:
          print("ERROR: not matches found")
          return False

def main():

  parser = argparse.ArgumentParser(description='secretstorage')
  subparsers = parser.add_subparsers()

  parser_add = subparsers.add_parser('add', help='add help')
  parser_add.add_argument('-a', '--app_name',type=str, help='app name', required=True)
  parser_add.add_argument('-p', '--password', type=str, help='password', required=True)
  parser_add.add_argument('-att', '--attributes', type=str, help='attributes as json', required=True)
  #parser_add.add_argument('-c', '--collection', type=str, help='collection name', required=False)
  parser_add.set_defaults(func=add)

  parser_get = subparsers.add_parser('get', help='get help')
  parser_get.add_argument( '-att', '--attributes', type=str, help='attributes as json', required=True)
  #parser_add.add_argument('-c', '--collection', type=str, help='collection name', required=False)
  parser_get.set_defaults(func=get)

  parser_remove = subparsers.add_parser('remove', help='remove help')
  parser_remove.add_argument('-att', '--attributes', type=str, help='attributes as json', required=True)
  #parser_add.add_argument('-c', '--collection', type=str, help='collection name', required=False)
  parser_remove.set_defaults(func=remove)

  args = parser.parse_args()
  #if len(sys.argv) == 0:
  #  parser.print_help()
  #  exit(1)
  args.func(args)


#  with create_connection() as conn:
#    collection = secretstorage.get_default_collection(conn)
#    if (collection.is_locked()):
#      print("base locked:" + str(collection.is_locked()))
#      collection.unlock()
#
#    attributes = {
#        'application': 'myapp',
#        'another attribute': 'another value'
#        }
#    item = collection.create_item('My first item', attributes, b'pa$$word')
#    
#    print("label: " + item.get_label())
#    print("attrib: ")
#    pprint(item.get_attributes())
#    print("secret: " + item.get_secret())
#    
#    items = collection.search_items({'application': 'myapp'})
#    print("----------------")
#    print("label: " + items.get_label())
#    print("attrib: " + items.get_attributes())
#    print("secret: " + items.get_secret())
#
#    collection.lock()
 
if __name__ == "__main__":
  main()
