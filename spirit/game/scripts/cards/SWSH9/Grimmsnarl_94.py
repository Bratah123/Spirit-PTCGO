from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


async def longhair_shot(ctx):
    """30 damage to 1 of your opponent's Pokemon for each Darkness Energy attached to this Pokemon."""
    count = count_energy("self", energy_type=PokemonTypes.DARKNESS)(ctx)
    if count <= 0:
        return
    targets = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    apply_mod = target is ctx.opponent_active()
    await ctx.deal_damage(30 * count, target=target, apply_modifiers=apply_mod)


card = PokemonCardDef(
    guid="1d3a5b87-4fe8-5598-a361-0a998602c6b9",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2", "Grimmsnarl"],
    subtypes=["Stage 2"],
    collector_number=94,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Longhair Shot",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each Darkness Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=longhair_shot,
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)