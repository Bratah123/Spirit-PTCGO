from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, damage_per, damage_counters_on


card = PokemonCardDef(
    guid="32b94309-1687-5b82-b07f-a43872a6b6d7",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AggronEX.Name",
    display_name="Aggron-EX",
    searchable_by=["Aggron-EX", "Basic", "EX", "AggronEX"],
    subtypes=["Basic", "EX"],
    collector_number=153,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=306,
    abilities=[
        Attack(
            title="Steel Headbutt",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Raging Hammer",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(damage_counters_on('self'), 10, base=60),
        ),
    ],
)