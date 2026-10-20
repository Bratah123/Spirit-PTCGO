from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb81a3a3-2a8e-58ba-a211-068fbbfa1ee7",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusEX.Name",
    display_name="Thundurus-EX",
    searchable_by=["Thundurus-EX", "Basic", "EX", "Team Plasma", "ThundurusEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=110,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Attack(
            title="Raiden Knuckle",
            game_text="Attach an Energy card from your discard pile to 1 of your Benched Team Plasma Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Thunderous Noise",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)