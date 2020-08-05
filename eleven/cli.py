"""Command line interface for eleven."""
import argh


def greet() -> None:
    r"""Say hello, eleven"""
    print(f'Hello, Data Science 511!')


def main():
    parser = argh.ArghParser()
    parser.add_commands([greet])
    parser.dispatch()


if __name__=='__main__':
    main()
