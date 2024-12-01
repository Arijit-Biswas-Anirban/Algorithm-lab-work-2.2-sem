#Lab_08_tower_of_hanoi
def tower_of_hanoi(disks, source, help, destination):
    if disks == 1:
        print(f'Move {disks} from {source} to {destination}')
        return
    tower_of_hanoi(disks - 1, source, destination,help)
    print(f'Move {disks} from {source} to {destination}')
    tower_of_hanoi(disks - 1, help, source, destination)

def main():
    disks = int(input('Enter number of disks: '))
    tower_of_hanoi(disks, 'source', 'help', 'destination')

if __name__ == '__main__':
    main()
