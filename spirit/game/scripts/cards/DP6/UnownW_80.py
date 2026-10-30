"""STUB: effect not implemented — do not guess mechanics.
Unown [W] (DP6 #80): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="e3fc7bef-603d-5b56-9008-e2277115ca9c",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownW.Name",
    display_name="Unown [W]",
    searchable_by=["Unown [W]", "Basic", "UnownW"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="WALL",
            game_text="As long as Unown W is your Active Pok\u00e9mon, any damage done to your Pok\u00e9mon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Draw a card.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=draw_attack(1),
        ),
    ],
)