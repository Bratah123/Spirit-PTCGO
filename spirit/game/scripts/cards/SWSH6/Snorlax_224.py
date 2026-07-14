from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import in_active_spot


async def gormandize(ctx):
    if await ctx.ask_yes_no("Draw cards until you have 7 cards in your hand?"):
        await ctx.draw_until(7)

card = PokemonCardDef(
    guid="c2dcd121-1cd4-563a-8e5e-0f1f31829146",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=224,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Gormandize",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may draw cards until you have 7 cards in your hand. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            ends_turn=True,
            effect=gormandize,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)