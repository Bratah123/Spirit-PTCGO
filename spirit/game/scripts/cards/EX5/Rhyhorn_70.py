"""STUB: effect not implemented — do not guess mechanics.
Rhyhorn (EX5 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, recoil_attack


card = PokemonCardDef(
    guid="2b63d000-5c20-5a04-820f-518768a18029",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    display_name="Rhyhorn",
    searchable_by=["Rhyhorn", "Basic", "Rhyhorn"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=111,
    abilities=[
        Attack(
            title="Double Stab",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Take Down",
            game_text="Rhyhorn does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=recoil_attack(10),
        ),
    ],
)