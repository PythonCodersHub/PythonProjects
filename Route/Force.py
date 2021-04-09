'''
People often joke around to chuck your mobile to test the gravity acting on the mobile,
and it sounds absurd to some people let's check out why some people think in the other dimension
'''


def potential_energy(mass,height):
    gravity  = 9.80665
    return f"Potential energy acting on the particle is {mass*gravity*height} J"

def kinetic_energy(mass,velocity):
    return f"Kinetic energy acting on the particle is {0.5*mass*(velocity**2)} J"