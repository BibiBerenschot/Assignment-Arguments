# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1
def greet(name, greeting='Hello, <name>!'):
    personalized_greeting = greeting.replace('<name>', name)
    return personalized_greeting

#Part 2
def force(mass, body='earth'):
    gravity_on_body = {
        'earth':9.798,
        'sun':274,
        'jupiter':24.92,
        'neptune':11.15,
        'saturn':10.44,
        'uranus':8.87,
        'venus':8.87,
        'mars':3.71,
        'mercury':3.7,
        'moon':1.62,
        'pluto':0.58
    }
    total_force = mass * round(gravity_on_body[body.lower()], 1)
    return total_force

#Part 3
def pull(m1, m2, d):
    total_pull = 6.674*(10**-11)*((m1*m2)/(d**2))
    return total_pull


    