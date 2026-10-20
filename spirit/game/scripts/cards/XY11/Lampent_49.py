from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _mirror_mirror(ctx):
    """Each player draws or discards until they have 4 cards in hand (opponent first)."""
    for pid in (ctx.opponent_id, ctx.player_id):
        n = ctx.hand_size(pid)
        if n < 4:
            await ctx.draw_until(4, pid)
        elif n > 4:
            await ctx.discard_from_hand(n - 4, minimum=n - 4, player_id=pid,
                                        prompt="Discard cards until you have 4")


card = PokemonCardDef(
    guid="73e05f42-db9e-5351-90a8-0ae8be539e7c",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Mirror Mirror",
            game_text="Each player either draws or discards cards until that player has 4 cards in his or her hand. (Your opponent does this first.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_mirror_mirror,
        ),
        Attack(
            title="Flickering Flames",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)