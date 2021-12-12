from API.backend.Comm.command import Command

from obfuscation_core.obfuscators.puzzle_obfuscator import PuzzleObfuscator


class CommandPuzzle(Command):
    id = 4

    def __init__(self):
        self.puzzle_size: int = None

        pass

    def set_params(self, params: dict):
        if "puzzle_size" not in params.keys():
            params["puzzle_size"] = 9
        self.puzzle_size = params["puzzle_size"]
        print(params)

    def execute(self) -> PuzzleObfuscator:
        print("Executing PuzzleObfuscator!")
        return PuzzleObfuscator(puzzle_size=self.puzzle_size)
