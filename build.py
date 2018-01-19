'''
Generate shell scripts, logrotate config and crontab for deployment of 
transportation-data-publishing scripts.
'''
import os
import sys

from config import CONFIG
from config import DOCKER_BASE_CMD
from config import LOGROTATE


def check_version():
    '''
    Check system python version and raise exception if <2.7
    '''
    if sys.version_info[0] < 2:
        raise Exception('Python v2.7+ is required')

    elif sys.version_info[0] == 2 and sys.version_info[1] < 7:
        raise Exception('Python v2.7+ is required')

    return


def shellScript(build_path, path, script, args, image):
    '''
    Build a shell script which will launch python script in Docker container
    '''
    cmd = 'cd {}; python {} {}'.format(
        path,
        script,
        ' '.join(args)
    )

    return DOCKER_BASE_CMD.replace('$BUILD_PATH', build_path).replace('$IMAGE', image).replace('$CMD', cmd)

    
def cron_entry(cron, path):
    '''
    Build a crontab entry
    '''
    return f'{cron} bash {path}'


def list_to_file(list_, filename, write_mode='a+'):
    '''
    Write a list of strings to file
    '''
    with open(filename, write_mode) as fout:
        for l in list_:
            fout.write(l)
            fout.write('\n')
    return


if __name__ == '__main__':
    check_version()

    crontab_filename = 'crontab.sh'
    logrotate_filename = 'tdp.logrotate'

    #  get the absolute path of the repository
    build_path = os.getcwd()

    crons = []
    crons.append('') # ensure newline when appending to crontab

    for script in CONFIG['scripts']:

        #  ignore script if not enabled
        if not script['enabled']:
            continue

        #  use default image if none is specified
        if not script.get('image'):
            script['image'] = CONFIG['default_image']

        #  generate shell script and write to /shell_scripts
        sh = shellScript(
            build_path,
            script['path'],
            script['script'],
            script['args'],
            script['image']
        )
        
        sh_filename = '{}/transportation-data-publishing/shell_scripts/{}.sh'.format(
            build_path,
            script['name']
        )

        list_to_file(
            [sh],
            sh_filename,
            write_mode='w+'
        )

        cron = cron_entry(
            script['cron'],
            sh_filename
        )

        crons.append(cron)

    #  Write cron jobs
    
    #  add empty cron entry to ensure last line of crontab file is empty (as required)
    crons.append('') 

    list_to_file(
        crons, 
        crontab_filename, 
        write_mode='a+'
    )

    #  Write logrotate config
    logrotate = LOGROTATE.replace('$BUILD_PATH', build_path)
    list_to_file(
        [logrotate], 
        logrotate_filename, 
        write_mode='a+'
    )
