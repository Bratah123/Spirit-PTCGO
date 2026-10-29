from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import impersonation, impersonation_condition


async def night_footsteps(ctx):
    """Choose 2 of your opponent's Pokemon and put 2 damage counters on each."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    count = min(2, len(candidates))
    targets = await ctx.choose_cards(
        candidates, count, prompt="Choose 2 of your opponent's Pokémon"
    )
    for target in targets:
        await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="87d91eb3-2ccb-54b7-92f5-55ca62b8bb01",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title="Impersonation",
            game_text="Discard a Supporter card from your hand. If you do, use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=impersonation_condition,
            effect=impersonation,
        ),
        Attack(
            title="Mischievous Hands",
            game_text="Choose 2 of your opponent's Pok\u00e9mon and put 2 damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=night_footsteps,
        ),
    ],
)