from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4027d789-fe1a-5c27-91d2-31107966390b",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    display_name="Corphish",
    searchable_by=["Corphish", "Basic", "Corphish"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=341,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)