from bakery import assert_equal
from drafter import *
from dataclasses import dataclass



hide_debug_information()
set_website_title("Your Drafter Website")
set_website_framed(False)
set_site_information(author="Andrew", description="Blah blah", sources=["asd", "asd"], planning=["part0.pdf"], links=["https://aorlov05.github.io/pet-adoption-website/"], server=None)


@dataclass
class State:
    pass


@route
def index(state: State) -> Page:
    return Page(state, ["Hello CS1 Students!"])

assert_equal(index(State()), Page(State(), ["Hello CS1 Students!"]))

start_server(State())
