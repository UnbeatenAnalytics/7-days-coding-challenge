import string as st

# create class
class PasswordStrengthAnalyzer:

    def check_length(self, password):
        score = 5 if (len(password) < 6) else 10

        return score

    def check_variety(self,password):
        
        l = list(password)
        score = 0

        # check for digits
        for _ in range(0,10):
            if str(_) in l:
                score += 15
                break

        # check for uppercase
        for _ in l:
            if _ in st.ascii_uppercase:
                score += 15
                break

        # check for lowercase
        for _ in l:
            if _ in st.ascii_lowercase:
                score += 15
                break

        # check for punctuation
        for _ in l:
            if _ in st.punctuation:
                score += 15
                break

        return score
    
    def check_penalty(self, password):
        return 0
        
    def calculate_score(self, password):
        length_score = self.check_length(password)
        variety_score = self.check_variety(password)
        penalty_score = self.check_penalty(password)

        return length_score + variety_score + penalty_score
    
        
if __name__ == "__main__":
    password = input('Enter Password:')  
    obj = PasswordStrengthAnalyzer()  
    score = obj.calculate_score(password)

    print(score)


