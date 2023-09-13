from tecton import on_demand_feature_view, RequestSource
from tecton.types import Field, Int64, String

request_schema = [Field("TEXT", String)]
similarity_request = RequestSource(schema=request_schema)
output_schema = [Field('similarity', Int64), Field('partial_similarity', Int64)]

@on_demand_feature_view(
    sources=[similarity_request],
    mode='python',
    schema=output_schema,
    environments=['tecton-python-snowpark:0.1'],
    owner='pooja@tecton.ai',
    tags={'release': 'production'},
)
def fuzzy_similarity(request):
    from fuzzywuzzy import fuzz
    baseline = "Golden Gate Bridge"
    result = {'similarity': fuzz.ratio(baseline, request["TEXT"]), 'partial_similarity': fuzz.partial_ratio(baseline, request["TEXT"])}
    return result
