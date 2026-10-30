from spirit.game.card_effects.ex import magnetic_lines_move_basic
"""STUB: effect not implemented — do not guess mechanics.
Dark Magneton (EX7 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="41a8398b-7167-5614-9e18-4013bd6899ec",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMagneton.Name",
    display_name="Dark Magneton",
    searchable_by=["Dark Magneton", "Stage 1", "DarkMagneton"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Magnetic Lines",
            game_text="If your opponent has at least 2 Pok\u00e9mon in play, move a basic Energy card from the Defending Pok\u00e9mon to another of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=magnetic_lines_move_basic(),
        ),
        Attack(
            title="Poison Pulse",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)