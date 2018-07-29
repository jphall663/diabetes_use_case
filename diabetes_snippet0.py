"""
train['num_lab_procedures'] = train['num_lab_procedures'] + ((2*np.random.rand(train.shape[0]))-1)/10000.0
train['num_procedures'] = train['num_procedures'] + ((2*np.random.rand(train.shape[0]))-1)/10000.0
train['num_medications'] = train['num_medications'] + ((2*np.random.rand(train.shape[0]))-1)/10000.0
train['number_outpatient'] = train['number_outpatient'] + ((2*np.random.rand(train.shape[0]))-1)/10000.0
train['number_emergency'] = train['number_emergency'] + ((2*np.random.rand(train.shape[0]))-1)/10000.0
train['number_inpatient'] = train['number_inpatient'] + ((2*np.random.rand(train.shape[0]))-1)/10000.0

test['num_lab_procedures'] = test['num_lab_procedures'] + ((2*np.random.rand(test.shape[0]))-1)/10000.0
test['num_procedures'] = test['num_procedures'] + ((2*np.random.rand(test.shape[0]))-1)/10000.0
test['num_medications'] = test['num_medications'] + ((2*np.random.rand(test.shape[0]))-1)/10000.0
test['number_outpatient'] = test['number_outpatient'] + ((2*np.random.rand(test.shape[0]))-1)/10000.0
test['number_emergency'] = test['number_emergency'] + ((2*np.random.rand(test.shape[0]))-1)/10000.0
test['number_inpatient'] = test['number_inpatient'] + ((2*np.random.rand(test.shape[0]))-1)/10000.0

train.loc[train[y] == 'NO', y] = '0'
train.loc[train[y] != '0', y] = '1'
train[y] = train[y].apply(pd.to_numeric)

test.loc[test[y] == 'NO', y] = '0'
test.loc[test[y] != '0', y] = '1'
test[y] = test[y].apply(pd.to_numeric)

train.to_csv('data/diabetes_train_nbr_random_readmit_0_1.csv', index=False)
test.to_csv('data/diabetes_test_nbr_random_readmit_0_1.csv', index=False)
"""
