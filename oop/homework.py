class Cat:

    saturation_level = 50
    average_speed = 0

    def __init__(self, age):
        self.age = age
        self._set_average_speed()

    def eat(self, product):
        """
        Increase saturation level depending on food eaten
        :param product:
        :return:
        """
        prod_variants = {"fodder": 10, "apple": 5, "milk": 2}
        if product in prod_variants.keys():
            self._increase_saturation_level(prod_variants[product])

    def _reduce_saturation_level(self, value):
        """
        Reducing saturation level
        :param value:
        :return:
        """
        self.saturation_level = self.saturation_level - value if self.saturation_level - value >= 0 else 0

    def _increase_saturation_level(self, value):
        """
        Increasing saturation level
        :param value:
        :return:
        """
        self.saturation_level = self.saturation_level + value if self.saturation_level + value <= 100 else 100

    def _set_average_speed(self):
        """
        Setting average speed depending on cat's age
        :return:
        """
        if self.age <= 7:
            self.average_speed = 12
        elif self.age in range(8, 11):
            self.average_speed = 9
        elif self.age > 10:
            self.average_speed = 6

    def run(self, hours):
        """
        Count distance ran by cat and reduce saturation level depending on that number
        :param hours:
        :return: string with distance
        """
        distance = self.average_speed * hours
        if distance <= 25:
            self._reduce_saturation_level(2)
        elif distance in range(26, 51):
            self._reduce_saturation_level(5)
        elif distance in range(51, 101):
            self._reduce_saturation_level(15)
        elif distance in range(101, 201):
            self._reduce_saturation_level(25)
        elif distance > 200:
            self._reduce_saturation_level(50)
        return f"Your cat ran {distance} kilometers"

    def get_saturation_level(self):
        """
        Get saturation level value
        :return:
        """
        return self.saturation_level if self.saturation_level > 0 else "Your cat is dead :("

    def get_average_speed(self):
        """
        Get average speed
        :return:
        """
        return self.average_speed


class Cheetah(Cat):

    def eat(self, product):
        """
        Increase saturation level depending on food eaten
        :param product:
        :return:
        """
        prod_variants = {"gazelle": 30, "rabbit": 15}
        if product in prod_variants.keys():
            self._increase_saturation_level(prod_variants[product])

    def _set_average_speed(self):
        """
        Setting average speed depending on cat's age
        :return:
        """
        if self.age <= 5:
            self.average_speed = 90
        elif self.age in range(6, 16):
            self.average_speed = 75
        elif self.age > 15:
            self.average_speed = 40


class Wall:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        """
        Get wall square value
        :return:
        """
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        """
        Get the number of wallpaper rolls for this wall
        :param roll_width_m:
        :param roll_length_m:
        :return:
        """
        lines_roll = roll_length_m // self.height
        lines_wall = self.width // roll_width_m
        return lines_wall / lines_roll


class Roof:

    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        """
        Calculate the roof square value
        :return:
        """
        if self.roof_type == "gable":
            return self.width * self.height * 2
        elif self.roof_type == "single-pitch":
            return self.width * self.height
        else:
            raise ValueError("Sorry there is only two types of roofs")


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        """
        Calculate window square value
        :return:
        """
        return self.width * self.height


class Door:

    wood_price = 10
    metal_price = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def door_square(self):
        """
        Calculate door square value
        :return:
        """
        return self.width * self.height

    def door_price(self, material):
        """
        Calculate the door price
        :param material:
        :return:
        """
        if material == "wood":
            return self.door_square() * self.wood_price
        elif material == "metal":
            return self.door_square() * self.metal_price
        else:
            raise ValueError("Sorry we don't have such material")

    def update_wood_price(self, new):
        """
        Update your wood price
        :param new:
        :return:
        """
        self.wood_price = new

    def update_metal_price(self, new):
        """
        Update your metal price
        :param new:
        :return:
        """
        self.metal_price = new


class House:

    __walls = []
    __windows = []
    __roof = None
    __door = None

    def __init__(self):
        pass

    def create_wall(self, width, height):
        """
        Create new wall and add it to the house if we have less then 4 walls
        :param width:
        :param height:
        :return:
        """

        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            if len(self.__walls) == 4:
                raise ValueError("Our house can not have more than 4 walls")
            self.__walls.append(Wall(width, height))

    def create_roof(self, width, height, roof_type):
        """
        Create new roof and add it to the house if we don't have one
        :param width:
        :param height:
        :param roof_type:
        :return:
        """
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            if self.__roof:
                raise ValueError("The house can not have two roofs")
            self.__roof = Roof(width, height, roof_type)

    def create_window(self, width, height):
        """
        Add new window to the house
        :param width:
        :param height:
        :return:
        """
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            self.__windows.append(Window(width, height))

    def create_door(self, width, height):
        """
        Add a door to the house
        :return:
        """
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            if self.__door:
                raise ValueError("The house can not have two doors")
            self.__door = Door(width, height)

    def get_count_of_walls(self):
        """Get number of walls in the house"""
        return len(self.__walls)

    def get_count_of_windows(self):
        """Get number of windows in the house"""
        return len(self.__windows)

    def get_door_price(self, material):
        """Get price for the door"""
        return self.__door.door_price(material)

    def update_wood_price(self, new):
        """Update wood price"""
        self.__door.wood_price = new

    def update_metal_price(self, new):
        """Update metal price"""
        self.__door.metal_price = new

    def get_roof_square(self):
        """Get roof square value"""
        return self.__roof.roof_square()

    def get_walls_square(self):
        """Get the sum of squares of all walls"""
        return sum([wall.wall_square() for wall in self.__walls])

    def get_windows_square(self):
        """Get the sum of squares of all windows"""
        return sum([window.window_square() for window in self.__windows])

    def get_door_square(self):
        """Get door square value"""
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        """Get the sum of the number of rolls of wallpapers needed for all our walls """
        if roll_width_m == 0 or roll_length_m ==0:
            raise ValueError("Sorry length must be not 0")
        else:
            return sum([wall.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m) for wall in self.__walls])

    def get_room_square(self):
        """Get the square of our rooms walls without windows and door"""
        return self.get_walls_square() - (self.get_door_square() + self.get_windows_square())
