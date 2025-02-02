import httpx

class NumberService:
    @staticmethod
    async def get_fun_fact(number: int) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://numbersapi.com/{number}/math?json")
        return response.json()['text']
    @staticmethod
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def is_perfect(number: int) -> bool:
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number

    @staticmethod
    def armstrong_number(number: int) -> bool:
        digits = list(map(int, str(number)))
        return sum(d ** len(digits) for d in digits) == number

    @staticmethod
    def digit_sum(number: int) -> int:
        return sum(int(digit) for digit in str(number))

number_service = NumberService()