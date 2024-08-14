class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls,hall):
        cls.__hall_list.append(hall)

    @classmethod
    def get_show_halls(cls):
        return cls.__hall_list
    


class hall_list(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        super().entry_hall(self)

        self.__seats ={}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no


    def entry_show(self,id,movie_name,time):
        if id in self.__seats:
            print(f"SHOW IS ON")
            return
        
        self.__show_list.append((id,movie_name,time))
        self.__seats[id] = [[0 for _ in range (self._cols)]  for _ in range (self._rows)]


    def book_seats(self,id,seat_list):
        if id in self.__seats:
            for row , col in seat_list:
                if 0<= row <self._rows and  0<=col <self._cols:
                    if self.__seats[id][row-1][col-1] == 0:
                        self.__seats[id][row-1][col-1] = 1

                    else:
                        print("Bokking Completed!!")

                else:
                    print("Id is not Valid !!")

        else:
            print("ID is not valid !!")


    def view_show_list(self):
        if not self.__show_list:
            print(f"Show is not running !!")
            return
        
        print("Current show is running Now :")
        for id,movie_name,time in self.__show_list:
            print(f"Movie Id : {id}, Movie Name : {movie_name}, Show TIme : {time}")


    def view_avilable_seats(self,id):
        if id in self.__seats:
            print(f"Seat is Avialable for show {id}")

            for row in range(self.__rows):
                print(self.__seats[id][row])

        else:
            print(f"Id is Invalid!!")




hall1 = hall_list (3,2,1)
hall1.entry_show (101,"C1","2pm")
hall1.entry_show (102,"C2","5pm")
hall1.entry_show (103,"C3","9pm")
    

while True:
    print("....WElcome Star Cineplex ....")
    print("1. View All List")
    print("2. Add New entry")
    print("3. Seat for booking ")
    print("4. Avialable seat")
    print("5. Exit ")

    choice = int(input("Enter Your option : "))

    if choice == 1:
        hall1.view_show_list()

    elif choice == 2:
        id = int(input("Enter ID : "))
        movie_name = input("Enter Movie Name : ")
        time = input("Enter Show TIme : ")
        hall1.entry_show(id,movie_name,time)

    elif choice == 3:
        id = int(input("Enter ID : "))
        row = int(input("PLease Enter Row : "))
        col = int(input("PLease Enter Column : "))
        hall1.book_seats(id,[(row,col)])
        hall1.view_avilable_seats(id)

    elif choice == 4:
        id = int(input("Enter ID : "))
        hall1.view_avilable_seats(id)

    elif choice == 5:
        break

    else:
        print("Your id is Invalid!!")
