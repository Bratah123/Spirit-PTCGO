from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import snipe_attack


async def hunting_claw(ctx):
    """Knock Out 1 of your opponent's Pokemon in play that has 60 HP or less remaining."""
    candidates = [
        p for p in ctx.opponent_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) <= 60
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon with 60 HP or less remaining"
    )
    if target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="63091c42-7636-53b0-a3e6-c4eecfe6a0da",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocVMAX.Name",
    display_name="Lycanroc VMAX",
    searchable_by=["Lycanroc VMAX", "VMAX", "LycanrocVMAX"],
    subtypes=["VMAX"],
    collector_number=213,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocV.Name",
    family_id=745,
    abilities=[
        Attack(
            title="Hunting Claw",
            game_text="Knock Out 1 of your opponent's Pok\u00e9mon in play that has 60 HP or less remaining.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=hunting_claw,
        ),
        Attack(
            title="Max Edge",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)