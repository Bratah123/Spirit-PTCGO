from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.smp import pulverizing_pancake_gx


async def hypno_roll(ctx):
    """100 damage only while this Pokémon is Asleep."""
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    current = (ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if ctx.attacker else []
    if asleep not in current:
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="284585c5-ca7c-5de6-9720-26d4cd90b869",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxGX.Name",
    display_name="Snorlax-GX",
    searchable_by=["Snorlax-GX", "Basic", "GX", "SnorlaxGX"],
    subtypes=["Basic", "GX"],
    collector_number=5,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Collapse",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
        Attack(
            title="Thunderous Snore",
            game_text="This attack can be used if this Pok\u00e9mon is Asleep. If it is not Asleep, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=180,
            usable_despite_conditions=True,
            effect=hypno_roll,
        ),
        Attack(
            title="Pulverizing Pancake-GX",
            game_text="This Pok\u00e9mon is now Asleep. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 5},
            damage=210,
            effect=pulverizing_pancake_gx,
        ),
    ],
)