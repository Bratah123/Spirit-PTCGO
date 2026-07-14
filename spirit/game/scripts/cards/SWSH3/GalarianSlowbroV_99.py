from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import in_active_spot


async def rapid_fire_poison(ctx):
    """Once during your turn, if this Pokemon is in the Active Spot, you may
    make your opponent's Active Pokemon Poisoned."""
    if await ctx.ask_yes_no("Make your opponent's Active Pokémon Poisoned?"):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="6b18af02-c73b-5603-a12e-195280311ac7",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowbroV.Name",
    display_name="Galarian Slowbro V",
    searchable_by=["Galarian Slowbro V", "Basic", "V", "GalarianSlowbroV"],
    subtypes=["Basic", "V"],
    collector_number=99,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=80,
    abilities=[
        Ability(
            title="Rapid-Fire Poison",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may make your opponent's Active Pokémon Poisoned.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=rapid_fire_poison,
        ),
        Attack(
            title="Tripping Shot",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
