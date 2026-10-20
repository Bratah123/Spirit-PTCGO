from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import snipe_attack


async def _spiteful_spirit(ctx):
    """If this Pokemon is your Active and is Knocked Out by damage from an
    opponent's attack, the Attacking Pokemon is now Confused and Poisoned."""
    attacker = ctx.ko_attacker
    if not (ctx.ko_from_attack and ctx.was_active_at_ko) or attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)
    await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="4bd3813d-9098-5333-97c4-ede9a2f334f5",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent", "Stage 1", "Team Plasma", "Jellicent"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=39,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Ability(
            title="Spiteful Spirit",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, the Attacking Pok\u00e9mon is now Confused and Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_spiteful_spirit,
        ),
        Attack(
            title="Aqua Bullet",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=snipe_attack(10, also_base=True),
        ),
    ],
)