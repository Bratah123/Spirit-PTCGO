from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_for_bonus
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import carrier_pokemon


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _from_basic(calc, carrier):
    """Damage to this Pokemon from attacks by the opponent's Basic Pokemon."""
    return (calc.target is carrier_pokemon(carrier) and calc.attacker is not None
            and is_basic_pokemon(calc.attacker))


card = PokemonCardDef(
    guid="7c71795f-ec1a-5fc0-b434-43fcf89e13c9",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1", "Pyroar"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Ability(
            title="Intimidating Mane",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Basic Pok\u00e9mon.",
            passive=prevent_damage_when(_from_basic),
        ),
        Attack(
            title="Scorching Fang",
            game_text="You may discard a Fire Energy attached to this Pok\u00e9mon. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=discard_for_bonus(source='self-energy', predicate=_is_fire_energy, max_count=1, flat=30, prompt='You may discard a Fire Energy for 30 more damage'),
        ),
    ],
)