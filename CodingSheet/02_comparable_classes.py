from typing import Self

class Person:
    def __init__(self, name: str, age: int) -> None:
            self.name = name
            self.age = age

    def __repr__(self) -> str:
        return f'{self.name} : {self.age}'

    def __lt__(self, others: Self) -> bool:
        return self.age < others.age

    def __gt__(self, other: Self) -> bool:
        return self.age > other.age

    def __eq__(self,other: Self) -> bool:
        return self.age == other.age
def main() -> None:
    people: list[Person] = [Person('aaa',45)
                             ,Person('bbb',23)
                             ,Person('ccc',62)
                             ,Person('ddd',12)
                             ,Person('eee',8)
                             ]
    # people.sort()
    # print(people)

    print(sorted(people))

    print(people[0] > people[1])
    print(people[0] < people[1])
    print(people[0] == people[1])

if __name__ == '__main__':
    main()