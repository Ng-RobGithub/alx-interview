#!/usr/bin/python3
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num, prime in enumerate(is_prime) if prime]

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_set = set(primes)
    
    def play_game(n):
        primes = [p for p in range(2, n + 1) if p in prime_set]
        turn = 'Maria'
        while primes:
            current_prime = primes.pop(0)
            primes = [p for p in primes if p % current_prime != 0]
            turn = 'Ben' if turn == 'Maria' else 'Maria'
        return 'Ben' if turn == 'Maria' else 'Maria'
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

if __name__ == "__main__":
    # Example usage
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
