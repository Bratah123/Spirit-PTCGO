from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import energy_provides_type


async def _disconnect(ctx):
    """Printed damage; opponent can't play Items during their next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


_crash_snipe = snipe_attack(80, pool='any')


async def _lightning_crash(ctx):
    """Discard all Lightning Energy from this Pokémon, then 80 to 1 of the
    opponent's Pokémon."""
    lightning = [e for e in ctx.attached_energies(ctx.attacker)
                 if energy_provides_type(e, PokemonTypes.LIGHTNING.value)]
    if lightning:
        await ctx.discard_cards(lightning)
    await _crash_snipe(ctx)


card = PokemonCardDef(
    guid="279caedb-d05b-5842-9f42-53b6e9e6aebd",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1", "Zebstrika"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Disconnect",
            game_text="Your opponent can't play any Item cards from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_disconnect,
        ),
        Attack(
            title="Lightning Crash",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 80 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=_lightning_crash,
        ),
    ],
)