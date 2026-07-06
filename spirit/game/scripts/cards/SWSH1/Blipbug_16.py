from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c67d774-44b5-58d6-af1f-22f257c80d90",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    display_name="Blipbug",
    searchable_by=["Blipbug", "Basic", "Blipbug"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=824,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)