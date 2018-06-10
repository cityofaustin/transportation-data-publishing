'''
Extract data from postgrest database and publish to Socrata, ArcGIS Online, 
or CSV.

By default, destination data is incrementally updated based on a
modified date field defined in the configuration file. Alternatively use
--replace to truncate/replace the entire dataset. CSV output is always handled
with --replace.

#TODO
- handle postgrest pagination
- date fiels from api def
- agol pub
'''
import argparse
from copy import deepcopy
import os
import pdb
import traceback

import arrow

import _setpath
from config.pgrest.knack.config import cfg as CFG
from config.secrets import *
from util import argutil
from util import datautil
from util import emailutil
from util import jobutil
from util import logutil
from util import socratautil


def endpoint():
    return 'http://transportation-data.austintexas.io/traffic_reports?traffic_report_status_date_time=gte.1/1/1900'

def socrata_pub(records, cfg, date_fields=None):
    if cfg.get('location_fields'):            
        lat_field = cfg['location_fields']['lat'].lower()
        lon_field = cfg['location_fields']['lon'].lower()
        location_field = cfg['location_fields']['location_field'].lower()
    else:
        lat_field = None
        lon_field = None
        location_field = None

    return socratautil.Soda(
        auth=SOCRATA_CREDENTIALS,
        records=records,
        resource=cfg['socrata_resource_id'],
        date_fields=date_fields,
        lat_field=lat_field,
        lon_field=lon_field,
        location_field=location_field,
        replace=args.replace)


def main(cfg, auth, job, args):
    
    last_run_date = job.most_recent()

    if not last_run_date or args.replace or job.destination == 'csv':
        # replace dataset by setting the last run date to a long, long time ago
        last_run_date = '1/1/1900'

    records = get_postgrest_records()

    if not records:
        return 0

    date_fields = cfg.get('date_fields') #TODO: extract from API definition!

    if job.destination == 'socrata':
        pub = socrata_pub(records, cfg, date_fields=date_fields)

        
    logger.info('END AT {}'.format( arrow.now() ))
    
    return len(records)


def cli_args():

    parser = argutil.get_parser(
        'pgrest_data_pub.py',
        'Publish PostgREST data to Socrata and ArcGIS Online',
        'dataset',
        'app_name',
        '--destination',
        '--replace'
    )
    
    args = parser.parse_args()
    
    return args


if __name__ == '__main__':
    script_name = os.path.basename(__file__).replace('.py', '')
    logfile = f'{LOG_DIRECTORY}/{script_name}.log'
    
    logger = logutil.timed_rotating_log(logfile)
    logger.info('START AT {}'.format( arrow.now() ))

    args = cli_args()
    logger.info( 'args: {}'.format( str(args) ))

    cfg = CFG[args.dataset]

    try:
        script_id = '{}_{}_{}_{}'.format(
            script_name,
            args.dataset,
            'knack',
            dest)

        job = jobutil.Job(
            name=script_id,
            url=JOB_DB_API_URL,
            source='postgrest',
            destination=dest,
            auth=JOB_DB_API_TOKEN)

        job.start()

        results = main(cfg, KNACK_CREDENTIALS[args.app_name], job, args)

        job.result(
            'success',
            records_processed=results)

    except Exception as e:
        error_text = traceback.format_exc()

        logger.error(error_text)
        
        email_subject = "Knack Data Pub Failure: {}".format(args.dataset)
        
        emailutil.send_email(
            ALERTS_DISTRIBUTION,
            email_subject,
            error_text,
            EMAIL['user'],
            EMAIL['password']
        )
        
        job.result('error', message=str(e))

        continue
        