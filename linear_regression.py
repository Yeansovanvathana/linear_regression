import pandas as pd

Covid19_inCambodia = {'Year': [2020, 2020, 2021, 2021],
                'Month': [10, 11, 1, 2],
                'NewCase': [37, 26, 23, 147],
                'Quarantine': [200, 100, 357, 2000],
                'DeathCase': [0, 0, 0, 0]
                }

data = pd.DataFrame(Covid19_inCambodia, columns=['Year', 'Month', 'NewCase', 'Quarantine', 'DeathCase'])

print(data)

import pandas as pd
import matplotlib.pyplot as plt

Covid19_inCambodia = {'Year': [2020, 2020, 2021, 2021],
                'Month': [10, 11, 1, 2],
                'NewCase': [37, 26, 23, 147],
                'Quarantine': [200, 100, 357, 2000],
                'DeathCase': [0, 0, 0, 0]
                }

data = pd.DataFrame(Covid19_inCambodia, columns=['Year', 'Month', 'NewCase', 'Quarantine', 'DeathCase'])

data.plot(kind='scatter', x='NewCase', y='Quarantine', fontsize=12)
plt.grid(True)
plt.show()

