from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card


async def _eruption(ctx):
    """80+; each player discards their top card; 60 more per Energy card discarded."""
    n = 0
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(1, player_id=pid)
        if top:
            n += sum(1 for c in top if is_energy_card(c))
            await ctx.discard_cards(top)
    await ctx.deal_damage(ctx.ability.damage + 60 * n)


card = PokemonCardDef(
    guid="713a2b9c-e416-51e1-b7cd-394f21bcc65e",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1", "Camerupt"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Eruption",
            game_text="Each player discards the top card of his or her deck. This attack does 60 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=_eruption,
        ),
    ],
)