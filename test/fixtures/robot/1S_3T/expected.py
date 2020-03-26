[
    # discovery_suite_level 0
    {
        'inventory_suites': ['1S 3T'],
        'check_suites' : {
            '1S 3T': {
                # checkgroup_parameters file
                None: {
                    'svc_status': 0,
                    'svc_output': ".*'1S 3T': PASS",
                },
                # Check that Keyword MySleepSleep gets not recursed
                'MySleepSleep_0': {
                    'svc_status': 0,
                    'svc_output': ".*\[T\] 'Test4 - 3 Nested Sleeps': PASS.*?\[K\] 'MySleepSleep': PASS \(\d+\.\d+s\)$"
                },
                # Check that Keyword MySleepSleep gets recursed only 1 level deep 
                'MySleepSleep_1': {
                    'svc_status': 0,
                    'svc_output': ".*\[T\] 'Test4 - 3 Nested Sleeps': PASS.*?\[K\] 'MySleepSleep': PASS \(\d+\.\d+s\).*?\[K\] 'MySleep': PASS \(\d+\.\d+s\)$"
                },
            }
        },
    },
]