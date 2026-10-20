from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


async def feint_attack(ctx):
    """30 to 1 of opponent's Pokémon; ignore W/R and other effects on that Pokémon."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to take 30 damage",
    )
    if target is None:
        return
    await ctx.deal_damage(
        30, target=target,
        apply_modifiers=False, ignore_target_effects=True,
    )


card = PokemonCardDef(
    guid="bd1f34cf-6e54-5934-9d3f-99b538a869d9",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Feint Attack",
            game_text="Does 30 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=feint_attack,
        ),
        Attack(
            title="Claw Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(has_damage(), 30),
        ),
    ],
)
