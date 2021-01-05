from pprintpp import pprint
from munch import munchify
import yaml

ifh = open("peonbot.yaml", "r")
config = munchify(yaml.safe_load(ifh))
ifh.close()