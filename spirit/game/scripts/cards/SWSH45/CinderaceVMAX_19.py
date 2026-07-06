from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6d49edc8-3477-5ce3-b8b0-642684647172",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceVMAX.Name",
    display_name="Cinderace VMAX",
    searchable_by=["Cinderace VMAX", "VMAX", "CinderaceVMAX"],
    subtypes=["VMAX"],
    collector_number=19,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceV.Name",
    family_id=815,
    abilities=[
        Attack(
            title="Counter",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Max Pyro Ball",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)