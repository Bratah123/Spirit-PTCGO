from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _wake_up_slap(ctx):
    """30, +60 if the opponent's Active has a Special Condition; then remove
    all Special Conditions from it."""
    defender = ctx.defender
    affected = defender is not None and bool(defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
    await ctx.deal_damage(30 + (60 if affected else 0))
    if affected:
        await ctx.cure_all_conditions(defender)


card = PokemonCardDef(
    guid="430a6089-e42e-5b49-abdd-a43555c0d5ec",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr", "Stage 2", "Conkeldurr"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Wake-Up Slap",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 60 more damage. Then, remove all Special Conditions from that Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=_wake_up_slap,
        ),
        Attack(
            title="Dynamic Punch",
            game_text="Flip a coin. If heads, this attack does 40 more damage and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True, heads_bonus_damage=40),
        ),
    ],
)