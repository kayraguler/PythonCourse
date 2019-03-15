def linearregression(filename):
    """#  importing the modules"""
    from beautifultable import BeautifulTable
    import pandas as pd
    import numpy as np
    """# reading the csv, dropping the missing values and retaining the label names"""
    data = pd.read_csv(filename)
    data = data.dropna()
    labels = list(data.columns.values)
    Labels = ['Constant']
    Labels = Labels + labels
    Labels = Labels[:len(Labels)-1]
    """# converting the data frame to necessary matrices"""
    data = data.values
    X = data[:, :data.shape[1]-1]
    X0 = np.ones((X.shape[0], 1))
    X = np.hstack((X0, X))
    Y = data[:, data.shape[1]-1:data.shape[1]]
    """# Estimating the Betas"""
    Beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
    """# Estimating y_hat and e"""
    y_hat = X.dot(Beta)
    e = Y - y_hat
    et = e.reshape((1, e.shape[0]))
    """# Estimating the Sigma Squared"""
    sigma_squared = et.dot(e)/(X.shape[0]-X.shape[1])
    sigma_squared = float(sigma_squared)
    """# Estimating the variance and SE"""
    Variance = sigma_squared*np.linalg.inv(X.T.dot(X))
    SE = np.sqrt(np.diag(Variance))
    """# Significance and 95% CIs"""
    Beta = np.hstack(Beta)
    Upper = Beta + 1.96*SE
    Lower = Beta - 1.96*SE
    Significant = []
    for i in range(0, X.shape[1]):
        if Upper[i] > 0 and Lower[i] < 0:
            Significant.append(False)
        else:
            Significant.append(True)
    """# Printing the necessary information """
    table = BeautifulTable()
    table.column_headers = Labels
    table.append_row(Beta)
    table.append_row(SE)
    table.append_row(Upper)
    table.append_row(Lower)
    table.append_row(Significant)
    table.insert_column(0, "Labels", ["Betas", "Standard Errors", "Upper", "Lower", "Significant"])
    print(table)

linearregression("C:/Users/Kayra/PycharmProjects/Linear_Regression/econ.csv")
