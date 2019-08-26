import sys


class Route:

    def run(self):
        action = sys.argv[1]
        action_module = ''
        try:
            action_module = __import__("src.actions.%s" % action.title(), fromlist=["src.actions"])
            action_module.run()
        except ImportError:
            print(ImportError)
            print(action)

        return True
