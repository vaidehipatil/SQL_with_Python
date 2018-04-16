# -*- coding: utf-8 -*-
list_initial = [ { 'first_name' : 'Rose',
                     'last_name'  : 'Tyler',
                     'home'       : 'Earth' },
                   { 'first_name' : 'Zoe',
                     'last_name'  : 'Heriot',
                     'home'       : 'Space Station W3'},
                   { 'first_name' : 'Jo',
                     'last_name'  : 'Grant',
                     'home'       : 'Earth'},
                   { 'first_name' : 'Leela',
                     'last_name'  : 'null',
                     'home'       : 'Unspecified'},
                   { 'first_name' : 'Romana',
                     'last_name'  : 'null',
                     'home'       : 'Gallifrey'},
                   { 'first_name' : 'Clara',
                     'last_name'  : 'Oswald',
                     'home'       : 'Earth'},
                   { 'first_name' : 'Adric',
                     'last_name'  : 'null',
                     'home'       : 'Alzarius'},
                   { 'first_name' : 'Susan',
                     'last_name'  : 'Foreman',
                     'home'       : 'Gallifrey'} ];
a = []
list_new = []
l = len(list_initial)

strTable = "<html><style>table, th, td {border: 1px solid black;}</style><table><tr><th>First Name</th> <th>Last Name</th>  <th>Home</th></tr>"

for i in range (0,l):
    dict = list_initial[i]
    strRW = "<tr><td>" + str(dict['first_name']) + "</td><td>" + str(dict['last_name']) + "</td>  <td>" + str(dict['home']) + "</td></tr>"
    strTable = strTable + strRW

strTable = strTable + "</table></html>"

hs = open("asciiCharHTMLTable.html", 'w')
hs.write(strTable)

print (strTable)



‌




                