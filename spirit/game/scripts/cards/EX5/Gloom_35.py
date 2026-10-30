"""STUB: effect not implemented — do not guess mechanics.
Gloom (EX5 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


from spirit.game.card_effects.ex import cling_heal

card = PokemonCardDef(
    guid="a1b7c982-e2e8-5b70-9530-2f7a573fd444",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1", "Gloom"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Cling",
            game_text="After your attack, remove from Gloom the number of damage counters equal to the damage you did to the Defending Pok\u00e9mon. If Gloom has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=cling_heal(),
        ),
        Attack(
            title="Double Razor Leaf",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)