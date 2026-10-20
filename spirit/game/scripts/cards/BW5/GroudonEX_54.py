from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage, bonus_if, damage_counters_on


_defender_counters = damage_counters_on('defender')


def _two_counters(ctx):
    return _defender_counters(ctx) >= 2


card = PokemonCardDef(
    guid="4a9d6e5a-4315-5ffb-9225-293a2edbee5f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GroudonEX.Name",
    display_name="Groudon-EX",
    searchable_by=["Groudon-EX", "Basic", "EX", "GroudonEX"],
    subtypes=["Basic", "EX"],
    collector_number=54,
    set_code="BW5",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=383,
    abilities=[
        Attack(
            title="Tromp",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=spread_damage(10, also_base=True),
        ),
        Attack(
            title="Giant Claw",
            game_text="If the Defending Pok\u00e9mon already has 2 or more damage counters on it, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_two_counters, 40),
        ),
    ],
)