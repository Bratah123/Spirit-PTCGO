from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.passives_common import takes_less_passive


async def shield_star(ctx):
    """VSTAR Power: during opponent's next turn, your Pokemon take 100 less
    damage from their attacks (after W/R); covers Pokemon played later too."""
    shield = takes_less_passive(100, protects="team")
    for pokemon in ctx.my_pokemon_in_play():
        ctx.add_passive_through_opponents_turn(pokemon, shield)


async def giga_impact(ctx):
    """220. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="ad9a6f18-d2fa-5436-a862-93ac3087a39b",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaVSTAR.Name",
    display_name="Zamazenta VSTAR",
    searchable_by=["Zamazenta VSTAR", "VSTAR", "ZamazentaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=99,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    family_id=889,
    abilities=[
        Ability(
            title="Shield Star",
            game_text="During your turn, you may use this Ability. During your opponent's next turn, all of your Pok\u00e9mon take 100 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). (This includes Pok\u00e9mon that come into play during this turn or during your opponent's next turn.) (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=shield_star,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=giga_impact,
        ),
    ],
)