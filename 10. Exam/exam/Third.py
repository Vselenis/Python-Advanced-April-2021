def fill_the_box(*numbers):
    size_of_box = numbers[0] * numbers[1] * numbers[2]
    cubes = list(numbers[3:])
    end = numbers.index("Finish") - 3
    for x in cubes:
        if type(x) == int:

            size_of_box -= x
            get_index = cubes.index(x)
            if size_of_box < 0:
                return f"No more free space! You have {sum(cubes[get_index +1:end]) - size_of_box} more cubes."

            elif size_of_box == 0:
                return f"No more free space! You have {sum(cubes[get_index:end])} more cubes."


        else:
            cubes.remove(x)
            return f"There is free space in the box. You could put {size_of_box} more cubes."










print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))