from io import StringIO
import pandas as pd
from contextlib import closing



def in_memory_csv(data):
    """Creates an in-memory csv.

    Assumes `data` is a list of dicts
    with native python types."""

    mem_csv = StringIO()
    pd.DataFrame(data).to_csv(mem_csv, index=False)
    mem_csv.seek(0)
    return mem_csv

mem_csv = in_memory_csv(things)
with closing(mem_csv) as csv_io:
    Thing.objects.from_csv(csv_io)