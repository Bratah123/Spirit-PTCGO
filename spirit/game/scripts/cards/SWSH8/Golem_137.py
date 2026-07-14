from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.pokemon import in_active_spot


async def desperate_blast(ctx):
    """Active Spot only: if Knocked Out by damage from an opponent's attack,
    put 10 damage counters on the Attacking Pokemon."""
    if not ctx.ko_from_attack or not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.ko_attacker
    if attacker is None:
        return
    await ctx.deal_damage(100, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="360da923-3054-5c81-b67c-46a19b9bd2f8",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name",
    display_name="Golem",
    searchable_by=["Golem", "Stage 2", "Golem"],
    subtypes=["Stage 2"],
    collector_number=137,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Ability(
            title="Desperate Blast",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, put 10 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=desperate_blast,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=recoil_attack(30),
        ),
    ],
)