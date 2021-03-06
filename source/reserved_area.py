# -*- coding: utf-8 -*-

from utils.clear import clear
from utils.enter_data import Input
from utils.hex import Hex


class ReservedArea:
    # Class Attributes
    BYTES_SECTOR = '[11:13]'
    SECTOR_CLUSTER = '[13]'
    SECTORS_RESERVED_AREA = '[14:16]'
    QTD_FAT = '[16]'
    QTD_DIRECTORY_ENTRY = '[17:19]'
    SECTORS_BY_FAT = '[22:24]'
    reserved_area_size = Hex("0")
    offset = Hex("0")

    # List of parameters used to set values
    PARAMETERS = ['bytes_sector', 'sector_cluster', 'sectors_reserved_area', 'qtd_fat', 'qtd_directory_entry',
                  'sectors_by_fat']

    def __init__(self, double_check=False):
        self.dump = 0
        self.take_dump(double_check)
        self.bytes_sector = self.sector_cluster = self.sectors_reserved_area = self.qtd_fat = 0
        self.qtd_directory_entry = self.sectors_by_fat = 0
        self.bytes_sector_hex = self.sector_cluster_hex = self.sectors_reserved_area_hex = self.qtd_fat_hex = 0
        self.qtd_directory_entry_hex = self.sectors_by_fat_hex = 0
        self.get_parameters()
        self.set_parameters()
        self.calc_size()

    def take_dump(self, double_check=False, rows=2):
        """
        Use the data in memory to instrospect the attributes of file system.
        The correct data passing is user's responsabilty.
        :param rows: Number of rows to read
        :param double_check: For who want warrancy against mistyping with this flag on you have to type the data
        twice to check if are equal. This do not deny the fact that you can get wrong equal two times.
        """
        self.input_warnings()
        # Input
        stream = Input.enter_data(rows=rows)

        # Double check trigger
        if double_check:
            check = Input.enter_data(rows=2, confirmation=True)
            if check != stream:
                clear()
                input("The data dont match, type all again, please.")
                self.take_dump(double_check=True)
        clear()
        self.dump = stream

    def get_parameters(self):
        """
        Call a function to assign values to the attributes listed in ATTRIBUTES's list
        :return: None
        """
        Input.set_parameters(self)

    def set_parameters(self):
        """
        Call a function to calculate value using hex values
        :return: None
        """
        Input.set_hex_values(self)

    def __repr__(self):
        # TODO: Maybe a global repr function?
        out = f"\n-----------------RESERVED AREA-------------------------------------------"
        out += f"\nBytes per sector: {self.bytes_sector_hex}  \nSectors per cluster: {self.sector_cluster_hex}"
        out += f"\nSectors of Reserved Area: {self.sectors_reserved_area_hex} \nQuantity of FAT's: {self.qtd_fat_hex}"
        out += f"\nQuantity of directory entries: {self.qtd_directory_entry_hex}"
        out += f"\nSectors by FAT: {self.sectors_by_fat_hex} " \
               f"\nSize of Reserved Area in bytes: {self.reserved_area_size}"
        out += f"\n---------------------------------------------------------------------------"
        return out

    def calc_size(self):
        """
        Get the size in bytes of the reserved area. Considering
        Size of Reserved Area = Sectors in reserverd area * Bytes per Sector
        :return: None
        """
        self.reserved_area_size = self.sectors_reserved_area_hex * self.bytes_sector_hex

    # TODO: Method to calc the used clusters by the file

    @staticmethod
    def input_warnings():
        clear()
        # Instructions
        print("Run the DEBUG program in MS-DOS")
        print("Load the floppy data into the RAM memory")
        print("In MS-DOS: L 0 0 0 70")
        print("Dump the Reserved Area's memory region")
        print("In MS-DOS: D 0")
        input("Copy each line just like are in DOS's terminal except for '-' between byte 7 and 8.")
        clear()
        print("Dump the Reserved Area's memory region (2 lines)")


if __name__ == '__main__':
    na = ReservedArea(False)
    # print(na.bytes_sector)
    # print(na.BYTES_SECTOR)
    # print(na.bytes_sector_hex)
    # print(na.qtd_directory_entry_hex)
    # print(na.size)
    print(na)
