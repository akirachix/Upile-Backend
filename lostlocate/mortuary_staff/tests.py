from django.test import TestCase
from django.core.exceptions import ValidationError
from mortuary.models import Mortuary
from mortuary_staff.models import MortuaryStaff  

class MortuaryStaffModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create test data for Mortuary and MortuaryStaff."""
        cls.mortuary = Mortuary.objects.create(
            id=1,
            mortuary_name='Central Mortuary',
            location='Downtown'
        )
    
    def test_mortuary_staff_creation(self):
        """Test the creation of a MortuaryStaff instance."""
        staff = MortuaryStaff.objects.create(
            id=1,
            position='Pathologist',
            contact='5551234567',
            mortuary_id=self.mortuary,
            generated_code='ABC123'
        )
        self.assertEqual(staff.position, 'Pathologist')
        self.assertEqual(staff.contact, '5551234567')
        self.assertEqual(staff.mortuary_id, self.mortuary)
        self.assertEqual(staff.generated_code, 'ABC123')
    
    def test_string_representation(self):
        """Test the string representation of a MortuaryStaff instance."""
        staff = MortuaryStaff.objects.create(
            id=2,
            position='Technician',
            contact='5559876543',
            mortuary_id=self.mortuary,
            generated_code='XYZ789'
        )
        self.assertEqual(str(staff), 'Staff 2 - Technician')

    def test_mortuary_staff_creation_unhappy(self):
        """Unhappy path: Test creating a MortuaryStaff instance with invalid data."""
        
        # Test with missing Mortuary instance
        staff = MortuaryStaff(
            id=3,
            position='Technician',
            contact='5559876543',
            mortuary_id=None,  # Invalid data: no Mortuary instance
            generated_code='LMN456'
        )
        with self.assertRaises(ValidationError):
            staff.full_clean()  # Trigger validation

        # Test with invalid contact number
        staff = MortuaryStaff(
            id=4,
            position='Receptionist',
            contact='555123',  # Invalid contact number length
            mortuary_id=self.mortuary,
            generated_code='PQR123'
        )
        with self.assertRaises(ValidationError):
            staff.full_clean()  # Trigger validation

        # Test with empty position
        staff = MortuaryStaff(
            id=5,
            position='',  # Empty position
            contact='5553219876',
            mortuary_id=self.mortuary,
            generated_code='STU789'
        )
        with self.assertRaises(ValidationError):
            staff.full_clean()  # Trigger validation

        # Test with position exceeding max_length
        staff = MortuaryStaff(
            id=6,
            position='A' * 31,  # Exceeds max_length of 30
            contact='5556543210',
            mortuary_id=self.mortuary,
            generated_code='VWX789'
        )
        with self.assertRaises(ValidationError):
            staff.full_clean()  # Trigger validation

        # Test with generated_code exceeding max_length
        staff = MortuaryStaff(
            id=7,
            position='Security Guard',
            contact='5551112233',
            mortuary_id=self.mortuary,
            generated_code='A' * 31  # Exceeds max_length of 30
        )
        with self.assertRaises(ValidationError):
            staff.full_clean()  # Trigger validation
