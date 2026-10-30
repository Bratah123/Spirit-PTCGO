from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="049ea307-fb07-5902-a09f-f78bb74af4cb",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    display_name="Seel δ",
    searchable_by=["Seel \u03b4", "Basic", "Seel"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)