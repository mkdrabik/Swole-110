class workout:
    goal: str
    type: str


    def __init__(self, reps: str, body_part: str = ""):
        rep_count: str = ""
        if reps == "Get Stronger":
            rep_count = "4 - 6"
        else:
            rep_count = "12 - 15"
        chest: str = f"Barbell Bench Press: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Incline Dumbell Bench: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps High to Low Flies: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Pec Deck Flies Warm up set of {rep_count} reps, 3 sets of {rep_count} reps" 
        back: str = f"High Rows: Warm up set of 6 reps each side, 3 sets of {rep_count} reps Landmine Rows: Warm up set of 6 reps, 3 sets of {rep_count} reps JPG Pulldowns: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps T-Bar Rows: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Barbell Shrugs: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps" 
        legs: str= f"Quad Extensions: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Prone Leg Curls: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Barbell Back Squat: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Babrell Hip Thrusts: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps" 
        shoulders: str = f"Dumbell Shoulder Press: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Rear Delt Cable Flies: Warm up set of {rep_count} reps: 3 sets of {rep_count} reps Dumbell Lateral Raises: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps" 
        triceps: str = f"Skullcrushers Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Tricep Pushdowns: Warm up set of {rep_count} reps, 2 sets of {rep_count} reps, dropset of at least 15 reps Overhead Rope Tricep Extensions: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps" 
        biceps: str = f"Preacher Curls: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Cross-Body Hammer Curls: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps Incline Dumbell Curls: Warm up set of {rep_count} reps, 3 sets of {rep_count} reps" 
        if body_part == "Chest":
            self.type = chest
        elif body_part == "Back":
            self.type = back
        elif body_part == "Legs":
            self.type = legs
        elif body_part == "Shoulders":
            self.type = shoulders
        elif body_part == "Triceps":
            self.type = triceps
        else:
            self.type = biceps
        
        self.goal = reps
        
