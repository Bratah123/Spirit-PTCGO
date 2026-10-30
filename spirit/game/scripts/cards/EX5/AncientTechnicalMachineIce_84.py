"""Ancient Technical Machine [Ice]: attach to Evolved non-ex non-owner; grants Ice Generator; discard end of turn."""
from spirit.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.ex import (
    attach_to_evolved_non_ex_non_owner,
    ice_generator,
    ancient_tm_discard_end_turn,
)

_GUID = "c13abb70-a9c8-5f6f-a79d-f6d4538ee2dd"

card = PokemonToolCardDef(
    guid=_GUID,
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineIce.Name",
    display_name="Ancient Technical Machine [Ice]",
    searchable_by=["Ancient Technical Machine [Ice]", "Technical Machine"],
    subtypes=["Technical Machine", "Pokémon Tool"],
    collector_number=84,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_evolved_non_ex_non_owner(),
    granted_abilities=[
        Attack(
            title="Ice Generator",
            game_text="Discard all of your opponent's Trainer cards in play. If you do, prevent all effects, including damage, done to the Pokémon using this attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ice_generator(_GUID),
        ),
        Ability(
            title="Ancient Technical Machine [Ice]",
            game_text="At the end of your turn, discard Ancient Technical Machine [Ice].",
            trigger=Triggers.END_OF_TURN,
            effect=ancient_tm_discard_end_turn(_GUID),
        ),
    ],
)
