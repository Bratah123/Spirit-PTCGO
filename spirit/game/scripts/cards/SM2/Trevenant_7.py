from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


from spirit.game.session.effects import is_trainer_card


async def poltergeist(ctx):
    """Reveal the opponent's hand; 30 damage per Trainer card there."""
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    n = sum(1 for c in hand if is_trainer_card(c))
    if n > 0:
        await ctx.deal_damage(30 * n)


card = PokemonCardDef(
    guid="8d3b9c10-111c-5d63-9d28-38c585d1cdae",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 30 damage for each Trainer card you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=poltergeist,
        ),
        Attack(
            title="Horn Leech",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=heal_attack(30, target='self'),
        ),
    ],
)