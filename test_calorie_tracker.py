import unittest
from calorie_tracker import CalorieTracker

class TestCalorieTracker(unittest.TestCase):
    
    def test_calorie_tracking_functionality(self):
        """Test basic calorie tracking functionality."""
        tracker = CalorieTracker()
        test_date = "2024-01-01"
        
        # Add some meals
        tracker.add_meal("Breakfast", 350, test_date)
        tracker.add_meal("Lunch", 600, test_date)
        tracker.add_meal("Dinner", 800, test_date)
        
        # Test calculations
        self.assertEqual(tracker.get_daily_calories(test_date), 1750)
        self.assertEqual(tracker.get_remaining_calories(test_date), 250)
        
        summary = tracker.get_daily_summary(test_date)
        self.assertEqual(summary["consumed"], 1750)
        self.assertEqual(summary["remaining"], 250)
        self.assertEqual(summary["goal"], 2000)

if __name__ == "__main__":
    unittest.main()
