import unittest
from fairness import return_fairness_metric
from equal_opportunity import Equal_Opportunity
from equalized_odds import Equalized_Odds
from disparate_impact import Disparate_Impact
from prevalence import Prevalence
from unbalanced_dataset import Unbalanced_Dataset

class FairnessTest(unittest.TestCase):

    def test_return_fairness_metric(self):
        self.assertEqual(Equal_Opportunity, return_fairness_metric('equal_opportunity'))
        self.assertEqual(Equalized_Odds, return_fairness_metric('equalized_odds'))
        self.assertEqual(Disparate_Impact, return_fairness_metric('disparate_impact'))
        self.assertEqual(Prevalence, return_fairness_metric('prevalence'))
        self.assertEqual(Unbalanced_Dataset, return_fairness_metric('unbalanced_dataset'))


if __name__ == '__main__':
    unittest.main()
