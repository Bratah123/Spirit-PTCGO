from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9e49930-d36c-5277-b227-301491cfac06",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionV.Name",
    display_name="Volcanion V",
    searchable_by=["Volcanion V", "Basic", "V", "Single Strike", "VolcanionV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=25,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Dynamite Tackle",
            game_text="If this Pok\u00e9mon has 10 or more damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)