class Dog:
    def make_sound(self):
        return f"bark"
class Cat:
    def make_sound(self):
        return f"meow"
def process_sound(sound_object):
    return sound_object.make_sound()
dog = Dog()
cat = Cat()
print(process_sound(dog))
print(process_sound(cat))
