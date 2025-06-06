#Make a program that reads a value in meters and shows it converted in centimeters and millimeters

meters = float(input('Type a distance in meters: '))
print('''The measure em meters {:.2f} matches to:
{} Km
{} hm
{} dam
{:.0f} dm
{:.0f} cm
{:.0f} mm'''.format(meters, meters / 1000, meters / 100, meters / 10, meters * 10, meters * 100, meters * 1000))