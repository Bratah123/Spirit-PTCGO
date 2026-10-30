"""Ancient Technical Machine [Steel]: attach to Evolved non-ex non-owner; grants Steel Generator; discard end of turn."""
from spirit.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.ex import (
    attach_to_evolved_non_ex_non_owner,
    steel_generator,
    ancient_tm_discard_end_turn,
)

_GUID = "b3a71da2-8057-5887-94bc-ada52dbb6aec"

card = PokemonToolCardDef(
    guid=_GUID,
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineSteel.Name",
    display_name="Ancient Technical Machine [Steel]",
    searchable_by=["Ancient Technical Machine [Steel]", "Technical Machine"],
    subtypes=["Technical Machine", "Pokémon Tool"],
    collector_number=86,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_evolved_non_ex_non_owner(),
    granted_abilities=[
        Attack(
            title="Steel Generator",
            game_text="If the Defending Pokémon has a Poké-Power or Poké-Body, choose up to 2 basic Energy cards attached to 1 of your opponent's Pokémon and attach them to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=steel_generator(),
        ),
        Ability(
            title="Ancient Technical Machine [Steel]",
            game_text="At the end of your turn, discard Ancient Technical Machine [Steel].",
            trigger=Triggers.END_OF_TURN,
            effect=ancient_tm_discard_end_turn(_GUID),
        ),
    ],
)
