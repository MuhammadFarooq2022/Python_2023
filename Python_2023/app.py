import pandas as pd
import seaborn as sns
import pandas_profiling
import streamlit as st

from streamlit_pands_profiling import st_profile_report

df = sns.load_dataset("titanic")
pr = df.profile_report()

st_profile_report(pr)