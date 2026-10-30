from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d27d1b0-2232-537b-ab25-e299c0dfbc16",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    display_name="Mareep δ",
    searchable_by=["Mareep \u03b4", "Basic", "Mareep"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=179,
    abilities=[
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)