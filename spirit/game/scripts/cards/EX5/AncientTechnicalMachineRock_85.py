"""Ancient Technical Machine [Rock]: attach to Evolved non-ex non-owner; grants Stone Generator; discard end of turn."""
from spirit.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.ex import (
    attach_to_evolved_non_ex_non_owner,
    stone_generator,
    ancient_tm_discard_end_turn,
)

_GUID = "46dd72ab-5db3-532a-9c67-153cb44cdbc1"

card = PokemonToolCardDef(
    guid=_GUID,
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineRock.Name",
    display_name="Ancient Technical Machine [Rock]",
    searchable_by=["Ancient Technical Machine [Rock]", "Technical Machine"],
    subtypes=["Technical Machine", "Pokémon Tool"],
    collector_number=85,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_evolved_non_ex_non_owner(),
    granted_abilities=[
        Attack(
            title="Stone Generator",
            game_text="If your opponent has any Evolved Pokémon in play, remove the highest Stage Evolution card from each of them and put those cards back into his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=stone_generator(),
        ),
        Ability(
            title="Ancient Technical Machine [Rock]",
            game_text="At the end of your turn, discard Ancient Technical Machine [Rock].",
            trigger=Triggers.END_OF_TURN,
            effect=ancient_tm_discard_end_turn(_GUID),
        ),
    ],
)
