from argparse import ArgumentParser

from data_loader import JSONLoader
from data_processing import DataAggregation
from data_saver import JSONSaver, XMLSaver

FORMATS = {'json': JSONSaver(), 'xml': XMLSaver()}


def parsing():
    parser = ArgumentParser(description='Aggregate rooms and students')
    parser.add_argument('students_file', type=str, help='Student file')
    parser.add_argument('rooms_file', type=str, help='Rooms file')
    parser.add_argument('out_format', type=str, help='Choice (json/xml).')
    args = parser.parse_args()
    return args


def main():
    args = parsing()

    loader_file_1 = JSONLoader()
    loader_file_2 = JSONLoader()

    in_format = args.out_format.lower()
    out_file = 'result.' + in_format

    students = loader_file_2.load(args.students_file)
    rooms = loader_file_1.load(args.rooms_file)
    output_file = DataAggregation.aggregate(students, rooms)

    return FORMATS[in_format].save(output_file, out_file)


if __name__ == '__main__':
    main()
