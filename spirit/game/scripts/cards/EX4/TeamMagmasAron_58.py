from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3de6da54-9cf7-5881-bdf6-0024e7a72870",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAron.Name",
    display_name="Team Magma's Aron",
    searchable_by=["Team Magma's Aron", "Basic", "TeamMagmasAron"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=304,
    abilities=[
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)