from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import invasion, invasion_condition, moons_eclipse_gx, more_prizes_remaining

async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)

card = PokemonCardDef(
    guid="639c044e-5b35-5a3a-9091-9c24562ead30",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozmaGX.Name",
    display_name="Dawn Wings Necrozma-GX",
    searchable_by=["Dawn Wings Necrozma-GX", "Basic", "GX", "Ultra Beast", "DawnWingsNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=101,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=800,
    abilities=[
        Ability(
            title="Invasion",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may switch it with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=invasion,
            activation=Activations.ONCE_PER_TURN,
            condition=invasion_condition,
        ),
        Attack(
            title="Dark Flash",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=feint,
        ),
        Attack(
            title="Moon's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. Prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=180,
            effect=moons_eclipse_gx,
            condition=more_prizes_remaining,
        ),
    ],
)