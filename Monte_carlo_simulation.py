import numpy as np
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
%load_ext autoreload
%autoreload 2
%matplotlib inline
##          Optimistic  Neutral  Pessimistic
##  mu      0.227       0.209    0.174
##  sigma   0.115       0.128    0.153

def gbm(n_years = 1, n_scenarios=100, mu=0.209, sigma=0.128, steps_per_year=12, s_0=1):
    ##neutral scenarios
    dt = 1/steps_per_year
    n_steps = int(n_years*steps_per_year) + 1
    rets_plus_1 = np.random.normal(loc=(1+mu)**dt, scale=(sigma*np.sqrt(dt)), size=(n_steps, n_scenarios))
    rets_plus_1[0] = 1
    prices = s_0*pd.DataFrame(rets_plus_1).cumprod()
    return prices

def show_gbm(n_scenarios, mu, sigma):
    s_0=1
    prices = gbm(n_scenarios=n_scenarios, mu=mu, sigma=sigma, s_0=s_0)
    ax = prices.plot(legend=False, alpha =0.8, linewidth=2, figsize=(12,5))
    ax.axhline(y=s_0, ls=":", color="red")
    ax.axhline(y=1.5, ls=":", color="red")
    ax.set_ylim(top=1.7)
    ax.plot(0,s_0, marker="o",color="darkred", alpha=0.2)
    
##          Optimistic  Neutral  Pessimistic
##  mu      0.227       0.209    0.174
##  sigma   0.115       0.128    0.153

gbm_controls = widgets.interactive(show_gbm, 
                                   n_scenarios=widgets.IntSlider(min=1, max=100, step=1, value=1), 
                                   mu=(0.174,0.227,0.001),
                                   sigma=(0.115,0.153,0.001)
)
display(gbm_controls)
