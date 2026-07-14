from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


async def loop_cannon(ctx):
    """160 damage. Put 2 Energy attached to this Pokémon into your hand."""
    await ctx.deal_damage()
    attached = ctx.attached_energies(ctx.attacker)
    if not attached:
        return
    picks = await ctx.choose_cards(
        attached, min(2, len(attached)),
        prompt="Choose Energy to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="04604f09-8442-5980-bb14-52a847738fb7",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toucannon.Name",
    display_name="Toucannon",
    searchable_by=["Toucannon", "Stage 2", "Toucannon"],
    subtypes=["Stage 2"],
    collector_number=145,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    family_id=731,
    abilities=[
        Attack(
            title="Energy Cutoff",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=discard_opponent_energy_attack(count=1),
        ),
        Attack(
            title="Loop Cannon",
            game_text="Put 2 Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=loop_cannon,
        ),
    ],
)