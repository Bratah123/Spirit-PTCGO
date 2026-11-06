from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _big_ol_bite(ctx):
    """Printed damage; heal 30 from this Pokemon. The Defending Pokemon can't
    retreat during your opponent's next turn."""
    await ctx.deal_damage()
    await ctx.heal(30, ctx.attacker)
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.lock_retreat(d)


card = PokemonCardDef(
    guid="82903d23-01f5-58d6-95d4-9aedd59cb712",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Attack(
            title="Dancing Tentacles",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Stick and Absorb",
            game_text="Heal 30 damage from this Pok\u00e9mon. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_big_ol_bite,
        ),
    ],
)