from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4228dbc7-1203-55b6-92f6-4022bcc6efff",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name",
    display_name="Latios-EX",
    searchable_by=["Latios-EX", "Basic", "EX", "LatiosEX"],
    subtypes=["Basic", "EX"],
    collector_number=113,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    family_id=381,
    abilities=[
        Attack(
            title="Mach Flight",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Luster Purge",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)