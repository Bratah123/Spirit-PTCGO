from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb3e99b5-92a5-522f-9ec8-d28c1bb79283",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeloettaEX.Name",
    display_name="Meloetta-EX",
    searchable_by=["Meloetta-EX", "Basic", "EX", "MeloettaEX"],
    subtypes=["Basic", "EX"],
    collector_number=140,
    set_code="BW11",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=648,
    abilities=[
        Attack(
            title="Brilliant Voice",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Round",
            game_text="Does 30 damage times the number of your Pok\u00e9mon that have the Round attack.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)