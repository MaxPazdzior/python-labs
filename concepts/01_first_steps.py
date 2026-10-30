# ==============================================================================

# Einfach Zuweisungen und Operationen:

a = 1                       # a ist eine Variable die Zahl ist der Wert
b = 2
c = a + b
print(c)                    # print = Ausgabe in der Konsole
c = c -1 
print(c)
c = c * 3                   # * = Multiplikation in Python 
print(c)
c =  c / 2                  # / = Division in Python
print(c)                    # Ergebnis ist jetzt 3.0 <-- Das ist nun eine Float. Nach dem Dividieren kommt IMMER eine Float

# print(type(c))              # type benutzen um die Klassen des codes zu bestimmen
# print(type(a))
# print(type(b))              # int = Ganze Zahl / # float = Kommazahl

# c = 1
# print(type(c))
# print(c)

# Basis-Datentypen (Primitiven)
a = 3                         # Integer = Ganze Zahl
b = 3.0                       # Float = Gemischte Zahl
c = False                     # Bool = True oder False
d = "Text"                    # String = Ein Text

# print(a,b,c,d)
# print(type(a), type(b), type(c), type(d))

print(a+b)                  # Das funktioniert, am Ende wird es als Float weiter gehen
# print(a+d)                  # Das funktioniert nicht weil es ein int und ein strg ist. (TypeError: unsupported operand type(s) for +: 'int' and 'str')

n1 = "5"                    # Hier wird die Zahl als String also Text gespeichert nicht als Zahl
n2 = "3"
print(n1+n2)                # Das ist eine Konkatenation von Strings

t1 = "Hello"
t2 = "World"
print(t1,t2)                # Mit Komma wird ein Leerzeichen in der Konsole ausgegeben
print(t1+t2)                # Mit + wird beides zusammen geschrieben in der Konsole

print (t1*5)                # Das funktioniert da es so nun 5x ausgegeben wird

# ==============================================================================