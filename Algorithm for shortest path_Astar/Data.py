# Reads france longitude file and stores node longitude values in a dictionary

# Path of the file

# Returns:   Returns dictionary with path longitude values of each node

def read_france_map_longitude(file_path):
    france_long = {}
    with open(file_path, 'r') as f:
        for i in range(18):
            f.readline()
        for line in f.readlines():
            key = line.strip().split(' ')
            if len(key) > 1:
                france_long[key[0]] = key[1]
            else:
                pass
    return france_long

# Reads france road map and stores node path  cost values in a nested dictionary

# Path of the file

# Returns:   Returns nested dictionary with path cost details


def read_france_map(file_path):
    roadmap_france = {}
    with open(file_path, 'r') as f:
        Lines = f.readlines()
        line_num = 0
        is_next_line_a_key = False
        current_key = None
        current_dict = {}
        for line in Lines:
            if line_num <= 2:
                pass
            else:
                if line == '\n':
                    is_next_line_a_key = True
                elif is_next_line_a_key:
                    if current_key is not None:
                        roadmap_france[current_key] = current_dict
                    key = line.split(':')
                    current_key = key[0].capitalize()
                    current_dict = {}
                    is_next_line_a_key = False
                else:
                    item = line.split()
                    current_dict[item[0]] = item[1]
            line_num = line_num + 1
        roadmap_france[current_key] = current_dict
    return roadmap_france

# class creation for Data
class Data:
    roadmap_france = {}
    france_long = {}

    # Method to call read_france_map method
    def get_roadmap_france(self):
        if not self.roadmap_france:
            self.roadmap_france = read_france_map(
                "/home/turing/t90rkf1/d656/dhw/hw2-astar/france-roads1.txt")
        return self.roadmap_france

    # Method to call read_france_map_longitude
    def get_roadmap_france_long(self):
        if not self.france_long:
            self.france_long = read_france_map_longitude("/home/turing/t90rkf1/d656/dhw/hw2-astar/france-long1.txt")
        return self.france_long

    # Method to calculate h value of a node
    def get_h_value(self,snode,gnode):
        h = 8 * (abs(int(self.get_roadmap_france_long().get(snode)) - int(self.get_roadmap_france_long().get(gnode))))
        return h

