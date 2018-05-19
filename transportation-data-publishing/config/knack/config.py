cfg = {
    'atd_visitor_log' : {
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_48',
        'obj' : None,
        'primary_key' : 'id',
        'scene' : 'scene_20',
        'view' : 'view_55',
        'ref_obj' : ['object_1'],
        'socrata_resource_id' : 'tkk5-uugs',
    },
    'cabinets' : {
        'primary_key' : 'CABINET_ID',
        'ref_obj' : ['object_118', 'object_12'],
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_1793',
        'obj' : None,
        'scene' : 'scene_571',
        'view' : 'view_1567',
        'service_url' : 'http://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/cabinet_assets/FeatureServer/0/',
        'service_id' : 'c3fd3bb177cc4291880bbe8c630ed5c4',
        'include_ids' : True,
        'socrata_resource_id' : 'x23u-shve',
        'ip_field' : None,
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }   
    },
    'cameras' : {
        'include_ids' : True,
        'ip_field' : 'CAMERA_IP',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'location_field' : 'location',
            'lon' : 'LOCATION_longitude',
        },
        'modified_date_field': 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_714',
        'obj' : None,
        'primary_key' : 'CAMERA_ID',
        'ref_obj' : ['object_53', 'object_11'],
        'scene' : 'scene_144',
        'service_url' : 'http://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/TRANSPORTATION_traffic_cameras/FeatureServer/0/',
        'service_id' : '52f2b5e51b9a4b5e918b0be5646f27b2',
        'socrata_resource_id' : 'b4k4-adkb',
        'status_field' : 'CAMERA_STATUS',
        'status_filter_comm_status' : ['TURNED_ON'],
        'view' : 'view_395',
    },
    'detectors' : {
        'primary_key' : 'DETECTOR_ID',
        'ref_obj' : ['object_98', 'object_12'],
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_1533',
        'obj' : None,
        'scene' : 'scene_468',
        'view' : 'view_1333',
        'service_url' : 'https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/traffic_detectors/FeatureServer/0/',
        'service_id' : '47d17ff3ce664849a16b9974979cd12e',
        'socrata_resource_id' : 'qpuw-8eeb',
        'include_ids' : True,
        'ip_field' : 'DETECTOR_IP',
        'fetch_locations' : True,
        'location_join_field' : 'SIGNAL_ID',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }
    },
    'dms' : {
        'primary_key' : 'DMS_ID',
        'ref_obj' : ['object_109', 'object_11'],
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_1658',
        'obj' : None,
        'scene' : 'scene_569',
        'view' : 'view_1564',
        'service_url' : 'http://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/dynamic_message_signs/FeatureServer/0/',
        'service_id' : 'e7104494593d4a44a2529e4044ef7d5d',
        'include_ids' : True,
        'socrata_resource_id' : '4r2j-b4rx',
        'ip_field' : 'DMS_IP',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }
    },
    'gridsmart' : {
        #  endpoint for device status check only. 
        #  data publishing is handled via detectors config
        'primary_key' : 'DETECTOR_ID',
        'ref_obj' : ['object_98', 'object_12'],
        'obj' : None,
        'scene' : 'scene_468',
        'view' : 'view_1791',
        'include_ids' : True,
        'ip_field' : 'DETECTOR_IP',
        'status_field' : 'DETECTOR_STATUS',
        'status_filter_comm_status' : ['OK', 'BROKEN', 'UNKNOWN']
    },
    'hazard_flashers' : {
        'primary_key' : 'ATD_FLASHER_ID',
        'ref_obj' : ['object_110', 'object_11'],
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_1701',
        'obj' : None,
        'scene' : 'scene_568',
        'view' : 'view_1563',
        'service_url' : 'http://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/hazard_flashers/FeatureServer/0/',
        'service_id' : '6c4392540b684d598c72e52206d774be',
        'include_ids' : True,
        'socrata_resource_id' : 'wczq-5cer',
        'ip_field' : None,
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }
    },
    'locations' : {  
        'obj' : None,
        'ref_obj' : ['object_11'],
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_508',
        'scene' : 'scene_425',
        'view' : 'view_1201',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }
    },
    'pole_attachments' : {
        'primary_key' : 'POLE_ATTACH_ID',
        'ref_obj' : ['object_120'],
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_1813',
        'obj' : None,
        'scene' : 'scene_589',
        'view' : 'view_1597',
        'service_url' : 'http://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/pole_attachments/FeatureServer/0/',
        'service_id' : '3a5a777f780447db940534b5808d4ba7',
        'include_ids' : True,
        'socrata_resource_id' : 'btg5-ebcy',
        'ip_field' : None,
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }
    },
    'signals' : {
        'include_ids' : True,
        'ip_field' : 'CONTROLLER_IP',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        },
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_205',
        'obj' : None,
        'primary_key' : 'SIGNAL_ID',
        'ref_obj' : ['object_12', 'object_11'],
        'scene' : 'scene_73',
        'service_id' : 'e6eb94d1e7cc45c2ac452af6ae6aa534',
        'socrata_resource_id' : 'p53x-x73x',
        'status_field' : 'SIGNAL_STATUS',
        'status_filter_comm_status' : ['TURNED_ON'],
        'view' : 'view_197',
    },
    'signal_requests' : {
        'primary_key' : 'REQUEST_ID',
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_217',
        'obj' : None,
        'scene' : 'scene_75',
        'view' : 'view_200',
        'ref_obj' : ['object_11', 'object_13'],
        'service_url' : 'http://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/TRANSPORTATION_signal_requests/FeatureServer/0/',
        'service_id' : 'c8577cef82ef4e6a89933a7a216f1ae1',
        'include_ids' : True,
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        },
        'socrata_resource_id': None
    },
    'signal_request_evals' : {
        'socrata_resource_id' : 'f6qu-b7zb',
        'fetch_locations' : True,
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        },
        'location_join_field' : 'ATD_LOCATION_ID',
        'multi_source' : True,
        'sources' : [
            #  knack_data_pub.py supports merging multiple source
            #  datasets to a destination layer
            {
                # traffic signal evals
                'include_ids' : True,
                'modified_date_field' : 'MODIFIED_DATE',
                'modified_date_field_id' : 'field_659',
                'obj' : None,
                'primary_key' : 'ATD_EVAL_ID',
                'ref_obj' : ['object_13', 'object_27'],
                'scene' : 'scene_175',
                'view' : 'view_908',
            },
            {
                #  phb evals
                'include_ids' : True,
                'modified_date_field' : 'MODIFIED_DATE',
                'modified_date_field_id' : 'field_715',
                'obj' : None,
                'primary_key' : 'ATD_EVAL_ID',
                'ref_obj' : ['object_13', 'object_26'],
                'scene' : 'scene_175',
                'view' : 'view_911',
            }
        ]
    },
    'task_orders' : {
        'primary_key' : 'TASK_ORDER',
        'ref_obj' : ['object_86'],
        'obj' : None,
        'scene' : 'scene_861',
        'view' : 'view_2229',
        'include_ids' : True
    },   
    'traffic_reports' : {
        'primary_key' : 'TRAFFIC_REPORT_ID',
        'modified_date_field' : 'TRAFFIC_REPORT_STATUS_DATE_TIME',
        'modified_date_field_id' : 'field_1966',
        'ref_obj' : ['object_121'],
        'obj' : None,
        'scene' : 'scene_614',
        'view' : 'view_1626',
        'service_url' : 'http://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/traffic_reports/FeatureServer/0/',
        'service_id' : 'bd7d8465ce2d4b11b632139594d887fc',
        'include_ids' : True,
        'socrata_resource_id' : 'dx9v-zd7x',
        'ip_field' : None,
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }
    },
    'travel_sensors' : {
        'primary_key' : 'ATD_SENSOR_ID', 
        'ref_obj' : ['object_56', 'object_11'],
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_710',
        'obj' : None,
        'scene' : 'scene_188',
        'view' : 'view_540',
        'include_ids' : True,
        'service_url' : 'https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/travel_sensors/FeatureServer/0/',
        'service_id' : '9776d3e894a74521a7f63443f7becc7c',
        'socrata_resource_id' : '6yd9-yz29',
        'ip_field' : 'SENSOR_IP',
        'status_field' : 'SENSOR_STATUS',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        },
        'status_filter_comm_status' : ['TURNED_ON']
    },
    'signal_retiming' : {
        'primary_key' : 'ATD_RETIMING_ID',
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_1257',
        'ref_obj' : ['object_42', 'object_45'],
        'obj' : None,
        'scene' : 'scene_375',
        'view' : 'view_1063',
        'service_url' : None,
        'socrata_resource_id' : 'g8w2-8uap',
        'include_ids' : False,
    },
    'timed_corridors' : {
        'primary_key' : 'ATD_SYNC_SIGNAL_ID',
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_2557',
        'ref_obj' : ['object_12', 'object_42', 'object_43'],
        'obj' : None,
        'scene' : 'scene_277',
        'view' : 'view_765',
        'service_url' : None,
        'socrata_resource_id' : 'efct-8fs9',
        'include_ids' : False,
        'fetch_locations' : True,
        'location_join_field' : 'SIGNAL_ID',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }    
    },
    'work_orders' : {
        'primary_key' : 'ATD_WORK_ORDER_ID',
        'modified_date_field' : 'MODIFIED_DATE',
        'modified_date_field_id' : 'field_1074',
        'obj' : None,
        'scene' : 'scene_683',
        'view' : 'view_1829',
        'ref_obj' : ['object_31', 'object_11'],
        'socrata_resource_id' : 'hst3-hxcz',
        'status_field' : 'WORK_ORDER_STATUS',
        'location_fields' : {
            'lat' : 'LOCATION_latitude',
            'lon' : 'LOCATION_longitude',
            'location_field' : 'location'
        }
    },
}
