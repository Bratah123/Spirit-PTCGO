from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e746750f-743c-5ed0-a512-bb5a52694992",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioV.Name",
    display_name="Lucario V",
    searchable_by=["Lucario V", "Basic", "V", "LucarioV"],
    subtypes=["Basic", "V"],
    collector_number=146,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=448,
    abilities=[
        Attack(
            title="Aura Sphere",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)