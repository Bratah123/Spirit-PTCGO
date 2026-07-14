from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8991cd72-4b2d-5473-87bf-4e73c6ec619d",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Rapid Strike", "Shinx"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=39,
    set_code="CZ",
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