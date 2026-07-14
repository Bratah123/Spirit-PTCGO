from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.passives_common import apply_protection


async def sonic_slip(ctx):
    if await ctx.ask_yes_no(
        "Prevent all damage from and effects of attacks from your opponent's "
        "Pokémon done to this Pokémon until the end of your opponent's next turn?"
    ):
        await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="403b03e9-6fbb-5749-91de-136851b5eb17",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp", "Stage 2", "Garchomp"],
    subtypes=["Stage 2"],
    collector_number=109,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Sonic Slip",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may prevent all damage from and effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon until the end of your opponent's next turn.",
            trigger=Triggers.ON_EVOLVE,
            effect=sonic_slip,
        ),
        Attack(
            title="Dragonblade",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=160,
            effect=mill_attack(2, opponent=False),
        ),
    ],
)