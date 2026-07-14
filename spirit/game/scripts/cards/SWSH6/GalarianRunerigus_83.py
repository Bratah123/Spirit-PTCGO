from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import in_active_spot, is_pokemon_vmax


async def spiteful_slate(ctx):
    """Active Spot only: if damaged by an attack from an opposing Pokemon
    VMAX (even if Knocked Out), put damage counters on the Attacking
    Pokemon equal to the damage done."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None or not is_pokemon_vmax(attacker.archetype_id):
        return
    if ctx.damage_amount:
        await ctx.deal_damage(ctx.damage_amount, target=attacker, apply_modifiers=False,
                              as_counters=True)


card = PokemonCardDef(
    guid="7e34bc62-a849-5422-8c34-435bde640931",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRunerigus.Name",
    display_name="Galarian Runerigus",
    searchable_by=["Galarian Runerigus", "Stage 1", "GalarianRunerigus"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianYamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Spiteful Slate",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon VMAX (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=spiteful_slate,
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 20, base=60),
        ),
    ],
)