import uuid, json

print(r'use \n'+' to seprate lines,\n {}'.format("""\nMinecraft colour codes (basically like CMD):\n§0 = Black       §8 = Gray\n§1 = Blue        §9 = Light Blue\n§2 = Green       §A = Light Green\n§3 = Aqua        §B = Light Aqua\n§4 = Red         §C = Light Red\n§5 = Purple      §D = Light Purple\n§6 = Yellow      §E = Light Yellow\n§7 = White       §F = Bright White\n§l = Bold        §o = Italic\n§k = Changing letter (?)\n\n"""))

text = '''
||"format_version":1,"header":||"description":"{}","min_engine_version":&&1,10,0@@,"name":"{}","uuid":"{}","version":&&0,0,1@@??,"modules":&&||"description":" ","type":"resources","uuid":"{}","version":&&0,0,1@@??@@??'''.format(input('Pack Description:'), input('Pack Name:'), f'{uuid.uuid4()}', f'{uuid.uuid4()}')
f = open('manifest.json', 'w')
f.write(json.dumps(json.loads(text.replace('||', '{').replace('??', '}').replace('&&', '[').replace('@@', ']')),indent=3))
f.close()
