import random

def main():
    print("������ �����")
    value = random.randint(1,6);
    print(f"������ {value}")
    if value == 5 or value == 6:
        print("�� ��������")
    elif value == 3 or value == 4:
        main()
    else:
        print("�� ���������")

if __name__ == '__main__':
    main()