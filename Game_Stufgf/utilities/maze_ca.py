__author__ = 'Greg'
import copy

class Navigator:

    def __init__(self, maze_dimensions, maze, start, style, ship_list):
        self.active = []
        self.new_active = []
        self.active_coordinates = set()
        self.height = maze_dimensions[1]
        self.width = maze_dimensions[0]
        self.active.append((start, 'Flow_Start'))
        self.active_coordinates.add(start)
        self.grid = copy.deepcopy(maze)
        self.maze = maze
        self.style = style
        self.ship_list = ship_list

    def push_block(self, block, string):
        self.new_active.append([block, string])

    def get_grid_value(self, coordinates):
        value = self.grid[coordinates[0]][coordinates[1]]
        if value == "Empty":
            return self.maze[coordinates[0]][coordinates[1]]
        return value

    def refresh(self, coordinates):
        self.new_active.append([coordinates, self.get_grid_value(coordinates)])

    def get_grid_tuple(self, coordinates, relative):
        return (relative[0] + coordinates[0]) % self.width, (relative[1] + coordinates[1]) % self.height

    def update_cells(self):

        for cell in self.active_coordinates:
            kind = self.grid[cell[0]][cell[1]]
            up = self.get_grid_tuple(cell, relative=(1, 0))
            down = self.get_grid_tuple(cell, relative=(-1, 0))
            left = self.get_grid_tuple(cell, relative=(0, -1))
            right = self.get_grid_tuple(cell, relative=(0, 1))

            def check_and_place_flow():
                for a, b in zip([up, down, left, right], ['Flow_Down', 'Flow_Up', 'Flow_Right', 'Flow_Left']):
                    if self.get_grid_value(a) == 'Empty':
                        self.push_block(a, b)

            def check_for_end():
                for a, b in zip([up, down, left, right], ['Path_Down', 'Path_Up', 'Path_Right', 'Path_Left']):
                    if self.get_grid_value(a) == 'End':
                        self.push_block(a, b)
                        self.push_block((cell[0], cell[1]), self.get_grid_value(cell))

            def check_for_path():
                for a, b in zip([up, down, left, right], ['Path_Down', 'Path_Up', 'Path_Right', 'Path_Left']):
                    if self.get_grid_value(a) == b:
                        string = 'Path_' + (self.get_grid_value(cell)[5:])
                        self.push_block((cell[0], cell[1]), string)
                        for o in [up, down, left, right]:
                            self.refresh(o)

            if 'Flow' in kind:
                check_and_place_flow()
                check_for_end()
                check_for_path()

    def update(self):
        self.active_coordinates.clear()

        if len(self.active) == 0:
            self.ship_list.remove(self)
        for block in self.active:
            self.grid[block[0][0]][block[0][1]] = block[1]
            self.active_coordinates.add((block[0][0], block[0][1]))

        self.update_cells()

        self.active = []
        self.active, self.new_active = self.new_active, self.active