from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import TurnDamageModifier


async def enthusiastic_dance(ctx):
    """On evolve: you may buff your Basic Pokemon's attacks +100 this turn."""
    if await ctx.ask_yes_no(
        "Use Enthusiastic Dance? Your Basic Pokémon's attacks do 100 more "
        "damage to your opponent's Active Pokémon this turn."
    ):
        ctx.add_turn_damage_modifier(
            TurnDamageModifier(100, ctx.player_id, requires_subtype="Basic")
        )


card = PokemonCardDef(
    guid="cf8f094b-19f2-5ba9-b7ee-32449319a97b",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Enthusiastic Dance",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may use this Ability. During this turn, your Basic Pok\u00e9mon's attacks do 100 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            trigger=Triggers.ON_EVOLVE,
            effect=enthusiastic_dance,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)