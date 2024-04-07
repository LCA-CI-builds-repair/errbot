from errbot import BotPlugin, cmdfilter


class TestCommandNotFoundFilter(BotPlugin):
    @cmdfilter(catch_unprocessed=True)
    def command_not_found(self, msg, cmd, args, dry_run, emptycmd=False):
---
def handle_command_not_found(self, message, cmd, args):
    """
    Display a message with the correct usage if the command is not found.
    """
    if not cmd:
        return message, "", args

    return "Command not found: {}{}".format(cmd, " " + " ".join(args) if args else "")
