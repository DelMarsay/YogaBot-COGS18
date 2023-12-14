import mock  
import builtins
from  functions import *
from classes import YogaClass

def test_get_image():
    # test no image available
    assert get_image('Warrior III', df) == f"Sorry. I don't have a Warrior III demo yet."
    
    # test successful image
    #assert get_image ('Warrior Three', df) == Image
        
def test_add_student():
    test_class = YogaClass('Day', 'Time')
    
    # test added student to class
    with mock.patch.object(builtins, 'input', lambda _: 'Name'):
        msg = test_class.add_student()
        assert msg == 'See you on Day at Time, Name!'
        assert 'Name' in test_class.students
        
    # test with full class
    test_class.available = False
    with mock.patch.object(builtins, 'input', lambda _: 'Nope'):
        msg = test_class.add_student()
        assert msg == 'Sorry, Nope. Class is full. Choose another day please.'
        assert 'Nope' not in test_class.students
    
        
def test_yoga_buddy():
    # test no yoga buddy
    test_class = YogaClass('Day', 'Time')
    test_classes = {'Day': test_class}
    assert yoga_buddy(test_classes) == 'Sorry, no yoga buddy found!'
    
    # test found yoga buddy 
    test_class.students = test_class.students + ['Name']
    test_classes = {'Day': test_class}
    assert yoga_buddy(test_classes) == 'Your yoga buddy is Name on Day at Time'