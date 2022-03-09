"""Rename files."""

import os
import datetime
import yaml
import sys
import colors

def renames(nameScript, configFile, iconFile, logsfile):
    """Rename files in a directory."""

    print("Enter the path to the directory where the script will act :")
    root = input()
    print('\n')

    with open(root+configFile, 'r') as file:
        try:
            data = yaml.load(file, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)

    date = datetime.datetime.now()
    dataConfig = data['config']
    separator = dataConfig['separator']
    indicationEpisode = dataConfig['indicationEpisode']
    indicationSeason = dataConfig['indicationSeason']
    formatEpisodes = dataConfig['formatEpisodes']
    formatSeasons = dataConfig['formatSeasons']
    modele = dataConfig['modele']
    year = dataConfig['year']
    month = dataConfig['month']
    day = dataConfig['day']
    season = dataConfig['season']
    name = dataConfig['name']
    version = dataConfig['version']
    type = dataConfig['type']
    modele = modele.split(separator)
    blacklist = [configFile, iconFile, logsfile]
    list = os.listdir(root)

    def resolvTemplate(string):
        """Resolve file template."""
        return {
        'SEASON': indicationSeason+season,
        'EPISODE': 'EPISODE',
        'NAME': name,
        'VERSION': version,
        'TYPE': type,
        'YYYY-MM-DD': year+'-'+month+'-'+day,
        'YYYY-DD-MM': year+'-'+day+'-'+month,
        'MM-YYYY-DD': month+'-'+year+'-'+day,
        'DD-YYYY-MM': day+'-'+year+'-'+month,
        'MM-DD-YYYY': month+'-'+day+'-'+year,
        'DD-MM-YYYY': day+'-'+month+'-'+year,
        'YYYY-MM': year+'-'+month,
        'YYYY-DD': year+'-'+day,
        'MM-YYYY': month+'-'+year,
        'DD-YYYY': day+'-'+year,
        'DD-MM': day+'-'+month,
        'MM-DD': month+'-'+day,
        'YYYY': year,
        'MM': month,
        'DD': day
        }[string]

    def resolvFormat(string):
        """Resolve the format of episodes and seasons."""
        return {
        '1': '',
        '2': '0',
        '3': '00',
        '4': '000',
        '5': '0000',
        '6': '00000'
        }[string]

    def resolv():
        """Rename files and generate logs."""
        resultTemplate = ''
        firstSection = 0
        for section in modele:
            if firstSection == 1:
                resultTemplate += separator+resolvTemplate(section)
            else:
                resultTemplate += resolvTemplate(section)
                firstSection = 1
        episode = 0
        if not os.path.isfile(root+logsfile):
            createLogs = open(root+logsfile,'w')
            createLogs.write('###################################################################################')
            createLogs.write('\n# Script: '+nameScript)
            createLogs.write('\n###################################################################################')
            createLogs.close()
        logs = open(root+logsfile, 'a')
        logs.write('\n\n\n###################################################################################')
        logs.write('\n# '+str(date.year)+'/'+str(date.month)+'/'+str(date.day))
        logs.write('\n###################################################################################')
        for element in list:
            if element not in blacklist:
                episode = episode + 1
                if episode < int(formatEpisodes):
                    formatEpisode = resolvFormat(str(len(formatEpisodes)))
                    if len(str(episode)) > 1:
                        formatEpisode = str(resolvFormat(str(len(str(episode)))))
                    newElement = (resultTemplate+os.path.splitext(element)[1]).replace('EPISODE', indicationEpisode+formatEpisode+str(episode))
                else:
                    newElement = (resultTemplate+os.path.splitext(element)[1]).replace('EPISODE', indicationEpisode+str(episode))
                os.rename(root+element, root+newElement)
                print(colors.bgColors.PRIMARY+'['+colors.bgColors.INFORMATION+'*'+colors.bgColors.PRIMARY+'] '+colors.bgColors.DEFAULT+element+' -> '+newElement)
                logs.write('\n[*] '+element+' -> '+newElement)
        logs.close()
    resolv()