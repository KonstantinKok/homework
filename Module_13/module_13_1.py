import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    t1 = 1 / power
    for i in range(5):
        await asyncio.sleep(t1)
        print(f'Силач {name} поднял {i + 1} шар.')
    print(f'Силач {name} закончил соревнования.', name)


async def start_tournament():
    task1 = asyncio.create_task(start_strongman(name='Pasha', power=3))
    task2 = asyncio.create_task(start_strongman(name='Denis', power=2))
    task3 = asyncio.create_task(start_strongman(name='Apollon', power=1))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())