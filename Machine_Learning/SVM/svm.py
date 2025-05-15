import numpy as np 


class SVM:

    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None


    def fit(self, X, y):
        n_samples, n_features = X.shape
        # convert all y values in -1 and 1
        # for this example iris classes has
        # givel in form of 0 and 1.
        # the line bellow convert those number
        # to -1 for zeros and 1 for ones
        y_ = np.where(y <= 0, -1, 1)
        
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for i, x_i in enumerate(X):
                # chech if y(w*xi)
                if y_[i] * (np.dot(x_i, self.w) - self.b) >= 1:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                # update rool
                # w = w - learning rate * 2 lambda yi-xi
                # b = b - learning rate * yi
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y_[i]))
                    self.b -= self.lr * y_[i]


    def predict(self, X):
        approx = np.dot(X, self.w) - self.b
        # Multiply the approximation with sign function
        # that returns -1 if the approximation is any number
        # lower than 0 and 1 if approximation is any number 
        # up to 0
        return np.sign(approx)
