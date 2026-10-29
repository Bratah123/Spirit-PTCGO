from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import AttrID
from spirit.game.data_utils import Triggers
from spirit.game.attributes import SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.passives_common import is_in_active_spot


async def comatose(ctx):
    """When you attach Energy from your hand to Active Komala, it is Asleep."""
    if ctx.attaching_player_id != ctx.player_id:
        return
    if ctx.energy_receiver is not ctx.source:
        return
    if ctx.source is not ctx.my_active():
        return
    await ctx.apply_special_condition(ctx.source, SpecialConditions.ASLEEP)


async def hypno_roll(ctx):
    """100 damage only while this Pokémon is Asleep."""
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    current = (ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if ctx.attacker else []
    if asleep not in current:
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="50ea346f-fd23-5e30-ae8c-297ca0b75c17",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name",
    display_name="Komala",
    searchable_by=["Komala", "Basic", "Komala"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Ability(
            title="Comatose",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever you attach an Energy from your hand to it, it is now Asleep.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=comatose,
        ),
        Attack(
            title="Hypno Roll",
            game_text="This attack can be used if this Pok\u00e9mon is Asleep. If it is not Asleep, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            usable_despite_conditions=True,
            effect=hypno_roll,
        ),
    ],
)