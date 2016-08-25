settings = {'BioPolimi': {'ArrhSpecies': 'Total',
                          'FittingKineticParameter_Select': 'None',
                          'Use': False,
                          'mechanism': 'Biomass.xml',
                          'nPoints': 1000},
            'CPD': {'active': True,
                    'dt': 1e-05,
                    'dt_max': 2e-05,
                    'fit': None,
                    'increment': 10,
                    'nmr_parameters': None,
                    'solver': None},
            'Calibration': {'speciesToFit': 'total',
                            'weightRate': 0.0,
                            'weightYield': 100.0},
            'Coal': {
                'HHV': 0.0,
                'proximate_analysis': {
                    'Ash': 4.3, 'FC': 45.1,
                    'Moist': 19.0, 'VM': 50.6},
                'rho_dry': 1310,
                'ultimate_analysis': {
                    'C': 69, 'H': 5, 'N': 0.8, 'O': 24.7,
                    'S': 0.5}},
            'FIT': {'C2SM': {'A1': 0.2,
                             'A1Bounds': [500, 10000.0],
                             'A2': 10000.0,
                             'A2Bounds': [5000, 30000.0],
                             'E1': 1000.0,
                             'E1Bounds': [2000.0, 10000.0],
                             'E2': 10000.0,
                             'E2Bounds': [1500.0, 20000.0],
                             'alpha1': 0.0,
                             'alpha1Bounds': [0.1, 0.4],
                             'alpha2': 0.6,
                             'alpha2Bounds': [0.4, 1]},
                    'DAEM': 'alpha1',
                    'FitMethod': 'evolve',
                    'Model': 'None',
                    'SCR': {'finalYield': 1.0,
                            'finalYieldBounds': [0.0, 1.0],
                            'k': 1.0,
                            'kBounds': [0.0, 1.0],
                            'tstart': 0.0,
                            'tstartBounds': [0.0, 1.0]},
                    'SFOR': {'activationEnergy': 0,
                             'activationEnergyBounds': [100.0, 100000.0],
                             'beta': 0.0,
                             'lowerDevolTemp': 600.0,
                             'preExp': 0.0,
                             'preExpBounds': [0, 10000.0]},
                    'Species': ['ftot']},
            'operating_conditions': {
                'pressure': 1.0,
                'run0': [[0, 500], [0.0016, 1300], [0.01, 1300]],
                'run1': [[0, 500], [0.003, 1300], [0.01, 1300]],
                'run2': [[0, 500], [0.001, 1300], [0.01, 1300]],
                'run3': [[0, 500], [0.1, 1400], [0.5, 2000]],
                'run4': [[0, 500], [0.1, 1400], [0.5, 2000]],
                'runs': 3},
            'Polimi': {'active': True,
                       'backend': 'dopri5',
                       'fit': None,
                       'mechanism': None}}
