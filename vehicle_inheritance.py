import unittest
import random

# classes code lifted from class announcement:
# Allen Voelcker
# CIS 245 Introduction to Programming
# Winter 2021/2022, Week 8

class Vehicle:
    '''defines the basic attributes of a vehicle'''
    def __init__(self, make, model, color, fueltype, options):
        self.make = make
        self.model = model
        self.color = color
        self.fueltype = fueltype
        self.options = options

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fueltype

    def getOptions(self):
        return self.options



class Car(Vehicle):
    def __init__(self, make, model, color, fueltype, options, engineSize, numDoors):
        super().__init__(make, model, color, fueltype, options)
        self.engineSize = engineSize
        self.numDoors = numDoors

    def getEngineSize(self):
      return self.engineSize

    def getNumDoors(self):
      return self.numDoors

    def display_info(self):
        result = {  'body_type': 'sedan',
                    'make': self.make, 
                    'model': self.model,
                    'color': self.color,
                    'fuel_type': self.fueltype,
                    'engine_size': self.getEngineSize(), 
                    'number_of_doors': self.getNumDoors(),
                    'options': self.options}
        print(result)


class Truck(Vehicle):
    def __init__(self, make, model, color, fueltype, options, cabStyle, bedLength):
        super().__init__(make, model, color, fueltype, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def getCabStyle(self):
      return self.cabStyle

    def getbedLength(self):
      return self.bedLength
    
    def display_info(self):
        result = {  'body_type': 'pickup',
                    'make': self.make, 
                    'model': self.model,
                    'color': self.color,
                    'fuel_type': self.fueltype,
                    'cab_style': self.getCabStyle(),
                    'bed_length': self.getbedLength(),
                    'options': self.options
                    }
        print(result)


def prompt_vehicle_options():
    options_menu = {
        1: 'power mirrors', 
        2: 'power locks', 
        3: 'remote start', 
        4: 'backup camera', 
        5: 'bluetooth', 
        6: 'cruise control',
        7: 'collision warning',
        8: 'automatic emergency braking'
    }
    options_selected = []
    while len(options_selected) < 8:
        if len(options_selected)==2:
            options_menu[0] = 'exit options menu'
        if len(options_selected) > 0:
            print('you have selected the following options:')
            print(options_selected)
        print('please select from the following options: ')
        print(options_menu)
        selected_option = input('selected_option: ')
        try:
            selected_option = int(selected_option)
        except:
            selected_option = random.choice(list(options_menu.keys()))
            print(f'that didn\'t work so let\'s randomly go with {selected_option}')
            print('(you\'re welcome)')
        if selected_option in options_menu.keys():
            if selected_option == 0:
                print('exiting options menu')
                break
            else:
                options_selected.append(options_menu[selected_option])
                del options_menu[selected_option]
    print('you selected the following options:')
    print(options_selected)
    return(options_selected)


def prompt_vehicle_type():
    print('select one of the following types of vehicles:')
    print('1) car')
    print('2) truck')
    vehicle_selection = input('selection: ')
    if not vehicle_selection.lower() in ('1', '2', 'car', 'truck'):
        vehicle_selection = random.choice(list(['1','2']))
        print(f'That selection makes no sense. Randomly selecting ' + vehicle_selection)
        print('(you\'re welcome)')
    make = input('please specify make: ')
    model = input('please specify model: ')
    color = input('please specify color: ')
    fueltype = input('please specify fueltype: ')
    options = prompt_vehicle_options()
    if vehicle_selection.lower() in ('1', 'car'):
        engineSize = input('please specify engineSize: ')
        numDoors = input('please specify numDoors: ')
        return Car( make = make,
                    model = model,
                    color = color,
                    fueltype = fueltype,
                    options = options,
                    engineSize = engineSize,
                    numDoors = numDoors)
    elif vehicle_selection.lower() in ('2', 'truck'):
        cabStyle = input('please specify cabStyle: ')
        bedLength = input('please specify bedLength: ')
        return Truck(   make = make,
                        model = model,
                        color = color,
                        fueltype = fueltype,
                        options = options,
                        cabStyle = cabStyle,
                        bedLength = bedLength)
    else:
        print(vehicle_selection+' is not an option')
        prompt_vehicle_type()

def prompt_garage_vehicles():
    current_vehicles = []
    vehicle_summary = {'Car': 0, 'Truck': 0, 'total': 0}
    requirements_complete = False
    termination_requested = False
    while requirements_complete is False or termination_requested is False:
        new_vehicle = prompt_vehicle_type()
        current_vehicles.append(new_vehicle)
        vehicle_summary[type(new_vehicle).__name__] += 1
        vehicle_summary['total'] += 1
        print(f'you added a {type(new_vehicle).__name__}!')
        if vehicle_summary['Car'] > 0 and vehicle_summary['Truck'] > 0:
            requirements_complete = True
            print('1) yes')
            print('2) no')
            add_vehicle_input = input('Would you like to add more vehicles? ')
            if add_vehicle_input.lower() in ('1', 'yes'):
                print('let\'s add another!')
            elif add_vehicle_input.lower() in ('2', 'no'):
                termination_requested = True
            else:
                print('let\'s just assume that\'s a yes ;)')
        else:
            if vehicle_summary['Truck'] < 1:
                print('you still need at least 1 truck to complete your garage')
            if vehicle_summary['Car'] < 1:
                print('you still need at least 1 car to complete your garage')
    print('vehicles in your garage:')
    for vehicle in current_vehicles:
        vehicle.display_info()
    return current_vehicles


class testClasses(unittest.TestCase):
    my_vehicle = Vehicle(
        make='Toyota', 
        model='foobar', 
        color='red', 
        fueltype='plutonium', 
        options=['some', 'options'])

    my_car = Car(
        make='Toyota', 
        model='Camry', 
        color='gray', 
        fueltype='hybrid', 
        options=['some', 'options'], 
        engineSize=4, 
        numDoors=4)

    my_truck = Truck(
        make='Toyota', 
        model='Tundra', 
        color='green', 
        fueltype='gas', 
        options=['foo', 'bar'], 
        cabStyle='box', 
        bedLength='7')

    def test_types(self):
        self.assertEqual(type(testClasses.my_vehicle).__name__, 'Vehicle')
        self.assertEqual(type(testClasses.my_car).__name__, 'Car')
        self.assertEqual(type(testClasses.my_truck).__name__, 'Truck')


    def test_vehicle_attributes(self):
        self.assertEqual(testClasses.my_vehicle.make, 'Toyota')
        self.assertEqual(testClasses.my_vehicle.model, 'foobar')
        self.assertEqual(testClasses.my_vehicle.color, 'red')
        self.assertEqual(testClasses.my_vehicle.fueltype, 'plutonium')
        self.assertEqual(len(testClasses.my_vehicle.options), 2)


    def test_vehicle_methods(self):
        self.assertEqual(testClasses.my_vehicle.getMake(), 'Toyota')
        self.assertEqual(testClasses.my_vehicle.getModel(), 'foobar')
        self.assertEqual(testClasses.my_vehicle.getColor(), 'red')
        self.assertEqual(testClasses.my_vehicle.getFuelType(), 'plutonium')
        self.assertEqual(len(testClasses.my_vehicle.getOptions()), 2)


    def test_inheritance_attributes(self):
        self.assertTrue(hasattr(testClasses.my_car, 'make'))
        self.assertTrue(hasattr(testClasses.my_truck, 'make'))
        self.assertTrue(hasattr(testClasses.my_car, 'model'))
        self.assertTrue(hasattr(testClasses.my_truck, 'model'))
        self.assertTrue(hasattr(testClasses.my_car, 'color'))
        self.assertTrue(hasattr(testClasses.my_truck, 'color'))
        self.assertTrue(hasattr(testClasses.my_car, 'fueltype'))
        self.assertTrue(hasattr(testClasses.my_truck, 'fueltype'))
        self.assertTrue(hasattr(testClasses.my_car, 'options'))
        self.assertTrue(hasattr(testClasses.my_truck, 'options'))


    def test_inheritance_methods(self):
        self.assertTrue(callable(getattr(testClasses.my_car, 'getMake')))
        self.assertTrue(callable(getattr(testClasses.my_truck, 'getMake')))
        self.assertTrue(callable(getattr(testClasses.my_car, 'getModel')))
        self.assertTrue(callable(getattr(testClasses.my_truck, 'getModel')))
        self.assertTrue(callable(getattr(testClasses.my_car, 'getColor')))
        self.assertTrue(callable(getattr(testClasses.my_truck, 'getColor')))
        self.assertTrue(callable(getattr(testClasses.my_car, 'getFuelType')))
        self.assertTrue(callable(getattr(testClasses.my_truck, 'getFuelType')))
        self.assertTrue(callable(getattr(testClasses.my_car, 'getOptions')))
        self.assertTrue(callable(getattr(testClasses.my_truck, 'getOptions')))


    def test_truck_attributes(self):
        # Truck should have its own attributes and methods
        self.assertTrue(hasattr(testClasses.my_truck, 'cabStyle'))
        self.assertTrue(hasattr(testClasses.my_truck, 'bedLength'))


    def test_truck_methods(self):
        self.assertTrue(callable(getattr(testClasses.my_truck, 'getCabStyle')))
        self.assertTrue(callable(getattr(testClasses.my_truck, 'getbedLength')))


    def test_car_attributes(self):
        self.assertTrue(hasattr(testClasses.my_car, 'engineSize'))
        self.assertTrue(hasattr(testClasses.my_car, 'numDoors'))


    def test_car_methods(self):
        self.assertTrue(hasattr(testClasses.my_car, 'getEngineSize'))
        self.assertTrue(hasattr(testClasses.my_car, 'getNumDoors'))

prompt_garage_vehicles()

if __name__ == '__main__':
    unittest.main()
else:
    unittest.main(module='Vehicle_inheritance', exit=False)

