"""STUB: effect not implemented — do not guess mechanics.
Forretress (XY2 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b397933b-333b-5f98-b58f-57e7610732cd",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Ability(
            title="Thorn Tempest",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Crash",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)