import xlrd

class read_cls():

    def read(self, file_name, sheet_name):

        table =  xlrd.open_workbook(file_name)

        sheet = table.sheet_by_name(sheet_name)

        rows = sheet.nrows
        dict_key = sheet.row_values(0)
        print(len(dict_key))


        list = []
        for i in range(1, rows):
            row = sheet.row_values(i)
            if row:
                data = {}
                for j in range(len(dict_key)):
                    data[dict_key[j]] = row[j]
            list.append(data)
        return list


if __name__ == '__main__':
    table = read_cls()
    list = table.read('test.xlsx','测试1-1')
