import uuid, json

def manif():
  try:
    print(r'use \n','to seprate lines.\n',"\nMinecraft text colour codes:\n§0 = Black       §8 = Gray\n§1 = Blue        §9 = Light Blue\n§2 = Green       §A = Light Green\n§3 = Aqua        §B = Light Aqua\n§4 = Red         §C = Light Red\n§5 = Purple      §D = Light Purple\n§6 = Yellow      §E = Light Yellow\n§7 = White       §F = Bright White\n§l = Bold        §o = Italic\n§k = Changing letter thing (?)\n\n")
    with open('manifest.json', 'w') as f:
      json.dump({"format_version":1,"header":{"description":input('Pack Description - '),"min_engine_version":[1,10,0],"name":input('Pack Name - '),"uuid":str(uuid.uuid4()),"version":[0,0,1]},"modules":[{"description":" ","type":"resources","uuid":str(uuid.uuid4()),"version":[0,0,1]}]},f,indent=3)
    return 'File successfully created!'
  except Exception as exception:
    return(f'Script ran into an error!\n{exception}')
print(manif())
