from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.sm6 import twister

async def poison_point(ctx):
    """Active Spot only: if damaged by an opponent's attack (even if
    Knocked Out), the Attacking Pokemon is now Poisoned."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)

card = PokemonCardDef(
    guid="29991544-f0c2-5fd1-bbf0-b90e4bf750be",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name",
    display_name="Dragalge",
    searchable_by=["Dragalge", "Stage 1", "Dragalge"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Ability(
            title="Poison Point",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=poison_point,
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. For each heads, discard an Energy from your opponent's Active Pok\u00e9mon. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=twister,
        ),
    ],
)
