from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


async def _burning_shot(ctx):
    """Discard 2 Energy from this Pokemon: 150 to 1 of the opponent's Pokemon."""
    discarded = await ctx.discard_energy_from(ctx.attacker, 2, minimum=2,
                                              prompt="Discard 2 Energy")
    targets = ctx.opponent_pokemon_in_play()
    if len(discarded or []) < 2 or not targets:
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    await ctx.deal_damage(150, target=target or targets[0])


card = PokemonCardDef(
    guid="fdbacd4c-c1aa-548b-ae06-022060a67687",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Burning Shot",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack does 150 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            effect=_burning_shot,
        ),
    ],
)