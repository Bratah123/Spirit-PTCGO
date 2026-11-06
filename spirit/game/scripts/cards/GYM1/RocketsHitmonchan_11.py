from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import crosscounter


card = PokemonCardDef(
    guid="a9fab924-d40b-59ba-9d80-5fc50be66204",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsHitmonchan.Name",
    display_name="Rocket's Hitmonchan",
    searchable_by=["Rocket's Hitmonchan", "Basic", "RocketsHitmonchan"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Crosscounter",
            game_text="If an attack does damage to Rocket's Hitmonchan during your opponent's next turn (even if Rocket's Hitmonchan is Knocked Out), flip a coin. If heads, Rocket's Hitmonchan attacks your opponent's Active Pok\u00e9mon for double that amount of damage. (If Rocket's Hitmonchan takes 20 damage, it does 40 damage to that Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=crosscounter,
        ),
        Attack(
            title="Magnum Punch",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
