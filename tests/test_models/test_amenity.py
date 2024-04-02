#!/usr/bin/python3
"""Test City class."""
from tests.test_models.test_base_model import BaseModel
from models.city import City


class TestCity(BaseModel):
    """Test City class."""

    def __init__(self, *args, **kwargs):
        """Initialize instance."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_name(self):
        """Test name attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)
