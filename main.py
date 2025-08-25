import os

def main():
    print("Hello from langchain-helloworld!")
    print(os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
