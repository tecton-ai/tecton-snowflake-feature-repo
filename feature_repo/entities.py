from tecton import Entity


user = Entity(
    name='fraud_user',
    join_keys=['USER_ID'],
    description='A user of the platform',
    owner='matt@tecton.ai',
    tags={'release': 'production'}
)

merchant = Entity(
    name='merchant',
    join_keys=['MERCHANT'],
    description='A  merchant',
    owner='david@tecton.ai',
    tags={'release': 'production'}
)


category = Entity(
    name='category',
    join_keys=['CATEGORY'],
    description='A purchase category',
    owner='david@tecton.ai',
    tags={'release': 'production'}
)
