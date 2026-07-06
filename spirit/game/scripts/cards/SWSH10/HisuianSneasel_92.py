from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ef08f22-4771-5e95-ac77-8da4ce8bcd01",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSneasel.Name",
    display_name="Hisuian Sneasel",
    searchable_by=["Hisuian Sneasel", "Basic", "HisuianSneasel"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=215,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)