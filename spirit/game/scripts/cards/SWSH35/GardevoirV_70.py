from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="09446d01-b852-5d6b-8e85-faec31fd84ca",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirV.Name",
    display_name="Gardevoir V",
    searchable_by=["Gardevoir V", "Basic", "V", "GardevoirV"],
    subtypes=["Basic", "V"],
    collector_number=70,
    set_code="SWSH35",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=282,
    abilities=[
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Swelling Pulse",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)