from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import roll_over, snorlax_guard_passive


card = PokemonCardDef(
    guid="f8589435-6dc1-5a25-aa2b-8f556aba1562",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=143,
    abilities=[
        Ability(
            title="Guard",
            game_text="As long as Snorlax is your Active Pok\u00e9mon, the Defending Pok\u00e9mon can't Retreat. This power stops working when Snorlax is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=snorlax_guard_passive,
        ),
        Attack(
            title="Roll Over",
            game_text="Snorlax is now Asleep. Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=30,
            effect=roll_over,
        ),
    ],
)
