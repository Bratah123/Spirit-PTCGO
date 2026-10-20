"""STUB: effect not implemented — do not guess mechanics.
Ninetales (XY5 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ec9b782e-cdb3-5f69-8677-dfbc28b2a0e6",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Barrier Shrine",
            game_text="Each player can't play any Stadium cards from his or her hand.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flickering Flames",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)