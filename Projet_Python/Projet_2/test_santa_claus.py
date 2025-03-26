from santa_claus.py import*

dic = {
    'Paris': {
        'Lyon': 394.5056834297657, 
        'Marseille': 661.8616554466852, 
        'Lille': 203.67224282542662
    }, 
    'Lyon': {
        'Paris': 394.5056834297657, 
        'Marseille': 275.87965367431525, 
        'Lille': 558.5472363339595
    }, 
    'Marseille': {
        'Paris': 661.8616554466852, 
        'Lyon': 275.87965367431525, 
        'Lille': 834.0220261600157
    }, 
    'Lille': {
        'Paris': 203.67224282542662, 
        'Lyon': 558.5472363339595, 
        'Marseille': 834.0220261600157
    }
}

# 1°/

def test_dictionary_cities():
    assert dictionary_cities(["Paris", 2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]) == dic
    print("Test de la fonction dictionnary_cities : OK")

test_dictionary_cities()

# 2°/

def test_distance_cities():
    assert isclose(distance_cities('Paris', 'Lyon', dic), 394.5056834297657)
    assert isclose(distance_cities('Marseille', 'Lille', dic), 834.0220261600157)
    assert isclose(distance_cities('Lille', 'Lyon', dic), 558.5472363339595)
    assert isclose(distance_cities('Toulouse', 'Lyon', dic), -1)
    print("Test de la fonction distance_cities : OK")

test_distance_cities()

# 3°/

def test_tour_length():
    assert isclose(tour_length(["Paris", "Lyon", "Marseille", "Lille"], dic), 1708.0796060895232)
    assert isclose(tour_length(["Marseille", "Paris", "Lyon", "Lille"], dic), 2448.936601370426)
    assert isclose(tour_length(["Marseille", "Paris", "Lille", "Lyon"], dic), 1699.9607882803866)
    assert isclose(tour_length(["Marseille", "Lyon", "Paris", "Lille"], dic), 1708.0796060895232)
    print("Test de la fonction tour_length : OK")

test_tour_length()

# 5°/

def test_closest_city():
    assert closest_city("Paris", ["Marseille", "Lyon"], dic) == 1
    assert closest_city("Lille", ["Lyon", "Marseille"], dic) == 0
    assert closest_city("Lyon", ["Lille", "Paris", "Marseille"], dic) == 2
    print("Test de la fonction closest_city : OK")

test_closest_city()

# 6°/

def test_tour_from_closest_city():
    assert tour_from_closest_city("Paris", dic) == ["Paris","Lille","Lyon","Marseille"]
    assert tour_from_closest_city("Marseille", dic) == ["Marseille", "Lyon", "Paris", "Lille"]
    assert tour_from_closest_city("Lyon", dic) == ["Lyon", "Marseille", "Paris", "Lille"]
    print("Test de la fonction tour_from_closest_city : OK")

test_tour_from_closest_city()

# 7°/

def test_best_tour_from_closest_city():
    assert best_tour_from_closest_city(dic) == ["Paris", "Lille", "Lyon", "Marseille"]
    print("Test de la fonction best_tour_from_closest_city : OK")

test_best_tour_from_closest_city()

# 9°/

def test_reverse_part_tour():
    tour1 = ["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    tour2 = ["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    tour3 = ["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    reverse_part_tour(tour1, 2, 5)
    reverse_part_tour(tour2, 1, 6)
    reverse_part_tour(tour3, 3, 5)
    assert tour1 == ["Agen", "Belfort", 'Fréjus', 'Épinay', 'Dijon', 'Cahors', 'Grenoble', 'Hyères']
    assert tour2 == ['Agen', 'Grenoble', 'Fréjus', 'Épinay', 'Dijon', 'Cahors', 'Belfort', 'Hyères']
    assert tour3 == ['Agen', 'Belfort', 'Cahors', 'Fréjus', 'Épinay', 'Dijon', 'Grenoble', 'Hyères']
    print("Test de la fonction reverse_part_tour : OK")

test_reverse_part_tour()

# 10°/

def test_inversion_length_diff():
    assert isclose(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"], dic, 1, 2), -740.8569952808871)
    assert isclose(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"], dic, 2, 3), 8.118817809136544)
    assert isclose(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"], dic, 0, 3), 0.0)
    print("Test de la fonction inversion_length_diff : OK")

test_inversion_length_diff()

# 11°/

def test_better_inversion():
    assert better_inversion(["Marseille", "Paris", "Lyon", "Lille"], dic)
    assert not better_inversion(["Marseille", "Lyon", "Lille", "Paris"], dic)
    print("Test de la fonction better_inversion : OK")

test_better_inversion()

# 12°/

def test_best_obtained_with_inversions():
    assert best_obtained_with_inversions(["Marseille", "Paris", "Lyon", "Lille"], dic) == 1
    assert best_obtained_with_inversions(["Marseille", "Lyon", "Paris", "Lille"], dic) == 1
    assert best_obtained_with_inversions(["Marseille", "Lyon", "Lille", "Paris"], dic) == 0
    print("Test de la fonction best_obtained_with_inversions : OK")

test_best_obtained_with_inversions()