from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.attacks_common import flip_bonus


async def rough_skin(ctx):
    """Active only: put 2 damage counters on Attacking Pokemon."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="10b93774-1edd-5d1e-8cd2-4b64c6523360",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1", "Team Plasma", "Sharpedo"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=33,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=rough_skin,
        ),
        Attack(
            title="Hard Bite",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)