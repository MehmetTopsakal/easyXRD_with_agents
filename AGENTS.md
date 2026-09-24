# User environment preference

Use the user's Pixi environment at `/home/mt/mpixi` by default for Python commands, scripts, and tests. Prefer `/home/mt/mpixi/.pixi/envs/default/bin/python` for Python execution, or `pixi run --manifest-path /home/mt/mpixi/pixi.toml <command>` when environment activation is needed. Use a different environment when the user explicitly requests it or the project requires it.
