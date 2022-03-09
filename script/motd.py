"""Message of the Day."""

import colors

def motd(DATE, AUTHOR, CONTRIBUTOR, VERSION):
    """Display the message of the day."""
    print('\n')
    print(colors.bgColors.PRIMARY+' ███╗   ███╗ ██████╗███████╗')
    print(colors.bgColors.PRIMARY+' ████╗ ████║██╔════╝██╔════╝    '+colors.bgColors.TITLE_DESCRIPTION_MOTD+'Author : '+colors.bgColors.TEXTE_DESCRIPTION_MOTD+AUTHOR)
    print(colors.bgColors.PRIMARY+' ██╔████╔██║██║     ███████╗    '+colors.bgColors.TITLE_DESCRIPTION_MOTD+'Contributor : '+colors.bgColors.TEXTE_DESCRIPTION_MOTD+CONTRIBUTOR)
    print(colors.bgColors.PRIMARY+' ██║╚██╔╝██║██║     ╚════██║    '+colors.bgColors.TITLE_DESCRIPTION_MOTD+'Version : '+colors.bgColors.TEXTE_DESCRIPTION_MOTD+VERSION)
    print(colors.bgColors.PRIMARY+' ██║ ╚═╝ ██║╚██████╗███████║    '+colors.bgColors.TITLE_DESCRIPTION_MOTD+'Updated : '+colors.bgColors.TEXTE_DESCRIPTION_MOTD+DATE)
    print(colors.bgColors.PRIMARY+' ╚═╝     ╚═╝ ╚═════╝╚══════╝'+colors.bgColors.DEFAULT)
    print('\n')