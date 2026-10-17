from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="08e542e8-4979-5072-8f8a-c13f5d071699",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    display_name="Petilil",
    searchable_by=["Petilil", "Basic", "Petilil"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=548,
    abilities=[
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 10 more damage and heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)