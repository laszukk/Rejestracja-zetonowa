
def parzyste(a_list,b_list):
    c_list=[]
    for i in range(len(a_list)):
        if(i%2==0):
            c_list.append(a_list[i])
        else:
            c_list.append(b_list[i])
    return c_list

print(parzyste([1,1,1],[2,2,2]))

def info(data_text):
    slownik_dane = {
        "Dlugosc ": len(data_text),
        "Znaki w liście ": list(data_text),
        "Wielkie litery ": data_text.upper(),
        "Małe litery ": data_text.lower(),
    }
    return slownik_dane

def usun(text,letter):
    return text.replace(letter, "")

def przelicznikTemp(cel):
    przeliczone= {
        "Celsjusze ": cel,
        "Fahrenheit": (cel*9/5)+32,
        "Kelvin": cel+273.15,
        "Rankine": cel*1.8000+491.67,
    }
    return przeliczone

class Calculator:
    def __init__(self,zmienna1,zmienna2):
        self.zmienna1=zmienna1
        self.zmienna2 = zmienna2
    def menu(self):
        print("Menu")
        print("Dodawanie")
        print("Odejmowanie")
        print("Mnożenie")
        print("Dzielenie")
    def dodawanie(self):
        return self.zmienna1 + self.zmienna2
    def odejmowanie(self):
        return self.zmienna1 - self.zmienna2
    def mnozenie(self):
        return self.zmienna1 * self.zmienna2
    def dzielenie(self):
        if(self.zmienna2!=0):
            return self.zmienna1 / self.zmienna2
        else:
            return "Nie dziel przez zero pajacu"
class ScienceCalculator(Calculator):
    def __init__(self, zmienna1, zmienna2):
        Calculator.__init__(self, zmienna1, zmienna2)
    def potegowanie(self):
        return self.zmienna1 ** self.zmienna2

def odwroc(text):
    return text[::-1]

text="totok"
print(info(text))
print(usun(text,"t"))
cel=0
print(przelicznikTemp(cel))
print(Calculator(2,3).dodawanie())
print(ScienceCalculator(2,2).potegowanie())
print(ScienceCalculator(2,2).odejmowanie())
print(odwroc(text))
