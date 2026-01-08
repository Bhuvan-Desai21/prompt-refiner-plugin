"""
My Plugin - Template for Tailor plugins

This is a template plugin that demonstrates the standard structure
and best practices for creating Tailor plugins.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add tailor root to path for imports
tailor_path = Path(__file__).resolve().parent.parent.parent
if str(tailor_path) not in sys.path:
    sys.path.insert(0, str(tailor_path))

from sidecar.api.plugin_base import PluginBase
from sidecar.constants import Severity


class Plugin(PluginBase):
    """
    Template Plugin.
    
    This plugin demonstrates the standard patterns for:
    - Command registration
    - Hook registration
    - Event emission
    - Settings management
    - Lifecycle hooks
    """
    
    def __init__(
        self,
        plugin_dir: Path,
        vault_path: Path,
        config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the plugin.
        
        Args:
            plugin_dir: Path to this plugin's directory
            vault_path: Path to the vault root
            config: Optional configuration dict
        """
        super().__init__(plugin_dir, vault_path, config)
        
        # Load settings from config
        self.greeting = self.config.get("greeting", "Hello")
        
        self.logger.info(f"{self.name} plugin initialized")
    
    def register_commands(self) -> None:
        """
        Register plugin commands.
        
        This method is called automatically after __init__.
        Register all commands your plugin provides here.
        """
        self.brain.register_command(
            "myPlugin.hello",
            self._handle_hello,
            self.name
        )
        
        self.brain.register_command(
            "myPlugin.getStatus",
            self._handle_get_status,
            self.name
        )
        
        self.logger.debug(f"Registered {2} commands")
    
    def register_hooks(self) -> None:
        """
        Register LLM processing hooks.
        
        Available hooks:
        - input.transform: Modify user message before processing
        - input.validate: Validate/filter input (can abort)
        - process.before_llm: Inject context before LLM call
        - process.after_llm: Post-process LLM response
        - output.format: Format response for UI
        
        Uncomment the hooks you want to use.
        """
        # Example: Register a hook to transform input
        # self.register_hook(
        #     "input.transform",
        #     self._transform_input,
        #     priority=100  # Lower = runs first
        # )
        pass
    
    # -------------------------------------------------------------------------
    # Command Handlers
    # -------------------------------------------------------------------------
    
    async def _handle_hello(
        self,
        name: str = "World",
        **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Handle the hello command.
        
        Args:
            name: Name to greet
            **kwargs: Additional arguments from caller
            
        Returns:
            Dict with status and message
        """
        message = f"{self.greeting}, {name}!"
        
        # Emit notification to UI
        self.notify(message, severity=Severity.SUCCESS)
        
        return {
            "status": "success",
            "message": message
        }
    
    async def _handle_get_status(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Get plugin status.
        
        Returns:
            Dict with plugin status information
        """
        return {
            "status": "success",
            "plugin": self.name,
            "version": "1.0.0",
            "loaded": self.is_loaded,
            "greeting": self.greeting
        }
    
    # -------------------------------------------------------------------------
    # Hook Handlers (uncomment to use)
    # -------------------------------------------------------------------------
    
    # async def _transform_input(self, ctx: "HookContext") -> "HookContext":
    #     """
    #     Transform user input before processing.
    #     
    #     Args:
    #         ctx: Hook context with message and metadata
    #         
    #     Returns:
    #         Modified context
    #     """
    #     # Example: Add a prefix to all messages
    #     # ctx.message = f"[Enhanced] {ctx.message}"
    #     return ctx
    
    # -------------------------------------------------------------------------
    # Lifecycle Hooks
    # -------------------------------------------------------------------------
    
    async def on_load(self) -> None:
        """
        Called after the plugin is fully loaded.
        
        Use this for initialization that requires other plugins
        to be available (e.g., cross-plugin communication).
        """
        await super().on_load()
        
        if self.is_client_connected:
            self.notify(
                f"Plugin '{self.name}' loaded successfully",
                severity=Severity.SUCCESS
            )
    
    async def on_tick(self) -> None:
        """
        Called periodically (every 5 seconds by default).
        
        Use for background tasks, polling, or periodic updates.
        Keep this lightweight to avoid performance issues.
        """
        # Example: Log a debug message every tick
        # self.logger.debug(f"{self.name} tick")
        pass
    
    async def on_unload(self) -> None:
        """
        Called when the plugin is being unloaded.
        
        Use for cleanup: close connections, save state, etc.
        """
        self.logger.info(f"{self.name} unloading")
        await super().on_unload()
