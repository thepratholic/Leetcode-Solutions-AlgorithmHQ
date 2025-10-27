# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)   # number of rows (floors) in the bank

        beams = 0       # total number of laser beams

        # iterate through each row (current floor)
        for cur_row in range(m):
            cur_devices = 0  # count of security devices ('1') in current floor
            
            # count number of devices in current row
            for cell in range(len(bank[cur_row])):
                if bank[cur_row][cell] == '1':
                    cur_devices += 1

            # if there are no devices in the current floor, skip to next
            if cur_devices > 0:

                # look for the next row below that also has at least one device
                for next_row in range(cur_row + 1, m):
                    other_floor_devices = 0  # count of devices in next floor

                    # count devices in the next row
                    for cell_ in range(len(bank[next_row])):
                        if bank[next_row][cell_] == '1':
                            other_floor_devices += 1

                    # if a row with devices is found
                    if other_floor_devices > 0:
                        # beams are formed between every pair of devices
                        # from current floor and next floor with devices
                        beams += (cur_devices * other_floor_devices)

                        # break because we only connect to the first row below
                        # that has devices — not all rows
                        break

        # return the total number of laser beams formed
        return beams
