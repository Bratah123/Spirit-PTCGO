from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import bonus_if

from spirit.game.data_utils import Attack, def_for
from spirit.game.attributes import SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES


async def amnesia(ctx):
    """20 damage; lock 1 of the Defending Pokémon's attacks next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    definition = def_for(defender.archetype_id)
    candidates = [
        (defender, ability) for ability in getattr(definition, "abilities", []) or []
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to lock")
    if picked is None:
        return
    _, chosen = picked
    ctx.session.turn_state.lock_attack(defender.entity_id, chosen.ability_id)


def _burned_or_poisoned(ctx):
    defender = ctx.attacker
    if defender is None:
        return False
    current = defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    burned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.BURNED]
    poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
    return burned in current or poisoned in current


card = PokemonCardDef(
    guid="f1be7ceb-b271-59d0-bbb5-7463f7538c21",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=amnesia,
        ),
        Attack(
            title="Facade",
            game_text="If this Pok\u00e9mon is Burned or Poisoned, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_burned_or_poisoned, 80),
        ),
    ],
)