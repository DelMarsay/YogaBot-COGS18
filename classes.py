class YogaClass():
    
    capacity = 8
    
    def __init__(self, day, time):
        self.day = day
        self.time = time
        self.students = []
        self.available = True

    def add_student(self):
        
        """adds a student to this yoga class as long as it is not full """

        student = input('What\'s your name?: \t')
        
        if self.available:
            self.students = self.students + [student]
            if len(self.students) == self.capacity:
                self.available = False 
                
            output = f'See you on {self.day} at {self.time}, {student.capitalize()}!'
            
            
        else:
            output = f'Sorry, {student.capitalize()}. Class is full. Choose another day please.'
            
        return output
    