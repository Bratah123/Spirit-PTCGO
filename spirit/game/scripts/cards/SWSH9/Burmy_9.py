from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e21caff0-04d2-5b67-b091-abe447c04757",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    display_name="Burmy",
    searchable_by=["Burmy", "Basic", "Burmy"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Attack(
            title="Hang Down",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)