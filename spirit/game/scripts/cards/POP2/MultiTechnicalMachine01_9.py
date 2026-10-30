"""Multi Technical Machine 01: attach to any Pokémon; grants Paralyzing Gaze; discard end of turn."""
from spirit.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from spirit.game.attributes import Rarities, PokemonTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    multi_tm_attach_any, ancient_tm_discard_end_turn,
)

_GUID = "2c3a54c5-e8fa-5994-b0c2-93cfc9d3b592"

card = PokemonToolCardDef(
    guid="2c3a54c5-e8fa-5994-b0c2-93cfc9d3b592",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiTechnicalMachine01.Name",
    display_name="Multi Technical Machine 01",
    searchable_by=["Multi Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine", "Pokémon Tool"],
    collector_number=9,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    attach_to=multi_tm_attach_any(),
    granted_abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="The Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.PARALYZED),
        ),
        Ability(
            title="Multi Technical Machine 01",
            game_text="At the end of your turn, discard Multi Technical Machine 01.",
            trigger=Triggers.END_OF_TURN,
            effect=ancient_tm_discard_end_turn(_GUID),
        ),
    ],
)
