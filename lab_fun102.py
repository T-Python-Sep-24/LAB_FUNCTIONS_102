def prime_numbers(s,e):
    def prime_hlper(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for n in range(s, e):
         if prime_hlper(n):
              print(n)
prime_numbers(25,50)