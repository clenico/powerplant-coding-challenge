import unittest
from app.controller.load_planner import LoadPlannerBruteforce

class TestLoadPlannerBruteforce(unittest.TestCase):
    def test_permutations_generation(self):
        expected_comb = [(0,1,2,3),
                     (0,1,3,2),
                     (0,2,1,3),
                     (0,2,3,1),
                     (0,3,1,2),
                     (0,3,2,1),
                     (1,0,2,3),
                     (1,0,3,2),
                     (1,2,0,3),
                     (1,2,3,0),
                     (1,3,0,2),
                     (1,3,2,0),
                     (2,0,1,3),
                     (2,0,3,1),
                     (2,1,0,3),
                     (2,1,3,0),
                     (2,3,1,0),
                     (2,3,0,1),
                     (3,0,1,2),
                     (3,0,2,1),
                     (3,1,2,0),
                     (3,1,0,2),
                     (3,2,0,1),
                     (3,2,1,0),
                     ]
        planner = LoadPlannerBruteforce(None)
        generated_perm = planner.gen_all_permutations_index(nb_elements=4)
        self.assertSetEqual(set(list(generated_perm)), set(expected_comb))

    def test_load_planner_example_3(self):
        # TODO Refactoring needed before implementing
        pass