from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def shadow_claw(ctx):
    """120. Discard a random card from your opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)

card = PokemonCardDef(
    guid="cd42d379-3507-5b8a-8a42-229f76d0b5d0",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantV.Name",
    display_name="Trevenant V",
    searchable_by=["Trevenant V", "Basic", "V", "TrevenantV"],
    subtypes=["Basic", "V"],
    collector_number=13,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=709,
    abilities=[
        Attack(
            title="Absorb Life",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=heal_attack(30, target="self"),
        ),
        Attack(
            title="Shadow Claw",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=shadow_claw,
        ),
    ],
)