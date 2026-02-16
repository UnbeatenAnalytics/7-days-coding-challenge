# create class

class PasswordStrengthAnalyzer:

    def check_length(self, password):
        score = 5 if (len(password) < 6) else 10
        return score

    def check_variety(self,password):
        return None

if __name__ == "__main__":
    password = input('Enter Password:')  
    obj = PasswordStrengthAnalyzer()  
    score = obj.check_length(password)
    print(score)


