from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import in_active_spot


async def scorching_feathers(ctx):
    """If this Pokémon (in the Active Spot) is damaged by an attack, burn the attacker."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    await ctx.apply_special_condition(ctx.damaged_by, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="c4f7b0ea-8692-5daa-a748-14df67353dfb",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Ability(
            title="Scorching Feathers",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=scorching_feathers,
        ),
        Attack(
            title="Mach Flight",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)