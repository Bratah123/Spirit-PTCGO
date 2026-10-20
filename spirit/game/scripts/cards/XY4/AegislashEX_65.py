from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon
from spirit.game.session.effects import is_special_energy
from spirit.game.card_effects.attacks_common import damage_per, count_energy


def _from_special_energy(calc, carrier):
    """Attacks from opposing Pokemon that have any Special Energy attached."""
    a = calc.attacker
    return calc.target is carrier_pokemon(carrier) and a is not None and any(
        is_special_energy(c) for c in a.children)


card = PokemonCardDef(
    guid="b426e269-305a-5ce2-a51e-3f01d56b2bdd",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashEX.Name",
    display_name="Aegislash-EX",
    searchable_by=["Aegislash-EX", "Basic", "EX", "AegislashEX"],
    subtypes=["Basic", "EX"],
    collector_number=65,
    set_code="XY4",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=681,
    abilities=[
        Ability(
            title="Mighty Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from each of your opponent's Pok\u00e9mon that has any Special Energy attached to it.",
            passive=prevent_damage_when(_from_special_energy),
        ),
        Attack(
            title="Slash Blast",
            game_text="This attack does 20 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.METAL), 20, base=40),
        ),
    ],
)