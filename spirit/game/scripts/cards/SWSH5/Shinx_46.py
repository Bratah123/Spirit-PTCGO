from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f42f1ed1-4cd3-5d9f-9520-02ddcadc9a9d",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Rapid Strike", "Shinx"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=46,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=403,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)