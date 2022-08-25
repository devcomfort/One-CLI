from typing import Optional
import typer


def main(command: str, app: str, config: Optional[str] = typer.Argument(None)):
    if command == 'install':
        pass


if __name__ == '__main__':
    typer.run(main)
