print("===================================")
print(" Algorand Voting DApp Started ")
print("===================================")

def vote(candidate):
    print(f"Vote casted for {candidate}")

def main():
    print("Available Candidates: A, B, C")
    choice = input("Enter your vote: ")
    vote(choice)

if __name__ == "__main__":
    main()
