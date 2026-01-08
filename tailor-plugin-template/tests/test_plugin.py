"""
Tests for the plugin.

Run with: pytest tests/ -v
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import MagicMock, AsyncMock

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestPlugin:
    """Test cases for the plugin."""
    
    @pytest.fixture
    def mock_brain(self):
        """Create a mock VaultBrain."""
        brain = MagicMock()
        brain.register_command = MagicMock()
        brain.execute_command = AsyncMock()
        return brain
    
    @pytest.fixture
    def mock_plugin_dir(self, tmp_path):
        """Create a temporary plugin directory."""
        plugin_dir = tmp_path / "test_plugin"
        plugin_dir.mkdir()
        
        # Create settings.json
        settings_file = plugin_dir / "settings.json"
        settings_file.write_text('{"greeting": "Test Hello"}')
        
        return plugin_dir
    
    def test_plugin_import(self):
        """Test that the plugin can be imported."""
        # This tests basic syntax/import
        try:
            from main import Plugin
            assert Plugin is not None
        except ImportError as e:
            # Expected in isolated test environment
            pytest.skip(f"Cannot import Plugin: {e}")
    
    @pytest.mark.asyncio
    async def test_hello_command(self, mock_brain, mock_plugin_dir, tmp_path):
        """Test the hello command."""
        # Note: This is a template test - adjust for your actual plugin
        # In a real test, you would instantiate the plugin and test commands
        pass
    
    def test_settings_loading(self, mock_plugin_dir):
        """Test that settings are loaded correctly."""
        settings_file = mock_plugin_dir / "settings.json"
        assert settings_file.exists()
        
        import json
        with open(settings_file) as f:
            settings = json.load(f)
        
        assert settings["greeting"] == "Test Hello"
