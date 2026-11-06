from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.passives import effective_max_hp


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _purify_condition(board, player_id, pokemon=None):
    return pokemon is not None and any(is_basic_energy_card(c) and _is_fire_energy(c) for c in pokemon.children) \
        and effective_max_hp(board, pokemon) > pokemon.get_attribute(AttrID.HP, 0)


async def _purifying_fire(ctx):
    """Heal 50 damage from this Pokemon."""
    await ctx.heal(50, ctx.source)


card = PokemonCardDef(
    guid="bf786816-cd38-5c40-b289-49a688d9fc20",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhEX.Name",
    display_name="Ho-Oh-EX",
    searchable_by=["Ho-Oh-EX", "Basic", "EX", "HoOhEX"],
    subtypes=["Basic", "EX"],
    collector_number=92,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title="Purifying Fire",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon has any basic Fire Energy attached to it, you may heal 50 damage from it.",
            activation=Activations.ONCE_PER_TURN,
            condition=_purify_condition,
            effect=_purifying_fire,
        ),
        Attack(
            title="Elemental Feather",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=130,
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)