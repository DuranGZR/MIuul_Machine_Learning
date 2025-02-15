###############################################
## GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ ##
###############################################

# 1. Genel resim
# 2. Kategorik değişken analizi
# 3. Sayısal değişken analizi
# 4. Hedef değişken analizi
# 5. Korelasyon analizi

########################

# 1. Genel Resim #

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from astropy.utils.masked.function_helpers import quantile

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")

df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()


def check_df(dataframe,head=5):
    print("########## Shape ##########")
    print(dataframe.shape)
    print("########## Types ##########")
    print(dataframe.dtypes)
    print("########## Head ##########")
    print(dataframe.head(head))
    print("########## Tail ##########")
    print(dataframe.tail(head))
    print("########## NA ##########")
    print(dataframe.isnull().sum())
    print("########## Quantiles ##########")
    print(dataframe.describe([0,0.05,0.50,0.95,0.99,1]).T)


check_df(df)

df1 = sns.load_dataset("tips")
check_df(df1)

############################################################
# Kategorik değişken analizi #
############################################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts()
df["sex"].unique()
df["sex"].nunique()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols]

df[cat_cols].nunique()

[col for col in df.columns  if col not in cat_cols]



df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)

def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name : df[col_name].value_counts(),
                        "Ratio": 100 * df[col_name].value_counts() / len(dataframe) }))
    print("#########################################################")

cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df,col)


def cat_summary(dataframe,col_name , plot = False):
    print(pd.DataFrame({col_name : df[col_name].value_counts(),
                        "Ratio": 100 * df[col_name].value_counts() / len(dataframe) }))
    print("#########################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data = dataframe)
        plt.show(block=True)

cat_summary(df,"sex",plot = True)

for col in cat_cols:
    cat_summary(df,col,plot = True)

###########################################################
# Sayısal değişken analizi #
##########################################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]

num_cols = [col for col in num_cols if col not in cat_cols]

def num_summary(dataframe,numerical_col):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df,"age")

for col in num_cols:
    num_summary(df,col)

def num_summary(dataframe,numerical_col,plot = False):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(df,"age",plot = True)

for col in num_cols:
    num_summary(df, col, plot=True)


############################################################
# Değişkenlerin Yakalanması ve İşlemlerin Genelleştrilmesi #
############################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info()

def grab_col_names(dataframe,cat_th=10,car_th=30):
    """

    :param dataframe:
    :param cat_th:
    :param car_th:
    :return:
    """






