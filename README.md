# Tailor Plugin Template

A template repository for creating Tailor plugins. Fork this repository to start building your own plugin!

## Quick Start

1. **Fork this repository** on GitHub
2. **Clone your fork** locally
3. **Update `plugin.json`** with your plugin's metadata
4. **Implement your plugin** in `main.py`
5. **Test locally** by copying to a vault's `plugins/` directory
6. **Submit to Plugin Store** when ready

## Structure

```
my-plugin/
├── plugin.json           # Plugin manifest (required)
├── main.py               # Plugin entry point (required)
├── settings.json         # Default settings
├── settings.schema.json  # Settings validation schema
├── README.md             # This file
├── CONTRIBUTING.md       # Contribution guidelines
├── LICENSE               # MIT License
├── .github/
│   └── workflows/
│       └── lint.yml      # Automated linting
└── tests/
    └── test_plugin.py    # Plugin tests
```

## Plugin Manifest (`plugin.json`)

Required fields:

| Field | Description |
|-------|-------------|
| `name` | Unique plugin identifier (lowercase, hyphens) |
| `version` | Semver version string |
| `displayName` | Human-readable name |
| `description` | Brief description |
| `author` | Author info (name, email, url) |
| `main` | Entry point file (usually `main.py`) |

Optional fields:

| Field | Description |
|-------|-------------|
| `repository` | GitHub repository URL |
| `minTailorVersion` | Minimum Tailor version required |
| `categories` | Array of categories (tools, memory, integrations, ui-themes) |
| `keywords` | Search keywords |
| `dependencies.python` | Python package dependencies |
| `hooks` | Which LLM hooks this plugin uses |
| `commands` | List of commands this plugin registers |
| `settings` | Settings schema for configuration |

## Commands

Register commands in your plugin's `register_commands()` method:

```python
def register_commands(self) -> None:
    self.brain.register_command(
        "myPlugin.doSomething",  # Command ID
        self._handle_do_something,  # Handler function
        self.name  # Plugin name
    )

async def _handle_do_something(self, param: str = "", **kwargs) -> Dict[str, Any]:
    # Your logic here
    return {"status": "success", "result": param}
```

## Hooks

Register hooks to extend LLM processing:

| Hook | Purpose | Can Abort? |
|------|---------|------------|
| `input.transform` | Modify user message | No |
| `input.validate` | Filter/validate input | Yes |
| `process.before_llm` | Inject context (RAG, etc.) | No |
| `process.after_llm` | Post-process response | No |
| `output.format` | Format for UI | No |

```python
def register_hooks(self) -> None:
    self.register_hook(
        "process.before_llm",
        self._inject_context,
        priority=50  # Lower = runs first
    )

async def _inject_context(self, ctx: HookContext) -> HookContext:
    ctx.metadata["my_context"] = "injected data"
    return ctx
```

## Lifecycle Hooks

| Method | When Called |
|--------|-------------|
| `on_load()` | After all plugins loaded |
| `on_tick()` | Every 5 seconds |
| `on_unload()` | Before plugin shutdown |

## Testing Locally

1. Copy your plugin folder to a vault:
   ```bash
   cp -r my-plugin/ /path/to/vault/plugins/
   ```

2. Open the vault in Tailor

3. Check sidecar logs for your plugin initialization

## Submitting to Plugin Store

1. Ensure your plugin passes linting: `flake8 main.py`
2. Tag your GitHub repo with `tailor-plugin`
3. Fill out the [submission form](https://tailor.dev/submit-plugin)
4. Wait for review (usually 1-3 days)

## License

MIT License - see [LICENSE](LICENSE)
