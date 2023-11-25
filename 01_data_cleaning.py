import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.read_json(sys.argv[1], lines=True, convert_dates=['date'])

    # Filtering: We don't need CHIN & DDP courses, co-op courses, research courses, or graduate level courses. We can filter these out
    # Note: Even though research project courses can be full, we omit the courses as it is too dependent on non-quantifiable factors (eg: research topic, professor, etc.)
    data = data.loc[data['subject'].apply(lambda x: x == 'CMPT' or x == 'MACM')] # Filtering non-CMPT or MACM courses
    data = data.loc[data['number'].apply(lambda x: int(x[:3])<500)] # Filtering graduate-level courses, note: [:3] is to avoid edge cases such as 105W
    data = data.loc[data['number'].apply(lambda x: int(x[:3]) < 426 or int(x[:3]) > 430)] # Filtering co-op courses
    data = data.loc[data['number'].apply(lambda x: int(x[:3]) < 415 or int(x[:3]) > 416)] # Filtering research courses
    data

if __name__ == '__main__':
    main()
