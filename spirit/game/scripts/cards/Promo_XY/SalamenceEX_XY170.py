"""STUB: effect not implemented — do not guess mechanics.
Salamence-EX (Promo_XY #XY170): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="835dbd0a-fe86-5cbe-beab-976a8e690a53",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceEX.Name",
    display_name="Salamence-EX",
    searchable_by=["Salamence-EX", "Basic", "EX", "SalamenceEX"],
    subtypes=["Basic", "EX"],
    collector_number=170,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=373,
    abilities=[
        Attack(
            title="Beastly Fang",
            game_text="This attack does 50 more damage for each of your opponent's Pok\u00e9mon-EX.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Strike",
            game_text="This Pok\u00e9mon can't use Dragon Strike during your next turn.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)