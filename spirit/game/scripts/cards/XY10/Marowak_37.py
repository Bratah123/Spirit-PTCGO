"""STUB: effect not implemented — do not guess mechanics.
Marowak (XY10 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b49d7f42-e18a-5092-b10c-4ad8a5fcd66b",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=105,
    abilities=[
        Ability(
            title="Bodyguard",
            game_text="Prevent all effects of attacks done to you or your hand by your opponent's Pok\u00e9mon. Remove any existing effects.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bonemerang",
            game_text="Flip 2 coins. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)