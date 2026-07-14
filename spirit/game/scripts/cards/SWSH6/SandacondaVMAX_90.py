from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


async def _g_max_cyclone(ctx):
    await ctx.deal_damage()
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(pokemon, pokemon)


card = PokemonCardDef(
    guid="92a5f81b-c0f5-5237-a27e-1dfcee022087",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandacondaVMAX.Name",
    display_name="Sandaconda VMAX",
    searchable_by=["Sandaconda VMAX", "VMAX", "SandacondaVMAX"],
    subtypes=["VMAX"],
    collector_number=90,
    set_code="SWSH6",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SandacondaV.Name",
    family_id=844,
    abilities=[
        Attack(
            title="Sand Pulse",
            game_text="This attack also does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=spread_damage(20, side="opponent", also_base=True),
        ),
        Attack(
            title="G-Max Cyclone",
            game_text="Move any amount of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=_g_max_cyclone,
        ),
    ],
)