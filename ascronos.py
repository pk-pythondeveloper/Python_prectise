import asyncio

async def my_async_function():
    print("Starting asynchronous operation...")
    await asyncio.sleep(2)  # Simulate an I/O-bound operation
    print("Asynchronous operation completed.")
    return "Result"

async def main():
    task = asyncio.create_task(my_async_function())
    print("Doing other work while the async function runs...")
    print("ishar aaya re")
    


    result = await task
    print(f"The result is: {result}")

if __name__ == "__main__":
    print("phele yaha aaya ")
    asyncio.run(main())