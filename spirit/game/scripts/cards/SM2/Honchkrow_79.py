from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import damage_per

async def feint_attack(ctx):
    """30 to 1 of the opponent's Pokémon; ignore W/R and other effects."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Choose a Pokémon to take 30 damage",
    )
    if picks:
        await ctx.deal_damage(
            30, target=picks[0], apply_modifiers=False, ignore_target_effects=True,
        )


def _opp_damage_counters(ctx):
    total = 0
    for p in ctx.opponent_pokemon_in_play():
        total += max(0, (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10)
    return total


card = PokemonCardDef(
    guid="69e600db-ead1-5647-91c1-623ffdf62cef",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Feint Attack",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness, Resistance, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=feint_attack,
        ),
        Attack(
            title="Raven's Claw",
            game_text="This attack does 10 more damage for each damage counter on all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(_opp_damage_counters, 10, base=10),
        ),
    ],
)