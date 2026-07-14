from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ffb8bad-6032-5bd5-ac7e-007f59ddd894",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceV.Name",
    display_name="Cinderace V",
    searchable_by=["Cinderace V", "Basic", "V", "Single Strike", "CinderaceV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=44,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=815,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="All-Out Shot",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)