from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e63a685b-33a1-5b6e-8a1a-84214716c75e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    display_name="Gossifleur",
    searchable_by=["Gossifleur", "Basic", "Gossifleur"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=829,
    abilities=[
        Attack(
            title="Leafage",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)