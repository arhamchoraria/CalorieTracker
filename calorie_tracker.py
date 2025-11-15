from datetime import datetime
from typing import Dict, List, Tuple

class CalorieTracker:
    """A simple calorie tracker to monitor daily food intake."""
    
    def __init__(self):
        self.meals: Dict[str, List[Tuple[str, int]]] = {}
        self.daily_goal = 2000
    
    def set_daily_goal(self, calories: int) -> None:
        """Set the daily calorie goal."""
        self.daily_goal = calories
    
    def add_meal(self, food_name: str, calories: int, date: str = None) -> None:
        """Add a meal with calories for a specific date."""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        if date not in self.meals:
            self.meals[date] = []
        
        self.meals[date].append((food_name, calories))
    
    def get_daily_calories(self, date: str = None) -> int:
        """Get total calories consumed for a specific date."""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        if date not in self.meals:
            return 0
        
        return sum(calories for _, calories in self.meals[date])
    
    def get_remaining_calories(self, date: str = None) -> int:
        """Get remaining calories for the day based on daily goal."""
        daily_total = self.get_daily_calories(date)
        return self.daily_goal - daily_total
    
    def get_daily_summary(self, date: str = None) -> Dict:
        """Get a summary of the day's nutrition tracking."""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        consumed = self.get_daily_calories(date)
        remaining = self.get_remaining_calories(date)
        return {"date": date, "consumed": consumed, "remaining": remaining, "goal": self.daily_goal}
