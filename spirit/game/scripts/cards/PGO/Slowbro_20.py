from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _opponent_one_prize_left(board, player_id, pokemon):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if not opponent:
        return False
    area = board.find_player_area(opponent, "prizePile")
    return bool(area) and len(area.children) == 1


async def twilight_inspiration(ctx):
    """Take 2 Prize cards (usable only when the opponent has exactly 1 left)."""
    await ctx.take_prizes(2)

card = PokemonCardDef(
    guid="12412fc3-817b-507d-8705-64286986f951",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Tumbling Tackle",
            game_text="Both Active Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
        Attack(
            title="Twilight Inspiration",
            game_text="You can use this attack only if your opponent has exactly 1 Prize card remaining. Take 2 Prize cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=twilight_inspiration,
            condition=_opponent_one_prize_left,
        ),
    ],
)